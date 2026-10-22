# Studentinformatiesysteem (SIS)

Het studentinformatiesysteem is hier de combinatie van het **kernregistratiesysteem (KRS)**, dat de inschrijving en de verbintenis vastlegt, en het **studentvolgsysteem (SVS)**, dat de individuele structuur, de voortgang en de resultaten bijhoudt. Het bezit de verbintenissen, de individuele structuren, de voortgang en de resultaten ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)). Uit de catalogus haalt het twee dingen op, de onderwijsspecificatiestructuur en de resultaatstructuur, en richt daarmee het nominale template in plus de mapping van welke toetsonderdeelresultaten welke leeruitkomsten afdichten.

## Koppelvlak

![Koppelvlak van het studentinformatiesysteem op de hoofdplaat v1.7](../src/koppelvlak_sis_krs_svs_view_ihp_v1_7.png)

De view toont het koppelvlak van het studentinformatiesysteem op de informatiestromen-hoofdplaat v1.7. Kernregistratie (KRS) en studievoortgang (SVS) maken er deel van uit.

![Koppelvlakdiensten en endpoints van het koppelvlak](../src/diagrammen/referentie/koppelvlak-van-het-studentinformatiesysteem.png)

Dezelfde optelsom van binnen: elke koppelvlakdienst die het studentinformatiesysteem implementeert, met daaronder de endpoints waarmee het die levert. Een dienst die zelf niets aanbiedt draagt in plaats daarvan een blok dat benoemt wat hij dan doet. De plaat wordt gegenereerd uit [`src/likec4-model/componenten.c4`](../src/likec4-model/componenten.c4); die bron gaat met de release mee, zodat de inhoud machinaal te lezen is en niet alleen als plaat.

## Koppelvlakdiensten

Dit component implementeert de volgende [koppelvlakdiensten](../Koppelvlakdiensten/README.md):

- [afleverabonnement-aanbieder](../Koppelvlakdiensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md)
- [onderwijsspecificatiestructuur-afnemer](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md)
- [resultaatstructuur-afnemer](../Koppelvlakdiensten/resultaatstructuur-afnemer.md)
- [verbintenistoestand-aanbieder](../Koppelvlakdiensten/verbintenistoestand-aanbieder.md)
- [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md)

## Koppelingen

| Koppeling | Rol |
|---|---|
| [Onderwijsspecificatie ophalen](../Koppelingen/onderwijsspecificatie-ophalen.md) | Afnemer (SVS) |
| [Resultaatstructuur ophalen](../Koppelingen/resultaatstructuur-ophalen.md) | Afnemer (SVS) |
| [Inschrijfbaar aanbod ontsluiten](../Koppelingen/inschrijfbaar-aanbod-ontsluiten.md) | Afnemer (KRS) |
| [Plaatsingsgroepen ontsluiten](../Koppelingen/plaatsingsgroepen-ontsluiten.md) | Aanbieder (KRS) |
| [Opleidingsprogrammaverbintenis ontsluiten](../Koppelingen/opleidingsprogrammaverbintenis-ontsluiten.md) | Aanbieder (KRS) |
| [Keuzeverbintenis vastleggen](../Koppelingen/keuzeverbintenis-vastleggen.md) | Afnemer (KRS) |
| [Onderwijseenheidverbintenis doorgeven](../Koppelingen/onderwijseenheidverbintenis-doorgeven.md) | Afnemer (SVS) |
| [Planninggroepen met studenten ontsluiten](../Koppelingen/planninggroepen-met-studenten-ontsluiten.md) | Afnemer (KRS) |
| [Toetsresultaat doorgeven](../Koppelingen/toetsresultaat-doorgeven.md) | Afnemer (SVS) |
| [Nominaal template inrichten](../Koppelingen/nominaal-template-inrichten.md) | Aanbieder (SVS) |
| [Examenplanwijziging toetsen](../Koppelingen/examenplanwijziging-toetsen.md) | Aanbieder (SVS) |
