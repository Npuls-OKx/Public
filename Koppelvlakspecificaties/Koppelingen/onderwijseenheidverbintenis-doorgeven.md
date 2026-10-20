# Onderwijseenheidverbintenis doorgeven

Het studentvolgsysteem kent de opleidingsprogramma- en onderwijseenheidverbintenissen waarop het voortgang en resultaat bijhoudt.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afnemer | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (SVS) |
| Afgeleid van | *Verwerken van definitieve keuzes*, applicatiedienst van het studentkeuzesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-onderwijseenheidverbintenis-doorgeven` |

![Onderwijseenheidverbintenis doorgeven op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/onderwijseenheidverbintenis-doorgeven.png)

## Definitieve keuze melden

Doel: het studentvolgsysteem haalt een definitieve keuze op en neemt de verbintenissen op in de individuele structuur. Trigger: een keuze wordt definitief. Initiator: Studentkeuzesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
