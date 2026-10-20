# Planninggroepen met studenten ontsluiten

Het kernregistratiesysteem kent de planninggroepen met de studenten die erin zijn geplaatst.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Roostersysteem](../Applicatiecomponenten/roostersysteem.md) |
| Afnemer | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (KRS) |
| Afgeleid van | Geen: het roostersysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-planninggroepen-met-studenten-ontsluiten` |

![Planninggroepen met studenten ontsluiten op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/planninggroepen-met-studenten-ontsluiten.png)

## Planninggroepen met studenten melden

Doel: het kernregistratiesysteem haalt een planninggroep op wanneer de plaatsing van studenten erin wijzigt. Trigger: de plaatsing van studenten in een planninggroep wijzigt. Initiator: Roostersysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
