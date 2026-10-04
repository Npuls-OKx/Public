# Planningssysteem (P)

Het planningssysteem maakt van een gepubliceerde onderwijsspecificatie planbaar `opleidingsaanbod`: het bepaalt wanneer, hoe vaak en in welke vorm het onderwijs wordt aangeboden, en meldt de referentie naar dat aanbod terug aan de catalogus. Het bezit het onderwijsaanbod ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)). Het rooster zelf ligt bij het roostersysteem; dat kent in dit pakket geen eigen koppeling en komt alleen als context voor ([roostersysteem](roostersysteem.md)).

## Koppelvlak

![Gedeeld koppelvlak van planning en roostering op de hoofdplaat v1.7](../src/koppelvlak_p_en_r_view_ihp_v1_7.png)

De view toont het gedeelde koppelvlak van planning en roostering op de informatiestromen-hoofdplaat v1.7. Beide componenten delen dit koppelvlak; het rooster zelf blijft bij het roostersysteem.

![Applicatiediensten en endpoints van het koppelvlak](../src/diagrammen/referentie/koppelvlak-van-het-planningssysteem.png)

Dezelfde optelsom van binnen: elke applicatiedienst die het planningssysteem claimt, met daaronder de endpoints waarmee het die levert. Een dienst die zelf niets aanbiedt draagt in plaats daarvan een blok dat benoemt wat hij dan doet. De plaat wordt gegenereerd uit [`model/componenten.c4`](../model/componenten.c4); die bron gaat met de release mee, zodat de inhoud machinaal te lezen is en niet alleen als plaat.

## Applicatiediensten

Dit component implementeert de volgende [applicatiediensten](../Applicatiediensten/README.md):

- [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)
- [planbaar-onderwijsaanbod-aanbieder](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md)
- [verwerkingsuitkomst-aanbieder](../Applicatiediensten/verwerkingsuitkomst-aanbieder.md)
- [afleverabonnement-aanbieder](../Applicatiediensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Applicatiediensten/afleverabonnement-afnemer.md)

## Koppelingen

Het treedt op in deze koppelingen:

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
