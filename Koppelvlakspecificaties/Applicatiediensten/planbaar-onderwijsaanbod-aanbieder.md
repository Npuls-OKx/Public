# Planbaar-onderwijsaanbod-aanbieder

Stelt het planbare onderwijsaanbod beschikbaar: het stadium tussen specificatie en rooster.

## Doel

Er is aanbod dat herleidbaar is naar de specificatie die het instantieert, zonder dat het specificatie-inhoud dupliceert.

## Verplichtingen

Een component dat deze dienst implementeert:

- stelt een aanbod-instantie beschikbaar op id, met haar onderliggende structuur.
- stelt een opvraag op specificatie-id beschikbaar, die de instanties teruggeeft die die specificatie instantiëren.
- draagt in het aanbodobject een referentie naar specificatie en versie, en geen gekopieerde specificatie-inhoud.
- blijft eigenaar van de instantie: de referentie gaat over de koppeling, de inhoud alleen op verzoek ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)).

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `/onderwijsaanbod/{id}` | GET | `status`, optioneel filter op onderliggende instanties | — | [education-offering.json](../Datamodelschema's/education-offering.json): de instantie plus haar subtree via `bovenliggendAanbodId` | 200, 400, 404 |
| `/onderwijsaanbod` | GET | `specificatieId`, verplicht; `versie`, optioneel, standaard alle versies | — | [education-offering.json](../Datamodelschema's/education-offering.json) als lijst | 200, 400 |

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)

## Tegenhanger

[Planbaar-onderwijsaanbod-afnemer](planbaar-onderwijsaanbod-afnemer.md)
