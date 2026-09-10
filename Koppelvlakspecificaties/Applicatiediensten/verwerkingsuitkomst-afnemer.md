# Verwerkingsuitkomst-afnemer

Kan de uitkomst van een verwerking afnemen en zijn eigen beeld daarop bijstellen.

## Doel

De aanleverende partij hoeft niet te wachten en weet toch wat er met haar levering is gebeurd.

## Verplichtingen

Een component dat deze dienst implementeert:

- neemt elke uitkomst aan, ook een niet-terminale, en bevestigt de ontvangst.
- stelt de eigen afgeleide status alleen bij op een terminale uitkomst.
- behandelt afkeuring als geldige uitkomst en niet als fout van het kanaal.
- haalt het aangemaakte op via de meegeleverde referentie wanneer hij het wil inzien.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `verwerkingsuitkomst` | POST | — | [processing-status.json](../Datamodelschema's/processing-status.json) | — | 200 |

Dit endpoint heet vandaag `verwerkingsstatus` bij het planningssysteem en `inrichtingsstatus` bij het studentinformatiesysteem en het leermanagementsysteem; alleen de eerste draagt een schema. De naam hierboven is de voorgestelde keuze; die is nog niet vastgesteld.

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)

## Tegenhanger

[Verwerkingsuitkomst-aanbieder](verwerkingsuitkomst-aanbieder.md)
