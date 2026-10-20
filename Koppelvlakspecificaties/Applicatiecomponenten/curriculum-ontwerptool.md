# Curriculum-ontwerptool (CO)

De curriculum-ontwerptool is waar onderwijsspecificaties ontstaan: ontwerpers werken er het curriculum uit en leveren het resultaat aan de onderwijscatalogus, die het vanaf daar distribueert. Zij staat daarmee aan het begin van de keten die dit pakket beschrijft.

Hoe de curriculum-ontwerptool en de catalogus zich tot elkaar verhouden is wel als besluit vastgelegd: de catalogus synchroniseert de aangeleverde specificatie en kan die federatief overnemen ([ADR 0020](../../Referentiemateriaal/adr/0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md)).

## Koppelvlakdiensten

Dit component implementeert de volgende [koppelvlakdiensten](../Koppelvlakdiensten/README.md):

- [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md)
- [onderwijsspecificatie-inname-afnemer](../Koppelvlakdiensten/onderwijsspecificatie-inname-afnemer.md)

## Koppelingen

| Koppeling | Rol |
|---|---|
| [Specificatie ter vaststelling aanbieden](../Koppelingen/specificatie-ter-vaststelling-aanbieden.md) | Afnemer |
