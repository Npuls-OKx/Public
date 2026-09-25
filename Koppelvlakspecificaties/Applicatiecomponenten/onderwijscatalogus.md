# Onderwijscatalogus (OC)

De onderwijscatalogus is het distributiepunt voor onderwijsspecificaties: zij neemt ze aan van de curriculum-ontwerptool, legt ze vast en publiceert ze naar de systemen die het onderwijs klaarzetten voor de start van de student. Zij bezit de onderwijsspecificaties ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)), en is daarmee in elk van de drie koppelingen hieronder de partij die een wijziging meldt en de resource levert ([U4](../uitgangspunten.md#u4-event-notification)).

## Koppelvlak

![Koppelvlak van de onderwijscatalogus op de hoofdplaat v1.7](../src/koppelvlak_oc_view_ihp_v1_7.png)

De view toont het koppelvlak van de onderwijscatalogus: de optelsom van haar koppelingen op de informatiestromen-hoofdplaat v1.7.

![Applicatiediensten en endpoints van het koppelvlak](../src/diagrammen/referentie/koppelvlak-van-de-onderwijscatalogus.png)

Dezelfde optelsom van binnen: elke applicatiedienst die de catalogus claimt, met daaronder de endpoints waarmee zij die levert. Een dienst die zelf niets aanbiedt draagt in plaats daarvan een blok dat benoemt wat hij dan doet. De plaat wordt gegenereerd uit [`model/componenten.c4`](../model/componenten.c4); die bron gaat met de release mee, zodat de inhoud machinaal te lezen is en niet alleen als plaat.

## Applicatiediensten

Dit component implementeert de volgende [applicatiediensten](../Applicatiediensten/README.md):

- [onderwijsspecificatiestructuur-aanbieder](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md)
- [resultaatstructuur-aanbieder](../Applicatiediensten/resultaatstructuur-aanbieder.md)
- [planbaar-onderwijsaanbod-afnemer](../Applicatiediensten/planbaar-onderwijsaanbod-afnemer.md)
- [leermiddelkoppeling-afnemer](../Applicatiediensten/leermiddelkoppeling-afnemer.md)
- [verwerkingsuitkomst-afnemer](../Applicatiediensten/verwerkingsuitkomst-afnemer.md)
- [afleverabonnement-aanbieder](../Applicatiediensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Applicatiediensten/afleverabonnement-afnemer.md)

## Koppelingen

Het treedt op in deze koppelingen:

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)
