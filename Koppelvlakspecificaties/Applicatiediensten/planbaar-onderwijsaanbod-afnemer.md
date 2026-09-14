# Planbaar-onderwijsaanbod-afnemer

Het implementerende component neemt het planbare onderwijsaanbod af op de referentie die het heeft gekregen. Aan de andere kant staat een component dat [planbaar-onderwijsaanbod-aanbieder](planbaar-onderwijsaanbod-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- haalt een aanbod-instantie op via een referentie wanneer hij haar wil inzien.
- stelt via de opvraag op specificatie-id vast welke instanties bij een specificatie horen.
- werkt met de referentie waar dat kan, en haalt de instantie alleen op wanneer de inhoud nodig is.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Geen. Deze dienst vraagt geen eigen endpoints: de afnemer haalt op bij de aanbieder en stelt zelf niets beschikbaar. Dat er aanbod is, blijkt uit [verwerkingsuitkomst-afnemer](verwerkingsuitkomst-afnemer.md).

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
