# Planningssysteem (P)

Het planningssysteem maakt van een gepubliceerde onderwijsspecificatie planbaar `opleidingsaanbod`: het bepaalt wanneer, hoe vaak en in welke vorm het onderwijs wordt aangeboden, en meldt de referentie naar dat aanbod terug aan de catalogus. Het bezit het onderwijsaanbod ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)). Het rooster zelf ligt bij het roostersysteem; dat kent in dit pakket geen eigen koppeling en komt alleen als context voor ([roostersysteem](roostersysteem.md)).

## Koppelvlak

![Gedeeld koppelvlak van planning en roostering op de hoofdplaat v1.7](../src/koppelvlak_p_en_r_view_ihp_v1_7.png)

De view toont het gedeelde koppelvlak van planning en roostering op de informatiestromen-hoofdplaat v1.7. Beide componenten delen dit koppelvlak; het rooster zelf blijft bij het roostersysteem.

## Endpoints

Endpoints die het planningssysteem zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Parameters | Request | Response | Statuscodes | Interacties |
|---|---|---|---|---|---|---|
| `/onderwijsaanbod/{id}` | GET | `status` (optioneel filter op onderliggende instanties) | — | [education-offering.json](../Datamodelschema's/education-offering.json): de gevraagde instantie plus haar subtree via `bovenliggendAanbodId` | 200, 400, 404 | I5 |
| `/onderwijsaanbod` | GET | `specificatieId` (verplicht), `versie` (optioneel, standaard alle versies) | — | [education-offering.json](../Datamodelschema's/education-offering.json) (lijst): de instanties die deze specificatie instantiëren | 200, 400 | I7 |
| `/abonnementen` | POST | — | [subscription.json](../Datamodelschema's/subscription.json): `callbackUrl` en de events | Abonnement-id | 201, 400 | I8 |
| `specificatie-planbaar` | POST | — | [specification-reference.json](../Datamodelschema's/specification-reference.json) | — | 200 | I1 |
| `specificatie-gewijzigd` | POST | — | [specification-changed.json](../Datamodelschema's/specification-changed.json) | — | 200 | I4 |
| `specificatie-status-gewijzigd` | POST | — | [specification-status-changed.json](../Datamodelschema's/specification-status-changed.json) | — | 200 | I6 |
