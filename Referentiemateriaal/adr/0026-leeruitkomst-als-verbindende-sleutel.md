## Leeruitkomst als verbindende sleutel

Status: Voorstel

Datum: 2026-08-07

### Context

[ADR 0023](0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) legde vast dat leeruitkomst-ids binnen de koppeling OC-P&R "opaque sleutels" zijn. De werking klopt, maar de naam is voor functionele en businesslezers onbegrijpelijk jargon en onderschat de rol van het begrip: de leeruitkomst is de sleutel die specificaties, keuzeregels, aanbod, voortgang, resultaten en waardepapieren aan elkaar knoopt (zie ook [ADR 0022](0022-resultaatbegrippen-conform-rosa-koi.md)). De technische eigenschap, namelijk dat een afnemend systeem de inhoud van de leeruitkomst niet hoeft te kennen om ermee te werken, is een toelichting en geen naam. Relateert aan [meta-issue 138](https://github.com/Npuls-OKx/meta/issues/138).

### Beslissing

1. De term is voortaan **de leeruitkomst als verbindende sleutel**: de leeruitkomst verbindt specificatie, keuzeregel, aanbod, voortgang, resultaat en waardepapier. Systemen wisselen leeruitkomst-ids en behaald-status uit.
2. De werking uit ADR 0023 verandert niet. Binnen de koppeling OC-P&R komen leeruitkomst-ids uitsluitend voor in regelset-voorwaarden (`voorwaardeVooraf`) voor volgordebepaling en planvalidatie; de `leeruitkomsten`-lijst wordt daar niet meegeleverd. Een afnemer gebruikt de sleutel zonder de inhoud te hoeven kennen.
3. "Opaque sleutel" verdwijnt uit de actuele documenten; ADR 0023 blijft als historisch besluit staan met status Vervangen.

### Alternatieven

- Optie A: "opaque sleutel" behouden. Afgewezen: technisch jargon dat de functionele lezer buitensluit en de verbindende rol van de leeruitkomst wegdrukt.
- Optie B: "betekenisloze sleutel" of "pseudoniem". Afgewezen: benoemt alleen de technische eigenschap; voor de keten is de leeruitkomst juist betekenisvol, alleen de afnemer van deze ene koppeling hoeft de inhoud niet te kennen.

### Consequenties

- De koppelingspecificatie OC-P&R, de payload-onderwijsspecificatie en het Koppelvlakspecificaties-overzicht gebruiken de nieuwe term en verwijzen naar dit besluit.
- In de meta-repository volgen de requirementsboom (feature over leeruitkomst-ids in keuzeregels) en het begrippenkader; zie [meta-issue 138](https://github.com/Npuls-OKx/meta/issues/138).
- Conformance-tests en de werking van de koppeling veranderen niet.

### Relaties en links

- ADR's: [0022](0022-resultaatbegrippen-conform-rosa-koi.md) (resultaatbegrippen), [0023](0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) (vervangen door dit besluit)
- Meta: [meta-issue 138](https://github.com/Npuls-OKx/meta/issues/138) (terminologiebesluit en doorwerking)

### Vervangt (optioneel)

- [ADR 0023](0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md).
