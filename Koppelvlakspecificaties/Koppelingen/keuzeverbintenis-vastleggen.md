# Keuzeverbintenis vastleggen

Het kernregistratiesysteem legt de opleidingsprogrammaverbintenis vast die uit een definitieve keuze volgt, van het type keuzedeel of credential.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afnemer | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (KRS) |
| Afgeleid van | *Verwerken van definitieve keuzes*, applicatiedienst van het studentkeuzesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-keuzeverbintenis-vastleggen` |

![Keuzeverbintenis vastleggen op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/keuzeverbintenis-vastleggen.png)

## Definitieve keuze melden

Doel: het kernregistratiesysteem haalt een definitieve keuze op en legt de verbintenis vast. Trigger: een keuze wordt definitief. Initiator: Studentkeuzesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
