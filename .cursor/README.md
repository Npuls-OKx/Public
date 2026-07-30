# Agent harness

Configuratie voor de AI-agents die in dit repository werken: rules die automatisch meekomen, en commands die je met `/` start.

| Map | Wat erin staat |
|---|---|
| [`rules/`](rules/) | Conventies die een agent automatisch meekrijgt: governance, structuur, documentconventies, verwijzingen, stijl |
| [`commands/`](commands/) | Workflows die je met `/` start: nieuwe specificatie, document controleren, overhevelen uit meta, release voorbereiden |
| [`../.agents/skills/`](../.agents/skills/) | Skills met de domeinkennis en de valkuilen |

## Waarom skills in `.agents/` staan

De meta-repository gebruikt `.cursor/skills` als **symlink** naar `.agents/skills`. Dat werkt lokaal, maar GitHub volgt symlinks niet in blob-URL's: elke link naar `.cursor/skills/...` is daar dood. Omdat de documenten hier gereleased worden en hun links moeten kloppen, staan de skills op hun echte plek en verwijzen we daarheen.

## Wat een script doet, hoort niet alleen in een rule

De regels die machinaal te controleren zijn, staan in [`../scripts/`](../scripts/):

```bash
python3 scripts/check-links.py        # dode links, ontsnappingen buiten de repo, dode anchors
python3 scripts/check-conventies.py   # issueverwijzingen, metadatakoppen, branchlinks, inleiding
python3 scripts/json-tree.py --check  # schema en bomen van een payload-document
```

Een rule beschrijft de bedoeling; een script dwingt af wat afdwingbaar is. Loopt een van beide achter op de praktijk, werk dan allebei bij.
