# Leeromgeving inrichten

Het leermanagementsysteem richt de leeromgeving in op een gepubliceerde specificatie en meldt de uitkomst en de gelegde leermiddelkoppeling terug aan de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | Geen: het leermanagementsysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | `1.0` |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-leeromgeving-inrichten` |

![Leeromgeving inrichten op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/leeromgeving-inrichten.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0003](../../Referentiemateriaal/requirementsboom/stories.md#story-0003) | [Leeromgeving inrichten en leermiddelkoppeling melden](#leeromgeving-inrichten-en-leermiddelkoppeling-melden) |
| [story-0029](../../Referentiemateriaal/requirementsboom/stories.md#story-0029) | [Leeromgeving inrichten en leermiddelkoppeling melden](#leeromgeving-inrichten-en-leermiddelkoppeling-melden) |

## Leeromgeving inrichten en leermiddelkoppeling melden

Doel: een gepubliceerde specificatie omzetten in een ingerichte leeromgeving, met een leermiddelkoppeling terug naar de onderwijscatalogus. Trigger: de melding [Specificatie beschikbaar](onderwijsspecificatie-ophalen.md#specificatie-beschikbaar-melden) en het ophalen van de structuur. Initiator: Leermanagementsysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md), [Event Notification](../Interactiepatronen/event-notification.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md), [leermiddelkoppeling-aanbieder](../Koppelvlakdiensten/leermiddelkoppeling-aanbieder.md), [leermiddelkoppeling-afnemer](../Koppelvlakdiensten/leermiddelkoppeling-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)
- [webhook `leermiddelkoppeling-beschikbaar`](../Koppelvlakdiensten/leermiddelkoppeling-afnemer.md)
- [`GET /leermiddelkoppelingen/{id}` (optioneel)](../Koppelvlakdiensten/leermiddelkoppeling-aanbieder.md)

![Leeromgeving inrichten en leermiddelkoppeling melden: volgorde van de interacties](../src/diagrammen/koppelingen/leeromgeving-inrichten-en-leermiddelkoppeling-melden.png)
