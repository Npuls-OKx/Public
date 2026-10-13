# Behaalde-leeruitkomst-afnemer

Het implementerende component haalt de behaalde leeruitkomsten van een student op om er voorwaarden vooraf, vrijstelling of toetsbaarheid op te bepalen. Aan de andere kant staat een component dat [behaalde-leeruitkomst-aanbieder](behaalde-leeruitkomst-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- toetst voorwaarden vooraf op behaalde leeruitkomsten en niet op doorlopen specificaties.
- behandelt een leeruitkomst die elders is behaald gelijk aan een die binnen de eigen instelling is behaald.
- gebruikt het leeruitkomst-id als sleutel, zonder de inhoud nodig te hebben.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
