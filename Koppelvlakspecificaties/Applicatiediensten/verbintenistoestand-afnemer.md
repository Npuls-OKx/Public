# Verbintenistoestand-afnemer

Het implementerende component volgt de toestandsovergangen van een verbintenis en werkt zijn eigen afgeleide beeld daarop bij. Aan de andere kant staat een component dat [verbintenistoestand-aanbieder](verbintenistoestand-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- ontvangt de overgang met oude en nieuwe waarde en werkt het afgeleide beeld bij zonder op te halen.
- verwerkt de overgangen in volgorde per verbintenis; een verloren of omgedraaide overgang is hier niet met een opvraag te herstellen.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
