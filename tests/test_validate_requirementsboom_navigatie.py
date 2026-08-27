#!/usr/bin/env python3
"""Testgevallen voor scripts/validate-requirementsboom-navigatie.py.

Elk testgeval volgt de given-when-then-conventie:
- Given: een verse kopie van de requirementsboom plus de interactiepatronen,
  al dan niet met precies een geinjecteerde breuk;
- When: het validatiescript draait tegen die kopie;
- Then: exitcode en melding zijn zoals verwacht.

Gebruik: python3 -m unittest discover -s tests -v
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(REPO_ROOT, "scripts", "validate-requirementsboom-navigatie.py")
TREE_DIR = os.path.join(REPO_ROOT, "Referentiemateriaal", "requirementsboom")
IP_DIR = os.path.join(REPO_ROOT, "Koppelvlakspecificaties", "Interactiepatronen")


def run_validator(tree_dir: str) -> tuple[int, str]:
    """De when-stap: draai het validatiescript, geef exitcode en uitvoer terug."""
    result = subprocess.run([sys.executable, SCRIPT, tree_dir],
                            capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr


def copy_tree(tmp: str) -> str:
    """Kopieer boom en interactiepatronen in de echte mappenstructuur."""
    boom = os.path.join(tmp, "Referentiemateriaal", "requirementsboom")
    shutil.copytree(TREE_DIR, boom)
    shutil.copytree(IP_DIR, os.path.join(tmp, "Koppelvlakspecificaties", "Interactiepatronen"))
    return boom


def count_anchors(file_name: str, kind: str) -> int:
    """Onafhankelijke telling: rij-ankers van een soort in een boombestand.

    Bewust een andere methode (kale substring-telling) dan de rijparsing van
    het validatiescript, zodat de test de telling van het script controleert.
    """
    with open(os.path.join(TREE_DIR, file_name), encoding="utf-8") as handle:
        return handle.read().count(f'<a id="{kind}-')


class CleanTreeTest(unittest.TestCase):
    """Positief geval: de boom zoals hij in de repository staat."""

    def test_given_unchanged_tree_when_validated_then_clean_with_expected_counts(self):
        # Given: de requirementsboom zoals ingecheckt, met onafhankelijk
        # getelde aantallen per laag (groeit dynamisch mee met de boom)
        stories = count_anchors("stories.md", "story")
        features = count_anchors("features.md", "feature")
        epics = count_anchors("epics.md", "epic")
        goals = count_anchors("opdracht.md", "doel")
        for layer, count in (("stories", stories), ("features", features),
                             ("epics", epics), ("doelen", goals)):
            self.assertGreater(count, 0, f"onafhankelijke telling {layer} is 0")
        # When: het validatiescript draait
        exit_code, output = run_validator(TREE_DIR)
        # Then: schoon, en de telwaarden komen exact overeen
        self.assertEqual(exit_code, 0, output)
        self.assertIn(f"{stories} stories, {features} features, "
                      f"{epics} epics, {goals} doelen", output)
        self.assertIn("0 problemen", output)


class BrokenTreeTest(unittest.TestCase):
    """Negatieve gevallen: elke geinjecteerde breuk faalt met de juiste melding."""

    def assert_break_detected(self, rel_file: str, old: str, new: str,
                              expected_fragment: str) -> None:
        # Given: een verse kopie van boom en interactiepatronen met precies
        # een geinjecteerde breuk (rel_file is relatief aan de kopie-root)
        with tempfile.TemporaryDirectory() as tmp:
            boom = copy_tree(tmp)
            path = os.path.join(tmp, rel_file)
            with open(path, encoding="utf-8") as handle:
                text = handle.read()
            self.assertIn(old, text, f"mutatiedoel niet gevonden in {rel_file}")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(text.replace(old, new, 1))
            # When: het validatiescript draait tegen de gebroken kopie
            exit_code, output = run_validator(boom)
            # Then: exit 1 met de verwachte melding
            self.assertEqual(exit_code, 1, output)
            self.assertIn(expected_fragment, output)

    BOOM = "Referentiemateriaal/requirementsboom/"
    IP = "Koppelvlakspecificaties/Interactiepatronen/"

    def test_given_removed_anchor_when_validated_then_dead_link_reported(self):
        self.assert_break_detected(
            self.BOOM + "stories.md",
            '<a id="story-0002"></a>story-0002', "story-0002", "zonder anker")

    def test_given_duplicated_anchor_when_validated_then_duplicate_reported(self):
        self.assert_break_detected(
            self.BOOM + "stories.md",
            '<a id="story-0003"></a>', '<a id="story-0002"></a>', "dubbel anker")

    def test_given_epic_removed_from_goal_table_when_validated_then_set_mismatch(self):
        # Vooruit-richting van de set-gelijkheid doel<->epic.
        self.assert_break_detected(
            self.BOOM + "opdracht.md",
            "[epic-0003 Aanbod plannen en roosteren](epics.md#epic-0003); ", "",
            "doel<->epic")

    def test_given_changed_contributes_to_cell_when_validated_then_set_mismatch(self):
        # Terug-richting van de set-gelijkheid doel<->epic.
        self.assert_break_detected(
            self.BOOM + "epics.md", "[doel-0003](opdracht.md#doel-0003)",
            "[doel-0002](opdracht.md#doel-0002)", "doel<->epic")

    def test_given_wrong_epic_cell_when_validated_then_section_mismatch(self):
        self.assert_break_detected(
            self.BOOM + "features.md", "| [epic-0002](epics.md#epic-0002) | geen |",
            "| [epic-0003](epics.md#epic-0003) | geen |", "Epic-cel")

    def test_given_story_removed_from_stories_cell_when_validated_then_set_mismatch(self):
        self.assert_break_detected(
            self.BOOM + "features.md", "[story-0001](stories.md#story-0001)", "geen",
            "feature<->story")

    def test_given_wrong_section_link_when_validated_then_section_mismatch(self):
        self.assert_break_detected(
            self.BOOM + "epics.md",
            "[features](features.md#gezamenlijke-taal-en-standaard)",
            "[features](features.md#aanbod-plannen-en-roosteren)", "epic<->feature")

    def test_given_dead_requirement_link_when_validated_then_missing_anchor_reported(self):
        self.assert_break_detected(
            self.BOOM + "stories.md",
            "planning-en-roostering.md#functionele-eis-0004",
            "planning-en-roostering.md#functionele-eis-9999", "zonder rij-anker")

    def test_given_anchor_violating_id_convention_when_validated_then_reported(self):
        self.assert_break_detected(
            self.BOOM + "features.md", '<a id="feature-0009"></a>feature-0009',
            '<a id="feature-99"></a>feature-99', "volgt de id-conventie niet")

    def test_given_story_removed_from_backlink_cell_when_validated_then_mismatch(self):
        # Terugleiding: de Story-cel van de eis noemt de story niet meer.
        self.assert_break_detected(
            self.IP + "onderwijscatalogus-planning-en-roostering.md",
            "[story-0002](../../Referentiemateriaal/requirementsboom/stories.md#story-0002)",
            "geen", "terugleiding")

    def test_given_backlink_to_unrelated_story_when_validated_then_mismatch(self):
        # Terugleiding: de Story-cel noemt een story die de eis niet linkt.
        self.assert_break_detected(
            self.IP + "onderwijscatalogus-planning-en-roostering.md",
            "[story-0002](../../Referentiemateriaal/requirementsboom/stories.md#story-0002)",
            "[story-0009](../../Referentiemateriaal/requirementsboom/stories.md#story-0009)",
            "terugleiding")


class EdgeCaseTest(unittest.TestCase):
    """Randgevallen rond paden."""

    def test_given_missing_tree_path_when_validated_then_exit_2(self):
        # Given: een pad dat niet bestaat
        # When: het validatiescript draait
        exit_code, output = run_validator("/pad/dat/niet/bestaat")
        # Then: exit 2 (pad niet gevonden)
        self.assertEqual(exit_code, 2, output)


if __name__ == "__main__":
    unittest.main()
