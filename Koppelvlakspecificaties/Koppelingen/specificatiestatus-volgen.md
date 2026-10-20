# Specificatiestatus volgen

Een afnemer werkt zijn afgeleide status bij wanneer een specificatie van status wisselt zonder nieuwe versie, zoals van `gepubliceerd` naar `gedeactiveerd`.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md), [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md) |
| Afgeleid van | *Onderwijsspecificatie uitwerking*, applicatiedienst van de onderwijscatalogus |
| Versie | `1.0` |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-specificatiestatus-volgen` |

![Specificatiestatus volgen op de hoofdplaat, met de aanbieder, de afnemers en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/specificatiestatus-volgen.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0032](../../Referentiemateriaal/requirementsboom/stories.md#story-0032) | [Specificatiestatus gewijzigd melden](#specificatiestatus-gewijzigd-melden) |

## Specificatiestatus gewijzigd melden

Doel: de onderwijscatalogus een statuswijziging laten melden die los staat van een nieuwe versie, zodat de afnemer zijn afgeleide status kan bijwerken zonder op te halen. Trigger: specificatie krijgt een nieuwe status buiten een versiewijziging om (bv. `gepubliceerd` naar `gedeactiveerd`, [regels bij de schema's](../../Informatie-en-gegevensmodellen/regels.md)). Initiator: Onderwijscatalogus. Voorbeeldgeval: een opleiding die voor een ouder cohort bewust niet meer wordt aangeboden is nog wel planbaar, maar wordt niet meer gepland; dat is deze statuswijziging (met archivering als vervolg), geen planningsfout.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event-Carried State Transfer](../Interactiepatronen/event-carried-state-transfer.md) | [onderwijsspecificatiestructuur-afnemer](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md) |

Endpoints:

- [webhook `specificatie-status-gewijzigd`](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md)

![Specificatiestatus gewijzigd melden: volgorde van de interacties](../src/diagrammen/koppelingen/specificatiestatus-gewijzigd-melden.png)
