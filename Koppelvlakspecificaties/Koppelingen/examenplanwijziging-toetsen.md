# Examenplanwijziging toetsen

Een examenplanwijziging raakt lopende verbintenissen alleen als het studentinformatiesysteem haar accepteert; de uitkomst gaat terug naar de onderwijscatalogus.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (SVS) |
| Afnemer | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afgeleid van | Geen: het studentvolgsysteem heeft op de hoofdplaat nog geen applicatiedienst |
| Versie | `1.0` |
| Vereist | [Resultaatstructuur ophalen](resultaatstructuur-ophalen.md), [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-examenplanwijziging-toetsen` |

![Examenplanwijziging toetsen op de hoofdplaat, met de aanbieder en de afnemer](../src/diagrammen/hoofdplaat/examenplanwijziging-toetsen.png)

## Stories

| Story | Ingevuld door |
|---|---|
| [story-0020](../../Referentiemateriaal/requirementsboom/stories.md#story-0020) | [Acceptatietoets bij wijziging examenplan](#acceptatietoets-bij-wijziging-examenplan) |

## Acceptatietoets bij wijziging examenplan

Doel: lopende verbintenissen beschermen tegen een examenplanwijziging die er ongecontroleerd doorheen breekt. Trigger: de melding [Examenplanwijziging](resultaatstructuur-ophalen.md#examenplanwijziging-melden) terwijl er al verbintenissen lopen. Initiator: Studentinformatiesysteem.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md), [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md) |

Endpoints:

- [webhook `verwerkingsuitkomst`](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)

![Acceptatietoets bij wijziging examenplan: volgorde van de interacties](../src/diagrammen/koppelingen/acceptatietoets-bij-wijziging-examenplan.png)
