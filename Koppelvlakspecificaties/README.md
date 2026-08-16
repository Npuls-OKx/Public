# Koppelvlakspecificaties

Het releasepakket **koppelvlakspecificatie**. De inhoudelijke inleiding staat in [inleiding.md](inleiding.md); die gaat mee in het gebouwde document. Deze README beschrijft de map en gaat niet mee: een gereleased document kent de repostructuur niet.

## Wat staat waar

| Waar | Wat erin staat |
|---|---|
| [inleiding.md](inleiding.md) | De inleiding van het releasedocument: context, kernbegrippen, leeswijzer en afkortingen |
| [afbakening.md](afbakening.md) | De kaders waarop de begrippen verankeren, de eisen aan de keten, en de scope |
| [managementsamenvatting.md](managementsamenvatting.md) | Wat er ligt en wat het van een partij vraagt, zonder de specificaties te lezen |
| [`Referentiesystemen/`](Referentiesystemen/) | Per systeem het koppelvlak: de endpoints en events die het serveert, met parameters, payload en statuscodes |
| [`Interactiepatronen/`](Interactiepatronen/) | Per koppeling de functionele eisen, het interactieoverzicht, het berichtgedrag en de sequentiediagrammen |
| [`Datamodelschema's/`](Datamodelschema's/) | De informatiemodellen, de JSON Schema's, de regels die een schema niet kan uitdrukken, de gebruiksprofielen en de voorbeeldpayloads |
| [auth-standaard.md](auth-standaard.md) | De authenticatie die voor elk endpoint geldt |
| [uitgangspunten.md](uitgangspunten.md) | U1 tot en met U10, de aannames onder alles |
| [mapping.md](mapping.md) | Veldnamen Engels naar Nederlands |
| [`templates/`](templates/) | Waarmee je een nieuwe specificatie schrijft |

Wat er in welke volgorde in het releasedocument komt staat in [release.json](release.json).

## Voor schrijvers

Begin bij de [uitgangspunten](uitgangspunten.md) en kopieer daarna het passende template:

- [template-koppelingspecificatie.md](templates/template-koppelingspecificatie.md) voor een informatiestroom tussen twee componenten;
- [template-payload-specificatie.md](templates/template-payload-specificatie.md) voor de JSON die over zo'n koppeling gaat.

Beide templates bevatten instructies tussen HTML-commentaar die je verwijdert als het onderdeel af is. Werk je met een AI-agent, dan hanteert de skill [`okx-koppelingspecificatie`](https://github.com/Npuls-OKx/meta/blob/d47bb0c74ec899a4384d06331692f74b9bd1db58/.agents/skills/okx-koppelingspecificatie/SKILL.md) dezelfde opbouw.
