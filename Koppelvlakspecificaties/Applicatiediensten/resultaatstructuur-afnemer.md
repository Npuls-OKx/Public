# Resultaatstructuur-afnemer

Kan de resultaatstructuur afnemen, zijn beoordeling erop inrichten, en een gemelde wijziging beoordelen voordat hij hem doorvoert.

## Doel

Lopende verbintenissen blijven beschermd tegen een wijziging in het examenplan.

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
| `examenplanspecificatie-gewijzigd` | POST | — | [specification-changed.json](../Datamodelschema's/specification-changed.json), met wijzigingsklasse | — | 200 |

## Gebruikt in

- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)

## Tegenhanger

[Resultaatstructuur-aanbieder](resultaatstructuur-aanbieder.md)
