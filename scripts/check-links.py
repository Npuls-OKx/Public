#!/usr/bin/env python3
"""Controleert markdown-verwijzingen in dit repository.

Drie soorten fouten, elk uit de praktijk:

1. Dode link: het doelbestand bestaat niet.
2. Ontsnapping: de link wijst met genoeg `../` buiten het repository. Zo'n link
   kan lokaal toevallig resolveren naar een bestand in een naburige map en dus
   ten onrechte "goed" lijken, terwijl hij op GitHub altijd stuk is.
3. Dode anchor: het fragment (`#kopje`) heeft geen bijbehorende kop.

Voor anchors telt het algoritme van GitHub, niet dat van een willekeurige
markdown-renderer: kleine letters, leestekens weg, en daarna wordt *elke*
spatie afzonderlijk een koppelstreep. Een em-streep in een kop laat dus twee
spaties achter en levert een dubbele koppelstreep op:

    ### OKx-AP05 - Referentiecomponenten   ->  #okx-ap05--referentiecomponenten

Gebruik:
    python3 scripts/check-links.py            # hele repository
    python3 scripts/check-links.py <pad> ...  # alleen deze bestanden of mappen
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

LINK = re.compile(r"\]\(([^)]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*)")
HTML_ANKER = re.compile(r"<a\s+id=\"([^\"]+)\"\s*>")
EXTERN = ("http://", "https://", "mailto:", "tel:")


def slugs(tekst: str) -> set[str]:
    """De anchors die GitHub voor dit document aanmaakt.

    Naast kop-anchors telt een expliciet HTML-anker (`<a id="..."></a>`) mee;
    GitHub rendert die in markdown, bijvoorbeeld bij id's in tabelrijen.
    """
    gevonden: set[str] = set()
    in_codeblok = False
    for regel in tekst.splitlines():
        if regel.lstrip().startswith("```"):
            in_codeblok = not in_codeblok
            continue
        if in_codeblok:
            continue
        gevonden.update(HTML_ANKER.findall(regel))
        kop = HEADING.match(regel)
        if not kop:
            continue
        s = kop.group(1).strip()
        # GitHub slugt over de gerenderde koptekst: linkmarkup eerst strippen,
        # anders krijgt een kop-als-link (## [Naam](doel.md)) een fout anchor.
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s).lower()
        s = re.sub(r"[^\w\s-]", "", s)   # leestekens weg, spaties blijven
        gevonden.add(re.sub(r"\s", "-", s))  # elke spatie apart
    return gevonden


def doorlopen_symlink(doel: Path, root: Path) -> Path | None:
    """De symlink die dit pad doorloopt, of None.

    GitHub volgt symlinks niet in blob-URL's. Een link door een symlink heen
    werkt dus lokaal wel en in de webweergave niet.
    """
    try:
        deel_pad = doel.relative_to(root)
    except ValueError:
        return None
    huidig = root
    for deel in deel_pad.parts:
        huidig = huidig / deel
        if huidig.is_symlink():
            return huidig
    return None


def markdown_bestanden(paden: list[str], root: Path) -> list[Path]:
    def uit_map(p: Path) -> list[Path]:
        # Symlinks overslaan: die leveren hetzelfde bestand nog een keer op.
        return [q for q in p.rglob("*.md") if ".git" not in q.parts and not q.is_symlink()]

    if not paden:
        return sorted(uit_map(root))
    uit: list[Path] = []
    for pad in paden:
        p = Path(pad).resolve()
        if p.is_dir():
            uit += uit_map(p)
        elif p.suffix == ".md":
            uit.append(p)
    return sorted(set(uit))


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    bestanden = markdown_bestanden(argv, root)
    if not bestanden:
        print("Geen markdown-bestanden gevonden.")
        return 0

    anchor_cache: dict[Path, set[str]] = {}
    problemen = 0

    for bestand in bestanden:
        try:
            inhoud = bestand.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as fout:
            print(f"ONLEESBAAR   {bestand.relative_to(root)}: {fout}")
            problemen += 1
            continue

        for treffer in LINK.finditer(inhoud):
            link = treffer.group(1).strip()
            if link.startswith(EXTERN) or not link:
                continue

            pad, _, fragment = link.partition("#")
            hier = bestand.relative_to(root)

            # Lexicaal normaliseren, niet resolven: GitHub lost paden ook
            # lexicaal op en volgt daarbij geen symlinks.
            doel = (
                bestand
                if not pad
                else Path(os.path.normpath(bestand.parent / unquote(pad)))
            )

            if not str(doel).startswith(str(root)):
                print(f"ONTSNAPT     {hier} -> {link}")
                print("             wijst buiten het repository; op GitHub altijd stuk")
                problemen += 1
                continue

            if not doel.exists():
                print(f"DOOD         {hier} -> {link}")
                problemen += 1
                continue

            schakel = doorlopen_symlink(doel, root)
            if schakel is not None:
                print(f"VIA SYMLINK  {hier} -> {link}")
                print(
                    f"             loopt door {schakel.relative_to(root)}; "
                    "GitHub volgt symlinks niet, verwijs naar het echte pad"
                )
                problemen += 1
                continue

            if not fragment or doel.is_dir() or doel.suffix != ".md":
                continue

            if doel not in anchor_cache:
                anchor_cache[doel] = slugs(doel.read_text(encoding="utf-8"))
            if fragment not in anchor_cache[doel]:
                print(f"ANCHOR       {hier} -> {link}")
                print(f"             geen kop met dat anchor in {doel.relative_to(root)}")
                problemen += 1

    aantal = len(bestanden)
    if problemen:
        print(f"\nNIET SCHOON: {problemen} probleem(en) in {aantal} bestand(en).")
        return 1
    print(f"SCHOON - alle verwijzingen in {aantal} bestand(en) resolveren.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
