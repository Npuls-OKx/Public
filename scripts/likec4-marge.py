#!/usr/bin/env python3
"""Zet geëxporteerde LikeC4-platen op een witte ondergrond, met lucht eromheen.

LikeC4 exporteert met een transparante achtergrond en een krappe marge. Zonder
ondergrond vallen de titels van de doorzichtige containers weg in een donkere
viewer, en zonder marge plakt de bovenste rij blokken tegen de rand.

    python3 scripts/likec4-marge.py <beeldmap> [bestandsnaam ...]
"""

from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

MARGE_BOVEN_ONDER = 90
MARGE_ZIJKANT = 40


def met_marge(plaat: Image.Image) -> Image.Image:
    """Legt wit onder de plaat en zet er marge omheen."""
    ondergrond = Image.new(
        "RGBA",
        (plaat.width + 2 * MARGE_ZIJKANT, plaat.height + 2 * MARGE_BOVEN_ONDER),
        (255, 255, 255, 255),
    )
    ondergrond.alpha_composite(plaat.convert("RGBA"), (MARGE_ZIJKANT, MARGE_BOVEN_ONDER))
    return ondergrond.convert("RGB")


def main(argumenten: list[str]) -> int:
    if not argumenten:
        print(__doc__, file=sys.stderr)
        return 2

    beeldmap = Path(argumenten[0])
    namen = argumenten[1:] or sorted(p.name for p in beeldmap.glob("*.png"))
    for naam in namen:
        pad = beeldmap / naam
        plaat = met_marge(Image.open(pad))
        plaat.save(pad)
        print(f"{pad}: {plaat.width}x{plaat.height}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
