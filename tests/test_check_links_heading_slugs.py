#!/usr/bin/env python3
"""Testgevallen voor de kopslug-berekening van scripts/check-links.py.

Dekt de fix voor koppen die zelf een link zijn: GitHub berekent het anchor
over de gerenderde koptekst, dus linkmarkup moet eerst gestript worden.
Volgt de given-when-then-conventie; de bredere testdekking van de
CI-scripts is belegd in een eigen issue.

Gebruik: python3 -m unittest discover -s tests -v
"""
import importlib.util
import os
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "scripts", "check-links.py")
spec = importlib.util.spec_from_file_location("check_links", SCRIPT)
check_links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_links)


class HeadingSlugTest(unittest.TestCase):
    """De anchors die GitHub voor een document aanmaakt."""

    def test_given_plain_heading_when_slugged_then_lowercase_hyphenated(self):
        # Given: een gewone kop
        # When: de slugs berekend worden
        result = check_links.slugs("## Aanbod plannen en roosteren\n")
        # Then: het GitHub-anchor van de platte tekst
        self.assertIn("aanbod-plannen-en-roosteren", result)

    def test_given_heading_that_is_a_link_when_slugged_then_link_markup_stripped(self):
        # Given: een kop die zelf een link is (zoals de epicsecties in de
        # requirementsboom: ## [Naam](epics.md#epic-0002))
        # When: de slugs berekend worden
        result = check_links.slugs("## [Aanbod plannen en roosteren](epics.md#epic-0003)\n")
        # Then: het anchor volgt de gerenderde koptekst, niet de markup
        self.assertIn("aanbod-plannen-en-roosteren", result)

    def test_given_html_anchor_in_table_row_when_slugged_then_anchor_found(self):
        # Given: een expliciet HTML-anker in een tabelrij
        # When: de slugs berekend worden
        result = check_links.slugs('| <a id="functionele-eis-0001"></a>functionele-eis-0001 |\n')
        # Then: het anker telt mee als linkdoel
        self.assertIn("functionele-eis-0001", result)


if __name__ == "__main__":
    unittest.main()
