# Verwerkingsuitkomst-afnemer

Het implementerende component neemt de uitkomst van een verwerking af en stelt zijn eigen beeld daarop bij. Aan de andere kant staat een component dat [verwerkingsuitkomst-aanbieder](verwerkingsuitkomst-aanbieder.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- neemt elke uitkomst aan, ook een niet-terminale, en bevestigt de ontvangst.
- stelt de eigen afgeleide status alleen bij op een terminale uitkomst.
- behandelt afkeuring als geldige uitkomst en niet als fout van het kanaal.
- haalt het aangemaakte op via de meegeleverde referentie wanneer hij het wil inzien.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `verwerkingsuitkomst` | POST | — | [processing-status.json](../../Informatie-en-gegevensmodellen/schemas/processing-status.json) | — | 200 |

## Gebruikt in

- [Opleidingsaanbod aanmaken](../Koppelingen/opleidingsaanbod-aanmaken.md)
- [Opleidingsaanbod herplannen](../Koppelingen/opleidingsaanbod-herplannen.md)
- [Late wijziging toetsen](../Koppelingen/late-wijziging-toetsen.md)
- [Leeromgeving inrichten](../Koppelingen/leeromgeving-inrichten.md)
- [Leeromgeving bijwerken](../Koppelingen/leeromgeving-bijwerken.md)
- [Nominaal template inrichten](../Koppelingen/nominaal-template-inrichten.md)
- [Examenplanwijziging toetsen](../Koppelingen/examenplanwijziging-toetsen.md)
