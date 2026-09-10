# Leermiddelkoppeling-aanbieder

Publiceert de leermiddelkoppeling die het component heeft gelegd, als eigen resource met een eigen identiteit.

## Doel

De partij die de specificatie leverde kan tonen welke leermiddelen erbij horen, zonder die zelf te beheren.

## Verplichtingen

Een component dat deze dienst implementeert:

- kent de gelegde koppeling een eigen identiteit toe en serveert haar op die identiteit.
- meldt dat de koppeling beschikbaar is, met de referentie en de specificatie waarop zij slaat.
- blijft eigenaar: levert de referentie, niet de inhoud, in de melding ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)).

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `/leermiddelkoppelingen/{id}` | GET | — | — | Leermiddelkoppeling-instantie: leermiddelgroepen per specificatie. Payloadschema nog niet uitgewerkt | 200, 400, 404 |

## Gebruikt in

- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)

## Tegenhanger

[Leermiddelkoppeling-afnemer](leermiddelkoppeling-afnemer.md)

