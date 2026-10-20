# Planningselementen ontsluiten

De onderwijscatalogus kent de planningselementen die het planningssysteem hanteert, zodat specificaties daarbinnen blijven.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | *(Meer)jaar capaciteitsplanning*, applicatiedienst van het planningssysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-planningselementen-ontsluiten` |

![Planningselementen ontsluiten op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/planningselementen-ontsluiten.png)

## Planningselementen melden

Doel: de onderwijscatalogus haalt de planningselementen op wanneer het planningssysteem ze vastlegt of wijzigt. Trigger: het planningssysteem legt planningselementen vast of wijzigt ze. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
