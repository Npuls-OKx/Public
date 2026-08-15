# Planningssysteem (P)

Het planningssysteem maakt van een gepubliceerde onderwijsspecificatie planbaar `opleidingsaanbod`: het bepaalt wanneer, hoe vaak en in welke vorm het onderwijs wordt aangeboden, en meldt de referentie naar dat aanbod terug aan de catalogus. Het bezit het onderwijsaanbod ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)). Het rooster zelf ligt bij het roostersysteem; dat kent in dit pakket geen eigen koppeling en komt alleen als context voor ([P&R §5.5](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#55-context-doorwerking-naar-het-roostersysteem)).

Endpoints die het planningssysteem zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/onderwijsaanbod/{id}` | GET | — | [education-offering.json](../Datamodelschema's/education-offering.json) | `opleidingsaanbod` ophalen |
| `/onderwijsaanbod` | GET | — | [education-offering.json](../Datamodelschema's/education-offering.json) (lijst) | Reconciliatie: gepubliceerde specificaties of aanbod-instanties opnieuw opvragen na een event in de Dead Letter Channel |
| `/abonnementen` | POST | [subscription.json](../Datamodelschema's/subscription.json) | [subscription.json](../Datamodelschema's/subscription.json) | Abonnement registreren voor de events I1, I3, I4 en I6 |
| `specificatie-planbaar` | POST | [specification-reference.json](../Datamodelschema's/specification-reference.json) | — | Specificatie planbaar melden |
| `specificatie-gewijzigd` | POST | [specification-changed.json](../Datamodelschema's/specification-changed.json) | — | Specificatiewijziging melden |
| `specificatie-status-gewijzigd` | POST | [specification-status-changed.json](../Datamodelschema's/specification-status-changed.json) | — | Specificatiestatus gewijzigd, los van versie |
