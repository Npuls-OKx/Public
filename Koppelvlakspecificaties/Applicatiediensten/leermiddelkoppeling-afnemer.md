# Leermiddelkoppeling-afnemer

Het implementerende component volgt de gelegde leermiddelkoppelingen en haalt ze op om ze bij het aanbod te tonen. Aan de andere kant staat een component dat [leermiddelkoppeling-aanbieder](leermiddelkoppeling-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- ontvangt de melding dat een koppeling beschikbaar is.
- haalt de koppeling op via de referentie, en toont of gebruikt haar zonder een eigen kopie aan te leggen.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `leermiddelkoppeling-beschikbaar` | POST | — | Referentie naar de koppeling, specificatie-id en versie. Payloadschema nog niet uitgewerkt | — | 200 |

## Gebruikt in

- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)
