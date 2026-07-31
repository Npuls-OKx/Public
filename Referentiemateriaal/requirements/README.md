# Requirements

Wat de standaard moet **kunnen**, vastgelegd voordat er attributen en endpoints worden gekozen. Genummerde, toetsbare eisen met acceptatiecriteria.

Waarom dit apart staat van het releasepakket: een afnemer bouwt niet met een eisenlijst, maar leest er wel in waarom een payload de vorm heeft die hij heeft. De eisen zijn de onderbouwing, de payload is het product. Wie een uitwerking wil beoordelen, legt hem naast de eisen die eraan ten grondslag lagen.

Waarom eisen vóór attributen: zonder afspraak vult elke leverancier een open plek in met eigen aannames. Die worden de-facto standaard en zijn later niet meer te wijzigen.

| Requirements | Eisen | Uitgewerkt in |
| --- | --- | --- |
| [Keuzes rond onderwijsspecificaties](keuzes-rond-onderwijsspecificaties.md) | R1 t/m R16: kiesbaarheid, voorwaarden in behaalde leeruitkomsten, regels los van items, evalueerbaar met alleen sleutels | [Regelset als JSON-payload](../../Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/payload-regelset.md) |

De dekking is in beide richtingen na te lopen: het requirements-document heeft een matrix van eis naar figuur, en de payload-uitwerking een tabel van regeltype naar eis.
