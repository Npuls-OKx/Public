# Nominaal template inrichten

Het studentinformatiesysteem richt met een gepubliceerde specificatie en resultaatstructuur het nominale template in, en meldt de uitkomst terug aan de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (SVS) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | Geen: het studentvolgsysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | `1.0` |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Resultaatstructuur ophalen](resultaatstructuur-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-nominaal-template-inrichten` |

![Nominaal template inrichten op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/nominaal-template-inrichten.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0022](../../Referentiemateriaal/requirementsboom/stories.md#story-0022) | [Nominaal template en resultaatstructuur inrichten](#nominaal-template-en-resultaatstructuur-inrichten) |
| [story-0023](../../Referentiemateriaal/requirementsboom/stories.md#story-0023) | [Nominaal template en resultaatstructuur inrichten](#nominaal-template-en-resultaatstructuur-inrichten) |

## Nominaal template en resultaatstructuur inrichten

Doel: een gepubliceerde specificatie en examenplanspecificatie omzetten in een ingericht nominaal template en resultaatstructuur bij het studentinformatiesysteem. Trigger: de meldingen [Specificatie beschikbaar](onderwijsspecificatie-ophalen.md#specificatie-beschikbaar-melden) en [Resultaatstructuur beschikbaar](resultaatstructuur-ophalen.md#resultaatstructuur-beschikbaar-melden), en het ophalen van beide. Initiator: Studentinformatiesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)

![Nominaal template en resultaatstructuur inrichten: volgorde van de interacties](../src/diagrammen/koppelingen/nominaal-template-en-resultaatstructuur-inrichten.png)
