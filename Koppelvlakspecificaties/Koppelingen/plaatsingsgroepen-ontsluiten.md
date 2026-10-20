# Plaatsingsgroepen ontsluiten

Het planningssysteem kent de plaatsingsgroepen met hun studenten, zodat het plant op de werkelijke groepen.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (KRS) |
| Afnemer | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afgeleid van | *Inschrijving op opleidingsprogramma*, applicatiedienst van het kernregistratiesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-plaatsingsgroepen-ontsluiten` |

![Plaatsingsgroepen ontsluiten op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/plaatsingsgroepen-ontsluiten.png)

## Plaatsingsgroepen melden

Doel: het planningssysteem haalt een plaatsingsgroep op wanneer die ontstaat of wijzigt. Trigger: inschrijvingen leiden tot een nieuwe of gewijzigde plaatsingsgroep. Initiator: Studentinformatiesysteem (KRS).

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
