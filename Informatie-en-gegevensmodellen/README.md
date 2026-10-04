# Informatie- en gegevensmodellen

Het releasepakket **informatie- en gegevensmodellen**. De inhoudelijke inleiding staat in [inleiding.md](inleiding.md); die gaat mee in het gebouwde document. Deze README beschrijft de map en gaat niet mee: een gereleased document kent de repostructuur niet.

## Wat staat waar

De indeling volgt de modelleerlagen van OKx. Laag 1 (begrippen) en laag 2 (conceptueel informatiemodel) staan nog niet in dit pakket.

| Waar | Laag | Wat erin staat |
|---|---|---|
| [informatie-en-gegevensmodellen.md](informatie-en-gegevensmodellen.md) | — | Het volledige releasedocument als markdown. **Gegenereerd**: bouw opnieuw in plaats van het met de hand te wijzigen |
| [inleiding.md](inleiding.md) | — | De inleiding van het releasedocument: aanleiding, context, doel en scope |
| [logisch-gegevensmodel.md](logisch-gegevensmodel.md) | 3 | Per begrippenfamilie de entiteiten, hun velden en hun onderlinge relaties |
| [regels.md](regels.md) | 3 | Wat geldt bovenop het schema: aggregatie, versionering, wijzigingsklassen, knelpuntcodes |
| [`schemas/`](schemas/) | 4 | De JSON Schema's zelf, één bestand per resource |
| [voorbeeldpayloads.md](voorbeeldpayloads.md) | 4 | Ingevulde payloads met indicatieve waarden |
| [mapping.md](mapping.md) | 4 | Veldnamen Engels naar Nederlands |
| [gebruiksprofielen.md](gebruiksprofielen.md) | — | Per koppeling welk deel van de gedeelde payload meegaat; snijdt dwars door laag 3 en 4 |

Wat er in welke volgorde in het releasedocument komt staat in [release.json](release.json).

## Verhouding met de koppelvlakspecificatie

Dit pakket draagt de **vorm** van de gegevens, de [koppelvlakspecificatie](../Koppelvlakspecificaties/README.md) het **gebruik** ervan: welke applicatiedienst welke payload over welk endpoint stuurt. Die specificatie verwijst naar dit pakket op een vastgelegde versie, zodat een schemawijziging hier niet stilzwijgend de betekenis daar verschuift. Het manifest van de koppelvlakspecificatie noemt die versie onder `afhankelijkheden`; verhoog je de versie hier, dan hoort die vermelding mee te bewegen.

De schema's zijn de bron. Een bijlage die met de hand was overgeschreven zou bij de eerste schemawijziging uit de pas gaan lopen, dus het gebouwde document leest ze bij het bouwen in uit [`schemas/`](schemas/).
