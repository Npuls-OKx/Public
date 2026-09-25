# Geroosterd-onderwijsaanbod-aanbieder

Het implementerende component publiceert geroosterd onderwijsaanbod per periode: het derde en laatste stadium van aanbod. Aan de andere kant staat een component dat [geroosterd-onderwijsaanbod-afnemer](geroosterd-onderwijsaanbod-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- serveert het geroosterde aanbod per periode, met een referentie naar het planbare aanbod waaruit het volgt.
- meldt dat het rooster voor een periode bekend is.
- houdt de referentie naar aanbod en specificatie intact, zodat de keten van rooster tot specificatie herleidbaar blijft.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
