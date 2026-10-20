# Resultaatstructuur ophalen

Het studentinformatiesysteem haalt de resultaatstructuur van een gepubliceerde examenplanspecificatie op, en volgt een wijziging daarvan, nadat de onderwijscatalogus die heeft gemeld.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (SVS) |
| Afgeleid van | *Onderwijsspecificatie uitwerking*, applicatiedienst van de onderwijscatalogus |
| Versie | `1.0` |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-resultaatstructuur-ophalen` |

![Resultaatstructuur ophalen op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/resultaatstructuur-ophalen.png)

## Resultaatstructuur beschikbaar melden

Doel: het studentinformatiesysteem haalt de resultaatstructuur op zodra de examenplanspecificatie is gepubliceerd. Trigger: examenplanspecificatie krijgt status `gepubliceerd`. Initiator: Onderwijscatalogus.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | [resultaatstructuur-aanbieder](../Koppelvlakdiensten/resultaatstructuur-aanbieder.md), [resultaatstructuur-afnemer](../Koppelvlakdiensten/resultaatstructuur-afnemer.md) |

Endpoints:

- [webhook `resultaatstructuur-beschikbaar`](../Koppelvlakdiensten/resultaatstructuur-afnemer.md)
- [`GET /examenplanspecificaties/{id}`](../Koppelvlakdiensten/resultaatstructuur-aanbieder.md)

![Resultaatstructuur beschikbaar melden: volgorde van de interacties](../src/diagrammen/koppelingen/resultaatstructuur-beschikbaar-melden.png)

## Examenplanwijziging melden

Doel: het studentinformatiesysteem hoort van een wijziging in een examenplanspecificatie waarop het al heeft ingericht. Trigger: examenplanspecificatie wijzigt. Initiator: Onderwijscatalogus.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | [resultaatstructuur-afnemer](../Koppelvlakdiensten/resultaatstructuur-afnemer.md) |

Endpoints:

- [webhook `examenplanspecificatie-gewijzigd`](../Koppelvlakdiensten/resultaatstructuur-afnemer.md)

![Examenplanwijziging melden: volgorde van de interacties](../src/diagrammen/koppelingen/examenplanwijziging-melden.png)
