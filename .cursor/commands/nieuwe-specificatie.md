Zet een nieuwe koppelingspecificatie of payload-specificatie op. $ARGUMENTS

## Voorbereiden

Lees eerst, in deze volgorde:

1. [`Koppelvlakspecificaties/uitgangspunten.md`](../../Koppelvlakspecificaties/uitgangspunten.md) — U1 tot en met U10, de aannames die voor alles gelden
2. [`Koppelvlakspecificaties/README.md`](../../Koppelvlakspecificaties/README.md) — keten, afkortingen, wat waar staat
3. Het [kaderscenario](../../Referentiemateriaal/kaderscenario's/) van de leerroute waar je in werkt
4. Een bestaande specificatie van hetzelfde type, als spiegel

Vraag de gebruiker welke koppeling of welk object het betreft, en welke leerroute het scenario is.

## Opzetten

Kopieer het passende template:

| Wat je schrijft | Template | Doelmap |
|---|---|---|
| Informatiestroom tussen twee componenten | [`template-koppelingspecificatie.md`](../../Koppelvlakspecificaties/templates/template-koppelingspecificatie.md) | `Koppelingspecificaties/<koppeling>/` |
| De JSON die over zo'n koppeling gaat | [`template-payload-specificatie.md`](../../Koppelvlakspecificaties/templates/template-payload-specificatie.md) | dezelfde map, of `gedeeld/` bij hergebruik |

Bestandsnaam beschrijvend, zonder datum- of versieprefix.

## Schrijven

De templates dragen instructies tussen `<!-- -->`. Verwijder die zodra het onderdeel af is.

Twee dingen die vaak misgaan:

**Herhaal de uitgangspunten niet.** Noem het uitgangspunt in één regel en link erheen. Dat scheelt herstructureerwerk zodra een uitgangspunt wijzigt, en voorkomt dat de redenering op twee plekken uit elkaar loopt.

**Begin de inleiding bij de aanleiding**, niet bij een beschrijving van het document. Welk probleem of welke waarneming maakte dit nodig? Verwijs daarbij niet naar een issue: dit wordt gereleased.

## Payload-specifiek

Een payload-specificatie draagt een JSON Schema plus gegenereerde ASCII-bomen. Vervang de voorbeeld-JSON en draai daarna vanuit de repo-root:

```bash
python3 scripts/json-tree.py --write <document>.md
```

Dat overschrijft alles tussen de markers. Enumeraties horen in het schema, niet in een aparte tabel ernaast.

## Afronden

Werk de index bij in de README van de bovenliggende map, en draai `/controleer-document`.
