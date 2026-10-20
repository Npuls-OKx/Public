# Toetsresultaat doorgeven

Het studentvolgsysteem ontvangt het resultaat dat een student op een toetsgelegenheid behaalde, zodat het voortgang en behaalde leeruitkomsten kan bijhouden.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md) |
| Afnemer | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (SVS) |
| Afgeleid van | Geen: het leermanagementsysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-toetsresultaat-doorgeven` |

![Toetsresultaat doorgeven op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/toetsresultaat-doorgeven.png)

## Toetsresultaat melden

Doel: het studentvolgsysteem haalt een vastgesteld resultaat op een toetsgelegenheidverbintenis op. Trigger: een resultaat op een toetsgelegenheidverbintenis wordt vastgesteld. Initiator: Leermanagementsysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
