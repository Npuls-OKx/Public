# Agent harness

Configuratie voor de AI-agents die in dit repository werken. Het **entrypoint** is [`CLAUDE.md`](../CLAUDE.md) in de root: dat leest een agent als eerste en het verwijst hierheen. `AGENTS.md` is een symlink naar hetzelfde bestand, voor agents die die naam hanteren.

| Map | Wat erin staat |
|---|---|
| [`rules/`](rules/) | Conventies die een agent automatisch meekrijgt: governance, structuur, documentconventies, verwijzingen, stijl |
| [`commands/`](commands/) | Workflows die je met `/` start: nieuwe specificatie, document controleren, overhevelen uit meta, release voorbereiden |
| [`../.agents/skills/`](../.agents/skills/) | Skills met de domeinkennis en de valkuilen |

## Hoe de skills gevonden worden

De inhoud staat op één plek, `.agents/skills/`, met twee symlinks ernaartoe zodat beide tools hem ontdekken:

```
.agents/skills/          <- de echte inhoud; hierheen verwijzen
.claude/skills  -> ../.agents/skills
.cursor/skills  -> ../.agents/skills
```

**Verwijs altijd naar het `.agents/`-pad.** GitHub volgt symlinks niet in blob-URL's, dus een link naar `.claude/skills/...` of `.cursor/skills/...` is in de webweergave dood. `check-links.py` meldt zo'n link als `VIA SYMLINK`.

Dat is precies de fout die in de meta-repository zit, waar de skills alleen achter een symlink bereikbaar zijn en elke verwijzing ernaartoe stukloopt.

## Wat een script doet, hoort niet alleen in een rule

De regels die machinaal te controleren zijn, staan in [`../scripts/`](../scripts/):

```bash
python3 scripts/check-links.py        # dode links, ontsnappingen buiten de repo, dode anchors
python3 scripts/check-conventies.py   # issueverwijzingen, metadatakoppen, branchlinks, inleiding
python3 scripts/json-tree.py --check  # schema en bomen van een payload-document
```

Een rule beschrijft de bedoeling; een script dwingt af wat afdwingbaar is. Loopt een van beide achter op de praktijk, werk dan allebei bij.
