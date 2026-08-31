## Eisen komen vóór de techniekkeuze

Status: Voorstel

Datum: 2026-08-28

### Context

OKx bouwt de koppelvlakspecificaties op bestaande standaarden en referentiemodellen: OEAPI voor onderwijsgegevens, Edukoppeling voor transport en authenticatie, ROSA en KOI als semantisch kader. Dat is bewust beleid (AMIGO als standaardiseringsroute, OKx-AP03): aansluiten bij wat er is, in plaats van iets nieuws bouwen.

Tijdens het uitwerken van eisen blijkt soms dat een bestaande standaard een onderwijs- of ketenbehoefte niet of onhandig ondersteunt. Zonder afspraak ontstaat dan een sluipend risico: de eis wordt stilzwijgend afgezwakt naar wat de standaard toevallig toelaat, en de onderwijslogistiek wordt techniekvolgend in plaats van andersom. Voor instellingen is dat onzichtbaar: de specificatie oogt compleet, maar beschrijft de mogelijkheden van een standaard in plaats van de behoefte van het onderwijs.

Deze werkafspraak leeft al in de werkomgeving van het OKx-team; dit besluit formaliseert haar op de plek waar afnemers lezen.

### Beslissing

1. **Eisen worden vastgesteld op de onderwijs- en ketenbehoefte**, vóór en los van de vraag of een technische standaard ze ondersteunt. Dat geldt voor keten-eisen, functionele eisen en de stories in de requirementsboom.
2. **Een eis sneuvelt nooit omdat een standaard hem niet toestaat.** Past een standaard niet, dan blijft de eis staan en wordt de mismatch vastgelegd en als **signalering** ingebracht bij de beheerder van die standaard (bijvoorbeeld de OEAPI-werkgroep).
3. **Tot de standaard beweegt, kiest OKx een expliciet gedocumenteerde tussenoplossing**: een profiel, extensie of afgebakende afwijking, nooit een stilzwijgende afzwakking van de eis.

Het bijbehorende architectuurprincipe staat als OKx-AP14 in het [principes-document](../principes/principes.md).

### Alternatieven

- **De standaard is leidend** (eisen aanpassen aan wat de standaard kan): afgewezen. De keten bestaat om onderwijsflexibilisering te dragen; een specificatie die de behoefte afzwakt naar de techniek lost het verkeerde probleem op en maakt de beperking onzichtbaar voor instellingen.
- **Een eigen standaard, los van OEAPI en Edukoppeling**: afgewezen. Dat verplaatst de beheerlast naar OKx, breekt met de AMIGO-route (OKx-AP03) en ondergraaft de adoptie door leveranciers die de landelijke standaarden al implementeren.
- **Per geval beslissen zonder vaste regel**: afgewezen. Onvoorspelbaar voor leveranciers en instellingen; precies de willekeur die een afsprakenstelsel moet wegnemen.

### Consequenties

- Voor informatiemanagers van instellingen: de eisen in het releasepakket beschrijven de **behoefte van het onderwijs**, niet de beperkingen van een leveranciers- of sectorstandaard. Waar een standaard tekortschiet, is dat zichtbaar als gedocumenteerde signalering, niet weggemoffeld in een afgezwakte eis.
- Signaleringen richting een standaardbeheerder krijgen een vaste, navolgbare plek: een verwijzing bij de betrokken eis en een issue in deze repository, zodat te volgen is wat er met de signalering gebeurt.
- Het principes-document krijgt OKx-AP14 (eisen vóór techniekkeuze), in dezelfde reeks als AP02 (semantiek vóór techniek) en AP03 (AMIGO), die dit besluit flankeren.
- Geen impact op het ArchiMate-model in de meta-repository.

### Relaties en links

- Principes: [OKx-AP02, OKx-AP03 en OKx-AP14](../principes/principes.md)
- Requirementsboom: [Referentiemateriaal/requirementsboom](../requirementsboom/README.md) (de eisenlagen waarop dit besluit werkt)
- Oorsprong: de werkafspraak in de meta-werkomgeving ([AGENTS.md, gepind](https://github.com/Npuls-OKx/meta/blob/bd6fc9499b283fe974fd32c87bbb9307e75e7d1b/AGENTS.md))
- ArchiMate model: geen wijziging
