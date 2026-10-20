#!/usr/bin/env python3
"""Legt de hoofdplaatviews vast: in elke view dezelfde plaat, met de koppeling erboven.

Een hoofdplaatview, met een titel die begint met `Hoofdplaat /`, toont waar één
koppeling op de informatiestromen-hoofdplaat ligt. Graphviz legt de componenten
per view anders neer, omdat elke koppeling andere relaties draagt; dan herkent
de lezer de plaat niet terug van de ene koppeling naar de volgende. Dit script
geeft de plaat daarom in elke view dezelfde indeling en trekt de lijnen er zelf
overheen.

De indeling komt uit het model. Een element met `hoofdplaatrij` en
`hoofdplaatkolom` in zijn metadata staat op die rij en in die volgorde binnen
zijn ouder; de rijen staan gecentreerd onder elkaar. Wat eronder hangt zonder
die metadata, de applicatiediensten, gaat in een raster zoals likec4-layout.py
dat maakt. Een knoop bovenaan zonder plek, de koppeling, staat boven de plaat.

De lijnen zijn de relaties met de tag `#hoofdplaat` tussen knopen in de view.
Daar horen ook de relaties bij die LikeC4 zelf weglaat: loopt er een lijn naar
een dienst binnen een component, dan toont LikeC4 de lijn naar dat component
niet meer, terwijl de koppeling dat component als aanbieder heeft. Elke lijn
loopt rechthoekig om de blokken heen, gezocht met A* over een raster, en ontwijkt
de lijnen die er al liggen.

Een andere view die dezelfde plaatsing nodig heeft, krijgt de tag `#hoofdplaat`.

Het resultaat gaat als `<view>.likec4.snap` naar `<modelmap>/.likec4/`, net als
bij likec4-layout.py, en is net zo'n afgeleide.

    python3 scripts/likec4-hoofdplaat.py <modelmap> [likec4.json]
"""

from __future__ import annotations

import heapq
import importlib.util
import json
import sys
from pathlib import Path

_bron = Path(__file__).with_name("likec4-layout.py")
_spec = importlib.util.spec_from_file_location("likec4_layout", _bron)
likec4_layout = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(likec4_layout)

TITEL = "Hoofdplaat /"
TAG = "hoofdplaat"

RAND = likec4_layout.RAND
PADDING = likec4_layout.PADDING
PADDING_BOVEN = likec4_layout.PADDING_BOVEN

KOLOMRUIMTE = 60    # tussen twee componenten op een rij: ruimte voor lijnen
RIJRUIMTE = 110     # tussen twee rijen: ruimte voor lijnen en hun labels
BOVENRUIMTE = 140   # tussen de koppeling en de plaat
BUITENRAND = 60     # rond de plaat, voor lijnen die eromheen moeten

RASTER = 10         # celgrootte van het zoekraster, in pixels
AFSTAND = 1         # cellen die een lijn vrijhoudt van een blok dat niet het doel is
BOCHT = 12          # kosten van een bocht, uitgedrukt in cellen
NABIJ = 3           # binnen zoveel cellen van een blok kost een cel extra
PARALLEL = 40       # een cel waar al een lijn in dezelfde richting loopt
NAAST = (8, 3)      # een cel op één of twee cellen naast zo'n lijn
KRUISING = 40       # een cel waar een lijn haaks overheen gaat
TITELKOSTEN = 30    # een cel op de titel van een groep waar de lijn doorheen moet
INSPRONG = 12       # een lijn landt niet vlak bij de hoek van een blok
VERTREK = 0.15      # een lijn vertrekt niet uit de buitenste 15% van de onderkant
RONDES = 3          # zo vaak wordt elke lijn opnieuw gezocht, met de andere op hun plek
AANLOOP = (3, 5)    # binnen 3 cellen boven het doel kost een stap opzij 5 extra: de lijn landt recht
LABELWEG = 0.3      # kosten per pixel die een label verder van het doel staat

OMLAAG, OMHOOG, RECHTS, LINKS = (0, 1), (0, -1), (1, 0), (-1, 0)
RICHTINGEN = (OMLAAG, OMHOOG, RECHTS, LINKS)


# --- indeling -------------------------------------------------------------

def plek(element: dict | None) -> tuple[int, int] | None:
    """De (rij, kolom) uit de metadata van een element, of None als die ontbreekt."""
    metadata = (element or {}).get("metadata") or {}
    if "hoofdplaatrij" in metadata and "hoofdplaatkolom" in metadata:
        return int(metadata["hoofdplaatrij"]), int(metadata["hoofdplaatkolom"])
    return None


def rijen(blokken: list[dict], plekken: dict, links: int, boven: int) -> tuple[int, int]:
    """Zet blokken op hun rij, in kolomvolgorde, elke rij gecentreerd onder de breedste."""
    per_rij: dict[int, list[dict]] = {}
    for blok in blokken:
        per_rij.setdefault(plekken[blok["id"]][0], []).append(blok)
    reeksen = [sorted(per_rij[r], key=lambda b: plekken[b["id"]][1]) for r in sorted(per_rij)]
    breedtes = [sum(b["width"] for b in reeks) + KOLOMRUIMTE * (len(reeks) - 1) for reeks in reeksen]
    breedste = max(breedtes)

    y = boven
    for reeks, breedte in zip(reeksen, breedtes):
        x = links + (breedste - breedte) // 2
        for blok in reeks:
            likec4_layout.verplaats(blok, x - blok["x"], y - blok["y"])
            x += blok["width"] + KOLOMRUIMTE
        y += max(b["height"] for b in reeks) + RIJRUIMTE
    return breedste, y - RIJRUIMTE - boven


def leg_uit(knoop: dict, plekken: dict) -> None:
    """Plaatst eerst de inhoud, dan de knoop eromheen; van binnen naar buiten."""
    kinderen = knoop["_kinderen"]
    if not kinderen:
        return
    for kind in kinderen:
        leg_uit(kind, plekken)

    links, boven = knoop["x"] + PADDING, knoop["y"] + PADDING_BOVEN
    if all(kind["id"] in plekken for kind in kinderen):
        breedte, hoogte = rijen(kinderen, plekken, links, boven)
    else:
        breedte, hoogte = likec4_layout.raster(kinderen, links, boven)
    knoop["width"] = breedte + 2 * PADDING
    knoop["height"] = PADDING_BOVEN + hoogte + PADDING


# --- lijnen zoeken --------------------------------------------------------

class Raster:
    """Het zoekraster over de view: welke cellen vrij zijn en wat een cel kost."""

    def __init__(self, breedte: int, hoogte: int):
        self.nx = breedte // RASTER + 1
        self.ny = hoogte // RASTER + 1
        self.gebruikt: dict[tuple[int, int], dict[str, int]] = {}

    @staticmethod
    def midden(i: int) -> int:
        return i * RASTER + RASTER // 2

    @staticmethod
    def cel(waarde: float) -> int:
        return int(waarde // RASTER)

    def cellen_in(self, vlak: tuple[int, int, int, int], marge: int = 0):
        """De cellen waarvan het midden binnen het vlak valt, uitgebreid met marge cellen.

        Een vlak zonder breedte of hoogte, een rand, levert de cellen waar hij doorheen loopt.
        """
        x0, y0, x1, y1 = vlak
        i0 = max(0, -(-(x0 - RASTER // 2) // RASTER) - marge)
        i1 = min(self.nx - 1, (x1 - RASTER // 2) // RASTER + marge)
        j0 = max(0, -(-(y0 - RASTER // 2) // RASTER) - marge)
        j1 = min(self.ny - 1, (y1 - RASTER // 2) // RASTER + marge)
        if x0 == x1:
            i0 = i1 = min(self.nx - 1, int(x0 // RASTER))
        if y0 == y1:
            j0 = j1 = min(self.ny - 1, int(y0 // RASTER))
        for i in range(i0, i1 + 1):
            for j in range(j0, j1 + 1):
                yield i, j

    def markeer(self, pad: list[tuple[int, int]], teken: int = 1) -> None:
        """Legt vast waar een lijn loopt en in welke richting; met teken -1 haalt het hem weg."""
        for (i0, j0), (i1, j1) in zip(pad, pad[1:]):
            richting = "v" if i0 == i1 else "h"
            for cel in ((i0, j0), (i1, j1)):
                telling = self.gebruikt.setdefault(cel, {})
                telling[richting] = telling.get(richting, 0) + teken

    def loopt(self, cel: tuple[int, int], richting: str | None = None) -> bool:
        telling = self.gebruikt.get(cel, {})
        if richting:
            return telling.get(richting, 0) > 0
        return any(n > 0 for n in telling.values())

    def kosten_gebruik(self, i: int, j: int, richting: str) -> int:
        kosten = 0
        if self.loopt((i, j), richting):
            kosten += PARALLEL
        elif self.loopt((i, j)):
            kosten += KRUISING
        for afstand, boete in enumerate(NAAST, start=1):
            buren = ((i - afstand, j), (i + afstand, j)) if richting == "v" else ((i, j - afstand), (i, j + afstand))
            if any(self.loopt(buur, richting) for buur in buren):
                kosten += boete
        return kosten


def vlak(knoop: dict) -> tuple[int, int, int, int]:
    return knoop["x"], knoop["y"], knoop["x"] + knoop["width"], knoop["y"] + knoop["height"]


def titelvak(knoop: dict) -> tuple[int, int, int, int]:
    """Waar de titel van een groep staat: linksboven, in kleine hoofdletters."""
    x, y = knoop["x"], knoop["y"]
    return x, y, x + 24 + 10 * len(knoop.get("title") or ""), y + 34


def voorouders(knoop: dict, knopen: dict) -> set[str]:
    gevonden = set()
    ouder = knoop["parent"]
    while ouder:
        gevonden.add(ouder)
        ouder = knopen[ouder]["parent"]
    return gevonden


def bezet(raster: Raster, knopen: dict, van: dict, naar: dict) -> tuple[bytearray, list[int]]:
    """Welke cellen een lijn van `van` naar `naar` niet mag nemen, en wat elke cel extra kost.

    Elk blok is een obstakel, met een marge eromheen; de groepen waar het doel in
    ligt niet, want daar moet de lijn juist in. Begin en doel tellen zonder marge
    mee, zodat de lijn er direct tegenaan kan. Een lijn houdt afstand van een
    obstakel en van de rand van een groep waar zij doorheen moet.
    """
    vrij_door = voorouders(naar, knopen)
    geblokt = bytearray(raster.nx * raster.ny)
    randen, titels = set(), set()
    for knoop in knopen.values():
        if knoop["id"] in vrij_door:
            x0, y0, x1, y1 = vlak(knoop)
            for lat in ((x0, y0, x1, y0), (x0, y1, x1, y1), (x0, y0, x0, y1), (x1, y0, x1, y1)):
                randen.update(j * raster.nx + i for i, j in raster.cellen_in(lat))
            titels.update(j * raster.nx + i for i, j in raster.cellen_in(titelvak(knoop)))
            continue
        marge = 0 if knoop is van or knoop is naar else AFSTAND
        for i, j in raster.cellen_in(vlak(knoop), marge):
            geblokt[j * raster.nx + i] = 1

    # Afstand tot het dichtstbijzijnde obstakel of de dichtstbijzijnde rand, tot NABIJ cellen ver
    afstand = [NABIJ] * (raster.nx * raster.ny)
    rand = sorted(randen | {k for k, b in enumerate(geblokt) if b})
    for k in rand:
        afstand[k] = 0
    for stap in range(1, NABIJ):
        volgende = []
        for k in rand:
            i, j = k % raster.nx, k // raster.nx
            for di, dj in RICHTINGEN:
                ni, nj = i + di, j + dj
                if 0 <= ni < raster.nx and 0 <= nj < raster.ny:
                    nk = nj * raster.nx + ni
                    if afstand[nk] > stap:
                        afstand[nk] = stap
                        volgende.append(nk)
        rand = volgende
    extra = [NABIJ - a for a in afstand]
    for k in titels:
        extra[k] += TITELKOSTEN
    return geblokt, extra


def zoek(raster: Raster, geblokt: bytearray, extra: list[int],
         start_j: int, start_i: tuple[int, int], doel_j: int, doel_i: tuple[int, int]) -> list[tuple[int, int]]:
    """A* van een cel in rij start_j omlaag naar een cel in rij doel_j, binnenkomend van boven.

    Elke cel tussen start_i in de startrij mag het begin zijn, en elke cel tussen
    doel_i in de doelrij het eind; de zoektocht kiest zelf waar de lijn vertrekt
    en landt.
    """
    lo, hi = doel_i

    def schatting(i: int, j: int) -> int:
        dx = 0 if lo <= i <= hi else min(abs(i - lo), abs(i - hi))
        return dx + abs(doel_j - j)

    open_, kosten = [], {}
    for i in range(start_i[0], start_i[1] + 1):
        if geblokt[start_j * raster.nx + i]:
            continue
        begin = (i, start_j, OMLAAG)
        g = extra[start_j * raster.nx + i] + raster.kosten_gebruik(i, start_j, "v")
        kosten[begin] = g
        heapq.heappush(open_, (g + schatting(i, start_j), g, begin))
    vorige: dict = {}
    while open_:
        _, g, toestand = heapq.heappop(open_)
        i, j, richting = toestand
        if g > kosten.get(toestand, float("inf")):
            continue
        if j == doel_j and lo <= i <= hi and richting == OMLAAG:
            pad = [(i, j)]
            while toestand in vorige:
                toestand = vorige[toestand]
                pad.append(toestand[:2])
            return pad[::-1]
        for nieuw in RICHTINGEN:
            if nieuw == (-richting[0], -richting[1]):
                continue
            ni, nj = i + nieuw[0], j + nieuw[1]
            if not (0 <= ni < raster.nx and 0 <= nj < raster.ny):
                continue
            k = nj * raster.nx + ni
            if geblokt[k]:
                continue
            stap = 1 + extra[k] + raster.kosten_gebruik(ni, nj, "v" if nieuw[0] == 0 else "h")
            if nieuw != richting:
                stap += BOCHT
            if nieuw[1] == 0 and 0 <= doel_j - nj <= AANLOOP[0]:
                stap += AANLOOP[1]
            volgende = (ni, nj, nieuw)
            if g + stap < kosten.get(volgende, float("inf")):
                kosten[volgende] = g + stap
                vorige[volgende] = toestand
                heapq.heappush(open_, (g + stap + schatting(ni, nj), g + stap, volgende))
    raise RuntimeError("geen vrije weg gevonden")


def hoeken(punten: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Laat de punten weg die midden op een rechte lijn liggen."""
    over = [punten[0]]
    for punt, volgend in zip(punten[1:], punten[2:]):
        vorig = over[-1]
        if (vorig[0] == punt[0] == volgend[0]) or (vorig[1] == punt[1] == volgend[1]):
            continue
        over.append(punt)
    over.append(punten[-1])
    return over


def bezier(lijn: list[tuple[int, int]]) -> list[list[float]]:
    """Een gebroken lijn als bezier-punten, zoals LikeC4 ze verwacht: rechte stukken."""
    punten = [list(lijn[0])]
    for (x0, y0), (x1, y1) in zip(lijn, lijn[1:]):
        punten += [[x0 + (x1 - x0) / 3, y0 + (y1 - y0) / 3],
                   [x0 + 2 * (x1 - x0) / 3, y0 + 2 * (y1 - y0) / 3],
                   [x1, y1]]
    return punten


# --- labels ---------------------------------------------------------------

def overlapt(a: tuple, b: tuple) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def snijdt(vak: tuple, p: tuple, q: tuple) -> bool:
    """Of een recht stuk lijn van p naar q door het vak gaat."""
    x0, x1 = sorted((p[0], q[0]))
    y0, y1 = sorted((p[1], q[1]))
    return overlapt(vak, (x0 - 1, y0 - 1, x1 + 1, y1 + 1))


def plaats_label(lijn: list[tuple[int, int]], maat: tuple[int, int], knopen: dict,
                 labels: list[tuple], lijnen: list[list[tuple[int, int]]]) -> tuple:
    """Zoekt voor een label de plek langs de lijn die het minst in de weg zit.

    De lijn loopt hier naar het doel toe. Een label hoort zo dicht mogelijk bij
    dat doel, zodat duidelijk is bij welk blok het hoort; niet op een blok, niet
    op de titel of over de rand van een groep, niet op een ander label en liefst
    niet op een andere lijn.
    """
    breedte, hoogte = maat
    kandidaten = []
    afgelegd = 0
    for p, q in list(zip(lijn, lijn[1:]))[::-1]:
        lengte = abs(q[0] - p[0]) + abs(q[1] - p[1])
        verticaal = p[0] == q[0]
        half = (hoogte if verticaal else breedte) / 2 + 6
        d = half
        while d <= max(lengte - half, half):
            fractie = d / lengte if lengte else 0
            mx, my = q[0] + (p[0] - q[0]) * fractie, q[1] + (p[1] - q[1]) * fractie
            if verticaal:
                opties = [(mx + 6, my - hoogte / 2), (mx - 6 - breedte, my - hoogte / 2)]
            else:
                opties = [(mx - breedte / 2, my - hoogte - 4), (mx - breedte / 2, my + 4)]
            kandidaten += [((x, y, x + breedte, y + hoogte), afgelegd + d) for x, y in opties]
            d += RASTER
        afgelegd += lengte

    def score(kandidaat) -> float:
        vak, afstand = kandidaat
        totaal = afstand * LABELWEG
        for knoop in knopen.values():
            buiten = vlak(knoop)
            if not overlapt(vak, buiten):
                continue
            if not knoop["children"]:
                totaal += 1000
                continue
            binnen = buiten[0] < vak[0] and vak[2] < buiten[2] and buiten[1] < vak[1] and vak[3] < buiten[3]
            if not binnen:
                totaal += 300
            elif overlapt(vak, titelvak(knoop)):
                totaal += 400
        totaal += 1000 * sum(overlapt(vak, ander) for ander in labels)
        for andere in lijnen:
            totaal += 150 * sum(snijdt(vak, p, q) for p, q in zip(andere, andere[1:]))
        return totaal

    return min(kandidaten, key=score)[0]


# --- de view --------------------------------------------------------------

def schat_maat(label: str) -> tuple[int, int]:
    return 6 * len(label) + 12, 18


def leg_view_uit(view: dict, model: dict) -> dict:
    """Herberekent plaatsing en lijnen van één hoofdplaatview. Wijzigt en geeft de view terug."""
    elementen = model["elements"]
    knopen = {n["id"]: n for n in view["nodes"]}
    # LikeC4 levert de kinderen in de volgorde van zijn eigen layout; de plaat volgt het model
    volgorde = {element_id: n for n, element_id in enumerate(elementen)}
    for knoop in view["nodes"]:
        knoop["_kinderen"] = sorted((knopen[k] for k in knoop["children"]),
                                    key=lambda k: volgorde.get(k.get("modelRef") or k["id"], len(volgorde)))
    plekken = {k: p for k in knopen if (p := plek(elementen.get(knopen[k].get("modelRef") or k)))}

    # De plaat
    wortels = [n for n in view["nodes"] if n["parent"] is None]
    op_de_plaat = [n for n in wortels if n["id"] in plekken]
    los = [n for n in wortels if n["id"] not in plekken]
    for wortel in wortels:
        leg_uit(wortel, plekken)
    hoogste_los = max((n["height"] for n in los), default=0)
    plaat_boven = BUITENRAND + (hoogste_los + BOVENRUIMTE if los else 0)
    breedte, _ = rijen(op_de_plaat, plekken, BUITENRAND, plaat_boven)

    # De relaties met de tag, ook die LikeC4 heeft weggelaten
    maten = {e["label"]: (e["labelBBox"]["width"], e["labelBBox"]["height"])
             for e in view["edges"] if e.get("label") and e.get("labelBBox")}
    view_labels = {rid: e.get("label") or "" for e in view["edges"] for rid in e.get("relations") or []}
    relaties = [
        (rid, r) for rid, r in sorted(model["relations"].items())
        if TAG in (r.get("tags") or [])
        and r["source"].get("model") in knopen and r["target"].get("model") in knopen
    ]

    # Wat los staat, komt boven de plaat, met de onderkanten op één lijn. Eerst wat
    # niet met de plaat verbonden is, zoals de legenda, van links af. Wat wel
    # verbonden is, staat op een rij in de volgorde van de knopen waarmee het
    # verbonden is, en die rij staat boven hun midden, rechts van de legenda.
    def overkant(knoop: dict) -> list[dict]:
        return [knopen[r["target"]["model"]] if r["source"]["model"] == knoop["id"]
                else knopen[r["source"]["model"]] for _, r in relaties
                if knoop["id"] in (r["source"]["model"], r["target"]["model"])]

    def midden(knopen_: list[dict]) -> float:
        return sum(k["x"] + k["width"] / 2 for k in knopen_) / len(knopen_)

    def zet(knoop: dict, x: float) -> None:
        y = plaat_boven - BOVENRUIMTE - knoop["height"]
        likec4_layout.verplaats(knoop, int(x) - knoop["x"], y - knoop["y"])

    vrij_vanaf = BUITENRAND
    for knoop in (n for n in los if not overkant(n)):
        zet(knoop, vrij_vanaf)
        vrij_vanaf += knoop["width"] + KOLOMRUIMTE
    verbonden = sorted((n for n in los if overkant(n)), key=lambda n: (midden(overkant(n)), n["id"]))
    if verbonden:
        rijbreedte = sum(n["width"] for n in verbonden) + KOLOMRUIMTE * (len(verbonden) - 1)
        doel = sum(midden(overkant(n)) for n in verbonden) / len(verbonden)
        x = doel - rijbreedte / 2
        if rijbreedte <= breedte:  # past de rij boven de plaat, dan blijft hij erbinnen
            x = min(max(x, BUITENRAND), BUITENRAND + breedte - rijbreedte)
        if vrij_vanaf > BUITENRAND:  # en hij schuift niet over de legenda
            x = max(x, vrij_vanaf)
        for knoop in verbonden:
            zet(knoop, x)
            x += knoop["width"] + KOLOMRUIMTE

    # Steekt de rij links uit, dan schuift alles op, zodat het zoekraster bij nul begint
    uitsteek = BUITENRAND - min(n["x"] for n in wortels)
    if uitsteek > 0:
        for wortel in wortels:
            likec4_layout.verplaats(wortel, uitsteek, 0)

    rechts = max(n["x"] + n["width"] for n in view["nodes"]) + BUITENRAND
    onder = max(n["y"] + n["height"] for n in view["nodes"]) + BUITENRAND
    raster = Raster(rechts, onder)

    # Van boven naar beneden: van de hoogste knoop van een relatie naar de andere
    ritten = []
    for rid, relatie in relaties:
        bron, doel = knopen[relatie["source"]["model"]], knopen[relatie["target"]["model"]]
        van, naar = (bron, doel) if bron["y"] <= doel["y"] else (doel, bron)
        ritten.append((rid, relatie, bron, doel, van, naar))

    # De langste ritten eerst, dan krijgen zij de rechtste weg. Daarna wordt elke
    # lijn nog een paar keer opnieuw gezocht terwijl de andere liggen, zodat ook de
    # eerste weet waar de rest loopt.
    ritten.sort(key=lambda r: -(abs(r[5]["y"] - r[4]["y"]) + abs(r[5]["x"] - r[4]["x"])))
    zoekgebied, paden = {}, {}
    for rid, _, _, _, van, naar in ritten:
        zoekgebied[rid] = (
            *bezet(raster, knopen, van, naar),
            Raster.cel(van["y"] + van["height"]) + 1,   # de eerste rij cellen onder het begin
            (Raster.cel(van["x"] + van["width"] * VERTREK), Raster.cel(van["x"] + van["width"] * (1 - VERTREK))),
            (int(naar["y"]) - RASTER // 2 - 1) // RASTER,  # de laatste rij cellen boven het doel
            (Raster.cel(naar["x"] + INSPRONG), Raster.cel(naar["x"] + naar["width"] - INSPRONG)),
        )
    for _ in range(RONDES):
        for rid, *_ in ritten:
            if rid in paden:
                raster.markeer(paden[rid], -1)
            paden[rid] = zoek(raster, *zoekgebied[rid])
            raster.markeer(paden[rid])

    edges, lijnen, labels = [], [], []
    for rid, relatie, bron, doel, van, naar in ritten:
        pad = paden[rid]
        punten = [(Raster.midden(pad[0][0]), van["y"] + van["height"])]
        punten += [(Raster.midden(i), Raster.midden(j)) for i, j in pad]
        punten.append((Raster.midden(pad[-1][0]), naar["y"]))
        lijn = hoeken(punten)
        if van is not bron:
            lijn = lijn[::-1]

        # Een titel die de view aan de relatie geeft, gaat voor; ook een lege
        label = view_labels.get(rid, relatie.get("title")) or None
        kader = None
        if label:  # een relatie zonder titel krijgt geen label
            maat = maten.get(label, schat_maat(label))
            vak = plaats_label(lijn if van is bron else lijn[::-1], maat, knopen, labels, lijnen)
            labels.append(vak)
            kader = {"x": round(vak[0]), "y": round(vak[1]), "width": maat[0], "height": maat[1]}
        lijnen.append(lijn)

        edges.append({
            "id": rid,
            "source": bron["id"],
            "target": doel["id"],
            "label": label,
            "labelBBox": kader,
            "parent": None,
            "relations": [rid],
            "color": relatie.get("color", "gray"),
            "line": relatie.get("line", "dashed"),
            "head": relatie.get("head", "normal"),
            "tags": relatie.get("tags") or [],
            "points": bezier(lijn),
        })

    edges.sort(key=lambda e: e["id"])
    view["edges"] = edges
    for knoop in view["nodes"]:
        knoop["inEdges"] = [e["id"] for e in edges if e["target"] == knoop["id"]]
        knoop["outEdges"] = [e["id"] for e in edges if e["source"] == knoop["id"]]
        del knoop["_kinderen"]

    # Alles een eind naar linksboven, zodat de plaat op RAND begint
    punten = [p for e in edges for p in e["points"]]
    links = min([n["x"] for n in view["nodes"]] + [v[0] for v in labels] + [p[0] for p in punten]) - RAND
    boven = min([n["y"] for n in view["nodes"]] + [v[1] for v in labels] + [p[1] for p in punten]) - RAND
    for knoop in view["nodes"]:
        knoop["x"] -= links
        knoop["y"] -= boven
    for edge in edges:
        edge["points"] = [[x - links, y - boven] for x, y in edge["points"]]
        if edge["labelBBox"]:
            edge["labelBBox"]["x"] -= round(links)
            edge["labelBBox"]["y"] -= round(boven)
    uiterst_rechts = max([n["x"] + n["width"] for n in view["nodes"]]
                         + [e["labelBBox"]["x"] + e["labelBBox"]["width"] for e in edges if e["labelBBox"]]
                         + [p[0] for e in edges for p in e["points"]])
    uiterst_onder = max([n["y"] + n["height"] for n in view["nodes"]]
                        + [e["labelBBox"]["y"] + e["labelBBox"]["height"] for e in edges if e["labelBBox"]]
                        + [p[1] for e in edges for p in e["points"]])
    view["bounds"] = {"x": 0, "y": 0, "width": round(uiterst_rechts + RAND), "height": round(uiterst_onder + RAND)}
    return view


def te_plaatsen(model: dict) -> list[str]:
    """De hoofdplaatviews: hun titel begint met `Hoofdplaat /`, of de view draagt de tag."""
    return sorted(
        view_id for view_id, view in model["views"].items()
        if ((view.get("title") or "").startswith(TITEL) or TAG in (view.get("tags") or []))
        and view["nodes"]
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
        view = leg_view_uit(model["views"][view_id], model)
        pad = doelmap / f"{view_id}.likec4.snap"
        pad.write_text(json.dumps(view, indent=2, ensure_ascii=False) + "\n")
        print(f"{pad}: {view['bounds']['width']}x{view['bounds']['height']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
