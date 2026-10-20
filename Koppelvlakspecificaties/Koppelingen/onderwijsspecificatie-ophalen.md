# Onderwijsspecificatie ophalen

Een afnemer haalt de vastgestelde structuur van een gepubliceerde onderwijsspecificatie op, volledig of als delta, nadat de onderwijscatalogus heeft gemeld dat zij beschikbaar of gewijzigd is.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md), [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (SVS), [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md), [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afgeleid van | *Onderwijsspecificatie uitwerking*, applicatiedienst van de onderwijscatalogus |
| Versie | `1.0` |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-onderwijsspecificatie-ophalen` |

![Onderwijsspecificatie ophalen op de hoofdplaat, met de aanbieder, de afnemers en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/onderwijsspecificatie-ophalen.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0006](../../Referentiemateriaal/requirementsboom/stories.md#story-0006) | [Specificatie beschikbaar melden](#specificatie-beschikbaar-melden) |
| [story-0030](../../Referentiemateriaal/requirementsboom/stories.md#story-0030) | [Specificatiewijziging melden](#specificatiewijziging-melden) |

## Specificatie beschikbaar melden

Doel: een afnemer haalt een gepubliceerde specificatie op zodra die beschikbaar is. Trigger: onderwijsspecificatie krijgt status `gepubliceerd`. Initiator: Onderwijscatalogus.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | [onderwijsspecificatiestructuur-aanbieder](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md), [onderwijsspecificatiestructuur-afnemer](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md) |

Endpoints:

- [webhook `specificatie-beschikbaar`](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md)
- [`GET /onderwijsspecificaties/{id}`](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md)

![Specificatie beschikbaar melden: volgorde van de interacties](../src/diagrammen/koppelingen/specificatie-beschikbaar-melden.png)

## Specificatiewijziging melden

Doel: een afnemer volgt een nieuwe versie van een specificatie die hij al gebruikt, met de delta of de volledige structuur als zijn keuze. Trigger: nieuwe versie van een gepubliceerde specificatie. Initiator: Onderwijscatalogus.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | [onderwijsspecificatiestructuur-aanbieder](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md), [onderwijsspecificatiestructuur-afnemer](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md) |

Endpoints:

- [webhook `specificatie-gewijzigd`](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md)
- [`GET /onderwijsspecificaties/{id}/delta` of `GET /onderwijsspecificaties/{id}`](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md)

![Specificatiewijziging melden: volgorde van de interacties](../src/diagrammen/koppelingen/specificatiewijziging-melden.png)
