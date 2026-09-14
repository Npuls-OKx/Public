# Onderwijsspecificatie-inname-aanbieder

Het implementerende component neemt een elders ontworpen onderwijsspecificatie aan, stelt hem vast en bevestigt de opname. Dit is de enige inkomende dienst: de specificatie stroomt hier naar het implementerende component toe. Het aanleverende component implementeert [onderwijsspecificatie-inname-afnemer](onderwijsspecificatie-inname-afnemer.md).

## Verplichtingen

Een component dat deze dienst implementeert:

- neemt een aangeleverde specificatiestructuur aan en valideert haar vorm.
- valideert bij opname dat de studielast van onderliggende delen optelt naar het bovenliggende niveau, en wijst af wanneer dat niet klopt.
- bevestigt de opname, of keur af met een reden die de aanleverende partij kan verwerken.
- kent de opgenomen specificatie een eigen identiteit en versie toe.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
