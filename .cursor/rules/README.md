# Rules

Voorwaardelijke instructies (`*.mdc`) die een AI-agent automatisch meekrijgt bij het werken in dit repository. Ze bewaken consistentie zonder dat je ze handmatig hoeft mee te geven.

| Rule | Geldt | Waarover |
|---|---|---|
| [`okx-public-governance.mdc`](okx-public-governance.mdc) | altijd | Wat dit repository is, het branchmodel, wie merget |
| [`repo-structuur.mdc`](repo-structuur.mdc) | altijd | Waar inhoud landt en waarom daar |
| [`gereleasde-documenten.mdc`](gereleasde-documenten.mdc) | `**/*.md` | Geen issueverwijzingen, zelfdragende inleiding, geen metadatakop |
| [`verwijzingen.mdc`](verwijzingen.mdc) | `**/*.md` | Relatief intern, gepind naar meta, anchors volgens GitHub |
| [`docs-style.mdc`](docs-style.mdc) | `**/*.md` | Schrijfstijl, diagrammen, schema's en bomen |

De regels die met een script te controleren zijn, staan in [`scripts/`](../../scripts/): `check-links.py` en `check-conventies.py`. Wat een script kan vangen, hoort niet alleen in een rule te staan.
