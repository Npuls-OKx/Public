# Architectuurbesluiten (ADR's)

Een **architecture decision record** legt één besluit vast: de context waarin het speelde, de afwegingen, het genomen besluit en de gevolgen. Samen vormen ze het geheugen van de architectuur: waarom staat er in de specificaties wat er staat.

Waar een [principe](../principes/) richting geeft en een [kaderscenario](../kaderscenario's/) de keten beschrijft, beantwoordt een ADR één concrete vraag waarop de keten anders was doodgelopen. De specificaties in het releasepakket halen ze aan; wie een keuze wil begrijpen of aanvechten, begint hier.

Alle besluiten hebben op dit moment de status **voorstel**.

## De besluiten

| Nr | Onderwerp |
| --- | --- |
| [0001](0001-publieke-repo-en-samenwerkingsmodel.md) | Publieke repo als bron van waarheid; pull requests, issues, review |
| [0002](0002-prioriteitsketen-catalogus-drielagen-fundament.md) | Eerste keten curriculum naar catalogus; MORA/MOKA-drielagenfundament |
| [0003](0003-student-kiest-leeruitkomsten-domeinprincipes.md) | Student kiest; leeruitkomsten en de onderwijskundige laag |
| [0004](0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) | Leeruitkomsten met SBU/EC als logistieke containergrootte |
| [0005](0005-student-keuze-systeem-zelfstandige-referentiecomponent.md) | Studentkeuzesysteem als zelfstandige referentiecomponent |
| [0006](0006-studentorientatie-trechter-ketenfase.md) | Studentoriëntatie als ketenfase; trechter naar leeruitkomsten |
| [0007](0007-student-keuze-criteria-als-query-parameters-onderwijs-aanbod.md) | Studentkeuzecriteria als queryparameters richting de onderwijscatalogus |
| [0008](0008-scope-planning-eerst-intra-instelling.md) | Eerst intra-instelling; federatie gefaseerd |
| [0009](0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) | Rollen SKS en SVS: keuze tegenover resultaat en voortgang |
| [0010](0010-archimatemodel-werkafspraken.md) | Werkafspraken rond het ArchiMate-model en het MOKA-informatiemodel |
| [0011](0011-keuzeniveau-leeractiviteit-leervormen-als-aanbodkenmerk.md) | Keuze op leeractiviteitniveau; leervormen als aanbodkenmerk |
| [0012](0012-leerroute-onafhankelijk-keuzegate-nominaal-maatwerk.md) | Leerroute instellingsonafhankelijk; keuzegate nominaal tegenover maatwerk |
| [0013](0013-microcredentials-scope-en-credentialcontrole-intake.md) | Microcredentials: scope-afbakening en credentialcontrole bij intake |
| [0014](0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md) | Splitsing inschrijving (ROD/KRS) en onderwijskundige keuze (SKS) |
| [0015](0015-request-for-offering-haalbaarheidstoets-tussen-sks-en-planning.md) | Request for Offering: haalbaarheidstoets tussen keuze en planning |
| [0016](0016-ontwikkelingswallet-edu-wallet-eigenaarschap-toestemming-en-ontsluiting.md) | Ontwikkelingswallet: eigenaarschap, toestemming en ontsluiting |
| [0017](0017-hierarchisch-datamodel-aanbodstructuur-leeruitkomsten-en-sbuec-aggregatie.md) | Hiërarchisch aanboddatamodel; leeruitkomsten en SBU/EC-aggregatie |
| [0018](0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md) | Messaging-patronen: aflevering, idempotentie, dead-letter, volgorde |
| [0019](0019-conceptuele-gelaagdheid-kwalificatie-specificatie-aanbod-rosa-koi.md) | Gelaagdheid kwalificatie, specificatie en aanbod; ROSA/KOI |
| [0020](0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md) | Curriculumontwerp naar catalogus: notify-then-pull, adopt tegenover klonen |
| [0021](0021-koppeling-versus-koppelvlak-terminologie.md) | Koppeling tegenover koppelvlak; de mapindeling die daaruit volgt |
| [0022](0022-resultaatbegrippen-conform-rosa-koi.md) | Resultaatbegrippen conform het ROSA Kernmodel Onderwijsinformatie |
| [0023](0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) | Leeruitkomst-ids als opaque sleutels binnen de koppeling met planning |
| [0024](0024-consolidatie-architectuurprincipes.md) | Consolidatie van de architectuurprincipes en de introductie van uitgangspunten |
| [0025](0025-requirementsboom-als-koppeling-business-techniek.md) | Requirementsboom als getoonde koppeling tussen business en techniek |

## Een besluit toevoegen

Kopieer [`template.md`](template.md) en noem het bestand `NNNN-korte-titel.md`, met het eerstvolgende vrije nummer. Een ADR beschrijft de context, de overwogen alternatieven met hun afweging, het besluit en de gevolgen. Benoem ook wat het besluit **vervangt** of verfijnt, en welke impact het heeft op het ArchiMate-model in de meta-repository.

## Nummering: let op 0024

De besluiten 0001 tot en met 0023 komen uit één doorlopende reeks. Nummer **0024** is een uitzondering: dat besluit droeg in de bron het nummer 0006, maar dat nummer was daar al bezet door *Studentoriëntatie als ketenfase*. In de meta-repository leven die twee besluiten op verschillende branches, waardoor de botsing daar niet opviel. Bij het samenbrengen kon één van beide zijn nummer houden; de doorlopende reeks won, en *Consolidatie architectuurprincipes* kreeg het eerstvolgende vrije nummer.

Verwijzingen naar "ADR 0006" in ouder materiaal kunnen dus twee dingen betekenen. Binnen dit repository is 0006 altijd *Studentoriëntatie als ketenfase*.
