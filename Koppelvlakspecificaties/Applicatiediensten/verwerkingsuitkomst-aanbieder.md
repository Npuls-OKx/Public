# Verwerkingsuitkomst-aanbieder

Maakt bekend wat zijn verwerking van een aangeleverde structuur heeft opgeleverd, met een referentie naar wat daarbij is aangemaakt.

## Doel

De aanleverende partij weet of haar levering is verwerkt, en zo niet waarom, zonder op die verwerking te wachten.

## Verplichtingen

Een component dat deze dienst implementeert:

- stelt de uitkomst beschikbaar: ontvangen, gestart, gelukt, niet gelukt of afgekeurd.
- onderscheidt niet-terminale van terminale uitkomsten, zodat de afnemer weet wanneer hij zijn eigen status mag bijstellen.
- draagt bij een geslaagde verwerking een referentie naar wat is aangemaakt, en niet de instantie zelf ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)).
- draagt bij afkeuring of falen de reden, in een vorm die de afnemer kan verwerken.
- behandelt afkeuring als geldige uitkomst: niet kunnen of niet willen verwerken is een antwoord, geen fout.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Geen. De uitkomst wordt gemeld, niet aangeboden op een eigen endpoint; waar zij landt is een inrichtingskeuze van de koppeling. Het endpoint dat haar aanneemt staat bij [verwerkingsuitkomst-afnemer](verwerkingsuitkomst-afnemer.md).

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)

## Tegenhanger

[Verwerkingsuitkomst-afnemer](verwerkingsuitkomst-afnemer.md)
