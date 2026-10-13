#!/usr/bin/env python3
"""Berekent de plaatsing van LikeC4-views zonder relaties en legt die vast.

LikeC4 laat graphviz de plaatsing doen. Dat werkt goed zolang een view relaties
draagt: die leveren de rangen en de plaatsing volgt daaruit. Op een view zonder
relaties valt die sturing weg. LikeC4 rijgt de groepen dan aan elkaar met
onzichtbare edges van een knoop in de ene groep naar een knoop in de volgende,
waardoor een groep onder dát punt hangt in plaats van onder de linkerrand van
zijn voorganger. Er blijft ruimte leeg en de volgorde van de groepen is niet te
sturen: `rank same` werkt alleen op knopen, en een groep is een cluster dat geen
rang krijgt.

Dit script rekent zulke views opnieuw uit, van binnen naar buiten. Blokken zonder
kinderen gaan in een raster; elk niveau daarboven legt zijn kinderen op planken,
de grootste eerst, elke plank van links naar rechts gevuld. Het resultaat gaat
als `<view>.likec4.snap` naar `<modelmap>/.likec4/`, de map waarin LikeC4
handmatige layouts zoekt, zodat de export die gebruikt.

De snapshots zijn een afgeleide, geen bron: `likec4-render.sh` gooit ze elke keer
weg en maakt ze opnieuw uit het model. Blijft een verouderde snapshot staan, dan
meldt `likec4 validate` dat als "layout drift".

    python3 scripts/likec4-layout.py <modelmap> [likec4.json]
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

# Maten overgenomen uit wat LikeC4 zelf produceert, zodat de platen er hetzelfde uitzien.
RAND = 8            # marge tussen de plaat en de buitenste groep
PADDING = 40        # ruimte tussen een groepsrand en wat erin staat
PADDING_BOVEN = 61  # idem aan de bovenkant, waar de groepstitel staat
TUSSENRUIMTE = 40   # ruimte tussen twee blokken binnen een groep
PLANKRUIMTE = 24    # ruimte tussen twee groepen op dezelfde plank

# Boven deze breedte breekt een plank af. Per nestniveau blijft er minder over,
# want elk niveau kost aan weerszijden zijn eigen padding.
MAX_BREEDTE = 1900


def kolommen(aantal: int) -> int:
    """Eén rij tot en met drie blokken, daarboven een zo vierkant mogelijk raster."""
    if aantal <= 3:
        return max(aantal, 1)
    return math.ceil(math.sqrt(aantal))


def verplaats(knoop: dict, dx: int, dy: int) -> None:
    """Schuift een knoop en alles wat eronder hangt."""
    knoop["x"] += dx
    knoop["y"] += dy
    for kind in knoop["_kinderen"]:
        verplaats(kind, dx, dy)


def raster(blokken: list[dict], links: int, boven: int) -> tuple[int, int]:
    """Zet blokken in een raster met de linkerbovenhoek op (links, boven)."""
    per_rij = kolommen(len(blokken))
    rijen = [blokken[i:i + per_rij] for i in range(0, len(blokken), per_rij)]
    kolombreedte = [
        max((rij[k]["width"] for rij in rijen if k < len(rij)), default=0)
        for k in range(per_rij)
    ]
    rijhoogte = [max(b["height"] for b in rij) for rij in rijen]

    y = boven
    for rij, hoogte in zip(rijen, rijhoogte):
        x = links
        for k, blok in enumerate(rij):
            verplaats(blok, x - blok["x"], y + (hoogte - blok["height"]) // 2 - blok["y"])
            x += kolombreedte[k] + TUSSENRUIMTE
        y += hoogte + TUSSENRUIMTE

    return (
        sum(kolombreedte) + TUSSENRUIMTE * (per_rij - 1),
        sum(rijhoogte) + TUSSENRUIMTE * (len(rijen) - 1),
    )


def planken(groepen: list[dict], links: int, boven: int, max_breedte: int) -> tuple[int, int]:
    """Legt groepen op planken, de grootste eerst, elke plank van links naar rechts."""
    volgorde = {g["id"]: i for i, g in enumerate(groepen)}
    gesorteerd = sorted(groepen, key=lambda g: (-len(g["children"]), volgorde[g["id"]]))

    rijen: list[list[dict]] = []
    breedte_op_plank = 0
    for groep in gesorteerd:
        nodig = groep["width"] + (PLANKRUIMTE if breedte_op_plank else 0)
        if not rijen or breedte_op_plank + nodig > max_breedte:
            rijen.append([])
            breedte_op_plank = 0
            nodig = groep["width"]
        rijen[-1].append(groep)
        breedte_op_plank += nodig

    y = boven
    breedste = 0
    for rij in rijen:
        hoogte = max(g["height"] for g in rij)
        x = links
        for groep in rij:
            verplaats(groep, x - groep["x"], y - groep["y"])
            x += groep["width"] + PLANKRUIMTE
        breedste = max(breedste, x - PLANKRUIMTE - links)
        y += hoogte + PLANKRUIMTE

    return breedste, y - PLANKRUIMTE - boven


def leg_uit(knoop: dict, max_breedte: int) -> None:
    """Plaatst eerst de inhoud, dan pas de knoop eromheen. Van binnen naar buiten."""
    kinderen = knoop["_kinderen"]
    if not kinderen:
        return

    ruimte = max_breedte - 2 * PADDING
    for kind in kinderen:
        leg_uit(kind, ruimte)

    if all(not kind["_kinderen"] for kind in kinderen):
        breedte, hoogte = raster(kinderen, knoop["x"] + PADDING, knoop["y"] + PADDING_BOVEN)
    else:
        breedte, hoogte = planken(kinderen, knoop["x"] + PADDING, knoop["y"] + PADDING_BOVEN, ruimte)

    knoop["width"] = breedte + 2 * PADDING
    knoop["height"] = PADDING_BOVEN + hoogte + PADDING


def leg_view_uit(view: dict, max_breedte: int = MAX_BREEDTE) -> dict:
    """Herberekent de plaatsing van één view. Wijzigt en geeft dezelfde view terug."""
    knopen = {n["id"]: n for n in view["nodes"]}
    for knoop in view["nodes"]:
        knoop["_kinderen"] = [knopen[k] for k in knoop["children"]]

    wortels = [n for n in view["nodes"] if n["parent"] is None]
    for wortel in wortels:
        leg_uit(wortel, max_breedte)
    breedte, hoogte = planken(wortels, RAND, RAND, max_breedte)

    view["bounds"] = {"x": 0, "y": 0, "width": breedte + 2 * RAND, "height": hoogte + 2 * RAND}
    for knoop in view["nodes"]:
        del knoop["_kinderen"]
    return view


def te_plaatsen(model: dict) -> list[str]:
    """De views die dit script aankan: geen relaties, dus geen kantpunten te berekenen."""
    return sorted(
        view_id for view_id, view in model["views"].items()
        if not view["edges"] and view["nodes"]
    )


def main(argumenten: list[str]) -> int:
    if not argumenten:
        print(__doc__, file=sys.stderr)
        return 2

    modelmap = Path(argumenten[0])
    bron = Path(argumenten[1]) if len(argumenten) > 1 else Path("likec4.json")
    if not bron.exists():
        print(f"{bron} ontbreekt; draai eerst: npx likec4 export json {modelmap}", file=sys.stderr)
        return 1

    model = json.loads(bron.read_text())
    doelmap = modelmap / ".likec4"
    doelmap.mkdir(parents=True, exist_ok=True)

    for view_id in te_plaatsen(model):
        view = leg_view_uit(model["views"][view_id])
        pad = doelmap / f"{view_id}.likec4.snap"
        pad.write_text(json.dumps(view, indent=2, ensure_ascii=False) + "\n")
        print(f"{pad}: {view['bounds']['width']}x{view['bounds']['height']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
