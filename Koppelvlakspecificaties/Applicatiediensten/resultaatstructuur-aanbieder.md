# Resultaatstructuur-aanbieder

Stelt de resultaatstructuur beschikbaar: welke toetsonderdelen er zijn, hoe zij wegen en hoe zij aggregeren naar het bovenliggende niveau.

## Doel

Afnemers richten hun beoordeling in op dezelfde structuur, en een wijziging daarop is als zodanig herkenbaar voordat zij hem doorvoeren.

## Verplichtingen

Een component dat deze dienst implementeert:

- stelt de resultaatstructuur beschikbaar op id, met versie.
- maakt bekend dat de structuur beschikbaar is en dat zij is gewijzigd.
- draagt bij een wijziging de wijzigingsklasse mee, zodat de afnemer kan bepalen of hij hem kan doorvoeren.
- houdt een eerdere versie beschikbaar, zodat een afnemer die op lopende verbintenissen kan blijven toepassen.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `/examenplanspecificaties/{id}` | GET | `versie`, optioneel, standaard laatst gepubliceerd | — | [result-structure.json](../Datamodelschema's/result-structure.json): toetsonderdelen, weging en aggregatie | 200, 400, 404 |

Het endpoint heet naar de resource, `examenplanspecificaties`, en levert de resultaatstructuur. Welke van de twee namen leidend is, is nog niet vastgelegd.

## Gebruikt in

- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)

## Tegenhanger

[Resultaatstructuur-afnemer](resultaatstructuur-afnemer.md)
