# Leergelegenheden roosteren

Het roostersysteem plaatst de geplande leergelegenheden in tijd en ruimte en meldt het rooster terug aan het planningssysteem.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Roostersysteem](../Applicatiecomponenten/roostersysteem.md) |
| Afnemer | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afgeleid van | Geen: het roostersysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | — |
| Vereist | [Planninggroepen ontsluiten](planninggroepen-ontsluiten.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-leergelegenheden-roosteren` |

![Leergelegenheden roosteren op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/leergelegenheden-roosteren.png)

## Roosteren aanvragen

Doel: geplande leergelegenheden een plek in tijd en ruimte geven, met het rooster als uitkomst. Trigger: het planningssysteem stelt de leergelegenheden voor een periode vast. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [geroosterd-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-aanbieder.md), [geroosterd-onderwijsaanbod-afnemer](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-afnemer.md) |

Endpoints: nog niet vastgelegd.
