# Scripts

Gereedschap om te controleren wat machinaal te controleren is. Draai ze vanuit de repo-root.

| Script | Wat het vangt |
|---|---|
| [`check-links.py`](check-links.py) | Dode links, links die buiten de repository wijzen, links door een symlink heen, dode anchors |
| [`check-conventies.py`](check-conventies.py) | Issueverwijzingen, metadatakoppen, datumprefixen, links naar een meta-branch in plaats van een commit, onvolledige inleidingen |
| [`json-tree.py`](json-tree.py) | Drift tussen de JSON, het schema en de gegenereerde bomen in een payload-document |

```bash
python3 scripts/check-links.py                    # hele repository
python3 scripts/check-conventies.py <pad>         # of alleen een map of bestand
python3 scripts/json-tree.py --check <doc>.md     # controleren
python3 scripts/json-tree.py --write <doc>.md     # bomen bijwerken
```

Alle drie geven exitcode 1 bij een probleem, zodat ze in een pre-commit hook of workflow passen.

## Waarom deze controles bestaan

Elk van deze checks vangt een fout die een keer is gemaakt.

`check-links.py` lost paden **lexicaal** op in plaats van ze te resolven, precies zoals GitHub dat doet. Daardoor vangt hij twee dingen die een gewone bestandscontrole mist: een link die met genoeg `../` *buiten* de repository wijst en lokaal toevallig resolveert naar een bestand in een naburige map, en een link die door een **symlink** heen loopt. Beide werken op je eigen schijf en zijn stuk in de webweergave.

Het anchor-algoritme volgt dat van GitHub, waar elke spatie afzonderlijk een koppelstreep wordt: een em-streep in een kop levert daardoor een dubbele koppelstreep op.
