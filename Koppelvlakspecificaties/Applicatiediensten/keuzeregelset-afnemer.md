# Keuzeregelset-afnemer

Haalt de geldende regelsets op en past ze toe, zodat zijn uitkomst gelijk is aan die van elk ander component dat dezelfde regel toepast.

## Doel

Elk systeem berekent voor dezelfde keuzeregel dezelfde uitkomst, wat de voorwaarde is om conformiteit te kunnen toetsen.

## Verplichtingen

Een component dat deze dienst implementeert:

- haalt de regelset op in de versie die op het beoordeelde moment gold, niet altijd de laatste.
- evalueert de regel zonder eigen interpretatie toe te voegen.
- legt vast welke regelversie is toegepast, zodat de uitkomst herleidbaar blijft.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.

## Tegenhanger

[Keuzeregelset-aanbieder](keuzeregelset-aanbieder.md)

