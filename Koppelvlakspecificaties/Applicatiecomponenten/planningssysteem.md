# Planningssysteem (P)

Het planningssysteem maakt van een gepubliceerde onderwijsspecificatie planbaar `opleidingsaanbod`: het bepaalt wanneer, hoe vaak en in welke vorm het onderwijs wordt aangeboden, en meldt de referentie naar dat aanbod terug aan de catalogus. Het bezit het onderwijsaanbod ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)). Het rooster zelf ligt bij het [roostersysteem](roostersysteem.md).

## Koppelvlak

![Planning en roostering op de hoofdplaat v1.7](../src/koppelvlak_p_en_r_view_ihp_v1_7.png)

De view toont planning en roostering samen, zoals de informatiestromen-hoofdplaat v1.7 ze tekent. Elk van de twee heeft wel een eigen koppelvlak: de optelsom van de koppelingen die het raken ([U2](../uitgangspunten.md#u2-koppeling-versus-koppelvlak)).

![Koppelvlakdiensten en endpoints van het koppelvlak](../src/diagrammen/referentie/koppelvlak-van-het-planningssysteem.png)

Dezelfde optelsom van binnen: elke koppelvlakdienst die het planningssysteem implementeert, met daaronder de endpoints waarmee het die levert. Een dienst die zelf niets aanbiedt draagt in plaats daarvan een blok dat benoemt wat hij dan doet. De plaat wordt gegenereerd uit [`src/likec4-model/componenten.c4`](../src/likec4-model/componenten.c4); die bron gaat met de release mee, zodat de inhoud machinaal te lezen is en niet alleen als plaat.

## Koppelvlakdiensten

Dit component implementeert de volgende [koppelvlakdiensten](../Koppelvlakdiensten/README.md):

- [afleverabonnement-aanbieder](../Koppelvlakdiensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md)
- [geroosterd-onderwijsaanbod-afnemer](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-afnemer.md)
- [onderwijsspecificatiestructuur-afnemer](../Koppelvlakdiensten/onderwijsspecificatiestructuur-afnemer.md)
- [planbaar-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/planbaar-onderwijsaanbod-aanbieder.md)
- [verwerkingsuitkomst-aanbieder](../Koppelvlakdiensten/verwerkingsuitkomst-aanbieder.md)

## Koppelingen

| Koppeling | Rol |
|---|---|
| [Onderwijsspecificatie ophalen](../Koppelingen/onderwijsspecificatie-ophalen.md) | Afnemer |
| [Specificatiestatus volgen](../Koppelingen/specificatiestatus-volgen.md) | Afnemer |
| [Specificatie aanpassen op verzoek](../Koppelingen/specificatie-aanpassen-op-verzoek.md) | Afnemer |
| [Opleidingsaanbod aanmaken](../Koppelingen/opleidingsaanbod-aanmaken.md) | Aanbieder |
| [Opleidingsaanbod herplannen](../Koppelingen/opleidingsaanbod-herplannen.md) | Aanbieder |
| [Late wijziging toetsen](../Koppelingen/late-wijziging-toetsen.md) | Aanbieder |
| [Planningselementen ontsluiten](../Koppelingen/planningselementen-ontsluiten.md) | Aanbieder |
| [Geplande leergelegenheden ontsluiten](../Koppelingen/geplande-leergelegenheden-ontsluiten.md) | Aanbieder |
| [Planninggroepen ontsluiten](../Koppelingen/planninggroepen-ontsluiten.md) | Aanbieder |
| [Plaatsingsgroepen ontsluiten](../Koppelingen/plaatsingsgroepen-ontsluiten.md) | Afnemer |
| [Animo doorgeven](../Koppelingen/animo-doorgeven.md) | Afnemer |
| [Leergelegenheden roosteren](../Koppelingen/leergelegenheden-roosteren.md) | Afnemer |
