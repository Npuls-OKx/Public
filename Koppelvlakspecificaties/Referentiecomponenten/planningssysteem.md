# Planningssysteem (P)

Endpoints die het planningssysteem zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/onderwijsaanbod/{id}` | GET | — | [education-offering.json](../Datamodelschema's/education-offering.json) | `opleidingsaanbod` ophalen |
| `/onderwijsaanbod` | GET | — | [education-offering.json](../Datamodelschema's/education-offering.json) (lijst) | Reconciliatie: gepubliceerde specificaties of aanbod-instanties opnieuw opvragen na een event in de Dead Letter Channel |
| `/abonnementen` | POST | [subscription.json](../Datamodelschema's/subscription.json) | [subscription.json](../Datamodelschema's/subscription.json) | Abonnement registreren voor de events I1, I3, I4 en I6 |
| `specificatie-planbaar` | POST | [specification-reference.json](../Datamodelschema's/specification-reference.json) | — | Specificatie planbaar melden |
| `specificatie-gewijzigd` | POST | [specification-changed.json](../Datamodelschema's/specification-changed.json) | — | Specificatiewijziging melden |
| `specificatie-status-gewijzigd` | POST | [specification-status-changed.json](../Datamodelschema's/specification-status-changed.json) | — | Specificatiestatus gewijzigd, los van versie |
