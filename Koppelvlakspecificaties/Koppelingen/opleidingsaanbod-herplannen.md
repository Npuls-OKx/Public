# Opleidingsaanbod herplannen

Het planningssysteem laat lopend opleidingsaanbod volgen op een nieuwe specificatieversie en meldt de uitkomst terug aan de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | *(Meer)jaar capaciteitsplanning*, applicatiedienst van het planningssysteem |
| Versie | `1.0` |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-opleidingsaanbod-herplannen` |

![Opleidingsaanbod herplannen op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/opleidingsaanbod-herplannen.png)

## Herplanuitkomst melden

Doel: een lopende planning laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor het planningssysteem. Trigger: de melding [Specificatiewijziging](onderwijsspecificatie-ophalen.md#specificatiewijziging-melden) voor een specificatie die al in een manifest is vastgelegd. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)

![Herplanuitkomst melden: volgorde van de interacties](../src/diagrammen/koppelingen/herplanuitkomst-melden.png)
