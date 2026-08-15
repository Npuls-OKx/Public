#!/usr/bin/env python3
"""Controleert de documentconventies van dit repository.

De documenten hier worden gereleased. Een lezer daarvan heeft geen toegang tot
het werkproces erachter: geen issues, geen pull requests, geen kennis van wie
wanneer wat besloot. Daar volgen vijf controles uit.

1. Geen issueverwijzingen. Een issuenummer zegt zo'n lezer niets en veroudert.
   Schrijf de aanleiding uit in de inleiding.
2. Geen metadatakop. Auteur, datum en status komen uit de git-historie.
3. Geen datum- of versieprefix in bestandsnamen. Dat is een werkproces-conventie.
4. Verwijzingen naar de meta-repository zijn gepind op een commit. Een link naar
   een branch beweegt mee met de bron; een gereleased document mag dat niet.
5. Geen werkprocessecties: Reviewvragen, Open punten, Gerelateerde uitwerkingen.
   Een reviewvraag is een vraag aan de auteur, geen informatie voor de lezer; een
   open punt hoort in het werkproces; een lijst gerelateerde uitwerkingen herhaalt
   verwijzingen die al in de tekst staan.

Daarnaast een zachte controle: documenten met een genummerde inleiding horen
aanleiding, context, doel en scope te benoemen.

Gebruik:
    python3 scripts/check-conventies.py            # hele repository
    python3 scripts/check-conventies.py <pad> ...  # alleen deze bestanden of mappen
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Issueverwijzingen. Anchors (`](#kopje)`) en hexkleuren (`fill:#fff`) vallen af
# doordat er een cijfer direct achter het hekje moet staan en er geen `(`, `:`
# of woordteken voor mag staan.
ISSUE = re.compile(r"(?<![\w/#:(-])(?:[\w.-]+/[\w.-]+)?#\d+\b")
# Losse anchors zoals `](#33-lifecycle)` alsnog uitsluiten: cijfer gevolgd door
# een koppelstreep en letters is een kopnummer, geen issue.
ANCHOR_ACHTIG = re.compile(r"#\d+-[a-z]")

METADATAKOP = re.compile(
    r"^\s*(?:\*\*)?(Relateert aan|Status|Datum|Auteur|Versie|Eigenaar)(?:\*\*)?\s*:",
    re.IGNORECASE,
)
DATUMPREFIX = re.compile(r"^\d{6,8}[_-]")
META_BRANCH = re.compile(
    r"https://github\.com/Npuls-OKx/meta/(?:blob|tree|raw)/(main|dev|master|refs/heads/[^/\s)]+)/"
)
INLEIDING = re.compile(r"^#{2,3}\s+1\.\s+Inleiding", re.MULTILINE)
# Werkprocessecties. Ze horen bij het uitwerken, niet bij het uitgebrachte document.
WERKPROCESKOP = re.compile(
    r"^#{2,4}\s+(?:\d+(?:\.\d+)*\.?\s+)?(Reviewvragen|Open punten|Gerelateerde uitwerkingen)\s*$",
    re.MULTILINE | re.IGNORECASE,
)


INLINE_CODE = re.compile(r"`[^`]*`")


def zonder_inline_code(regel: str) -> str:
    """Wat tussen backticks staat is een letterlijke weergave, geen verwijzing.

    Een document dat uitlegt dat je nooit `#123` moet schrijven, schrijft dat
    voorbeeld als code. Dat is geen issueverwijzing.
    """
    return INLINE_CODE.sub("", regel)


def regels_buiten_codeblokken(inhoud: str):
    """(regelnummer, regel) voor alles buiten ``` -blokken en HTML-commentaar."""
    in_codeblok = False
    in_comment = False
    for nr, regel in enumerate(inhoud.splitlines(), 1):
        if regel.lstrip().startswith("```"):
            in_codeblok = not in_codeblok
            continue
        if in_codeblok:
            continue
        if "<!--" in regel and "-->" not in regel:
            in_comment = True
            continue
        if in_comment:
            if "-->" in regel:
                in_comment = False
            continue
        yield nr, regel


def markdown_bestanden(paden: list[str], root: Path) -> list[Path]:
    if not paden:
        alles = root.rglob("*.md")
    else:
        alles = []
        for pad in paden:
            p = Path(pad).resolve()
            if p.is_dir():
                alles += list(p.rglob("*.md"))
            elif p.suffix == ".md":
                alles.append(p)
    # Symlinks overslaan: die leveren hetzelfde bestand nog een keer op.
    return sorted({p for p in alles if ".git" not in p.parts and not p.is_symlink()})


def controleer(bestand: Path, root: Path) -> list[str]:
    hier = bestand.relative_to(root)
    inhoud = bestand.read_text(encoding="utf-8")
    # Een template herken je aan de map waarin hij staat of aan zijn naam. De
    # inleiding van een template is een invulinstructie; die kan per definitie
    # geen uitgeschreven aanleiding, doel en scope dragen.
    is_template = "templates" in bestand.parts or "template" in bestand.stem.lower()
    # Referentiemateriaal is overgenomen bronmateriaal. Een ADR hoort een status
    # en een datum te dragen; dat is onderdeel van het ADR-format en niet het
    # soort metadatakop dat we in het releasepakket willen vermijden.
    is_referentie = "Referentiemateriaal" in bestand.parts
    meldingen: list[str] = []

    if DATUMPREFIX.match(bestand.name):
        meldingen.append(
            f"BESTANDSNAAM {hier}\n"
            "             datum- of versieprefix; datum komt uit de git-historie"
        )

    kop_marge = 12  # een metadatakop staat bovenaan, niet halverwege
    for nr, regel in regels_buiten_codeblokken(inhoud):
        for treffer in ISSUE.finditer(zonder_inline_code(regel)):
            fragment = regel[treffer.start(): treffer.start() + 12]
            if ANCHOR_ACHTIG.match(fragment.lstrip("]").lstrip("(")):
                continue
            meldingen.append(
                f"ISSUEREF     {hier}:{nr}  {treffer.group(0)}\n"
                "             schrijf de aanleiding uit in de inleiding"
            )

        if nr <= kop_marge and not is_referentie and METADATAKOP.match(regel):
            meldingen.append(
                f"METADATAKOP  {hier}:{nr}  {regel.strip()[:60]}\n"
                "             auteur, datum en status komen uit de git-historie"
            )

        for treffer in META_BRANCH.finditer(regel):
            meldingen.append(
                f"BRANCHLINK   {hier}:{nr}  meta/{treffer.group(1)}\n"
                "             pin op een commit-SHA; een branch beweegt mee met de bron"
            )

    if not is_referentie:
        for treffer in WERKPROCESKOP.finditer(inhoud):
            nr = inhoud.count("\n", 0, treffer.start()) + 1
            meldingen.append(
                f"WERKPROCES   {hier}:{nr}  {treffer.group(1)}\n"
                "             hoort bij het uitwerken, niet in een uitgebracht document; "
                "wat de lezer nodig heeft staat in de tekst zelf"
            )

    if INLEIDING.search(inhoud) and not is_template:
        # Twee vormen zijn goed: een genummerde subkop (specificaties) of een
        # vetgedrukte aanhef in de lopende tekst (kortere beleidsdocumenten).
        # De conventie gaat over de inhoud, niet over de vorm van de kop.
        ontbreekt = [
            naam
            for naam, woord in (
                ("aanleiding", "Aanleiding"),
                ("doel", "Doel"),
                ("scope", "Scope"),
            )
            if not re.search(
                rf"\*\*{woord}\.?\*\*|#{{2,4}}\s+\d+(?:\.\d+)*\.?\s+{woord}\b",
                inhoud,
            )
        ]
        if ontbreekt:
            meldingen.append(
                f"INLEIDING    {hier}\n"
                f"             mist: {', '.join(ontbreekt)}; "
                "een inleiding benoemt aanleiding, context, doel en scope"
            )

    return meldingen


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    bestanden = markdown_bestanden(argv, root)
    if not bestanden:
        print("Geen markdown-bestanden gevonden.")
        return 0

    problemen = 0
    for bestand in bestanden:
        for melding in controleer(bestand, root):
            print(melding)
            problemen += 1

    if problemen:
        print(f"\nNIET SCHOON: {problemen} probleem(en) in {len(bestanden)} bestand(en).")
        return 1
    print(f"SCHOON - {len(bestanden)} bestand(en) voldoen aan de conventies.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
