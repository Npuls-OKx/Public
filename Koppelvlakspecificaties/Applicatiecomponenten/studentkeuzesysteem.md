# Studentkeuzesysteem (SKS)

Het studentkeuzesysteem is de component waar de student zijn keuzes maakt. Het is bewust als **zelfstandige** referentiecomponent belegd en niet verspreid over portaal, catalogus of leeromgeving, zodat de keuze-interactie expliciet wordt in plaats van verborgen ([ADR 0005](../../Referentiemateriaal/adr/0005-student-keuze-systeem-zelfstandige-referentiecomponent.md)). Het draagt de keuze-interacties van de student; het studentvolgsysteem blijft bij resultaat en voortgang, en de inschrijving blijft bij het kernregistratiesysteem ([ADR 0009](../../Referentiemateriaal/adr/0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md), [ADR 0014](../../Referentiemateriaal/adr/0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md)).

## Koppelvlak

![Koppelvlak van het studentkeuzesysteem op de hoofdplaat v1.7](../src/koppelvlak_sks_view_ihp_v1_7.png)

De view toont het koppelvlak van het studentkeuzesysteem: de optelsom van zijn koppelingen op de informatiestromen-hoofdplaat v1.7.

## Koppelvlakdiensten

Dit component implementeert de volgende [koppelvlakdiensten](../Koppelvlakdiensten/README.md):

- [afleverabonnement-aanbieder](../Koppelvlakdiensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md)
- [geroosterd-onderwijsaanbod-afnemer](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-afnemer.md)
- [keuzeregelset-afnemer](../Koppelvlakdiensten/keuzeregelset-afnemer.md)
- [onderwijsspecificatiestructuur-afnemer](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md)
- [planbaar-onderwijsaanbod-afnemer](../Koppelvlakdiensten/planbaar-onderwijsaanbod-afnemer.md)
- [verbintenistoestand-afnemer](../Koppelvlakdiensten/verbintenistoestand-afnemer.md)

## Koppelingen

| Koppeling | Rol |
|---|---|
| [Onderwijsspecificatie ophalen](../Koppelingen/onderwijsspecificatie-ophalen.md) | Afnemer |
| [Keuzeaanbod ontsluiten](../Koppelingen/keuzeaanbod-ontsluiten.md) | Afnemer |
| [Geplande leergelegenheden ontsluiten](../Koppelingen/geplande-leergelegenheden-ontsluiten.md) | Afnemer |
| [Opleidingsprogrammaverbintenis ontsluiten](../Koppelingen/opleidingsprogrammaverbintenis-ontsluiten.md) | Afnemer |
| [Animo doorgeven](../Koppelingen/animo-doorgeven.md) | Aanbieder |
| [Plaatsing op lesgelegenheid aanvragen](../Koppelingen/plaatsing-op-lesgelegenheid-aanvragen.md) | Afnemer |
| [Keuzeverbintenis vastleggen](../Koppelingen/keuzeverbintenis-vastleggen.md) | Aanbieder |
| [Onderwijseenheidverbintenis doorgeven](../Koppelingen/onderwijseenheidverbintenis-doorgeven.md) | Aanbieder |
| [Verbintenis en planninggroep doorgeven](../Koppelingen/verbintenis-en-planninggroep-doorgeven.md) | Aanbieder |
| [Geroosterde leergelegenheden ontsluiten](../Koppelingen/geroosterde-leergelegenheden-ontsluiten.md) | Afnemer |
