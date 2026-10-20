# Verbintenis en planninggroep doorgeven

Het leermanagementsysteem geeft een student toegang tot de gekozen opleidingseenheden, in de juiste planninggroep.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afnemer | [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md) |
| Afgeleid van | *Verwerken van definitieve keuzes*, applicatiedienst van het studentkeuzesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-verbintenis-en-planninggroep-doorgeven` |

![Verbintenis en planninggroep doorgeven op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/verbintenis-en-planninggroep-doorgeven.png)

## Definitieve keuze melden

Doel: het leermanagementsysteem haalt een definitieve keuze op met de verbintenis en de planninggroep. Trigger: een keuze wordt definitief. Initiator: Studentkeuzesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
