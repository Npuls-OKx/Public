# Reconciliatie

Een afnemer herstelt informatie die hem door een gemiste of onverwerkbare melding is ontgaan, met een gewone opvraag bij de aanbieder van die melding.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | Het component dat de gemiste melding verstuurde |
| Afnemer | Het component dat de melding miste |
| Afgeleid van | Geen: elke koppeling met meldingen steunt erop |
| Versie | `1.0` |
| Vereist | — |
| OEAPI-profiel | `okx-reconciliatie` |

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0011](../../Referentiemateriaal/requirementsboom/stories.md#story-0011) | [Reconciliatie na gemist event](#reconciliatie-na-gemist-event) |

## Reconciliatie na gemist event

Doel: de gemiste informatie via een gewone opvraag herstellen na een event dat in de Dead Letter Channel is beland, zonder op een herhaalde aflevering te wachten. Trigger: een event is niet aangekomen. Initiator: de afnemer.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Request-Reply](../Interactiepatronen/request-reply.md) | [onderwijsspecificatiestructuur-aanbieder](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md), [planbaar-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md) |

Endpoints:

- [`GET /onderwijsspecificaties` (op de onderwijscatalogus)](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md)
- [`GET /onderwijsaanbod` (op het planningssysteem)](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md)

De opvraag hoort bij de koppelvlakdienst van de resource waarover de melding ging. Voor de onderwijscatalogus en het planningssysteem ligt zij vast; voor de andere aanbieders nog niet.

![Reconciliatie na gemist event: volgorde van de interacties](../src/diagrammen/koppelingen/reconciliatie-na-gemist-event.png)
