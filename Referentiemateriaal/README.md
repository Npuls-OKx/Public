# Referentiemateriaal

Bronmateriaal dat de releasepakketten onderbouwt maar er zelf **geen onderdeel** van is: de richting, de besluiten en de kaderstellende scenario's waarop de specificaties steunen. Zonder deze context zijn de keuzes in een specificatie te lezen als willekeur; met deze context zijn ze navolgbaar.

Deze map is de container *Reference Material* uit het repo-setupmodel: bronmateriaal dat aan OKx gerelateerd is maar niet direct deel uitmaakt van de releasepakketten.

| Map | Inhoud |
| --- | --- |
| [`principes/`](principes/) | De architectuurprincipes (AP01–AP13) en de OKx-uitgangspunten: waarom en hoe we werken |
| [`kaderscenario's/`](kaderscenario's/) | Per Npuls-leerroute de kaderstellende uitwerking van de keten |
| [`persona's/`](persona's/) | De studenten die als rode draad door die scenario's lopen |
| [`requirements/`](requirements/) | Wat de standaard moet kunnen, als toetsbare eisen |
| [`memos/`](memos/) | Ingebrachte analyses die als invoer dienen voor een uitwerking |
| [`adr/`](adr/) | De architectuurbesluiten die de specificaties aanhalen |

## Principes en uitgangspunten

[`principes/`](principes/) bevat twee documenten die bij elkaar horen: de [architectuurprincipes](principes/principes.md) (AP01 tot en met AP13, abstract en stabiel: *waarom*) en de [OKx-uitgangspunten](principes/uitgangspunten.md) (concreter en evoluerend: *wat* en *hoe*). Samen leggen ze de richting onder alle uitwerkingen.

Niet te verwarren met de uitgangspunten U1 tot en met U10 van de koppelingspecificaties ([`Koppelvlakspecificaties/uitgangspunten.md`](../Koppelvlakspecificaties/uitgangspunten.md)); die gaan specifiek over het schrijven van een koppelingspecificatie en steunen op de principes hier.

## Kaderscenario's en persona's

[`kaderscenario's/`](kaderscenario's/) bevat per Npuls-leerroute de kaderstellende uitwerking: wat er in de keten gebeurt, welke referentiecomponenten daarvoor nodig zijn, welke informatie ontstaat en wat er tussen die componenten beweegt. Dit is de gedeelde basis waarop de koppelingspecificaties doorbouwen. [Leerroute 1 — regulier](kaderscenario's/leerroute-1-regulier.md) is de baseline; leerroute 2 en 3 worden als verschil daarop beschreven en volgen nog.

De persona die als rode draad door een scenario loopt, staat als eigen document in [`persona's/`](persona's/) — [Jochem](persona's/jochem.md) hoort bij leerroute 1.

## Requirements

[`requirements/`](requirements/) legt vast **wat de standaard moet kunnen**, voordat er attributen en endpoints worden gekozen: genummerde, toetsbare eisen met acceptatiecriteria. Een afnemer bouwt daar niet mee, maar leest er wel in waarom een uitwerking de vorm heeft die hij heeft. De [eisen rond keuzes bij onderwijsspecificaties](requirements/keuzes-rond-onderwijsspecificaties.md) dragen de [regelset-payload](../Koppelvlakspecificaties/Koppelingspecificaties/gedeeld/payload-regelset.md) in het pakket.

## Memo's

[`memos/`](memos/) bevat analyses die door een persoon zijn ingebracht en die als invoer dienen voor een uitwerking in het releasepakket. Waar een besluit vastlegt *wat* er is afgesproken, draagt een memo de **waarneming** waarop dat besluit steunt. De [Onderwijs PDCA-cyclus](memos/onderwijs-pdca-cyclus.md) voedt de lifecycle- en versioneringsuitwerking en de acceptatieregels rond het examenplan.

## Architectuurbesluiten (ADR's)

Een **architecture decision record** legt één besluit vast: de context, de afweging, het besluit en de gevolgen. Samen vormen ze het geheugen van de architectuur: waarom staat er in de specificaties wat er staat.

De volledige reeks en de toelichting staan in [`adr/`](adr/). Alle besluiten hebben op dit moment de status **voorstel**.

Al het overige bronmateriaal (ArchiMate-model, meeting-notulen, het OEAPI consumer-profiel, projectdocumentatie) blijft in de meta-repository en valt buiten deze map.
