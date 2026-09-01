#!/usr/bin/env python3
"""Bouwt het releasepakket van een specificatiepakket: docx uit de markdown-bronnen.

Een pakket is een map met een release.json (het manifest). Dat manifest bepaalt de
versie, de leesvolgorde van de documenten en wat er verder meegeleverd wordt. Een item
in `documenten` is een pad, of een **sectie** die documenten die bij elkaar horen onder
één kop bundelt:

    {"sectie": "Applicatiecomponenten",
     "inleiding": "Applicatiecomponenten/README.md",
     "documenten": ["Applicatiecomponenten/onderwijscatalogus.md", ...]}

Een pad mag met `../` buiten de pakketmap wijzen: de requirementsboom staat in
`Referentiemateriaal` en gaat wel mee als hoofdstuk. In de zip en de werkmap krijgt zo'n
document zijn pad zonder de `../`, zodat het onder de mapnaam uit het repository landt.

De sectiekop draagt de titel, de optionele `inleiding` staat er als tekst onder (haar
eigen H1 vervalt, want de sectiekop zegt hetzelfde al), en elk document eronder wordt
een subhoofdstuk. In de losse documenten verandert een sectie niets: die blijven per
bestand staan, met de mapstructuur eromheen.

Een sectie kan in plaats van `documenten` ook `schemas` dragen: de naam van een map met
JSON-schema's. Elk schema wordt dan een subhoofdstuk met zijn volledige inhoud, ingelezen
bij het bouwen. De schema's blijven zo hun eigen bron; een bijlage die met de hand was
overgeschreven zou bij de eerste schemawijziging uit de pas gaan lopen.

`{"inhoudsopgave": true}` bepaalt waar de inhoudsopgave staat. Zonder dat item komt zij
direct achter de titelpagina; ervoor kan dan bijvoorbeeld eerst een inleiding staan.

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
LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+?)(?:\s+\"[^\"]*\")?\)")
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


def uitvoerpad(doc: str) -> str:
    """Het pad waaronder een document in de werkmap en de zip landt.

    Een manifestpad mag buiten de pakketmap wijzen. Zo'n `../` hoort niet in een
    zip-ingang thuis en zou in de werkmap een map omhoog ontsnappen; hij valt hier weg,
    waarna het document onder zijn eigen mapnaam uit het repository staat.
    """
    return "/".join(deel for deel in doc.split("/") if deel != "..")


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


def paden_van(documenten: list) -> list:
    """Alle documentpaden uit het manifest in leesvolgorde, secties platgeslagen.

    Alles wat per document werkt - de anchorkaart, het herschrijven van verwijzingen,
    de losse documenten - kent geen secties en werkt op deze vlakke lijst.
    """
    uit = []
    for item in documenten:
        if isinstance(item, str):
            uit.append(item)
            continue
        if item.get("inhoudsopgave"):
            continue
        if not item.get("sectie") or not (item.get("documenten") or item.get("schemas")):
            raise SystemExit(
                "een sectie in het manifest vraagt om 'sectie' plus 'documenten' of 'schemas'")
        if item.get("inleiding"):
            uit.append(item["inleiding"])
        uit.extend(item.get("documenten") or [])
    return uit


def schemabestanden(pakket: pathlib.Path, item: dict) -> list:
    return sorted((pakket / item["schemas"]).glob("*.json"))


def schema_bijlage(pakket: pathlib.Path, item: dict) -> str:
    """Elk JSON-schema als subhoofdstuk, met zijn volledige inhoud."""
    delen = []
    for bestand in schemabestanden(pakket, item):
        inhoud = bestand.read_text(encoding="utf-8").rstrip()
        delen.append(f"### {bestand.name} {{#schema--{slug(bestand.stem)}}}\n\n"
                     f"```json\n{inhoud}\n```")
    return "\n\n".join(delen)


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


def bouw_inhoudsopgave(pakket: pathlib.Path, documenten: list, kaart: dict,
                       nummers: dict, diepte: int = 2) -> str:
    """Een inhoudsopgave als gewone tekst met interne verwijzingen.

    Pandoc kan met --toc een Word-veld plaatsen, maar zo'n veld blijft leeg tot de lezer
    de velden bijwerkt. Of dat gebeurt hangt af van het programma en van een klik van de
    lezer; een releaseartefact hoort niet leeg open te gaan. Deze inhoudsopgave staat er
    dus gewoon als tekst in, met dezelfde interne verwijzingen als de rest van het
    document. Prijs: geen paginanummers, want die kent alleen de renderer.
    """
    regels = ["## Inhoudsopgave", ""]

    def label(tekst: str, anchor: str) -> str:
        """De koptekst zoals hij in het document staat: genummerd, zonder opmaak."""
        schoon = NUMMER_VOORAF.sub("", re.sub(r"[`*]", "", tekst))
        nummer = nummers.get(anchor)
        return f"{nummer} {schoon}" if nummer else schoon

    def regels_voor(doc: str, inspring: int, sla_titel_over: bool = False) -> None:
        for i, (niveau, tekst, anchor) in enumerate(koppen_van(pakket, doc, kaart)):
            if i == 0 and sla_titel_over:
                continue  # de sectiekop staat er al
            if niveau > diepte or anchor is None:
                continue
            if slug(tekst) == "inhoudsopgave":
                continue  # de documenten dragen er zelf al een
            regels.append(f"{'  ' * (niveau - 1 + inspring)}- [{label(tekst, anchor)}](#{anchor})")

    for item in documenten:
        if isinstance(item, str):
            regels_voor(item, 0)
            continue
        if item.get("inhoudsopgave"):
            continue  # de inhoudsopgave noemt zichzelf niet
        anchor = sectie_anchor(item, kaart)
        regels.append(f"- [{label(item['sectie'], anchor)}](#{anchor})")
        if item.get("inleiding"):
            regels_voor(item["inleiding"], 0, sla_titel_over=True)
        for doc in item.get("documenten") or []:
            regels_voor(doc, 1)
        if item.get("schemas"):
            for bestand in schemabestanden(pakket, item):
                anchor = f"schema--{slug(bestand.stem)}"
                regels.append(f"  - [{label(bestand.name, anchor)}](#{anchor})")
    return "\n".join(regels)


def eerste_kop_anchor(doc: str, kaart: dict) -> str:
    """Het anchor van de H1 van een document, als landingspunt voor een verwijzing."""
    per_doc = kaart.get(doc) or {}
    return next(iter(per_doc.values()), doc_slug(doc))


def sectie_anchor(item: dict, kaart: dict) -> str:
    """Het anchor van een sectiekop.

    Draagt de sectie een inleiding, dan neemt de sectiekop het anchor van de H1 van dat
    document over. Die kop vervalt namelijk in het gebundelde document, en zonder deze
    overname zou elke verwijzing naar de inleiding nergens meer landen.
    """
    if item.get("inleiding"):
        return eerste_kop_anchor(item["inleiding"], kaart)
    return f"sectie--{slug(item['sectie'])}"


def verwijsbaar(bestand: pathlib.Path) -> str:
    """Geeft een pad in de vorm die een markdown-verwijzing aankan."""
    tekst = bestand.as_posix()
    return f"<{tekst}>" if set(" ()<>") & set(tekst) else tekst


def herschrijf_links(inhoud: str, doc: str, pakket: pathlib.Path, documenten: list,
                     kaart: dict, gebundeld: bool, repo_url: str, ref: str) -> str:
    """Herschrijft relatieve verwijzingen zodat ze in een docx werken."""
    hier = (pakket / doc).parent

    def vervang(m):
        beeld, tekst, doel = m.group(1), m.group(2), m.group(3)
        if doel.startswith(("http://", "https://", "mailto:")):
            return m.group(0)

        pad, _, anchor = doel.partition("#")

        # Een afbeelding hoort in de docx te zitten, niet erheen te verwijzen. Een
        # GitHub-URL wijst naar de blob-pagina; pandoc haalt daar HTML op en sluit die
        # in in plaats van de PNG. Een absoluut pad laat pandoc het bestand vinden,
        # net zoals bij de gerenderde mermaid-diagrammen.
        if beeld:
            bestand = (hier / pad).resolve() if pad else None
            if bestand is None or not bestand.is_file():
                return m.group(0)
            return f"![{tekst}]({verwijsbaar(bestand)})"

        # Verwijzing binnen hetzelfde document.
        if not pad:
            if gebundeld:
                nieuw = (kaart.get(doc) or {}).get(anchor, f"{doc_slug(doc)}--{anchor}")
                return f"[{tekst}](#{nieuw})"
            return m.group(0)

        doelpad = (hier / pad).resolve()

        # Een document dat meegaat in het pakket wordt herkend aan zijn opgeloste pad,
        # niet aan de vraag of het binnen de pakketmap ligt: het manifest mag met ../
        # ook daarbuiten wijzen.
        meegaand = next((d for d in documenten if (pakket / d).resolve() == doelpad), None)
        if meegaand is not None and gebundeld:
            if anchor:
                nieuw = (kaart.get(meegaand) or {}).get(anchor, f"{doc_slug(meegaand)}--{anchor}")
            else:
                nieuw = eerste_kop_anchor(meegaand, kaart)
            return f"[{tekst}](#{nieuw})"

        # Losse documenten en alles wat niet meegaat: naar GitHub, want zo'n URL blijft
        # werken waar een relatief pad in een docx niets betekent.
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


def verlaag_koppen(inhoud: str, niveaus: int = 1) -> str:
    """Schuift alle koppen op, zodat de documenttitel een hoofdstuk wordt.

    Een document binnen een sectie schuift twee niveaus op: de sectiekop is dan het
    hoofdstuk en de documenttitel het subhoofdstuk eronder.
    """
    zonder_code, blokken = maskeer_codeblokken(inhoud)
    zonder_code = KOP.sub(lambda m: f"{'#' * niveaus}{m.group(1)} {m.group(2)}", zonder_code)
    return herstel_codeblokken(zonder_code, blokken)


KOP_MET_ID = re.compile(r"^(#{1,6})[ \t]+(.+?)(?:[ \t]*\{#([^}]+)\})?[ \t]*$", re.MULTILINE)

# Een nummer dat een schrijver zelf voor een kop zette: "1.", "4.1", "5.5". Twee vormen,
# zodat "2026 in cijfers" niet als nummer wordt gelezen: of er staat een punt in het
# nummer, of het nummer sluit met een punt af.
NUMMER_VOORAF = re.compile(r"^(?:\d+(?:\.\d+)+\.?|\d+\.)[ \t]+")


def nummer_delen(delen: list, sla_over: set) -> tuple:
    """Nummert de koppen doorlopend: 1, 1.1, 1.1.1, 1.1.1.1.

    De nummers komen uit de plek in het gebundelde document, niet uit de kop zelf: een
    nummer dat de schrijver er zelf voor zette gaat eraf. Documenten nummeren hun
    paragrafen op volgorde vanaf 1, dus het laatste deel van het nieuwe nummer komt
    overeen met het oude; een verwijzing naar "§7" wijst nog steeds naar dezelfde
    paragraaf, nu als 9.7.

    Geeft de genummerde delen terug plus, per anchor, het nummer dat de kop draagt.
    Daarmee kan de inhoudsopgave dezelfde nummers tonen als het document zelf.
    """
    tellers, nummers, uit = [], {}, []

    def vervang(m):
        hekjes, tekst, anchor = m.group(1), m.group(2), m.group(3)
        # Niveau 1 draagt de titelpagina; de hoofdstukken beginnen op niveau 2.
        diepte = len(hekjes) - 2
        if diepte < 0:
            return m.group(0)
        # De documenten dragen elk hun eigen inhoudsopgave. Die telt niet mee: anders
        # schuift elke paragraaf erna een nummer op en wijst "§1" naar 1.2.
        if slug(NUMMER_VOORAF.sub("", tekst)) == "inhoudsopgave":
            return m.group(0)
        del tellers[diepte + 1:]
        tellers.extend([0] * (diepte + 1 - len(tellers)))
        tellers[diepte] += 1
        nummer = ".".join(str(t) for t in tellers)
        if anchor:
            nummers[anchor] = nummer
        staart = f" {{#{anchor}}}" if anchor else ""
        return f"{hekjes} {nummer} {NUMMER_VOORAF.sub('', tekst)}{staart}"

    for i, deel in enumerate(delen):
        if i in sla_over:
            uit.append(deel)
            continue
        zonder_code, blokken = maskeer_codeblokken(deel)
        uit.append(herstel_codeblokken(KOP_MET_ID.sub(vervang, zonder_code), blokken))
    return uit, nummers


def zonder_titel(inhoud: str) -> str:
    """Haalt de eerste kop weg, voor een inleiding die onder een sectiekop komt."""
    zonder_code, blokken = maskeer_codeblokken(inhoud)
    zonder_code = KOP.sub("", zonder_code, count=1).lstrip("\n")
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

# Basisgrootte voor lopende tekst, in halve punten: 18 is 9 punt. Pandoc staat op 24
# (12 punt). De koppen dragen hun eigen grootte en veranderen hier niet van mee.
BASISGROOTTE = "18"


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
                # Lopende tekst kleiner. Dit staat in docDefaults, dus het werkt door in
                # alles wat geen eigen grootte draagt; koppen doen dat wel en blijven.
                # Zowel sz als szCs, anders blijft de gewone tekst op de oude maat staan.
                def maat(m):
                    return re.sub(r'(<w:sz(?:Cs)? w:val=")\d+', r"\g<1>" + BASISGROOTTE, m.group(0))

                tekst = re.sub(r"<w:docDefaults>.*?</w:docDefaults>", maat, tekst,
                               count=1, flags=re.DOTALL)
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


# Breedte van de tekstkolom in twips: de paginabreedte min de marges, zie MARGES.
TEKSTBREEDTE = 11906 - 1134 - 1134
TEKEN = 88    # gemiddelde tekenbreedte bij 9 punt, in twips
CELMARGE = 220  # wat een cel links en rechts zelf al opeet

TABEL = re.compile(r"<w:tbl>.*?</w:tbl>", re.DOTALL)
RIJ = re.compile(r"<w:tr\b.*?</w:tr>", re.DOTALL)
CEL = re.compile(r"<w:tc>.*?</w:tc>", re.DOTALL)
CELTEKST = re.compile(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", re.DOTALL)
TBLGRID = re.compile(r"<w:tblGrid>.*?</w:tblGrid>", re.DOTALL)


def kolombreedtes(kolommen: list) -> list:
    """Verdeelt de tekstbreedte over de kolommen, naar wat erin staat.

    De breedte groeit mee met de langste cel, maar gedempt (macht 0,7). Ongedempt zou
    een kolom met één lange zin bijna de hele tabel opeisen; ongewogen krijgt een kolom
    met "FR1" evenveel als een kolom met een volzin, en dat is precies wat het leest als
    twee halve tabellen.

    Ondergrens per kolom is haar langste ononderbroken woord. Daaronder breekt Word een
    woord middenin af ("Wijziginge n tussen"), en dat was de oorspronkelijke klacht.
    """
    gewichten = [max(1, max(len(c) for c in kolom)) ** 0.7 for kolom in kolommen]
    breedtes = [TEKSTBREEDTE * g / sum(gewichten) for g in gewichten]

    minima = []
    for kolom in kolommen:
        woorden = [w for cel in kolom for w in cel.split()] or [""]
        minima.append(len(max(woorden, key=len)) * TEKEN + CELMARGE)
    # Passen de ondergrenzen samen niet op de pagina, dan zijn ze geen ondergrens meer.
    if sum(minima) > TEKSTBREEDTE:
        krimp = TEKSTBREEDTE / sum(minima)
        minima = [m * krimp for m in minima]

    for _ in range(len(breedtes)):
        tekort = sum(m - b for b, m in zip(breedtes, minima) if b < m)
        if tekort <= 0:
            break
        ruim = [i for i, (b, m) in enumerate(zip(breedtes, minima)) if b > m]
        speling = sum(breedtes[i] - minima[i] for i in ruim)
        if speling <= 0:
            break
        for i in ruim:
            breedtes[i] -= tekort * (breedtes[i] - minima[i]) / speling
        breedtes = [max(b, m) for b, m in zip(breedtes, minima)]

    afgerond = [int(round(b)) for b in breedtes]
    afgerond[-1] += TEKSTBREEDTE - sum(afgerond)  # afrondingsrest op de laatste kolom
    return afgerond


def tabellen_laten_meebewegen(docx: pathlib.Path) -> None:
    """Geeft elke kolom de breedte die bij haar inhoud past.

    Pandoc schrijft geen enkele breedte in het document. Dan verdeelt de lezer de ruimte
    gelijk: een kolom met "#" krijgt evenveel als een kolom met een volzin. Autofit
    aanzetten hielp niet, want zonder breedtes in het raster valt de renderer terug op
    diezelfde gelijke verdeling. De breedtes worden hier dus uitgerekend en vastgelegd.
    """
    z = zipfile.ZipFile(docx)
    onderdelen = {i.filename: z.read(i.filename) for i in z.infolist()}
    z.close()
    xml = onderdelen["word/document.xml"].decode("utf-8")

    def vervang(m):
        tabel = m.group(0)
        rijen = [[re.sub(r"\s+", " ", "".join(CELTEKST.findall(cel))).strip()
                  for cel in CEL.findall(rij)] for rij in RIJ.findall(tabel)]
        rijen = [r for r in rijen if r]
        if not rijen:
            return tabel
        aantal = max(len(r) for r in rijen)
        kolommen = [[r[i] for r in rijen if i < len(r)] for i in range(aantal)]
        breedtes = kolombreedtes(kolommen)

        raster = "".join(f'<w:gridCol w:w="{b}" />' for b in breedtes)
        tabel = TBLGRID.sub(f"<w:tblGrid>{raster}</w:tblGrid>", tabel, count=1)
        tabel = tabel.replace('<w:tblLayout w:type="autofit" />',
                              '<w:tblLayout w:type="fixed" />')
        # De cel draagt haar breedte zelf ook: niet elke lezer leest het raster.
        def per_rij(rm):
            kolom = [0]

            def per_cel(cm):
                i = min(kolom[0], aantal - 1)
                kolom[0] += 1
                return cm.group(0).replace(
                    "<w:tcPr />",
                    f'<w:tcPr><w:tcW w:w="{breedtes[i]}" w:type="dxa" /></w:tcPr>', 1)

            return CEL.sub(per_cel, rm.group(0))

        return RIJ.sub(per_rij, tabel)

    xml = xml.replace('<w:tblW w:type="auto" w:w="0" />',
                      '<w:tblW w:type="pct" w:w="5000" /><w:tblLayout w:type="autofit" />')
    xml = TABEL.sub(vervang, xml)
    onderdelen["word/document.xml"] = xml.encode("utf-8")
    with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as uit:
        for naam, inhoud in onderdelen.items():
            uit.writestr(naam, inhoud)


EINDE_ALINEA = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
# Tussen het pagina-einde en de alinea erna staan de bookmarks van de anchors.
NA_EINDE = re.compile(
    re.escape(EINDE_ALINEA) + r"\s*((?:<w:bookmark(?:Start|End)\b[^>]*/>\s*)*)(<w:p\b[^>]*>)"
    r"(<w:pPr>)?")
# De volgorde van de kinderen van pPr ligt vast; pageBreakBefore hoort na deze drie.
VOOR_EINDE = re.compile(r"(?:<w:(?:pStyle|keepNext|keepLines)\b[^>]*/>\s*)*")


def paginaeinden_verankeren(docx: pathlib.Path) -> None:
    """Hangt elk pagina-einde aan de alinea erna in plaats van aan een lege alinea.

    Een einde in een eigen lege alinea levert een blanco pagina op zodra de pagina
    ervoor tot de laatste regel vol staat: die lege alinea past er dan niet meer bij,
    schuift naar de volgende pagina, en het einde erin duwt de inhoud nog een pagina
    verder. Als eigenschap van de kop erna kan dat niet gebeuren, want er is dan geen
    lege alinea die zelf nog een regel vraagt.

    Volgt er geen alinea maar bijvoorbeeld een tabel, dan blijft het einde staan zoals
    het was: een tabel draagt de eigenschap niet.
    """
    z = zipfile.ZipFile(docx)
    onderdelen = {i.filename: z.read(i.filename) for i in z.infolist()}
    z.close()
    xml = onderdelen["word/document.xml"].decode("utf-8")

    stukken, i = [], 0
    for m in NA_EINDE.finditer(xml):
        bookmarks, alinea, ppr = m.group(1), m.group(2), m.group(3)
        stukken.append(xml[i:m.start()])
        if ppr is None:
            stukken.append(f"{bookmarks}{alinea}<w:pPr><w:pageBreakBefore /></w:pPr>")
            i = m.end()
        else:
            # Achter de kinderen die volgens het schema voorgaan.
            plek = VOOR_EINDE.match(xml, m.end()).end()
            stukken.append(f"{bookmarks}{alinea}{ppr}{xml[m.end():plek]}"
                           "<w:pageBreakBefore />")
            i = plek
    stukken.append(xml[i:])

    onderdelen["word/document.xml"] = "".join(stukken).encode("utf-8")
    with zipfile.ZipFile(docx, "w", zipfile.ZIP_DEFLATED) as doel:
        for naam, inhoud in onderdelen.items():
            doel.writestr(naam, inhoud)


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
    paden = paden_van(documenten)
    basisnaam = f"{manifest['bestandsnaam']}-v{versie}"

    ontbreekt = [d for d in paden if not (pakket / d).exists()]
    if ontbreekt:
        print("manifest noemt documenten die niet bestaan:", file=sys.stderr)
        for d in ontbreekt:
            print(f"  {d}", file=sys.stderr)
        return 1

    op_schijf = {p.relative_to(pakket).as_posix() for p in pakket.rglob("*.md")}
    vergeten = sorted(op_schijf - set(paden))
    if vergeten:
        print("let op: deze markdown-bestanden staan niet in het manifest en gaan niet mee:")
        for d in vergeten:
            print(f"  {d}")

    uit = pathlib.Path(tempfile.mkdtemp(prefix="okx-release-")) if args.alleen_controle else args.uit
    uit.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="okx-bouw-") as tmp:
        werk = pathlib.Path(tmp)
        beelden = werk / "diagrammen"
        kaart = bouw_anchorkaart(pakket, paden)
        teller, mislukt = [0], []
        referentie = referentiedocument(werk)

        print(f"{manifest['naam']} v{versie}: {len(paden)} documenten")

        losse, gebundelde_delen = [], []

        def bouw_deel(doc: str, in_sectie: bool) -> str:
            """Zet één document klaar: los voor de zip, en als deel van de bundel."""
            ruw = (pakket / doc).read_text(encoding="utf-8")
            met_beelden = render_mermaid(ruw, doc, beelden, teller, mislukt, args.streng)

            # Losse variant: verwijzingen naar GitHub, eigen anchors blijven.
            los = herschrijf_links(met_beelden, doc, pakket, paden, kaart,
                                   False, args.repo_url, args.ref)
            los_pad = werk / "los" / uitvoerpad(doc)
            los_pad.parent.mkdir(parents=True, exist_ok=True)
            los_pad.write_text(los, encoding="utf-8")
            losse.append((doc, los_pad))

            # Gebundelde variant: unieke kop-id's, interne verwijzingen, een niveau dieper.
            deel = herschrijf_links(met_beelden, doc, pakket, paden, kaart,
                                    True, args.repo_url, args.ref)
            deel = geef_koppen_ids(deel, doc, kaart)
            return verlaag_koppen(deel, 2 if in_sectie else 1)

        inhoud_op = None

        for item in documenten:
            if isinstance(item, str):
                gebundelde_delen.append(bouw_deel(item, False))
                continue
            if item.get("inhoudsopgave"):
                # De inhoudsopgave draagt de nummers van de koppen, en die staan pas
                # vast als alle delen er zijn. Nu een plaats vrijhouden, straks vullen.
                inhoud_op = len(gebundelde_delen)
                gebundelde_delen.append("")
                continue
            # De sectiekop en zijn inleiding vormen één deel: anders valt er een
            # pagina-einde tussen, en blijft de kop alleen op een pagina achter.
            kop = f"## {item['sectie']} {{#{sectie_anchor(item, kaart)}}}"
            subdocumenten = item.get("documenten") or []
            if item.get("inleiding"):
                kop += "\n\n" + zonder_titel(bouw_deel(item["inleiding"], False))
            elif subdocumenten:
                # Zonder inleiding is er niets om de kop gezelschap te houden en houdt
                # hij een pagina voor zich alleen. Dan maar samen met het eerste document.
                kop += "\n\n" + bouw_deel(subdocumenten[0], True)
                subdocumenten = subdocumenten[1:]
            gebundelde_delen.append(kop)
            for doc in subdocumenten:
                gebundelde_delen.append(bouw_deel(doc, True))
            if item.get("schemas"):
                # Achter de documenten, want de inhoudsopgave zet ze daar ook. En als
                # één deel: elk schema een eigen pagina zou een bijlage van
                # vijfentwintig halflege pagina's opleveren.
                gebundelde_delen.append(schema_bijlage(pakket, item))

        # Noemt het manifest geen plek, dan staat de inhoudsopgave achter de titelpagina.
        if inhoud_op is None:
            inhoud_op = 0
            gebundelde_delen.insert(0, "")

        gebundelde_delen, nummers = nummer_delen(gebundelde_delen, {inhoud_op})
        gebundelde_delen[inhoud_op] = bouw_inhoudsopgave(pakket, documenten, kaart, nummers)

        print(f"  {teller[0] - len(mislukt)} van {teller[0]} mermaid-diagrammen gerenderd")
        for doc, n, reden in mislukt:
            print(f"    blijft codeblok: {doc} (diagram {n}) - {reden}")

        # Gebundeld document.
        titel = (f"# {manifest['naam']}\n\n{manifest.get('omschrijving', '')}\n\n"
                 f"Versie {versie}\n")
        gebundeld_md = werk / "gebundeld.md"
        gebundeld_md.write_text(
            titel + PAGINA_EINDE + PAGINA_EINDE.join(gebundelde_delen), encoding="utf-8")
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
        paginaeinden_verankeren(gebundeld_docx)
        print(f"  {gebundeld_docx.name}")

        # Losse documenten in een zip, mapstructuur behouden.
        zip_pad = uit / f"{basisnaam}-documenten.zip"
        with zipfile.ZipFile(zip_pad, "w", zipfile.ZIP_DEFLATED) as z:
            for doc, pad in losse:
                docx = werk / "docx" / (uitvoerpad(doc)[:-3] + ".docx")
                docx.parent.mkdir(parents=True, exist_ok=True)
                pandoc([
                    "-f", "gfm", "-t", "docx",
                    "--reference-doc", str(referentie),
                            "--resource-path", str(werk),
                    "-o", str(docx), str(pad),
                ])
                tabellen_laten_meebewegen(docx)
                z.write(docx, uitvoerpad(doc)[:-3] + ".docx")
            for extra in manifest.get("meeleveren", []):
                bron = pakket / extra
                if bron.is_dir():
                    for bestand in sorted(bron.rglob("*")):
                        naam = bestand.relative_to(pakket).as_posix()
                        # Een document uit het manifest zit al als docx in de zip; de
                        # markdown-bron er dan naast leggen levert twee versies op.
                        if bestand.is_file() and naam not in paden:
                            z.write(bestand, naam)
                elif bron.is_file():
                    z.write(bron, extra)
        print(f"  {zip_pad.name}")

    if args.alleen_controle:
        shutil.rmtree(uit, ignore_errors=True)
        print("controle geslaagd, artefacten verwijderd")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
