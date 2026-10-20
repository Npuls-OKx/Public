# Onderwijscatalogus (OC)

De onderwijscatalogus is het distributiepunt voor onderwijsspecificaties: zij neemt ze aan van de curriculum-ontwerptool, legt ze vast en publiceert ze naar de systemen die het onderwijs klaarzetten voor de start van de student. Zij bezit de onderwijsspecificaties ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)), en is daarmee de aanbieder van de koppelingen die specificaties ontsluiten: zij meldt een wijziging en levert de resource ([U4](../uitgangspunten.md#u4-event-notification)).

## Koppelvlak

![Koppelvlak van de onderwijscatalogus op de hoofdplaat v1.7](../src/koppelvlak_oc_view_ihp_v1_7.png)

De view toont het koppelvlak van de onderwijscatalogus: de optelsom van haar koppelingen op de informatiestromen-hoofdplaat v1.7.

![Koppelvlakdiensten en endpoints van het koppelvlak](../src/diagrammen/referentie/koppelvlak-van-de-onderwijscatalogus.png)

Dezelfde optelsom van binnen: elke koppelvlakdienst die de catalogus implementeert, met daaronder de endpoints waarmee zij die levert. Een dienst die zelf niets aanbiedt draagt in plaats daarvan een blok dat benoemt wat hij dan doet. De plaat wordt gegenereerd uit [`model/componenten.c4`](../model/componenten.c4); die bron gaat met de release mee, zodat de inhoud machinaal te lezen is en niet alleen als plaat.

## Koppelvlakdiensten

Dit component implementeert de volgende [koppelvlakdiensten](../Koppelvlakdiensten/README.md):

- [afleverabonnement-aanbieder](../Koppelvlakdiensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md)
- [keuzeregelset-aanbieder](../Koppelvlakdiensten/keuzeregelset-aanbieder.md)
- [leermiddelkoppeling-afnemer](../Koppelvlakdiensten/leermiddelkoppeling-afnemer.md)
- [onderwijsspecificatie-inname-aanbieder](../Koppelvlakdiensten/onderwijsspecificatie-inname-aanbieder.md)
- [onderwijsspecificatiestructuur-aanbieder](../Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md)
- [planbaar-onderwijsaanbod-afnemer](../Koppelvlakdiensten/planbaar-onderwijsaanbod-afnemer.md)
- [resultaatstructuur-aanbieder](../Koppelvlakdiensten/resultaatstructuur-aanbieder.md)
- [verwerkingsuitkomst-afnemer](../Koppelvlakdiensten/verwerkingsuitkomst-afnemer.md)

## Koppelingen

| Koppeling | Rol |
|---|---|
| [Onderwijsspecificatie ophalen](../Koppelingen/onderwijsspecificatie-ophalen.md) | Aanbieder |
| [Specificatiestatus volgen](../Koppelingen/specificatiestatus-volgen.md) | Aanbieder |
| [Resultaatstructuur ophalen](../Koppelingen/resultaatstructuur-ophalen.md) | Aanbieder |
| [Specificatie aanpassen op verzoek](../Koppelingen/specificatie-aanpassen-op-verzoek.md) | Aanbieder |
| [Keuzeaanbod ontsluiten](../Koppelingen/keuzeaanbod-ontsluiten.md) | Aanbieder |
| [Inschrijfbaar aanbod ontsluiten](../Koppelingen/inschrijfbaar-aanbod-ontsluiten.md) | Aanbieder |
| [Specificatie ter vaststelling aanbieden](../Koppelingen/specificatie-ter-vaststelling-aanbieden.md) | Aanbieder |
| [Opleidingsaanbod aanmaken](../Koppelingen/opleidingsaanbod-aanmaken.md) | Afnemer |
| [Opleidingsaanbod herplannen](../Koppelingen/opleidingsaanbod-herplannen.md) | Afnemer |
| [Late wijziging toetsen](../Koppelingen/late-wijziging-toetsen.md) | Afnemer |
| [Planningselementen ontsluiten](../Koppelingen/planningselementen-ontsluiten.md) | Afnemer |
| [Leeromgeving inrichten](../Koppelingen/leeromgeving-inrichten.md) | Afnemer |
| [Leeromgeving bijwerken](../Koppelingen/leeromgeving-bijwerken.md) | Afnemer |
| [Nominaal template inrichten](../Koppelingen/nominaal-template-inrichten.md) | Afnemer |
| [Examenplanwijziging toetsen](../Koppelingen/examenplanwijziging-toetsen.md) | Afnemer |
