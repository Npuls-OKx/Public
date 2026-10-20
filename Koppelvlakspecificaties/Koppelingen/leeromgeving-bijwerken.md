# Leeromgeving bijwerken

Het leermanagementsysteem laat een bestaande inrichting volgen op een nieuwe specificatieversie en meldt de uitkomst terug aan de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | Geen: het leermanagementsysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | `1.0` |
| Vereist | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-leeromgeving-bijwerken` |

![Leeromgeving bijwerken op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/leeromgeving-bijwerken.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0031](../../Referentiemateriaal/requirementsboom/stories.md#story-0031) | [Inrichting bijwerken na wijziging](#inrichting-bijwerken-na-wijziging) |

## Inrichting bijwerken na wijziging

Doel: een bestaande inrichting laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor het leermanagementsysteem. Trigger: de melding [Specificatiewijziging](onderwijsspecificatie-ophalen.md#specificatiewijziging-melden) voor een specificatie waarop het leermanagementsysteem is ingericht. Initiator: Leermanagementsysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)

![Inrichting bijwerken na wijziging: volgorde van de interacties](../src/diagrammen/koppelingen/inrichting-bijwerken-na-wijziging.png)
