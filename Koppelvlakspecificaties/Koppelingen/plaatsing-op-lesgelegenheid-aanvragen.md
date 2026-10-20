# Plaatsing op lesgelegenheid aanvragen

Een student wordt op een geroosterde lesgelegenheid geplaatst; het studentkeuzesysteem krijgt de verbintenis met de planninggroep terug.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Roostersysteem](../Applicatiecomponenten/roostersysteem.md) |
| Afnemer | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afgeleid van | *Verwerken van definitieve keuzes*, applicatiedienst van het studentkeuzesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-plaatsing-op-lesgelegenheid-aanvragen` |

![Plaatsing op lesgelegenheid aanvragen op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/plaatsing-op-lesgelegenheid-aanvragen.png)

## Plaatsing aanvragen

Doel: de keuze van een student voor een lesgelegenheid omzetten in een plaatsing in een planninggroep. Trigger: een student kiest definitief een lesgelegenheid. Initiator: Studentkeuzesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
