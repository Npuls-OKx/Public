# Kiesbaarheidsbepaling-aanbieder

Het implementerende component bepaalt voor een student welke onderwijsspecificaties hij mag kiezen: het berekent een oordeel uit regelsets en behaalde leeruitkomsten in plaats van een resource te ontsluiten. Aan de andere kant staat een component dat [kiesbaarheidsbepaling-afnemer](kiesbaarheidsbepaling-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- beoordeelt kiesbaarheid op elk specificatieniveau en op leeruitkomsten van elke orde, met dezelfde regelvorm.
- betrekt voorwaarden vooraf, uitgedrukt in behaalde leeruitkomsten en niet in doorlopen specificaties.
- geeft bij niet-kiesbaar de reden terug, zodat de afnemer die kan tonen.
- geeft dezelfde uitkomst op dezelfde vraag met dezelfde regelversie.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
