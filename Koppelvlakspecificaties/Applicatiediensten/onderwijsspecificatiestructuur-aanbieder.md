# Onderwijsspecificatiestructuur-aanbieder

Het implementerende component stelt de vastgestelde onderwijsspecificatiestructuur beschikbaar en maakt bekend wanneer die verandert. Elk component dat onderwijsspecificaties bezit kan deze dienst implementeren; aan de andere kant staat een component dat [onderwijsspecificatiestructuur-afnemer](onderwijsspecificatiestructuur-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- stelt de structuur beschikbaar op id, met de versie als parameter en de laatst gepubliceerde als standaard.
- stelt daarnaast de delta tussen twee versies beschikbaar, zodat de afnemer kan kiezen wat hij ophaalt ([U11](../uitgangspunten.md#u11-toekomstvaste-endpoints-volledige-structuur-en-delta)).
- stelt een lijst beschikbaar met filter op status en wijzigingsmoment, zodat een afnemer kan vaststellen wat hij mist.
- maakt bekend dat een specificatie beschikbaar is, dat hij is gewijzigd, en dat zijn status is gewijzigd zonder nieuwe versie.
- houdt een eerder afgegeven verwijzing geldig: de vorige versie blijft beschikbaar voor lopend gebruik, de nieuwe geldt voor nieuw gebruik.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `/onderwijsspecificaties/{id}` | GET | `versie`, optioneel, standaard laatst gepubliceerd | — | [education-specification.json](../../Datamodelschema's/schemas/education-specification.json) | 200, 400, 404 |
| `/onderwijsspecificaties/{id}/delta` | GET | `van` en `naar`, beide verplicht | — | JSON Patch (RFC 6902), [education-specification-delta.json](../../Datamodelschema's/schemas/education-specification-delta.json) | 200, 400, 404 |
| `/onderwijsspecificaties` | GET | `status`, optioneel, standaard `gepubliceerd`; `gewijzigdSinds`, optioneel | — | Lijst van [specification-reference.json](../../Datamodelschema's/schemas/specification-reference.json) | 200, 400 |

Het bekendmaken van een wijziging vraagt geen endpoint van de aanbieder: waar die melding landt hangt af van hoe de koppeling is ingericht.

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)
