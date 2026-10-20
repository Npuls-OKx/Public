# Specificatie ter vaststelling aanbieden

Een in de curriculum-ontwerptool uitgewerkte meerjarige nominale route wordt in de onderwijscatalogus vastgesteld als onderwijsspecificatie, en de curriculum-ontwerptool krijgt de bevestiging of de afkeuring terug.

| Kenmerk | Waarde |
|---|---|
| Aanbieder | [Onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) |
| Afnemer | [Curriculum-ontwerptool](../Applicatiecomponenten/curriculum-ontwerptool.md) |
| Afgeleid van | *Nominale route meerjaar uitwerking*, applicatiedienst van de curriculum-ontwerptool |
| Versie | — |
| Vereist | [Afleverabonnement registreren](afleverabonnement-registreren.md), [Reconciliatie](reconciliatie.md) |
| OEAPI-profiel | `okx-specificatie-ter-vaststelling-aanbieden` |

![Specificatie ter vaststelling aanbieden op de hoofdplaat, met de aanbieder, de afnemer en de applicatiedienst waarvan zij is afgeleid](../src/diagrammen/hoofdplaat/specificatie-ter-vaststelling-aanbieden.png)

## Specificatie aanleveren

Doel: een ontwerp vastleggen als onderwijsspecificatie met een eigen identiteit en versie. Trigger: een ontwerp is gereed voor vaststelling. Initiator: Curriculum-ontwerptool.

| Interactiepatronen | Koppelvlakdiensten |
|---|---|
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [onderwijsspecificatie-inname-aanbieder](../Koppelvlakdiensten/onderwijsspecificatie-inname-aanbieder.md), [onderwijsspecificatie-inname-afnemer](../Koppelvlakdiensten/onderwijsspecificatie-inname-afnemer.md) |

Endpoints: nog niet vastgelegd.
