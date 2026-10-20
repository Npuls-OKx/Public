# Onderwijsaanbod-zoekvraag-aanbieder

Het implementerende component beantwoordt zoekvragen op het onderwijsaanbod met criteria die rechtstreeks uit de leervraag volgen: het ontsluit geen resource maar berekent een selectie. Aan de andere kant staat een component dat [onderwijsaanbod-zoekvraag-afnemer](onderwijsaanbod-zoekvraag-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- accepteert de keuzecriteria als queryparameters, niet als vrije zoektekst.
- geeft terug welk aanbod aan alle opgegeven criteria voldoet, als verwijzingen.
- geeft dezelfde uitkomst op dezelfde vraag: de zoekvraag heeft geen neveneffect en is herhaalbaar.
- ondersteunt ten minste de criteria die uit locatie en periode volgen, zodat onhaalbaar aanbod niet in de uitkomst valt.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
