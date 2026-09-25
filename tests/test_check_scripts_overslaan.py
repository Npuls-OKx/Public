#!/usr/bin/env python3
"""Testgevallen voor de mappen die check-links.py en check-conventies.py overslaan.

Sinds het repository een node-gereedschapskist draagt voor de diagrammen, staat er
markdown van derden in `node_modules`. Die is niet van ons en voldoet niet aan onze
conventies, dus de controlescripts horen hem niet te zien. Hetzelfde geldt voor de
bouwuitvoer in `dist`.

Volgt de given-when-then-conventie.

Gebruik: python3 -m unittest discover -s tests -v
"""
import importlib.util
import os
import pathlib
import tempfile
import unittest

SCRIPTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts")


def laad(bestandsnaam: str, modulenaam: str):
    spec = importlib.util.spec_from_file_location(modulenaam, os.path.join(SCRIPTS, bestandsnaam))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


check_links = laad("check-links.py", "check_links")
check_conventies = laad("check-conventies.py", "check_conventies")


def repository_met_gereedschap() -> pathlib.Path:
    """Eén eigen document, en markdown van derden in de mappen die we negeren."""
    wortel = pathlib.Path(tempfile.mkdtemp(prefix="okx-test-"))
    (wortel / "eigen.md").write_text("# Eigen\n", encoding="utf-8")
    for map_ in ("node_modules", "dist", "__pycache__"):
        (wortel / map_ / "pakket").mkdir(parents=True)
        (wortel / map_ / "pakket" / "README.md").write_text("# Van een ander\n", encoding="utf-8")
    return wortel


class GegevenEenRepositoryMetNodeGereedschap(unittest.TestCase):

    def setUp(self):
        self.wortel = repository_met_gereedschap()

    def test_wanneer_check_links_de_bestanden_verzamelt_dan_blijft_node_modules_buiten_beeld(self):
        gevonden = check_links.markdown_bestanden([], self.wortel)
        self.assertEqual(["eigen.md"], [p.name for p in gevonden])

    def test_wanneer_check_conventies_de_bestanden_verzamelt_dan_blijft_node_modules_buiten_beeld(self):
        gevonden = check_conventies.markdown_bestanden([], self.wortel)
        self.assertEqual(["eigen.md"], [p.name for p in gevonden])

    def test_wanneer_de_overgeslagen_mappen_worden_opgesomd_dan_zijn_ze_in_beide_scripts_gelijk(self):
        self.assertEqual(check_links.OVERSLAAN, check_conventies.OVERSLAAN)


if __name__ == "__main__":
    unittest.main()
