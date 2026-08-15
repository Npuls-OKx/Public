# Onderwijscatalogus (OC)

De onderwijscatalogus is het distributiepunt voor onderwijsspecificaties: zij neemt ze aan van de curriculum-ontwerptool, legt ze vast en publiceert ze naar de systemen die het onderwijs klaarzetten voor de start van de student. Zij bezit de onderwijsspecificaties ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)), en is daarmee in elk van de drie koppelingen hieronder de partij die een wijziging meldt en de resource levert ([U4](../uitgangspunten.md#u4-notify-then-pull)).

Endpoints die OC zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/onderwijsspecificaties/{id}` | GET | — | [education-specification.json](../Datamodelschema's/education-specification.json) | Onderwijsspecificatiestructuur of delta ophalen |
| `/onderwijsspecificaties/{id}/delta` | GET | — | [education-specification-delta.json](../Datamodelschema's/education-specification-delta.json) | Onderwijsspecificatiestructuur of delta ophalen |
| `/onderwijsspecificaties` | GET | — | [specification-reference.json](../Datamodelschema's/specification-reference.json) (lijst) | Reconciliatie: gepubliceerde specificaties of aanbod-instanties opnieuw opvragen na een event in de Dead Letter Channel |
| `/examenplanspecificaties/{id}` | GET | — | [result-structure.json](../Datamodelschema's/result-structure.json) | Resultaatstructuur ophalen |
| `/abonnementen` | POST | [subscription.json](../Datamodelschema's/subscription.json) | [subscription.json](../Datamodelschema's/subscription.json) | Abonnement registreren voor de events I1, I3, I4 en I6 |
| `verwerkingsstatus` | POST | [processing-status.json](../Datamodelschema's/processing-status.json) | — | Verwerkingsstatus melden, met referentie naar het `opleidingsaanbod` |
| `inrichtingsstatus` | POST | Status en referentie naar de inrichting (uuid), specificatie-id en versie (payloadschema nog niet uitgewerkt) | — | Inrichtingsstatus melden, met referentie naar de inrichting |
| `leermiddelkoppeling-beschikbaar` | POST | Referentie (uuid) naar de leermiddelkoppeling, specificatie-id en versie (payloadschema nog niet uitgewerkt) | — | Leermiddelkoppeling beschikbaar melden |
