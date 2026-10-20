# Roostersysteem (R)

Het roostersysteem plaatst het geplande onderwijs in tijd en ruimte: het maakt van het `opleidingsaanbod` een rooster met momenten, docenten en zalen. Het bezit het rooster, waar het planningssysteem het aanbod bezit en de catalogus de specificaties ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)).

## Koppelvlak

![Planning en roostering op de hoofdplaat v1.7](../src/koppelvlak_p_en_r_view_ihp_v1_7.png)

De view toont planning en roostering samen, zoals de informatiestromen-hoofdplaat v1.7 ze tekent. Elk van de twee heeft wel een eigen koppelvlak: de optelsom van de koppelingen die het raken ([U2](../uitgangspunten.md#u2-koppeling-versus-koppelvlak)).

## Koppelvlakdiensten

Dit component implementeert de volgende [koppelvlakdiensten](../Koppelvlakdiensten/README.md):

- [afleverabonnement-aanbieder](../Koppelvlakdiensten/afleverabonnement-aanbieder.md)
- [afleverabonnement-afnemer](../Koppelvlakdiensten/afleverabonnement-afnemer.md)
- [geroosterd-onderwijsaanbod-aanbieder](../Koppelvlakdiensten/geroosterd-onderwijsaanbod-aanbieder.md)

## Koppelingen

| Koppeling | Rol |
|---|---|
| [Planninggroepen ontsluiten](../Koppelingen/planninggroepen-ontsluiten.md) | Afnemer |
| [Plaatsing op lesgelegenheid aanvragen](../Koppelingen/plaatsing-op-lesgelegenheid-aanvragen.md) | Aanbieder |
| [Leergelegenheden roosteren](../Koppelingen/leergelegenheden-roosteren.md) | Aanbieder |
| [Geroosterde leergelegenheden ontsluiten](../Koppelingen/geroosterde-leergelegenheden-ontsluiten.md) | Aanbieder |
| [Planninggroepen met studenten ontsluiten](../Koppelingen/planninggroepen-met-studenten-ontsluiten.md) | Aanbieder |
