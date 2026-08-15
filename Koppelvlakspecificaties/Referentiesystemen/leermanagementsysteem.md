# Leermanagementsysteem (LMS)

Het leermanagementsysteem is de online leeromgeving waarin de student het onderwijs volgt. Het neemt de onderwijsspecificatiestructuur van de catalogus over, inclusief de inhoudsvelden van de leeruitkomsten die het aan de student toont, en richt daarmee de leeromgeving in. Het bezit de leermiddelkoppeling, de koppeling tussen leermiddelgroepen en specificatie ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)), en meldt die terug aan de catalogus. Kiesbaarheid is niet zijn domein: regelsets gaan over deze koppeling niet mee.

Endpoints die LMS zelf implementeert. Authenticatie op elk endpoint: [auth-standaard](../auth-standaard.md).

| Endpoint/event | Methode | Request | Response | Interacties |
|---|---|---|---|---|
| `/leermiddelkoppelingen/{id}` | GET | — | Leermiddelkoppeling-instantie: leermiddelgroepen per specificatie (payload nog uit te werken) | Leermiddelkoppeling ophalen |
| `specificatie-beschikbaar` | POST | [specification-reference.json](../Datamodelschema's/specification-reference.json) | — | Specificatie beschikbaar melden |
| `specificatie-gewijzigd` | POST | [specification-changed.json](../Datamodelschema's/specification-changed.json) | — | Specificatiewijziging melden, met wijzigingsklasse |
