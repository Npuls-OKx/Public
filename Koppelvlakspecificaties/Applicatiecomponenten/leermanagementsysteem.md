# Leermanagementsysteem (LMS)

Het leermanagementsysteem is de online leeromgeving waarin de student het onderwijs volgt. Het neemt de onderwijsspecificatiestructuur van de catalogus over, inclusief de inhoudsvelden van de leeruitkomsten die het aan de student toont, en richt daarmee de leeromgeving in. Het bezit de leermiddelkoppeling, de koppeling tussen leermiddelgroepen en specificatie ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)), en meldt die terug aan de catalogus. Kiesbaarheid is niet zijn domein: regelsets gaan over deze koppeling niet mee.

## Koppelvlak

![Koppelvlak van het leermanagementsysteem op de hoofdplaat v1.7](../src/koppelvlak_lms_view_ihp_v1_7.png)

De view toont het koppelvlak van het leermanagementsysteem: de optelsom van zijn koppelingen op de informatiestromen-hoofdplaat v1.7.

![Applicatiediensten en endpoints van het koppelvlak](../src/diagrammen/referentie/koppelvlak-van-het-leermanagementsysteem.png)

Dezelfde optelsom van binnen: elke applicatiedienst die het leermanagementsysteem claimt, met daaronder de endpoints waarmee het die levert. Een dienst die zelf niets aanbiedt draagt in plaats daarvan een blok dat benoemt wat hij dan doet. De plaat wordt gegenereerd uit [`model/componenten.c4`](../model/componenten.c4); die bron gaat met de release mee, zodat de inhoud machinaal te lezen is en niet alleen als plaat.

## Applicatiediensten

Dit component implementeert de volgende [applicatiediensten](../Applicatiediensten/README.md):

- [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)
- [leermiddelkoppeling-aanbieder](../Applicatiediensten/leermiddelkoppeling-aanbieder.md)
- [verwerkingsuitkomst-aanbieder](../Applicatiediensten/verwerkingsuitkomst-aanbieder.md)

## Koppelingen

Het treedt op in deze koppelingen:

- [Onderwijscatalogus naar leermanagementsysteem](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem.md)
