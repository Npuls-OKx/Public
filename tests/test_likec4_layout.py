#!/usr/bin/env python3
"""Testgevallen voor de plaatsing die scripts/likec4-layout.py berekent.

Het script vervangt de plaatsing die graphviz maakt voor views zonder relaties.
Drie eigenschappen moeten daaruit volgen: geen enkele groep overlapt een andere,
de groep met de meeste kinderen staat bovenaan, en een plank breekt af zodra de
maximumbreedte wordt overschreden in plaats van door te lopen.

Volgt de given-when-then-conventie.

Gebruik: python3 -m unittest discover -s tests -v
"""
import importlib.util
import os
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "scripts", "likec4-layout.py")
spec = importlib.util.spec_from_file_location("likec4_layout", SCRIPT)
likec4_layout = importlib.util.module_from_spec(spec)
spec.loader.exec_module(likec4_layout)


def knoop(id_: str, ouder, kinderen, breedte=320, hoogte=180) -> dict:
    """Eén knoop in de vorm die LikeC4 in zijn JSON-export oplevert."""
    return {"id": id_, "parent": ouder, "children": list(kinderen),
            "x": 0, "y": 0, "width": breedte, "height": hoogte}


def view(*groepen_met_aantallen: int) -> dict:
    """Een view met per opgegeven aantal één groep met dat aantal blokken erin."""
    knopen = []
    for nummer, aantal in enumerate(groepen_met_aantallen):
        groep = f"g{nummer}"
        kinderen = [f"{groep}.k{k}" for k in range(aantal)]
        knopen.append(knoop(groep, None, kinderen))
        knopen.extend(knoop(kind, groep, []) for kind in kinderen)
    return {"id": "proef", "nodes": knopen, "edges": [],
            "bounds": {"x": 0, "y": 0, "width": 0, "height": 0}}


def vlakken(view_: dict) -> list[tuple[str, int, int, int, int]]:
    return [(n["id"], n["x"], n["y"], n["x"] + n["width"], n["y"] + n["height"])
            for n in view_["nodes"] if n["parent"] is None]


def overlapt(a, b) -> bool:
    return a[1] < b[3] and b[1] < a[3] and a[2] < b[4] and b[2] < a[4]


class GegevenEenViewZonderRelaties(unittest.TestCase):

    def test_wanneer_de_plaatsing_is_berekend_dan_overlapt_geen_enkele_groep(self):
        berekend = likec4_layout.leg_view_uit(view(4, 2, 1, 1, 1, 3))
        plekken = vlakken(berekend)
        for i, eerste in enumerate(plekken):
            for tweede in plekken[i + 1:]:
                self.assertFalse(overlapt(eerste, tweede),
                                 f"{eerste[0]} overlapt {tweede[0]}")

    def test_wanneer_groepen_verschillen_in_omvang_dan_staat_de_grootste_bovenaan(self):
        # given: de grootste groep staat als laatste in het model gedeclareerd
        berekend = likec4_layout.leg_view_uit(view(1, 1, 5))
        plekken = {n[0]: n for n in vlakken(berekend)}
        bovenste = min(plekken.values(), key=lambda v: (v[2], v[1]))
        self.assertEqual("g2", bovenste[0])

    def test_wanneer_de_plank_vol_is_dan_begint_de_volgende_groep_op_een_nieuwe_regel(self):
        # given: drie groepen waarvan er twee naast elkaar passen en drie niet
        breed = 700
        knopen = []
        for nummer in range(3):
            groep, kind = f"g{nummer}", f"g{nummer}.k0"
            knopen.append(knoop(groep, None, [kind]))
            knopen.append(knoop(kind, groep, [], breedte=breed))
        berekend = likec4_layout.leg_view_uit(
            {"id": "proef", "nodes": knopen, "edges": [],
             "bounds": {"x": 0, "y": 0, "width": 0, "height": 0}})

        hoogtes = {n[0]: n[2] for n in vlakken(berekend)}
        self.assertEqual(hoogtes["g0"], hoogtes["g1"], "eerste twee horen op dezelfde plank")
        self.assertGreater(hoogtes["g2"], hoogtes["g0"], "de derde hoort op de volgende plank")

    def test_wanneer_een_view_relaties_draagt_dan_wordt_hij_overgeslagen(self):
        model = {"views": {
            "zonder": {"nodes": [knoop("a", None, [])], "edges": []},
            "met": {"nodes": [knoop("a", None, [])], "edges": [{"id": "a-b"}]},
            "leeg": {"nodes": [], "edges": []},
        }}
        self.assertEqual(["zonder"], likec4_layout.te_plaatsen(model))


class GegevenEenGroepMetBlokken(unittest.TestCase):

    def test_wanneer_er_hoogstens_drie_blokken_zijn_dan_staan_ze_op_een_rij(self):
        for aantal in (1, 2, 3):
            self.assertEqual(aantal, likec4_layout.kolommen(aantal))

    def test_wanneer_er_meer_dan_drie_blokken_zijn_dan_wordt_het_raster_vierkant(self):
        self.assertEqual(2, likec4_layout.kolommen(4))
        self.assertEqual(3, likec4_layout.kolommen(9))
        self.assertEqual(4, likec4_layout.kolommen(13))

    def test_wanneer_de_groep_is_berekend_dan_omsluit_hij_zijn_blokken_met_padding(self):
        berekend = likec4_layout.leg_view_uit(view(2))
        groep = next(n for n in berekend["nodes"] if n["parent"] is None)
        kinderen = [n for n in berekend["nodes"] if n["parent"] is not None]
        for kind in kinderen:
            self.assertGreaterEqual(kind["x"] - groep["x"], likec4_layout.PADDING)
            self.assertGreaterEqual(kind["y"] - groep["y"], likec4_layout.PADDING)
            self.assertGreaterEqual(
                groep["x"] + groep["width"] - (kind["x"] + kind["width"]), likec4_layout.PADDING)


if __name__ == "__main__":
    unittest.main()
