# Specificatie aanpassen op verzoek

Het planningssysteem vraagt een aanpassing aan van een specificatie die niet planbaar blijkt, en krijgt de uitkomst van dat verzoek terug.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afgeleid van | *Onderwijsspecificatie uitwerking*, applicatiedienst van de onderwijscatalogus |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-specificatie-aanpassen-op-verzoek` |

![Specificatie aanpassen op verzoek op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/specificatie-aanpassen-op-verzoek.png)

## Aanpassing aanvragen

Doel: een specificatie die niet planbaar blijkt, laten aanpassen in plaats van de planning te forceren. Trigger: het planningssysteem kan een specificatie niet plannen zoals zij is gespecificeerd. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
