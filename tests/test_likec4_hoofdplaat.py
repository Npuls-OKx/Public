#!/usr/bin/env python3
"""Testgevallen voor de hoofdplaatviews die scripts/likec4-hoofdplaat.py vastlegt.

Het script legt de plaat in elke hoofdplaatview hetzelfde neer en trekt de lijnen
er zelf overheen. Vier eigenschappen moeten daaruit volgen: de plaat ligt gelijk,
welke koppeling er ook boven staat; elke relatie met de tag wordt een lijn, ook
een die LikeC4 zelf heeft weggelaten; een lijn gaat nergens door een blok dat
niet haar doel is; en de rijen en kolommen uit de metadata kloppen.

Volgt de given-when-then-conventie.

Gebruik: python3 -m unittest discover -s tests -v
"""
import copy
import importlib.util
import os
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "scripts", "likec4-hoofdplaat.py")
spec = importlib.util.spec_from_file_location("likec4_hoofdplaat", SCRIPT)
likec4_hoofdplaat = importlib.util.module_from_spec(spec)
spec.loader.exec_module(likec4_hoofdplaat)


def element(rij=None, kolom=None) -> dict:
    if rij is None:
        return {}
    return {"metadata": {"hoofdplaatrij": str(rij), "hoofdplaatkolom": str(kolom)}}


def knoop(id_: str, ouder, kinderen=(), breedte=320, hoogte=140, titel=None) -> dict:
    """Eén knoop in de vorm die LikeC4 in zijn JSON-export oplevert."""
    return {"id": id_, "modelRef": id_, "parent": ouder, "children": list(kinderen),
            "title": titel or id_, "x": 0, "y": 0, "width": breedte, "height": hoogte,
            "inEdges": [], "outEdges": []}


def relatie(bron: str, doel: str, titel: str, tags=("hoofdplaat",)) -> dict:
    return {"source": {"model": bron}, "target": {"model": doel}, "title": titel, "tags": list(tags)}


def model_met(koppeling: str, relaties: dict, getoond: list[str]) -> tuple[dict, dict]:
    """Een plaat met drie componenten op twee rijen, een koppeling erboven.

    Component a staat linksboven en draagt twee diensten, b rechtsboven, c op de
    tweede rij. `getoond` zijn de relaties die LikeC4 zelf als edge zou leveren.
    """
    elementen = {
        "plaat": element(1, 1),
        "plaat.a": element(1, 1), "plaat.a.d1": element(), "plaat.a.d2": element(),
        "plaat.b": element(1, 2),
        "plaat.c": element(2, 1),
        koppeling: element(),
    }
    knopen = [
        knoop("plaat", None, ["plaat.a", "plaat.b", "plaat.c"]),
        knoop("plaat.a", "plaat", ["plaat.a.d1", "plaat.a.d2"]),
        knoop("plaat.a.d1", "plaat.a", breedte=240, hoogte=100),
        knoop("plaat.a.d2", "plaat.a", breedte=240, hoogte=100),
        knoop("plaat.b", "plaat"),
        knoop("plaat.c", "plaat"),
        knoop(koppeling, None, breedte=300, hoogte=120),
    ]
    edges = [{"id": rid, "label": relaties[rid]["title"],
              "labelBBox": {"x": 0, "y": 0, "width": 60, "height": 18}} for rid in getoond]
    view = {"id": "hp", "title": "Hoofdplaat / Proef", "nodes": knopen, "edges": edges,
            "bounds": {"x": 0, "y": 0, "width": 0, "height": 0}}
    return {"elements": elementen, "relations": relaties, "views": {"hp": view}}, view


def standaard(koppeling="k1") -> tuple[dict, dict]:
    relaties = {
        "r1": relatie(koppeling, "plaat.a.d1", "afgeleid van"),
        "r2": relatie(koppeling, "plaat.a", "aanbieder"),
        "r3": relatie(koppeling, "plaat.c", "afnemer"),
        "r4": relatie(koppeling, "plaat.b", "iets anders", tags=()),
    }
    # LikeC4 laat r2 weg: er loopt al een lijn naar een dienst binnen plaat.a
    return model_met(koppeling, relaties, ["r1", "r3"])


def vlak(n: dict) -> tuple:
    return n["x"], n["y"], n["x"] + n["width"], n["y"] + n["height"]


def hoeken(edge: dict) -> list[tuple]:
    """De hoekpunten van een lijn: elk derde bezier-punt."""
    return [tuple(p) for p in edge["points"][::3]]


def snijdt_binnenkant(stuk: tuple, rechthoek: tuple) -> bool:
    """Of een horizontaal of verticaal stuk lijn door de binnenkant van een rechthoek gaat."""
    (x0, y0), (x1, y1) = stuk
    rx0, ry0, rx1, ry1 = rechthoek
    if x0 == x1:
        return rx0 < x0 < rx1 and max(min(y0, y1), ry0) < min(max(y0, y1), ry1)
    return ry0 < y0 < ry1 and max(min(x0, x1), rx0) < min(max(x0, x1), rx1)


class GegevenEenHoofdplaatview(unittest.TestCase):

    def test_wanneer_de_view_is_uitgelegd_dan_wordt_elke_relatie_met_de_tag_een_lijn(self):
        model, view = standaard()
        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        self.assertEqual({"r1", "r2", "r3"}, {e["id"] for e in uit["edges"]},
                         "r2 hoort erbij hoewel LikeC4 hem wegliet; r4 draagt de tag niet")

    def test_wanneer_twee_koppelingen_verschillen_dan_ligt_de_plaat_gelijk(self):
        # given: een tweede koppeling met andere relaties
        model1, view1 = standaard("k1")
        relaties = {"q1": relatie("k2", "plaat.b", "aanbieder"), "q2": relatie("k2", "plaat.a.d2", "afgeleid van")}
        model2, view2 = model_met("k2", relaties, ["q1", "q2"])

        uit1 = likec4_hoofdplaat.leg_view_uit(view1, model1)
        uit2 = likec4_hoofdplaat.leg_view_uit(view2, model2)

        def plaat(uit):
            knopen = {n["id"]: n for n in uit["nodes"]}
            basis = knopen["plaat"]
            return {i: (n["x"] - basis["x"], n["y"] - basis["y"], n["width"], n["height"])
                    for i, n in knopen.items() if i.startswith("plaat")}
        self.assertEqual(plaat(uit1), plaat(uit2))

    def test_wanneer_de_lijnen_zijn_gezocht_dan_gaat_geen_lijn_door_een_blok_dat_niet_haar_doel_is(self):
        model, view = standaard()
        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        knopen = {n["id"]: n for n in uit["nodes"]}
        for edge in uit["edges"]:
            doel = knopen[edge["target"]]
            vrij = {edge["source"], edge["target"]} | likec4_hoofdplaat.voorouders(doel, knopen)
            punten = hoeken(edge)
            for stuk in zip(punten, punten[1:]):
                for knoop_ in uit["nodes"]:
                    if knoop_["id"] in vrij:
                        continue
                    self.assertFalse(snijdt_binnenkant(stuk, vlak(knoop_)),
                                     f"{edge['id']} gaat door {knoop_['id']}")

    def test_wanneer_de_lijnen_zijn_gezocht_dan_lopen_ze_rechthoekig_en_landen_ze_op_het_doel(self):
        model, view = standaard()
        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        knopen = {n["id"]: n for n in uit["nodes"]}
        for edge in uit["edges"]:
            punten = hoeken(edge)
            for (x0, y0), (x1, y1) in zip(punten, punten[1:]):
                self.assertTrue(x0 == x1 or y0 == y1, f"{edge['id']} loopt schuin")
            doel = knopen[edge["target"]]
            eind = punten[-1]
            self.assertEqual(doel["y"], eind[1], f"{edge['id']} landt niet op de bovenrand van het doel")
            self.assertTrue(doel["x"] < eind[0] < doel["x"] + doel["width"])

    def test_wanneer_de_labels_zijn_geplaatst_dan_staat_er_geen_op_een_blok(self):
        model, view = standaard()
        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        for edge in uit["edges"]:
            b = edge["labelBBox"]
            label = (b["x"], b["y"], b["x"] + b["width"], b["y"] + b["height"])
            for knoop_ in uit["nodes"]:
                if knoop_["children"]:
                    continue
                self.assertFalse(likec4_hoofdplaat.overlapt(label, vlak(knoop_)),
                                 f"het label van {edge['id']} staat op {knoop_['id']}")


class GegevenDeMetadataVanDePlaat(unittest.TestCase):

    def test_wanneer_de_plaat_is_uitgelegd_dan_volgen_rij_en_kolom_de_metadata(self):
        model, view = standaard()
        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        knopen = {n["id"]: n for n in uit["nodes"]}
        a, b, c = knopen["plaat.a"], knopen["plaat.b"], knopen["plaat.c"]
        self.assertEqual(a["y"], b["y"], "a en b staan op dezelfde rij")
        self.assertLess(a["x"] + a["width"], b["x"], "kolom 1 staat links van kolom 2")
        self.assertGreater(c["y"], a["y"] + a["height"], "rij 2 staat onder rij 1")

    def test_wanneer_een_knoop_bovenaan_geen_plek_heeft_dan_staat_hij_boven_de_plaat(self):
        model, view = standaard()
        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        knopen = {n["id"]: n for n in uit["nodes"]}
        self.assertLess(knopen["k1"]["y"] + knopen["k1"]["height"], knopen["plaat"]["y"])

    def test_wanneer_er_een_legenda_naast_de_koppeling_staat_dan_overlappen_ze_niet(self):
        # given: een legenda zonder plek, met twee voorbeelden en een lijn zonder titel ertussen
        model, view = standaard()
        model["elements"].update({"legenda": element(), "legenda.a": element(1, 1), "legenda.b": element(2, 1)})
        model["relations"]["l1"] = relatie("legenda.a", "legenda.b", None)
        view["nodes"] += [knoop("legenda", None, ["legenda.a", "legenda.b"]),
                          knoop("legenda.a", "legenda"), knoop("legenda.b", "legenda")]

        uit = likec4_hoofdplaat.leg_view_uit(view, model)
        knopen = {n["id"]: n for n in uit["nodes"]}
        legenda, koppeling, plaat = knopen["legenda"], knopen["k1"], knopen["plaat"]
        self.assertFalse(likec4_hoofdplaat.overlapt(vlak(legenda), vlak(koppeling)))
        self.assertLess(legenda["x"], koppeling["x"], "wat niet met de plaat verbonden is, staat links")
        self.assertLess(legenda["y"] + legenda["height"], plaat["y"])
        lijn = next(e for e in uit["edges"] if e["id"] == "l1")
        self.assertIsNone(lijn["labelBBox"], "een relatie zonder titel krijgt geen label")

    def test_wanneer_kinderen_in_een_andere_volgorde_binnenkomen_dan_volgt_het_raster_het_model(self):
        # given: LikeC4 levert de diensten van a in omgekeerde volgorde
        model, view = standaard()
        omgekeerd = copy.deepcopy(view)
        next(n for n in omgekeerd["nodes"] if n["id"] == "plaat.a")["children"].reverse()

        gewoon = {n["id"]: n["x"] for n in likec4_hoofdplaat.leg_view_uit(view, model)["nodes"]}
        andersom = {n["id"]: n["x"] for n in likec4_hoofdplaat.leg_view_uit(omgekeerd, model)["nodes"]}
        self.assertLess(gewoon["plaat.a.d1"], gewoon["plaat.a.d2"])
        self.assertEqual(gewoon["plaat.a.d1"] - gewoon["plaat"], andersom["plaat.a.d1"] - andersom["plaat"])


class GegevenEenModelMetVerschillendeViews(unittest.TestCase):

    def test_wanneer_de_views_worden_gekozen_dan_tellen_de_titel_en_de_tag(self):
        model = {"views": {
            "hp_a": {"title": "Hoofdplaat / A", "nodes": [knoop("a", None)], "edges": []},
            "ref": {"title": "Referentie / B", "nodes": [knoop("a", None)], "edges": []},
            "hp_leeg": {"title": "Hoofdplaat / Leeg", "nodes": [], "edges": []},
            "getagd": {"title": "Uitgangspunten / C", "tags": ["hoofdplaat"], "nodes": [knoop("a", None)], "edges": []},
        }}
        self.assertEqual(["getagd", "hp_a"], likec4_hoofdplaat.te_plaatsen(model))


if __name__ == "__main__":
    unittest.main()
