# Opleidingsprogrammaverbintenis ontsluiten

Het studentkeuzesysteem en het leermanagementsysteem kennen de student, zijn opleidingsprogrammaverbintenis en de groepen die daarbij horen.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md) (KRS) |
| Afnemer | [Studentkeuzesysteem](../Applicatiecomponenten/studentkeuzesysteem.md), [Leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md) |
| Afgeleid van | *Inschrijving op opleidingsprogramma*, applicatiedienst van het kernregistratiesysteem |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-opleidingsprogrammaverbintenis-ontsluiten` |

![Opleidingsprogrammaverbintenis ontsluiten op de hoofdplaat, met de aanbieder, de afnemers en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/opleidingsprogrammaverbintenis-ontsluiten.png)

## Verbintenistoestand melden

Doel: afnemers werken hun beeld van de verbintenis bij zonder op te halen. Trigger: een opleidingsprogrammaverbintenis ontstaat of wisselt van toestand. Initiator: Studentinformatiesysteem (KRS).

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Event-Carried State Transfer](../Interactiepatronen/event-carried-state-transfer.md) | [verbintenistoestand-aanbieder](../Koppelvlakdiensten/verbintenistoestand-aanbieder.md), [verbintenistoestand-afnemer](../Koppelvlakdiensten/verbintenistoestand-afnemer.md) |

Endpoints: nog niet vastgelegd.
