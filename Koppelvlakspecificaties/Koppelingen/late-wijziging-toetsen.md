# Late wijziging toetsen

Een specificatiewijziging na een afgeronde planning komt alleen in de planning terecht als het planningssysteem haar accepteert; de uitkomst gaat terug naar de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Planningssysteem](../Applicatiecomponenten/planningssysteem.md) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | *(Meer)jaar capaciteitsplanning*, applicatiedienst van het planningssysteem |
| Versie | `1.0` |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-late-wijziging-toetsen` |

![Late wijziging toetsen op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/late-wijziging-toetsen.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0002](../../Referentiemateriaal/requirementsboom/stories.md#story-0002) | [Acceptatietoets bij late wijziging](#acceptatietoets-bij-late-wijziging) |

## Acceptatietoets bij late wijziging

Doel: een afgeronde planning beschermen tegen een wijziging die er ongecontroleerd doorheen breekt. Trigger: de melding [Specificatiewijziging](onderwijsspecificatie-ophalen.md#specificatiewijziging-melden) terwijl de planning al is afgerond. Initiator: Planningssysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)

![Acceptatietoets bij late wijziging: volgorde van de interacties](../src/diagrammen/koppelingen/acceptatietoets-bij-late-wijziging.png)
