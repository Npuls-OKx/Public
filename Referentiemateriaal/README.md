# Referentiemateriaal

Bronmateriaal dat de releasepakketten onderbouwt maar er zelf **geen onderdeel** van is: de richting, de besluiten en de kaderstellende scenario's waarop de specificaties steunen. Zonder deze context zijn de keuzes in een specificatie te lezen als willekeur; met deze context zijn ze navolgbaar.

Deze map is de container *Reference Material* uit het repo-setupmodel: bronmateriaal dat aan OKx gerelateerd is maar niet direct deel uitmaakt van de releasepakketten.

| Map | Inhoud |
| --- | --- |
| [`principes/`](principes/) | De architectuurprincipes (AP01–AP13) en de OKx-uitgangspunten: waarom en hoe we werken |
| [`kaderscenario's/`](kaderscenario's/) | Per Npuls-leerroute de kaderstellende uitwerking van de keten |
| [`persona's/`](persona's/) | De studenten die als rode draad door die scenario's lopen |
| [`memos/`](memos/) | Ingebrachte analyses die als invoer dienen voor een uitwerking |
| [`adr/`](adr/) | De architectuurbesluiten die de specificaties aanhalen |

## Principes en uitgangspunten

[`principes/`](principes/) bevat twee documenten die bij elkaar horen: de [architectuurprincipes](principes/principes.md) (AP01 tot en met AP13, abstract en stabiel: *waarom*) en de [OKx-uitgangspunten](principes/uitgangspunten.md) (concreter en evoluerend: *wat* en *hoe*). Samen leggen ze de richting onder alle uitwerkingen.

Niet te verwarren met de uitgangspunten U1 tot en met U10 van de koppelingspecificaties ([`Koppelvlakspecificaties/uitgangspunten.md`](../Koppelvlakspecificaties/uitgangspunten.md)); die gaan specifiek over het schrijven van een koppelingspecificatie en steunen op de principes hier.

## Kaderscenario's en persona's

[`kaderscenario's/`](kaderscenario's/) bevat per Npuls-leerroute de kaderstellende uitwerking: wat er in de keten gebeurt, welke referentiecomponenten daarvoor nodig zijn, welke informatie ontstaat en wat er tussen die componenten beweegt. Dit is de gedeelde basis waarop de koppelingspecificaties doorbouwen. [Leerroute 1 — regulier](kaderscenario's/leerroute-1-regulier.md) is de baseline; leerroute 2 en 3 worden als verschil daarop beschreven en volgen nog.

De persona die als rode draad door een scenario loopt, staat als eigen document in [`persona's/`](persona's/) — [Jochem](persona's/jochem.md) hoort bij leerroute 1.

## Memo's

[`memos/`](memos/) bevat analyses die door een persoon zijn ingebracht en die als invoer dienen voor een uitwerking in het releasepakket. Waar een besluit vastlegt *wat* er is afgesproken, draagt een memo de **waarneming** waarop dat besluit steunt. De [Onderwijs PDCA-cyclus](memos/onderwijs-pdca-cyclus.md) voedt de lifecycle- en versioneringsuitwerking en de acceptatieregels rond het examenplan.

## Architectuurbesluiten (ADR's)

Een **ADR** (architecture decision record) legt één besluit vast: de context, de afweging, het besluit en de gevolgen. In [`adr/`](adr/) staan de besluiten die de koppelingspecificaties in dit repository aanhalen. Alle aangehaalde besluiten hebben op dit moment de status **voorstel**.

| ADR | Besluit | Waarvoor het in de specificaties wordt aangehaald |
| --- | --- | --- |
| [0003](adr/0003-student-kiest-leeruitkomsten-domeinprincipes.md) | Student kiest, leeruitkomsten als domeinprincipes | De leeruitkomst als sleutelbegrip |
| [0004](adr/0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md) | Leeruitkomsten met SBU/EC als logistieke containergrootte | Omvang en aggregatie in de payloads |
| [0008](adr/0008-scope-planning-eerst-intra-instelling.md) | Scope planning: eerst intra-instelling | Scopediscipline (U10): federatie volgt gefaseerd |
| [0009](adr/0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md) | Rollenverdeling SKS en SVS: keuze versus resultaat en voortgang | Afbakening van de koppeling OC-SIS |
| [0014](adr/0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md) | Splitsing inschrijving (ROD/KRS) en studentkeuze (SKS) | Welk systeem welke resource bezit |
| [0018](adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md) | Enterprise messaging-patronen voor betrouwbare koppelvlakken | De vier eigenschappen die een kanaal moet leveren (U5) |
| [0020](adr/0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md) | Curriculumontwerp naar onderwijscatalogus: synchronisatie en federatie | Notify-then-pull (U4) |
| [0021](adr/0021-koppeling-versus-koppelvlak-terminologie.md) | Koppeling versus koppelvlak: terminologie | Het onderscheid dat de mapstructuur van dit repository draagt (U2) |
| [0022](adr/0022-resultaatbegrippen-conform-rosa-koi.md) | Resultaatbegrippen conform ROSA Kernmodel Onderwijsinformatie | Resultaten hangen aan leeruitkomsten (U6) |
| [0023](adr/0023-leeruitkomsten-als-opaque-sleutels-in-koppeling-oc-p-en-r.md) | Leeruitkomsten als opaque sleutels in de koppeling OC naar P&R | Waarom planning alleen ids krijgt en geen leeruitkomst-laag |

**Niet uitputtend.** Dit is de selectie die de specificaties in dit repository aanhalen, niet de volledige besluitenlijst. De complete reeks staat in [`architecture/dr/` in de meta-repository](https://github.com/Npuls-OKx/meta/tree/d47bb0c74ec899a4384d06331692f74b9bd1db58/architecture/dr). Verwijzingen naar besluiten die hier niet staan, wijzen uit deze documenten gepind naar meta-commit [`d47bb0c`](https://github.com/Npuls-OKx/meta/tree/d47bb0c74ec899a4384d06331692f74b9bd1db58).

Al het overige bronmateriaal (ArchiMate-model, meeting-notulen, het OEAPI consumer-profiel, projectdocumentatie) blijft in de meta-repository en valt buiten deze map.
