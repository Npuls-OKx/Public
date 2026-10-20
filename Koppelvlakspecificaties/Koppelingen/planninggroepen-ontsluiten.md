# Planninggroepen ontsluiten

Het roostersysteem kent de planninggroepen bij de leergelegenheden die het roostert.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afnemer | [Roostersysteem](../Applicatiecomponenten/roostersysteem.md) |
| Afgeleid van | *Periode planning*, applicatiedienst van het planningssysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-planninggroepen-ontsluiten` |

![Planninggroepen ontsluiten op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/planninggroepen-ontsluiten.png)

## Planninggroepen melden

Doel: het roostersysteem haalt de planninggroepen van een periode op zodra die zijn vastgesteld. Trigger: het planningssysteem stelt de planninggroepen voor een periode vast. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
