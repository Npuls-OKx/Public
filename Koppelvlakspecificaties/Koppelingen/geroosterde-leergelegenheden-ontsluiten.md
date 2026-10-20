# Geroosterde leergelegenheden ontsluiten

Het studentkeuzesysteem kent de geroosterde leergelegenheden met hun details en capaciteit, zodat een student op lesgelegenheid kan kiezen.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Roostersysteem](../Applicatiecomponenten/roostersysteem.md) |
| Afnemer | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md) |
| Afgeleid van | Geen: het roostersysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-geroosterde-leergelegenheden-ontsluiten` |

![Geroosterde leergelegenheden ontsluiten op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/geroosterde-leergelegenheden-ontsluiten.png)

## Geroosterde leergelegenheden melden

Doel: het studentkeuzesysteem haalt het rooster van een periode op zodra het bekend is of wijzigt. Trigger: het rooster voor een periode is bekend of wijzigt. Initiator: Roostersysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | [geroosterd-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-aanbieder.md), [geroosterd-onderwijsaanbod-afnemer](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-afnemer.md) |

Endpoints: nog niet vastgelegd.
