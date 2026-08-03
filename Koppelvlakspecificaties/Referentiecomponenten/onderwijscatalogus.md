# Onderwijscatalogus (OC)

Endpoints die OC zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/onderwijsspecificaties/{id}` | GET | — | [onderwijsspecificatie.json](../Datamodelschema's/onderwijsspecificatie.json) | Onderwijsspecificatiestructuur of delta ophalen |
| `/onderwijsspecificaties/{id}/delta` | GET | — | [onderwijsspecificatie-delta.json](../Datamodelschema's/onderwijsspecificatie-delta.json) | Onderwijsspecificatiestructuur of delta ophalen |
| `/onderwijsspecificaties` | GET | — | [specificatie-referentie.json](../Datamodelschema's/specificatie-referentie.json) (lijst) | Reconciliatie: gepubliceerde specificaties of aanbod-instanties opnieuw opvragen na een event in de Dead Letter Channel |
| `/abonnementen` | POST | [abonnement.json](../Datamodelschema's/abonnement.json) | [abonnement.json](../Datamodelschema's/abonnement.json) | Abonnement registreren voor de events I1, I3, I4 en I6 |
| `verwerkingsstatus` | POST | [verwerkingsstatus.json](../Datamodelschema's/verwerkingsstatus.json) | — | Verwerkingsstatus melden, met referentie naar het `opleidingsaanbod` |
