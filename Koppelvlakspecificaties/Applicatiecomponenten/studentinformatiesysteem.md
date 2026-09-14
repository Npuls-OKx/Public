# Studentinformatiesysteem (SIS)

Het studentinformatiesysteem is hier de combinatie van het **kernregistratiesysteem (KRS)**, dat de inschrijving en de verbintenis vastlegt, en het **studentvolgsysteem (SVS)**, dat de individuele structuur, de voortgang en de resultaten bijhoudt. Het bezit de verbintenissen, de individuele structuren, de voortgang en de resultaten ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)). Uit de catalogus haalt het twee dingen op, de onderwijsspecificatiestructuur en de resultaatstructuur, en richt daarmee het nominale template in plus de mapping van welke toetsonderdeelresultaten welke leeruitkomsten afdichten.

## Koppelvlak

![Koppelvlak van het studentinformatiesysteem op de hoofdplaat v1.7](../src/koppelvlak_sis_krs_svs_view_ihp_v1_7.png)

De view toont het koppelvlak van het studentinformatiesysteem op de informatiestromen-hoofdplaat v1.7. Kernregistratie (KRS) en studievoortgang (SVS) maken er deel van uit.

## Applicatiediensten

Dit component implementeert de volgende [applicatiediensten](../Applicatiediensten/README.md):

- [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)
- [resultaatstructuur-afnemer](../Applicatiediensten/resultaatstructuur-afnemer.md)
- [verwerkingsuitkomst-aanbieder](../Applicatiediensten/verwerkingsuitkomst-aanbieder.md)

## Koppelingen

Het treedt op in deze koppelingen:

- [Onderwijscatalogus naar studentinformatiesysteem](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem.md)
