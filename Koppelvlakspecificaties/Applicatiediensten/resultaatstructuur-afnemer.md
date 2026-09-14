# Resultaatstructuur-afnemer

Het implementerende component neemt de resultaatstructuur af, richt zijn beoordeling erop in, en beoordeelt een gemelde wijziging voordat het die doorvoert. Aan de andere kant staat een component dat [resultaatstructuur-aanbieder](resultaatstructuur-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- neemt de melding aan dat de resultaatstructuur beschikbaar is, en haalt haar op om het nominale template in te richten.
- neemt een wijzigingsmelding aan en toetst die aan zijn acceptatieregels voordat hij hem doorvoert.
- houdt de oude versie geldig voor lopende verbintenissen wanneer de nieuwe alleen op nieuwe instroom wordt toegepast.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `resultaatstructuur-beschikbaar` | POST | — | Specificatie-id en versie, examenplan-id en versie. Payloadschema nog niet uitgewerkt | — | 200 |
| `examenplanspecificatie-gewijzigd` | POST | — | [specification-changed.json](../../Datamodelschema's/schemas/specification-changed.json), met wijzigingsklasse | — | 200 |

## Gebruikt in

- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
