# Verwerkingsuitkomst-aanbieder

Het implementerende component maakt bekend wat zijn verwerking van een aangeleverde structuur heeft opgeleverd, met een referentie naar wat daarbij is aangemaakt. Aan de andere kant staat een component dat [verwerkingsuitkomst-afnemer](verwerkingsuitkomst-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- meldt de uitkomst: ontvangen, gestart, gelukt, niet gelukt of afgekeurd.
- onderscheidt niet-terminale van terminale uitkomsten, zodat de afnemer weet wanneer hij zijn eigen status mag bijstellen.
- draagt bij een geslaagde verwerking een referentie naar wat is aangemaakt, en niet de instantie zelf ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)).
- draagt bij afkeuring of falen de reden, in een vorm die de afnemer kan verwerken.
- behandelt afkeuring als geldige uitkomst: niet kunnen of niet willen verwerken is een antwoord, geen fout.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Geen eigen endpoint: het component verstuurt de uitkomst alleen. Het endpoint dat haar aanneemt, `verwerkingsuitkomst`, staat bij [verwerkingsuitkomst-afnemer](verwerkingsuitkomst-afnemer.md).

## Gebruikt in

- [Opleidingsaanbod aanmaken](../Koppelingen/opleidingsaanbod-aanmaken.md)
- [Opleidingsaanbod herplannen](../Koppelingen/opleidingsaanbod-herplannen.md)
- [Late wijziging toetsen](../Koppelingen/late-wijziging-toetsen.md)
- [Leeromgeving inrichten](../Koppelingen/leeromgeving-inrichten.md)
- [Leeromgeving bijwerken](../Koppelingen/leeromgeving-bijwerken.md)
- [Nominaal template inrichten](../Koppelingen/nominaal-template-inrichten.md)
- [Examenplanwijziging toetsen](../Koppelingen/examenplanwijziging-toetsen.md)
