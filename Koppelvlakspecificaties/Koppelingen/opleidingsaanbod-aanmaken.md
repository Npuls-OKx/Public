# Opleidingsaanbod aanmaken

Het planningssysteem maakt van een gepubliceerde opleidingsprogramma- of onderwijseenheidspecificatie planbaar opleidingsaanbod, en meldt de uitkomst met een referentie naar dat aanbod terug aan de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | *(Meer)jaar capaciteitsplanning*, applicatiedienst van het planningssysteem |
| Versie | `1.0` |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-opleidingsaanbod-aanmaken` |

![Opleidingsaanbod aanmaken op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/opleidingsaanbod-aanmaken.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0007](../../Referentiemateriaal/requirementsboom/stories.md#story-0007) | [Planuitkomst melden](#planuitkomst-melden) en [Planning niet gelukt melden](#planning-niet-gelukt-melden) |

## Planuitkomst melden

Doel: het planningssysteem meldt of het van een opgehaalde specificatie planbaar `opleidingsaanbod` kon maken, met een referentie naar dat aanbod. Trigger: de melding [Specificatie beschikbaar](onderwijsspecificatie-ophalen.md#specificatie-beschikbaar-melden) en het ophalen van de structuur. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md), [planbaar-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md), [planbaar-onderwijsaanbod-afnemer](../Koppelvlakdiensten/planbaar-onderwijsaanbod-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)
- [`GET /onderwijsaanbod/{id}` (optioneel)](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md)

![Planuitkomst melden: volgorde van de interacties](../src/diagrammen/koppelingen/planuitkomst-melden.png)

## Planning niet gelukt melden

Doel: de onderwijscatalogus in kennis stellen dat een specificatie voor een of meer cohorten niet planbaar blijkt, met referentie en knelpunten, zonder de aanroep te blokkeren. Trigger: planproces bij het planningssysteem vindt geen geldige planning. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md), [planbaar-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)
- [`GET /onderwijsaanbod/{id}` (optioneel)](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md)

![Planning niet gelukt melden: volgorde van de interacties](../src/diagrammen/koppelingen/planning-niet-gelukt-melden.png)
