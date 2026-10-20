# Keuzeaanbod ontsluiten

Het studentkeuzesysteem kent het onderwijsprogramma-aanbod waaruit een student kan kiezen, met de regelsets die de keuzeruimte begrenzen.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afgeleid van | *Onderwijsspecificatie uitwerking*, applicatiedienst van de onderwijscatalogus |
| Versie | — |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-keuzeaanbod-ontsluiten` |

![Keuzeaanbod ontsluiten op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/keuzeaanbod-ontsluiten.png)

## Keuzeregelset melden

Doel: het studentkeuzesysteem haalt de regelset op die de keuzeruimte binnen een specificatie begrenst. Trigger: een regelset wordt vastgesteld of gewijzigd. Initiator: Onderwijscatalogus.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | [keuzeregelset-aanbieder](../Koppelvlakdiensten/keuzeregelset-aanbieder.md), [keuzeregelset-afnemer](../Koppelvlakdiensten/keuzeregelset-afnemer.md) |

Endpoints: nog niet vastgelegd.
