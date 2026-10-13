# Informatie- en gegevensmodellen

Het releasepakket **informatie- en gegevensmodellen**. De inhoudelijke inleiding staat in [inleiding.md](inleiding.md); die gaat mee in het gebouwde document. Deze README beschrijft de map en gaat niet mee: een gereleased document kent de repostructuur niet.

## Wat staat waar

De indeling volgt de modelleerlagen van OKx, van betekenis naar techniek.

| Waar | Laag | Wat erin staat |
|---|---|---|
| [informatie-en-gegevensmodellen.md](informatie-en-gegevensmodellen.md) | — | Het volledige releasedocument als markdown. **Gegenereerd**: bouw opnieuw in plaats van het met de hand te wijzigen |
| [inleiding.md](inleiding.md) | — | De inleiding van het releasedocument: aanleiding, context, doel en scope |
| [begrippen.md](begrippen.md) | 1 | Per begrip de definitie, de vindplaats en de relatie met MORA en het Kernmodel Onderwijsinformatie binnen ROSA |
| [informatiemodel.md](informatiemodel.md) | 2 | De plaat met de objecttypen en hun relaties, de notatie, de ontwerpkeuzes en de brug naar de entiteiten van laag 3 |
| [informatiemodel-oeapi-mapping.md](informatiemodel-oeapi-mapping.md) | 2 | Dezelfde objecttypen naast OEAPI v6: wat OEAPI draagt en waarvoor nog geen equivalent is geïdentificeerd |
| [`img/`](img/) | 2 | De twee platen: het informatiemodel en het informatiemodel naast OEAPI v6 |
| [`informatiemodel.json`](informatiemodel.json), [`begrippen.json`](begrippen.json), [`referentiekaders.json`](referentiekaders.json) | 1, 2 | Laag 1 en 2 machineleesbaar: de objecttypen met hun relaties en OEAPI-koppelingen, de begrippen met definitie en bron, de letterlijk overgenomen definities uit de kaders |
| [logisch-gegevensmodel.md](logisch-gegevensmodel.md) | 3 | Per begrippenfamilie de entiteiten, hun velden en hun onderlinge relaties |
| [regels.md](regels.md) | 3 | Wat geldt bovenop het schema: aggregatie, versionering, wijzigingsklassen, knelpuntcodes |
| [`schemas/`](schemas/) | 4 | De JSON Schema's zelf, één bestand per resource |
| [voorbeeldpayloads.md](voorbeeldpayloads.md) | 4 | Ingevulde payloads met indicatieve waarden |
| [mapping.md](mapping.md) | 4 | Veldnamen Engels naar Nederlands |
| [gebruiksprofielen.md](gebruiksprofielen.md) | — | Per koppeling welk deel van de gedeelde payload meegaat; snijdt dwars door laag 3 en 4 |

Wat er in welke volgorde in het releasedocument komt staat in [release.json](release.json).

## Herkomst van laag 1 en 2

Het ArchiMate-model waaruit de platen en `informatiemodel.json` komen, `begrippen.json` en de generatoren staan in de [meta-repository](https://github.com/Npuls-OKx/meta); daar wordt gemodelleerd en gereviewd. De documenten van laag 1 en 2 hier zijn de release-variant: geschreven door `scripts/publiceer-informatiemodel.py` in meta, met de verwijzingen omgezet naar paden binnen dit repository en de resterende verwijzingen naar meta gepind op een commit. Wijzig ze niet met de hand; een wijziging begint in meta en komt via dat script terug.

## Verhouding met de koppelvlakspecificatie

Dit pakket draagt de **vorm** van de gegevens, de [koppelvlakspecificatie](../Koppelvlakspecificaties/README.md) het **gebruik** ervan: welke applicatiedienst welke payload over welk endpoint stuurt. Die specificatie verwijst naar dit pakket op een vastgelegde versie, zodat een schemawijziging hier niet stilzwijgend de betekenis daar verschuift. Het manifest van de koppelvlakspecificatie noemt die versie onder `afhankelijkheden`; verhoog je de versie hier, dan hoort die vermelding mee te bewegen.

De schema's zijn de bron. Een bijlage die met de hand was overgeschreven zou bij de eerste schemawijziging uit de pas gaan lopen, dus het gebouwde document leest ze bij het bouwen in uit [`schemas/`](schemas/).
