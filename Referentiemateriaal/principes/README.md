# Principes en uitgangspunten

Twee documenten die samen de richting onder alle OKx-uitwerkingen leggen. Ze horen bij elkaar en verwijzen naar elkaar.

| Document | Wat het zegt | Karakter |
| --- | --- | --- |
| [Architectuurprincipes](principes.md) | **Waarom** we dingen op een bepaalde manier doen. OKx-AP01 tot en met AP13, elk met stelling, rationale en implicaties. | Abstract en stabiel; wijzigt niet snel |
| [OKx-uitgangspunten](uitgangspunten.md) | **Wat** we aannemen en **hoe** we werken. Gefundeerde besluiten om blocking issues te voorkomen. | Concreter; evolueert met voortschrijdend inzicht |

Bij twijfel of uitzondering op een principe hoort een besluit in [`../adr/`](../adr/), niet een stilzwijgende afwijking.

## Niet te verwarren met

De koppelingspecificaties hebben hun **eigen** uitgangspunten, genummerd U1 tot en met U10: zie [`Koppelvlakspecificaties/uitgangspunten.md`](../../Koppelvlakspecificaties/uitgangspunten.md). Die gaan specifiek over hoe je een koppelingspecificatie schrijft (doelbinding, notify-then-pull, payloadvorm, sleutelconventie). De uitgangspunten hier gelden voor OKx als geheel en staan er een niveau boven; U1 steunt bijvoorbeeld op [OKx-AP04](principes.md#okx-ap04--koppelvlakken-als-open-gestandaardiseerde-contracten) en [OKx-AP05](principes.md#okx-ap05--referentiecomponenten-als-gedeeld-referentiekader).

## Herkomst

Overgenomen uit [`architecture/docs/principes/doc/`](https://github.com/Npuls-OKx/meta/tree/cf9d62a84d06dca0f6818cce01250e70d319f549/architecture/docs/principes/doc) in de meta-repository, gepind op commit [`cf9d62a`](https://github.com/Npuls-OKx/meta/tree/cf9d62a84d06dca0f6818cce01250e70d319f549) (branch `main`). De onderbouwing bij de consolidatie van zeventien principes naar dertien staat in [ADR 0006 — Consolidatie architectuurprincipes](https://github.com/Npuls-OKx/meta/blob/cf9d62a84d06dca0f6818cce01250e70d319f549/architecture/dr/0006-consolidatie-architectuurprincipes.md).

> **Let op bij het volgen van die ADR-link.** In de meta-repository dragen `main` en `dev` een **verschillende** ADR 0006: op `main` is dat *Consolidatie architectuurprincipes*, op `dev` *Studentoriëntatie trechter ketenfase*. De links hierboven wijzen expliciet naar de `main`-variant. De overige besluiten in [`../adr/`](../adr/) komen uit de `dev`-lijn.

Achtergrond bij beide documenten: het MOSA-visiedocument en de MOSA-versus-OKx-analyse, beide in [dezelfde map in meta](https://github.com/Npuls-OKx/meta/tree/cf9d62a84d06dca0f6818cce01250e70d319f549/architecture/docs/principes/doc).
