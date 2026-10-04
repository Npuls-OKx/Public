#!/usr/bin/env python3
"""Zet de geëxporteerde platen in een map per categorie, met een leesbare naam.

De titel van een view draagt zijn indeling: `Referentie / Koppelvlak van de
onderwijscatalogus` wordt `referentie/koppelvlak-van-de-onderwijscatalogus.png`.
De map en de bestandsnaam volgen dus uit het model, zodat ze niet apart hoeven
te worden bijgehouden.

    python3 scripts/likec4-plaatsen.py <bronmap> <doelmap> [likec4.json]
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path


def slug(tekst: str) -> str:
    """Maakt een bestandsnaam van een titel: kleine letters, streepjes, geen accenten."""
    zonder_accent = "".join(
        teken for teken in unicodedata.normalize("NFKD", tekst)
        if not unicodedata.combining(teken)
    )
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", zonder_accent.lower())).strip("-")


def doelpad(titel: str, view_id: str) -> Path:
    """`Categorie / Naam` wordt `categorie/naam.png`; zonder categorie de view-id."""
    delen = [deel.strip() for deel in titel.split("/")] if titel else []
    if len(delen) < 2:
        return Path(f"{slug(view_id)}.png")
    return Path(*[slug(deel) for deel in delen[:-1]]) / f"{slug(delen[-1])}.png"


def main(argumenten: list[str]) -> int:
    if len(argumenten) < 2:
        print(__doc__, file=sys.stderr)
        return 2

    bronmap, doelmap = Path(argumenten[0]), Path(argumenten[1])
    model = json.loads(Path(argumenten[2] if len(argumenten) > 2 else "likec4.json").read_text())

    if doelmap.exists():
        shutil.rmtree(doelmap)

    for view_id, view in sorted(model["views"].items()):
        bron = bronmap / f"{view_id}.png"
        if not bron.exists():
            print(f"{view_id}: geen plaat gerenderd", file=sys.stderr)
            continue
        doel = doelmap / doelpad(view.get("title") or "", view_id)
        doel.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(bron, doel)
        print(doel)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
