#!/usr/bin/env python3
"""Testgevallen voor de afhankelijkheid tussen releasepakketten in scripts/build-release.py.

Een pakket kan in zijn manifest vastleggen dat het op een ander pakket bouwt, op een
vastgelegde versie. Twee dingen moeten daaruit volgen: de bouw stopt zodra dat andere
pakket doorgeschoven is, en een verwijzing die in dat pakket landt draagt de tag van de
vastgelegde versie in plaats van de ref die nu gebouwd wordt.

Volgt de given-when-then-conventie.

Gebruik: python3 -m unittest discover -s tests -v
"""
import importlib.util
import json
import os
import pathlib
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "scripts", "build-release.py")
spec = importlib.util.spec_from_file_location("build_release", SCRIPT)
build_release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_release)

REPO_URL = "https://github.com/Npuls-OKx/Public"


def repository(versie_van_ander: str) -> pathlib.Path:
    """Twee pakketten naast elkaar, waarvan het ene op het andere bouwt."""
    wortel = pathlib.Path(tempfile.mkdtemp(prefix="okx-test-"))
    ander = wortel / "Ander"
    ander.mkdir()
    (ander / "release.json").write_text(json.dumps({
        "naam": "Ander pakket", "bestandsnaam": "ander", "versie": versie_van_ander,
        "documenten": ["inleiding.md"]}), encoding="utf-8")
    (ander / "inleiding.md").write_text("# Ander\n", encoding="utf-8")

    pakket = wortel / "Pakket"
    pakket.mkdir()
    (pakket / "release.json").write_text(json.dumps({
        "naam": "Pakket", "bestandsnaam": "pakket", "versie": "1.0.0",
        "documenten": ["inleiding.md"],
        "afhankelijkheden": [{"pakket": "../Ander", "versie": "2.3.4"}]}), encoding="utf-8")
    (pakket / "inleiding.md").write_text("# Pakket\n", encoding="utf-8")
    return pakket


class GepindePakkettenTest(unittest.TestCase):
    """Het oplossen van een afhankelijkheid tegen het manifest van het andere pakket."""

    def test_given_matching_version_when_resolved_then_tag_of_that_version(self):
        # Given: het andere pakket staat op de versie die het manifest noemt
        pakket = repository("2.3.4")
        manifest = json.loads((pakket / "release.json").read_text(encoding="utf-8"))
        # When: de afhankelijkheden worden opgelost
        gepind = build_release.gepinde_pakketten(pakket, manifest, REPO_URL)
        # Then: de tag draagt de bestandsnaam en de versie van dat pakket
        self.assertEqual(1, len(gepind))
        self.assertEqual("ander-v2.3.4", gepind[0]["tag"])
        self.assertEqual("Ander pakket", gepind[0]["naam"])

    def test_given_other_package_moved_on_when_resolved_then_build_stops(self):
        # Given: het andere pakket is doorgeschoven naar een hogere versie
        pakket = repository("2.4.0")
        manifest = json.loads((pakket / "release.json").read_text(encoding="utf-8"))
        # When: de afhankelijkheden worden opgelost
        # Then: de bouw stopt en noemt beide versies
        with self.assertRaises(SystemExit) as gestopt:
            build_release.gepinde_pakketten(pakket, manifest, REPO_URL)
        self.assertIn("2.3.4", str(gestopt.exception))
        self.assertIn("2.4.0", str(gestopt.exception))

    def test_given_dependency_without_manifest_when_resolved_then_build_stops(self):
        # Given: de genoemde map is geen releasepakket
        pakket = repository("2.3.4")
        (pakket.parent / "Ander" / "release.json").unlink()
        manifest = json.loads((pakket / "release.json").read_text(encoding="utf-8"))
        # When: de afhankelijkheden worden opgelost
        # Then: de bouw stopt met de reden erbij
        with self.assertRaises(SystemExit) as gestopt:
            build_release.gepinde_pakketten(pakket, manifest, REPO_URL)
        self.assertIn("release.json", str(gestopt.exception))


class GepindeVerwijzingTest(unittest.TestCase):
    """Verwijzingen die in een pakket landen waarop dit pakket bouwt."""

    def setUp(self):
        self.pakket = repository("2.3.4")
        manifest = json.loads((self.pakket / "release.json").read_text(encoding="utf-8"))
        self.gepind = build_release.gepinde_pakketten(self.pakket, manifest, REPO_URL)

    def herschrijf(self, inhoud: str, gebundeld: bool, beeldbasis=None) -> str:
        return build_release.herschrijf_links(
            inhoud, "inleiding.md", self.pakket, ["inleiding.md"], {},
            gebundeld, REPO_URL, "release-1", beeldbasis=beeldbasis, gepind=self.gepind)

    def test_given_link_into_pinned_package_when_rewritten_then_url_carries_its_tag(self):
        # Given: een verwijzing naar een document in het andere pakket
        inhoud = "Zie [de inleiding](../Ander/inleiding.md).\n"
        # When: de verwijzing herschreven wordt voor de losse documenten
        result = self.herschrijf(inhoud, gebundeld=False)
        # Then: de URL draagt de tag van de vastgelegde versie, niet de gebouwde ref
        self.assertIn(f"{REPO_URL}/blob/ander-v2.3.4/Ander/inleiding.md", result)
        self.assertNotIn("release-1", result)

    def test_given_link_into_pinned_package_when_bundled_then_url_instead_of_relative(self):
        # Given: dezelfde verwijzing, nu voor het gebundelde markdown-document, waarin
        # verwijzingen binnen het repository juist relatief blijven
        inhoud = "Zie [de inleiding](../Ander/inleiding.md).\n"
        # When: de verwijzing herschreven wordt met de pakketmap als beeldbasis
        result = self.herschrijf(inhoud, gebundeld=True, beeldbasis=self.pakket.resolve())
        # Then: ook daar staat de gepinde URL, want een relatief pad zou meebewegen
        self.assertIn(f"{REPO_URL}/blob/ander-v2.3.4/Ander/inleiding.md", result)

    def test_given_anchor_on_pinned_link_when_rewritten_then_anchor_kept(self):
        # Given: een verwijzing naar een kop in het andere pakket
        inhoud = "Zie [de regels](../Ander/inleiding.md#regels).\n"
        # When: de verwijzing herschreven wordt
        result = self.herschrijf(inhoud, gebundeld=False)
        # Then: het anchor reist mee achter de gepinde URL
        self.assertIn("/blob/ander-v2.3.4/Ander/inleiding.md#regels", result)

    def test_given_link_outside_any_pinned_package_when_rewritten_then_built_ref(self):
        # Given: een verwijzing naar een map die geen releasepakket is
        (self.pakket.parent / "Referentiemateriaal").mkdir()
        (self.pakket.parent / "Referentiemateriaal" / "adr.md").write_text("# ADR\n",
                                                                          encoding="utf-8")
        inhoud = "Zie [het besluit](../Referentiemateriaal/adr.md).\n"
        # When: de verwijzing herschreven wordt
        result = self.herschrijf(inhoud, gebundeld=False)
        # Then: die wijst naar de ref die nu gebouwd wordt
        self.assertIn(f"{REPO_URL}/blob/release-1/Referentiemateriaal/adr.md", result)


if __name__ == "__main__":
    unittest.main()
