# Onderwijsspecificatiestructuur-afnemer

Kan de onderwijsspecificatiestructuur van een aanbieder afnemen en actueel houden. Eén contract, ongeacht waarvoor het component de specificatie gebruikt.

## Doel

Het component werkt nooit op een verouderde specificatie, ook niet wanneer een melding verloren gaat.

## Verplichtingen

Een component dat deze dienst implementeert:

- neemt de meldingen aan dat een specificatie beschikbaar is, is gewijzigd, of van status is veranderd.
- haalt de structuur of de delta op wanneer het hem uitkomt; de melding legt geen termijn op.
- verwerkt dezelfde melding tweemaal zonder effect.
- stelt na een gemiste of onverwerkbare melding alsnog vast wat ontbreekt, via de lijst, en haalt dat op.
- werkt op de versie die de melding noemt, en niet ongevraagd op een nieuwere.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `specificatie-beschikbaar` | POST | — | [specification-reference.json](../Datamodelschema's/specification-reference.json) | — | 200 |
| `specificatie-gewijzigd` | POST | — | [specification-changed.json](../Datamodelschema's/specification-changed.json) | — | 200 |
| `specificatie-status-gewijzigd` | POST | — | [specification-status-changed.json](../Datamodelschema's/specification-status-changed.json) | — | 200 |

Het eerste endpoint heet vandaag `specificatie-planbaar` bij het planningssysteem, `specificatie-beschikbaar` bij het leermanagementsysteem en `specificatie-en-resultaatstructuur-beschikbaar` bij het studentinformatiesysteem, terwijl het om hetzelfde bericht gaat. De naam hierboven is de voorgestelde keuze; die is nog niet vastgesteld.

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)

## Tegenhanger

[Onderwijsspecificatiestructuur-aanbieder](onderwijsspecificatiestructuur-aanbieder.md)
