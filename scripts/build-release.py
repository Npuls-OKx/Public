#!/usr/bin/env python3
"""Bouwt het releasepakket van een specificatiepakket: docx uit de markdown-bronnen.

Een pakket is een map met een release.json (het manifest). Dat manifest bepaalt de
versie, de leesvolgorde van de documenten en wat er verder meegeleverd wordt.

Wat dit script oplost dat pandoc alleen niet doet:

- **Mermaid.** De specificaties dragen tientallen mermaid-diagrammen. Pandoc kent
  mermaid niet en zou de codeblokken als letterlijke tekst afdrukken. Elk blok wordt
  daarom vooraf met mermaid-cli naar een PNG gerenderd en vervangen door een
  afbeeldingsverwijzing.
- **Verwijzingen.** De documenten verwijzen naar elkaar met relatieve paden
  (`../Koppelingspecificaties/...md#anchor`). In een docx bestaat dat pad niet. Voor
  het gebundelde document worden die verwijzingen interne verwijzingen; voor de losse
  documenten en voor alles buiten het pakket (Referentiemateriaal) worden het
  GitHub-URL's, want die blijven altijd werken.
- **Botsende anchors.** Meerdere documenten dragen een kop "3. Interactieoverzicht".
  In een gebundeld document levert dat dubbele id's op en landt een verwijzing in het
  verkeerde hoofdstuk. Elke kop krijgt daarom een id met het document als voorvoegsel.

Uitvoer in de doelmap:

    <bestandsnaam>-v<versie>.docx           het gebundelde document
    <bestandsnaam>-v<versie>-documenten.zip de losse documenten, mapstructuur behouden

Exitcodes: 0 gebouwd, 1 bouwfout, 2 pakket of manifest niet gevonden.
"""

import argparse
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

MERMAID = re.compile(r"^([ \t]*)```mermaid[ \t]*\n(.*?)^[ \t]*```[ \t]*$", re.DOTALL | re.MULTILINE)
KOP = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.MULTILINE)
LINK = re.compile(r"\[([^\]]*)\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^```.*?^```", re.DOTALL | re.MULTILINE)

STANDAARD_REPO_URL = "https://github.com/Npuls-OKx/Public"

# Een docx kent \newpage niet; dat zou als letterlijke tekst in het document belanden.
PAGINA_EINDE = '\n\n```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n'


def slug(tekst: str) -> str:
    """Zet een koptekst om in een anchor, zoals GitHub dat doet.

    GitHub vervangt elke spatie afzonderlijk door een koppelstreep. Een em-streep
    tussen spaties levert daardoor een dubbele koppelstreep op; dat gedrag wordt hier
    nagebootst zodat de anchors overeenkomen met wat in de bron staat.
    """
    tekst = re.sub(r"<[^>]+>", "", tekst)
    tekst = re.sub(r"[`*_]", "", tekst)
    tekst = tekst.strip().lower()
    tekst = re.sub(r"[^\w\s-]", "", tekst, flags=re.UNICODE)
    return tekst.replace(" ", "-")


def doc_slug(relatief_pad: str) -> str:
    """Uniek voorvoegsel per document, afgeleid van het pad binnen het pakket."""
    return re.sub(r"[^\w]+", "-", relatief_pad[:-3] if relatief_pad.endswith(".md") else relatief_pad).strip("-").lower()


def maskeer_codeblokken(inhoud: str):
    """Haalt fenced code blocks weg zodat regexen niet in code gaan zoeken."""
    blokken = []

    def vervang(m):
        blokken.append(m.group(0))
        return f"\x00CODE{len(blokken) - 1}\x00"

    return FENCE.sub(vervang, inhoud), blokken


def herstel_codeblokken(inhoud: str, blokken: list) -> str:
    for i, blok in enumerate(blokken):
        inhoud = inhoud.replace(f"\x00CODE{i}\x00", blok)
    return inhoud


def render_mermaid(inhoud: str, doc: str, beeldmap: pathlib.Path, teller: list,
                   mislukt: list, streng: bool) -> str:
    """Vervangt elk mermaid-blok door een verwijzing naar een gerenderde PNG.

    Een diagram dat niet rendert blijft als codeblok staan. Dat is geen noodgreep maar
    het gewenste gedrag voor de templates: die dragen een skelet met invulplekken
    (`\\<type\\>`) dat per definitie geen geldige mermaid is, en dan is de broncode
    precies wat een schrijver wil zien. Met --streng faalt de bouw er alsnog op.
    """
    beeldmap.mkdir(parents=True, exist_ok=True)
    puppeteer = beeldmap / "puppeteer.json"
    if not puppeteer.exists():
        # Chrome draait in CI als root en zonder sandbox; zonder deze vlaggen start hij niet.
        puppeteer.write_text(json.dumps({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}))

    def vervang(m):
        inspringing, diagram = m.group(1), m.group(2)
        teller[0] += 1
        naam = f"{doc_slug(doc)}-{teller[0]:02d}"
        bron = beeldmap / f"{naam}.mmd"
        doel = beeldmap / f"{naam}.png"
        bron.write_text(diagram, encoding="utf-8")
        resultaat = subprocess.run(
            ["npx", "--yes", "@mermaid-js/mermaid-cli",
             "-i", str(bron), "-o", str(doel),
             "-b", "white", "-s", "3", "-p", str(puppeteer)],
            capture_output=True, text=True,
        )
        if resultaat.returncode != 0 or not doel.exists():
            reden = (resultaat.stderr or resultaat.stdout).strip().splitlines()
            mislukt.append((doc, teller[0], reden[0] if reden else "onbekende fout"))
            if streng:
                print(f"  mermaid faalde in {doc} (diagram {teller[0]}):", file=sys.stderr)
                print("   ", "\n    ".join(reden[:6]), file=sys.stderr)
                raise SystemExit(1)
            return m.group(0)  # laat het codeblok staan
        return f"{inspringing}![]({doel.as_posix()})"

    return MERMAID.sub(vervang, inhoud)


def bouw_anchorkaart(pakket: pathlib.Path, documenten: list) -> dict:
    """Per document: van oorspronkelijk anchor naar uniek anchor in het gebundelde document."""
    kaart = {}
    for doc in documenten:
        inhoud = (pakket / doc).read_text(encoding="utf-8")
        zonder_code, _ = maskeer_codeblokken(inhoud)
        gezien = {}
        per_doc = {}
        for m in KOP.finditer(zonder_code):
            basis = slug(m.group(2))
            n = gezien.get(basis, 0)
            gezien[basis] = n + 1
            origineel = basis if n == 0 else f"{basis}-{n}"
            per_doc[origineel] = f"{doc_slug(doc)}--{origineel}"
        kaart[doc] = per_doc
    return kaart


def koppen_van(pakket: pathlib.Path, doc: str, kaart: dict) -> list:
    """(niveau, tekst, uniek anchor) per kop in een document."""
    zonder_code, _ = maskeer_codeblokken((pakket / doc).read_text(encoding="utf-8"))
    gezien, uit = {}, []
    for m in KOP.finditer(zonder_code):
        niveau, tekst = len(m.group(1)), m.group(2).strip()
        basis = slug(tekst)
        n = gezien.get(basis, 0)
        gezien[basis] = n + 1
        origineel = basis if n == 0 else f"{basis}-{n}"
        uit.append((niveau, tekst, (kaart.get(doc) or {}).get(origineel)))
    return uit


def bouw_inhoudsopgave(pakket: pathlib.Path, documenten: list, kaart: dict, diepte: int = 2) -> str:
    """Een inhoudsopgave als gewone tekst met interne verwijzingen.

    Pandoc kan met --toc een Word-veld plaatsen, maar zo'n veld blijft leeg tot de lezer
    de velden bijwerkt. Of dat gebeurt hangt af van het programma en van een klik van de
    lezer; een releaseartefact hoort niet leeg open te gaan. Deze inhoudsopgave staat er
    dus gewoon als tekst in, met dezelfde interne verwijzingen als de rest van het
    document. Prijs: geen paginanummers, want die kent alleen de renderer.
    """
    regels = ["## Inhoudsopgave", ""]
    for doc in documenten:
        for niveau, tekst, anchor in koppen_van(pakket, doc, kaart):
            if niveau > diepte or anchor is None:
                continue
            if slug(tekst) == "inhoudsopgave":
                continue  # de documenten dragen er zelf al een
            schoon = re.sub(r"[`*]", "", tekst)
            regels.append(f"{'  ' * (niveau - 1)}- [{schoon}](#{anchor})")
    return "\n".join(regels)


def eerste_kop_anchor(doc: str, kaart: dict) -> str:
    """Het anchor van de H1 van een document, als landingspunt voor een verwijzing."""
    per_doc = kaart.get(doc) or {}
    return next(iter(per_doc.values()), doc_slug(doc))


def herschrijf_links(inhoud: str, doc: str, pakket: pathlib.Path, documenten: list,
                     kaart: dict, gebundeld: bool, repo_url: str, ref: str) -> str:
    """Herschrijft relatieve verwijzingen zodat ze in een docx werken."""
    hier = (pakket / doc).parent

    def vervang(m):
        tekst, doel = m.group(1), m.group(2)
        if doel.startswith(("http://", "https://", "mailto:")):
            return m.group(0)

        pad, _, anchor = doel.partition("#")

        # Verwijzing binnen hetzelfde document.
        if not pad:
            if gebundeld:
                nieuw = (kaart.get(doc) or {}).get(anchor, f"{doc_slug(doc)}--{anchor}")
                return f"[{tekst}](#{nieuw})"
            return m.group(0)

        doelpad = (hier / pad).resolve()
        try:
            binnen_pakket = doelpad.relative_to(pakket.resolve()).as_posix()
        except ValueError:
            binnen_pakket = None

        # Document dat meegaat in het pakket.
        if binnen_pakket in documenten:
            if gebundeld:
                if anchor:
                    nieuw = (kaart.get(binnen_pakket) or {}).get(anchor, f"{doc_slug(binnen_pakket)}--{anchor}")
                else:
                    nieuw = eerste_kop_anchor(binnen_pakket, kaart)
                return f"[{tekst}](#{nieuw})"
            url = f"{repo_url}/blob/{ref}/{pakket.name}/{binnen_pakket}"
            return f"[{tekst}]({url}#{anchor})" if anchor else f"[{tekst}]({url})"

        # Alles daarbuiten (Referentiemateriaal, scripts, schema's): naar GitHub.
        try:
            vanaf_root = doelpad.relative_to(pakket.resolve().parent).as_posix()
        except ValueError:
            return m.group(0)
        url = f"{repo_url}/blob/{ref}/{vanaf_root}"
        return f"[{tekst}]({url}#{anchor})" if anchor else f"[{tekst}]({url})"

    zonder_code, blokken = maskeer_codeblokken(inhoud)
    zonder_code = LINK.sub(vervang, zonder_code)
    return herstel_codeblokken(zonder_code, blokken)


def geef_koppen_ids(inhoud: str, doc: str, kaart: dict) -> str:
    """Zet een uniek id op elke kop, zodat anchors tussen documenten niet botsen."""
    gezien = {}

    def vervang(m):
        hekjes, tekst = m.group(1), m.group(2)
        basis = slug(tekst)
        n = gezien.get(basis, 0)
        gezien[basis] = n + 1
        origineel = basis if n == 0 else f"{basis}-{n}"
        nieuw = (kaart.get(doc) or {}).get(origineel, f"{doc_slug(doc)}--{origineel}")
        return f"{hekjes} {tekst} {{#{nieuw}}}"

    zonder_code, blokken = maskeer_codeblokken(inhoud)
    zonder_code = KOP.sub(vervang, zonder_code)
    return herstel_codeblokken(zonder_code, blokken)


def verlaag_koppen(inhoud: str) -> str:
    """Schuift alle koppen een niveau op, zodat de documenttitel een hoofdstuk wordt."""
    zonder_code, blokken = maskeer_codeblokken(inhoud)
    zonder_code = KOP.sub(lambda m: f"#{m.group(1)} {m.group(2)}", zonder_code)
    return herstel_codeblokken(zonder_code, blokken)


# Opmaak van codeblokken. Pandoc's eigen SourceCode-stijl draagt geen lettergrootte,
# geen inspringing en geen achtergrond, waardoor een JSON-blok even groot is als de
# lopende tekst, zonder zichtbare rand, en een afgebroken regel links uitlijnt alsof
# het een nieuwe regel is. Juist bij JSON verdwijnt daarmee de nesting uit beeld.
CODE_STIJL = """<w:style w:type="paragraph" w:customStyle="1" w:styleId="SourceCode">
  <w:name w:val="Source Code"/><w:basedOn w:val="Normal"/><w:link w:val="VerbatimChar"/>
  <w:pPr>
    <w:wordWrap w:val="off"/>
    <w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>
    <w:ind w:left="340" w:hanging="340"/>
    <w:shd w:val="clear" w:color="auto" w:fill="F4F4F4"/>
  </w:pPr>
  <w:rPr><w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/><w:sz w:val="18"/></w:rPr>
</w:style>"""

TABEL_STIJL_RPR = '<w:rPr><w:sz w:val="18"/></w:rPr>'


# 2 cm rondom in plaats van de standaard 2,54 cm: dat scheelt ruim tien tekens per
# regel in een codeblok, en de brede tabellen krijgen er ook lucht van.
MARGES = ('<w:pgSz w:w="11906" w:h="16838"/>'
          '<w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134"'
          ' w:header="709" w:footer="709" w:gutter="0"/>')


def referentiedocument(werk: pathlib.Path) -> pathlib.Path:
    """Pandoc's eigen referentiedocument, met codeblokken leesbaar opgemaakt.

    Het document komt uit pandoc zelf en wordt hier aangepast, zodat er geen binair
    bestand in het repository hoeft te staan dat bij een pandoc-upgrade stilletjes
    veroudert.
    """
    resultaat = subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                               capture_output=True)
    if resultaat.returncode != 0 or not resultaat.stdout:
        print("kon het referentiedocument niet uit pandoc halen:", file=sys.stderr)
        print((resultaat.stderr or b"").decode("utf-8", "ignore")[:400], file=sys.stderr)
        raise SystemExit(1)

    ruw = werk / "referentie-ruw.docx"
    ruw.write_bytes(resultaat.stdout)
    ref = werk / "referentie.docx"
    with zipfile.ZipFile(ruw) as bron, zipfile.ZipFile(ref, "w", zipfile.ZIP_DEFLATED) as doel:
        for item in bron.infolist():
            data = bron.read(item.filename)
            if item.filename == "word/styles.xml":
                tekst = data.decode("utf-8")
                # Kleinere letter voor code binnen een alinea, zodat een lange regel
                # minder snel afbreekt.
                tekst = re.sub(r'(w:styleId="VerbatimChar".*?<w:sz w:val=")\d+',
                               r"\g<1>18", tekst, count=1, flags=re.DOTALL)
                # Tabellen een punt kleiner, anders past een tabel met vijf kolommen niet.
                # De volgorde van de kinderen van een stijl ligt vast in OOXML: rPr hoort
                # vlak voor tblPr te staan, anders negeert Word de hele stijl.
                def kleiner(m):
                    blok = m.group(0)
                    if "<w:rPr>" in blok.split("<w:tblPr>")[0]:
                        return blok
                    return blok.replace("<w:tblPr>", TABEL_STIJL_RPR + "<w:tblPr>", 1)

                tekst = re.sub(r'<w:style [^>]*w:styleId="Table"[^>]*>.*?</w:style>',
                               kleiner, tekst, count=1, flags=re.DOTALL)
                if 'w:styleId="SourceCode"' in tekst:
                    tekst = re.sub(r'<w:style [^>]*w:styleId="SourceCode".*?</w:style>',
                                   CODE_STIJL, tekst, count=1, flags=re.DOTALL)
                else:
                    tekst = tekst.replace("</w:styles>", CODE_STIJL + "</w:styles>")
                data = tekst.encode("utf-8")
            elif item.filename == "word/document.xml":
                tekst = data.decode("utf-8")
                tekst = tekst.replace("<w:sectPr>", "<w:sectPr>" + MARGES, 1)
                data = tekst.encode("utf-8")
            doel.writestr(item, data)
    return ref


def tabellen_laten_meebewegen(docx: pathlib.Path) -> None:
    """Laat Word de kolombreedtes bepalen in plaats van pandoc.

    Pandoc geeft elke kolom dezelfde breedte, ongeacht wat erin staat: bij een tabel met
    vijf kolommen wordt elke kolom een vijfde, en dan breekt Word woorden middenin af
    ("Wijziginge n tussen"). Met autofit en zonder vaste breedtes verdeelt Word de ruimte
    naar de inhoud.
    """
    z = zipfile.ZipFile(docx)
    onderdelen = {i.filename: z.read(i.filename) for i in z.infolist()}
    z.close()
    xml = onderdelen["word/document.xml"].decode("utf-8")
    xml = xml.replace('<w:tblW w:type="auto" w:w="0" />',
                      '<w:tblW w:type="pct" w:w="5000" /><w:tblLayout w:type="autofit" />')
    xml = re.sub(r'<w:gridCol w:w="\d+" />', "<w:gridCol />", xml)
    onderdelen["word/document.xml"] = xml.encode("utf-8")
    with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as uit:
        for naam, inhoud in onderdelen.items():
            uit.writestr(naam, inhoud)


def pandoc(argumenten: list) -> None:
    resultaat = subprocess.run(["pandoc", *argumenten], capture_output=True, text=True)
    if resultaat.returncode != 0:
        print("pandoc faalde:", file=sys.stderr)
        print((resultaat.stderr or resultaat.stdout).strip()[:2000], file=sys.stderr)
        raise SystemExit(1)


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pakket", type=pathlib.Path, help="map met release.json")
    ap.add_argument("--uit", type=pathlib.Path, default=pathlib.Path("dist"), help="doelmap")
    ap.add_argument("--versie", help="overschrijft de versie uit het manifest")
    ap.add_argument("--ref", default=os.environ.get("GITHUB_REF_NAME", "dev"),
                    help="git-ref waarnaar verwijzingen buiten het pakket wijzen")
    ap.add_argument("--repo-url", default=os.environ.get("OKX_REPO_URL", STANDAARD_REPO_URL))
    ap.add_argument("--streng", action="store_true",
                    help="faal ook op een mermaid-diagram dat niet rendert")
    ap.add_argument("--alleen-controle", action="store_true",
                    help="bouw naar een tijdelijke map; controleert de toolchain zonder artefacten achter te laten")
    args = ap.parse_args(argv)

    pakket = args.pakket
    manifest_pad = pakket / "release.json"
    if not manifest_pad.exists():
        print(f"geen release.json in {pakket}", file=sys.stderr)
        return 2

    manifest = json.loads(manifest_pad.read_text(encoding="utf-8"))
    versie = args.versie or manifest["versie"]
    documenten = manifest["documenten"]
    basisnaam = f"{manifest['bestandsnaam']}-v{versie}"

    ontbreekt = [d for d in documenten if not (pakket / d).exists()]
    if ontbreekt:
        print("manifest noemt documenten die niet bestaan:", file=sys.stderr)
        for d in ontbreekt:
            print(f"  {d}", file=sys.stderr)
        return 1

    op_schijf = {p.relative_to(pakket).as_posix() for p in pakket.rglob("*.md")}
    vergeten = sorted(op_schijf - set(documenten))
    if vergeten:
        print("let op: deze markdown-bestanden staan niet in het manifest en gaan niet mee:")
        for d in vergeten:
            print(f"  {d}")

    uit = pathlib.Path(tempfile.mkdtemp(prefix="okx-release-")) if args.alleen_controle else args.uit
    uit.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="okx-bouw-") as tmp:
        werk = pathlib.Path(tmp)
        beelden = werk / "diagrammen"
        kaart = bouw_anchorkaart(pakket, documenten)
        teller, mislukt = [0], []
        referentie = referentiedocument(werk)

        print(f"{manifest['naam']} v{versie}: {len(documenten)} documenten")

        losse, gebundelde_delen = [], []
        for doc in documenten:
            ruw = (pakket / doc).read_text(encoding="utf-8")
            met_beelden = render_mermaid(ruw, doc, beelden, teller, mislukt, args.streng)

            # Losse variant: verwijzingen naar GitHub, eigen anchors blijven.
            los = herschrijf_links(met_beelden, doc, pakket, documenten, kaart,
                                   False, args.repo_url, args.ref)
            los_pad = werk / "los" / doc
            los_pad.parent.mkdir(parents=True, exist_ok=True)
            los_pad.write_text(los, encoding="utf-8")
            losse.append((doc, los_pad))

            # Gebundelde variant: unieke kop-id's, interne verwijzingen, een niveau dieper.
            deel = herschrijf_links(met_beelden, doc, pakket, documenten, kaart,
                                    True, args.repo_url, args.ref)
            deel = geef_koppen_ids(deel, doc, kaart)
            deel = verlaag_koppen(deel)
            gebundelde_delen.append(deel)

        print(f"  {teller[0] - len(mislukt)} van {teller[0]} mermaid-diagrammen gerenderd")
        for doc, n, reden in mislukt:
            print(f"    blijft codeblok: {doc} (diagram {n}) - {reden}")

        # Gebundeld document.
        titel = (f"# {manifest['naam']}\n\n{manifest.get('omschrijving', '')}\n\n"
                 f"Versie {versie}\n")
        inhoud = bouw_inhoudsopgave(pakket, documenten, kaart)
        gebundeld_md = werk / "gebundeld.md"
        gebundeld_md.write_text(
            titel + PAGINA_EINDE + inhoud + PAGINA_EINDE
            + PAGINA_EINDE.join(gebundelde_delen), encoding="utf-8")
        gebundeld_docx = uit / f"{basisnaam}.docx"
        pandoc([
            # gfm+attributes, niet gfm+header_attributes: die laatste bestaat niet voor
            # gfm en laat pandoc afbreken. Zie --list-extensions=gfm.
            "-f", "gfm+attributes+raw_attribute",
            "-t", "docx",
            "--reference-doc", str(referentie),
            "--metadata", f"title={manifest['naam']} v{versie}",
            "--resource-path", str(werk),
            "-o", str(gebundeld_docx), str(gebundeld_md),
        ])
        tabellen_laten_meebewegen(gebundeld_docx)
        print(f"  {gebundeld_docx.name}")

        # Losse documenten in een zip, mapstructuur behouden.
        zip_pad = uit / f"{basisnaam}-documenten.zip"
        with zipfile.ZipFile(zip_pad, "w", zipfile.ZIP_DEFLATED) as z:
            for doc, pad in losse:
                docx = werk / "docx" / (doc[:-3] + ".docx")
                docx.parent.mkdir(parents=True, exist_ok=True)
                pandoc([
                    "-f", "gfm", "-t", "docx",
                    "--reference-doc", str(referentie),
                            "--resource-path", str(werk),
                    "-o", str(docx), str(pad),
                ])
                tabellen_laten_meebewegen(docx)
                z.write(docx, doc[:-3] + ".docx")
            for extra in manifest.get("meeleveren", []):
                bron = pakket / extra
                if bron.is_dir():
                    for bestand in sorted(bron.rglob("*")):
                        if bestand.is_file():
                            z.write(bestand, bestand.relative_to(pakket).as_posix())
                elif bron.is_file():
                    z.write(bron, extra)
        print(f"  {zip_pad.name}")

    if args.alleen_controle:
        shutil.rmtree(uit, ignore_errors=True)
        print("controle geslaagd, artefacten verwijderd")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
