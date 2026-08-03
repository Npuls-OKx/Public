# Planningssysteem (P)

Endpoints die het planningssysteem zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/onderwijsaanbod/{id}` | GET | — | [onderwijsaanbod.json](../Datamodelschema's/onderwijsaanbod.json) | `opleidingsaanbod` ophalen |
| `/onderwijsaanbod` | GET | — | [onderwijsaanbod.json](../Datamodelschema's/onderwijsaanbod.json) (lijst) | Reconciliatie: gepubliceerde specificaties of aanbod-instanties opnieuw opvragen na een event in de Dead Letter Channel |
| `/abonnementen` | POST | [abonnement.json](../Datamodelschema's/abonnement.json) | [abonnement.json](../Datamodelschema's/abonnement.json) | Abonnement registreren voor de events I1, I3, I4 en I6 |
| `specificatie-planbaar` | POST | [specificatie-referentie.json](../Datamodelschema's/specificatie-referentie.json) | — | Specificatie planbaar melden |
| `specificatie-gewijzigd` | POST | [specificatie-gewijzigd.json](../Datamodelschema's/specificatie-gewijzigd.json) | — | Specificatiewijziging melden |
| `specificatie-status-gewijzigd` | POST | [specificatie-status-gewijzigd.json](../Datamodelschema's/specificatie-status-gewijzigd.json) | — | Specificatiestatus gewijzigd, los van versie |
