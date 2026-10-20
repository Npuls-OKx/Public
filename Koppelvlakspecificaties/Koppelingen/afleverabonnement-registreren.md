# Afleverabonnement registreren

Een afnemer legt bij de aanbieder van een koppeling vast op welk adres hij welke meldingen wil ontvangen, voordat die worden afgeleverd.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | Het component dat de meldingen verstuurt |
| Afnemer | Het component dat de meldingen ontvangt |
| Afgeleid van | Geen: elke koppeling met meldingen steunt erop |
| Versie | `1.0` |
| Vereist | — |
| OEAPI-profiel | `okx-afleverabonnement-registreren` |

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0010](../../Referentiemateriaal/requirementsboom/stories.md#story-0010) | [Abonnement registreren](#abonnement-registreren) |

## Abonnement registreren

Doel: een afnemer een callback-URL laten vastleggen voor de meldingen die hij van de aanbieder ontvangt, als voorwaarde voor de event-gedreven stromen. Trigger: inrichting van een koppeling, of wijziging van de callback-URL. Initiator: de afnemer.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Subscription registration](../Interactiepatronen/subscription-registration.md) | [afleverabonnement-aanbieder](../Koppelvlakdiensten/afleverabonnement-aanbieder.md), [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md) |

Endpoints:

- [`POST /abonnementen`](../Koppelvlakdiensten/afleverabonnement-aanbieder.md)

![Abonnement registreren: volgorde van de interacties](../src/diagrammen/koppelingen/abonnement-registreren.png)
