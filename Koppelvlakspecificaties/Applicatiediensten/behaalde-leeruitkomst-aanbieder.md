# Behaalde-leeruitkomst-aanbieder

Het implementerende component publiceert welke leeruitkomsten een student heeft behaald, met de bewijsvoering die daarbij hoort. Aan de andere kant staat een component dat [behaalde-leeruitkomst-afnemer](behaalde-leeruitkomst-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- serveert behaalde leeruitkomsten per student, gewogen en herleidbaar naar het resultaat waaruit zij volgen.
- levert de bewijsvoering mee of als opvraagbare referentie, zodat een afnemer meer heeft dan een status.
- gebruikt het leeruitkomst-id als verbindende sleutel, zonder de inhoud van de leeruitkomst te hoeven delen.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
