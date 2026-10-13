# Verwerkingsuitkomst-afnemer

Het implementerende component neemt de uitkomst van een verwerking af en stelt zijn eigen beeld daarop bij. Aan de andere kant staat een component dat [verwerkingsuitkomst-aanbieder](verwerkingsuitkomst-aanbieder.md) implementeert.

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
| `verwerkingsuitkomst` | POST | — | [processing-status.json](../../Informatie-en-gegevensmodellen/schemas/processing-status.json) | — | 200 |

Dit endpoint heet vandaag `verwerkingsstatus` bij het planningssysteem en `inrichtingsstatus` bij het studentinformatiesysteem en het leermanagementsysteem; alleen de eerste draagt een schema. De naam hierboven is de voorgestelde keuze; die is nog niet vastgesteld.

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)
