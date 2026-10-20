# Inschrijfbaar aanbod ontsluiten

Het kernregistratiesysteem en de externe aanmeldkanalen kennen het opleidingsprogramma-aanbod waarvoor een student zich kan aanmelden en inschrijven.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (KRS), EduHub, Voorziening Centraal Aanmelden (CAMBO) |
| Afgeleid van | *Onderwijsspecificatie uitwerking*, applicatiedienst van de onderwijscatalogus |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-inschrijfbaar-aanbod-ontsluiten` |

![Inschrijfbaar aanbod ontsluiten op de hoofdplaat, met de aanbieder, de afnemers en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/inschrijfbaar-aanbod-ontsluiten.png)

## Inschrijfbaar aanbod melden

Doel: afnemers horen dat er opleidingsprogramma-aanbod is waarvoor aanmelding openstaat, en halen het op. Trigger: opleidingsprogramma-aanbod wordt voor aanmelding opengesteld. Initiator: Onderwijscatalogus.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Nog niet belegd |

Endpoints: nog niet vastgelegd.
