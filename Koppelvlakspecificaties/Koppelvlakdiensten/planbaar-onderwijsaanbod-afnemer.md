# Planbaar-onderwijsaanbod-afnemer

Het implementerende component neemt het planbare onderwijsaanbod af op de referentie die het heeft gekregen. Aan de andere kant staat een component dat [planbaar-onderwijsaanbod-aanbieder](planbaar-onderwijsaanbod-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- haalt een aanbod-instantie op via een referentie wanneer hij haar wil inzien.
- stelt via de opvraag op specificatie-id vast welke instanties bij een specificatie horen.
- werkt met de referentie waar dat kan, en haalt de instantie alleen op wanneer de inhoud nodig is.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Geen eigen endpoint. **Ophalen is vereist**: het component haalt het aanbod op bij [planbaar-onderwijsaanbod-aanbieder](planbaar-onderwijsaanbod-aanbieder.md), met `GET /onderwijsaanbod/{id}` en `GET /onderwijsaanbod`, wanneer het de inhoud nodig heeft. Dat er aanbod is, hoort het op het endpoint van [verwerkingsuitkomst-afnemer](verwerkingsuitkomst-afnemer.md).

## Gebruikt in

- [Opleidingsaanbod aanmaken](../Koppelingen/opleidingsaanbod-aanmaken.md)
- [Geplande leergelegenheden ontsluiten](../Koppelingen/geplande-leergelegenheden-ontsluiten.md)
