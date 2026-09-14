# Datamodelschema's

Het releasepakket **datamodelschema's**. De inhoudelijke inleiding staat in [inleiding.md](inleiding.md); die gaat mee in het gebouwde document. Deze README beschrijft de map en gaat niet mee: een gereleased document kent de repostructuur niet.

## Wat staat waar

| Waar | Wat erin staat |
|---|---|
| [datamodelschemas.md](datamodelschemas.md) | Het volledige releasedocument als markdown. **Gegenereerd**: bouw opnieuw in plaats van het met de hand te wijzigen |
| [inleiding.md](inleiding.md) | De inleiding van het releasedocument: aanleiding, context, doel en scope |
| [informatiemodellen.md](informatiemodellen.md) | Per begrippenfamilie de entiteiten, hun velden en hun onderlinge relaties |
| [regels.md](regels.md) | Wat geldt bovenop het schema: aggregatie, versionering, wijzigingsklassen, knelpuntcodes |
| [gebruiksprofielen.md](gebruiksprofielen.md) | Per koppeling welk deel van de gedeelde payload meegaat |
| [`schemas/`](schemas/) | De JSON Schema's zelf, één bestand per resource |
| [voorbeeldpayloads.md](voorbeeldpayloads.md) | Ingevulde payloads met indicatieve waarden |
| [mapping.md](mapping.md) | Veldnamen Engels naar Nederlands |

Wat er in welke volgorde in het releasedocument komt staat in [release.json](release.json).

## Verhouding met de koppelvlakspecificatie

Dit pakket draagt de **vorm** van de gegevens, de [koppelvlakspecificatie](../Koppelvlakspecificaties/README.md) het **gebruik** ervan: welke applicatiedienst welke payload over welk endpoint stuurt. Die specificatie verwijst naar dit pakket op een vastgelegde versie, zodat een schemawijziging hier niet stilzwijgend de betekenis daar verschuift. Het manifest van de koppelvlakspecificatie noemt die versie onder `afhankelijkheden`; verhoog je de versie hier, dan hoort die vermelding mee te bewegen.

De schema's zijn de bron. Een bijlage die met de hand was overgeschreven zou bij de eerste schemawijziging uit de pas gaan lopen, dus het gebouwde document leest ze bij het bouwen in uit [`schemas/`](schemas/).
