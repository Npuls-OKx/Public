# Animo doorgeven

Het planningssysteem kent de belangstelling van studenten voor opleidingsprogramma's en opleidingseenheden die nog niet gepland zijn.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afnemer | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afgeleid van | *Keuze aanvraag beheer*, applicatiedienst van het studentkeuzesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-animo-doorgeven` |

![Animo doorgeven op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/animo-doorgeven.png)

## Animo melden

Doel: het planningssysteem haalt de intekeningen op nog niet gepland aanbod op, als invoer voor haalbaar aanbod. Trigger: studenten tekenen in op aanbod dat nog niet gepland is. Initiator: Studentkeuzesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
