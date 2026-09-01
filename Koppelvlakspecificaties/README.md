# Koppelvlakspecificaties

Het releasepakket **koppelvlakspecificatie**. De inhoudelijke inleiding staat in [inleiding.md](inleiding.md); die gaat mee in het gebouwde document. Deze README beschrijft de map en gaat niet mee: een gereleased document kent de repostructuur niet.

## Wat staat waar

| Waar | Wat erin staat |
|---|---|
| [koppelvlakspecificatie.md](koppelvlakspecificatie.md) | Het volledige releasedocument als markdown. **Gegenereerd**: bouw opnieuw in plaats van het met de hand te wijzigen |
| [inleiding.md](inleiding.md) | De inleiding van het releasedocument: context, kernbegrippen, leeswijzer en afkortingen |
| [`../Referentiemateriaal/requirementsboom/`](../Referentiemateriaal/requirementsboom/) | De requirementsboom: opdracht, epics, features en stories. Staat buiten deze map en gaat wel mee in het gebouwde document |
| [`Applicatiecomponenten/`](Applicatiecomponenten/) | Per systeem het koppelvlak: de endpoints en events die het serveert, met parameters, payload en statuscodes |
| [`Interactiepatronen/`](Interactiepatronen/) | Per koppeling de functionele eisen, het interactieoverzicht, het berichtgedrag en de sequentiediagrammen |
| [`Datamodelschema's/`](Datamodelschema's/) | De informatiemodellen, de JSON Schema's, de regels die een schema niet kan uitdrukken, de gebruiksprofielen en de voorbeeldpayloads |
| [auth-standaard.md](auth-standaard.md) | De authenticatie die voor elk endpoint geldt |
| [uitgangspunten.md](uitgangspunten.md) | U1 tot en met U10, de aannames onder alles |
| [mapping.md](mapping.md) | Veldnamen Engels naar Nederlands |

Wat er in welke volgorde in het releasedocument komt staat in [release.json](release.json).

## Koppelvlak versus koppeling

![Koppelvlak versus koppeling](src/applicatie_component_koppelvlak_view.png)

Een **koppeling** is de gestandaardiseerde informatiestroom tussen twee applicatiecomponenten; een **koppelvlak** is de optelsom van alle koppelingen die één component raken ([ADR 0021](../Referentiemateriaal/adr/0021-koppeling-versus-koppelvlak-terminologie.md)). De mappen hierboven volgen die knip: de [interactiepatronen](Interactiepatronen/) beschrijven per koppeling de functionele eisen en het berichtgedrag, de [applicatiecomponenten](Applicatiecomponenten/) tonen per component het koppelvlak met de endpoints en events die het serveert.

Elke interactie van een koppelvlak is te herleiden tot een informatiestroom op de [informatiestromen-hoofdplaat](src/informatiestromen_hoofdplaat_v1_7.png) (versie 1.7 is leidend; de legenda draagt nog "concept", dus richtinggevend). Die lijn loopt van scenario naar informatiestroom, naar koppeling, naar koppelvlak: een scenario maakt zichtbaar welke informatie moet bewegen, de hoofdplaat toont die beweging als stroom, de koppeling standaardiseert de stroom, en het koppelvlak bundelt wat één component daarvan serveert.

