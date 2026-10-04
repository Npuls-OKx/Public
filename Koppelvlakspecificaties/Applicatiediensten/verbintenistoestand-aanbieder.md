# Verbintenistoestand-aanbieder

Het implementerende component houdt de toestand van de onderwijsverbintenis bij, per niveau van programma tot toets, en meldt de overgangen. Aan de andere kant staat een component dat [verbintenistoestand-afnemer](verbintenistoestand-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- houdt de toestand per niveau bij, zodat een student in totaal op tempo kan zijn en per werkproces uit ritme.
- meldt een toestandsovergang met de oude en de nieuwe waarde, zodat de afnemer zijn afgeleide beeld bijwerkt zonder op te halen.
- ondersteunt onderbreken en hervatten als geldige overgangen.
- houdt keuze, inschrijving en resultaat gescheiden: deze dienst draagt de verbintenis, niet de keuze en niet het resultaat.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
