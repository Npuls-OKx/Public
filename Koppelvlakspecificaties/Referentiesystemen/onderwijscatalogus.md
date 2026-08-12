# Onderwijscatalogus (OC)

Endpoints die OC zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/onderwijsspecificaties/{id}` | GET | — | [education-specification.json](../Datamodelschema's/education-specification.json) | Onderwijsspecificatiestructuur of delta ophalen |
| `/onderwijsspecificaties/{id}/delta` | GET | — | [education-specification-delta.json](../Datamodelschema's/education-specification-delta.json) | Onderwijsspecificatiestructuur of delta ophalen |
| `/onderwijsspecificaties` | GET | — | [specification-reference.json](../Datamodelschema's/specification-reference.json) (lijst) | Reconciliatie: gepubliceerde specificaties of aanbod-instanties opnieuw opvragen na een event in de Dead Letter Channel |
| `/abonnementen` | POST | [subscription.json](../Datamodelschema's/subscription.json) | [subscription.json](../Datamodelschema's/subscription.json) | Abonnement registreren voor de events I1, I3, I4 en I6 |
| `verwerkingsstatus` | POST | [processing-status.json](../Datamodelschema's/processing-status.json) | — | Verwerkingsstatus melden, met referentie naar het `opleidingsaanbod` |
