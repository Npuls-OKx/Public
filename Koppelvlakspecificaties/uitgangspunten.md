# Uitgangspunten voor koppelingen

**Aanleiding.** Bij het uitwerken van de eerste koppelingen bleek dat elk document dezelfde aannames opnieuw uitlegde: wat een beschrijving vastlegt en wat niet, wie welke resource bezit, waarom een event dun blijft. Die herhaling maakte de documenten langer dan nodig en, erger, liet de redenering op meerdere plekken uit elkaar lopen zodra er iets wijzigde. Daarom staan de gedeelde aannames hier eenmaal.

Deze uitgangspunten gelden voor **elke** koppeling in dit pakket en voor de payloads die zij uitwisselt. Een individueel document noemt het uitgangspunt in één regel en verwijst hierheen; het herhaalt de motivering niet. Zo hoeft een wijziging in de redenering maar op één plek te gebeuren.

De uitgangspunten zijn genummerd (U1 tot en met U11) zodat je er in een document of een review naar kunt verwijzen: "conform U5".

Herkomst: de [OKx-architectuurprincipes](../Referentiemateriaal/principes/principes.md) en [OKx-uitgangspunten](../Referentiemateriaal/principes/uitgangspunten.md), plus de architectuurbesluiten in [`Referentiemateriaal/adr/`](../Referentiemateriaal/adr/). Waar een uitgangspunt op een besluit steunt, staat dat erbij. Alle aangehaalde besluiten hebben op dit moment de status voorstel.

## U1. Bouwblokken liggen vast, de keuze van koppelingen is vrij

De **bouwblokken** zijn normatief: de koppelvlakdiensten met hun endpoints en payloads, en de interactiepatronen. Wie een bouwblok implementeert, implementeert het zoals het beschreven staat. Daardoor sluiten twee partijen die dezelfde berichtstroom implementeren op elkaar aan zonder aanvullende afspraak. Hoe een partij een bouwblok intern realiseert, blijft haar eigen keuze.

De **keuze van koppelingen** is vrij. Een partij implementeert de koppelingen die zij nodig heeft; OKx verplicht niemand tot een koppeling en legt niet op wie met wie koppelt. Binnen een koppeling is niets vrij: wie haar implementeert, implementeert in zijn rol elke berichtstroom ervan. Voor twee partijen die dezelfde koppeling implementeren, staat daarmee vast welke stromen er tussen hen lopen.

De afweging is die tussen vrijheid en aansluiting. Een vrije keuze per stroom laat elke partij precies bouwen wat zij nodig heeft, maar garandeert niet dat twee partijen dezelfde stromen hebben. Een koppeling legt de verplichting op het niveau van één doel. De prijs is dat een partij een stroom implementeert die zij binnen die koppeling zelf niet nodig heeft.

De scenario's waarmee een stroom wordt toegelicht zijn illustratief: ze onderbouwen waarom een bouwblok bestaat, maar leggen zelf niets vast.

De bouwblokken komen voort uit die scenario's. We hebben nog beperkt zicht op de werking van het ecosysteem; door koppeling voor koppeling en scenario voor scenario de interacties te bestuderen, ontdekken we welke operaties, endpoints en data nodig zijn. De **som** van de koppelingbeschrijvingen levert de koppelvlakspecificatie per referentiecomponent op: de endpoints en operaties die dat component kan bieden, elk gegrond in een beschreven interactie.

![Van scenario naar koppelvlakspecificatie: scenario's en latere behoeften leveren koppelingen op, die samen per component de koppelvlakspecificatie vormen](src/diagrammen/uitgangspunten/van-scenario-naar-koppelvlakspecificatie.png)

De beschreven koppelingen zijn **niet uitputtend**. Nieuwe functionaliteit kan operaties vragen die niet uit de huidige scenario's naar voren komen. Voorbeeld: een studentkeuzesysteem dat namens een student onderwijs aanvraagt dat nog niet bestaat. Zo'n behoefte komt binnen als nieuw scenario met een eigen koppelingbeschrijving, en onderbouwt daarmee een nieuwe operatie op het koppelvlak. Het koppelvlak houdt die ruimte.

Sluit aan op [OKx-AP04 — Koppelvlakken als open, gestandaardiseerde contracten](../Referentiemateriaal/principes/principes.md#okx-ap04--koppelvlakken-als-open-gestandaardiseerde-contracten) (het externe contract ligt vast, de interne realisatie niet), [OKx-AP02 — Semantiek vóór techniek](../Referentiemateriaal/principes/principes.md#okx-ap02--semantiek-vóór-techniek) (geen API-first zonder voorafgaande keten- en informatiemodelcontext) en [OKx-AP06 — Contracten zijn versieerbaar en evolueerbaar](../Referentiemateriaal/principes/principes.md#okx-ap06--contracten-zijn-versieerbaar-en-evolueerbaar).

## U2. Koppeling versus koppelvlak

Een **koppeling** is één of meer endpoint-interacties met één doel, tussen een aanbieder en een afnemer. Zij is afgeleid van een applicatiedienst uit de domeinarchitectuur en komt één op één overeen met een OEAPI-profiel; de opbouw en de ontwerpregels staan bij [Koppelingen](Koppelingen/README.md). Een **koppelvlak** is de verzameling van alle koppelingen die één component raken, als aanbieder of als afnemer; de koppelvlakspecificatie is de optelsom per component.

Dit verfijnt [ADR 0021](../Referentiemateriaal/adr/0021-koppeling-versus-koppelvlak-terminologie.md), waarin een koppeling de volledige informatiestroom tussen twee referentiecomponenten was. Wat dat besluit één koppeling noemt, zoals onderwijscatalogus naar planning en roostering, bestaat hier uit meerdere koppelingen met elk een eigen doel.

## U3. Resource-eigenaarschap

Elk systeem bezit zijn eigen resource en is er de enige bron van. De onderwijscatalogus bezit de onderwijsspecificaties, planning bezit het onderwijsaanbod, roostering bezit het rooster, het studentinformatiesysteem bezit de verbintenissen en resultaten. Niemand kopieert de resource van een ander.

Over de koppeling gaan daarom **referenties** (uuid) en niet de resource zelf, tenzij die expliciet wordt opgevraagd. Dat voorkomt dat dezelfde gegevens op meerdere plekken een eigen leven gaan leiden.

## U4. Event notification

Een melding over een koppeling is dun: zij draagt de aanleiding en een verwijzing, niet de inhoud, en de afnemer haalt de resource zelf op. Het patroon staat uitgewerkt bij [Event Notification](Interactiepatronen/event-notification.md).

Dit uitgangspunt legt de keuze vast en niet het patroon: elke koppeling in dit pakket gebruikt het, en het is geen afweging per koppeling. Vastgelegd in [ADR 0020](../Referentiemateriaal/adr/0020-curriculumontwerp-onderwijscatalogus-happy-flow-synchronisatie-en-federatie-adopt-klonen.md).

## U5. Bericht versus kanaal

Een koppeling legt het **bericht** vast: wat erin staat, wanneer het wordt verstuurd, hoe een ontvanger een herhaling herkent, en in welke volgorde berichten over dezelfde sleutel aankomen.

Hoe dat bericht bij de ontvanger komt, het **kanaal**, is een inrichtingskeuze van instelling en leverancier: een webhook, een bus, een broker of een cloud-pubsubdienst. OKx schrijft dat product niet voor.

Het kanaal is daarmee niet volledig vrij. [ADR 0018](../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md) is technologie-agnostisch maar niet vrijblijvend: welk kanaal je ook kiest, het moet aantoonbaar vier eigenschappen leveren.

| Eigenschap | Wat het betekent | Waarom het niet vrij is |
|---|---|---|
| Gegarandeerde aflevering | Een bericht raakt niet stil zoek | Zonder deze eigenschap merkt de keten een gemiste mutatie pas veel later |
| Idempotente verwerking | Een herhaald bericht heeft geen extra effect | Vereist een stabiel event-id in het bericht; dat is dus wel onze zorg |
| Dead-letterpad | Onverwerkbare berichten komen ergens zichtbaar terecht | Anders verdwijnt een fout zonder spoor |
| Volgorde per sleutel | Berichten over dezelfde entiteit komen in volgorde aan | Veel cloud-pubsubdiensten garanderen dit niet standaard en vragen expliciete configuratie |

De laatste is de scherpste. Twee implementaties die allebei "een bericht sturen" maar de volgorde per entiteitsleutel niet bewaken, leveren verschillende uitkomsten op bij statusovergangen.

**Open punt.** Welk afleveringsmechanisme partijen onderling kiezen is nog niet belegd. Twee systemen die beide aan het bericht voldoen maar waarvan het ene een webhook aanbiedt en het andere op een eigen broker publiceert, kunnen zonder afspraak of adapter alsnog niet koppelen. Dat is een vraag voor het koppelvlak, niet voor een afzonderlijke koppeling.

## U6. Semantiek uit de ankertabel

Begrippen komen uit de [ankertabel](../Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#betrokken-informatie-bij-proces): kader, beoogde leeruitkomst, specificatie, aanbod, verbintenis, resultaat. Geen verzonnen termen; subtypen voluit met backquotes.

De **leeruitkomst is de sleutel**. Specificaties verankeren erop, en onderwijsresultaten worden erop behaald ([ADR 0022](../Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md), conform het ROSA Kernmodel Onderwijsinformatie). Verankering gebeurt op de uuid van de leeruitkomst, niet op een tekstcode; een leesbare aanduiding mag ernaast staan.

## U7. Payload plat met verwijzingen, en de sleutelconventie

Objecten staan in **platte arrays** met een zelfverwijzende ouder-pointer, niet fysiek genest. Daardoor is elk object los adresseerbaar en los te versioneren, en hoef je geen halve boom mee te sturen om één onderdeel te wijzigen. De prijs is dat de hiërarchie niet meer uit de JSON zelf blijkt; daarom hoort er een instantieboom bij (U8).

**Sleutelconventie.** Het eigen sleutelveld van een object binnen zijn array heet `id`. Zodra een veld naar een ander object wijst, draagt het een expliciete naam die zegt waarheen: `bovenliggendSpecificatieId`, `bovenliggendAanbodId`, `leeruitkomstId`, `locatieId`, `specificatieVerwijzing.specificatieId`. Een kaal `bovenliggendId` is context-gevoelig en dus niet toegestaan.

Dit wijkt bewust af van de Open Onderwijs API, die getypeerde sleutels hanteert zoals `educationSpecificationId`. De payloads zijn Nederlandstalig, dus die afwijking bestond al; te betrekken bij de latere binding (uitgangspunt [OEAPI, tenzij](../Referentiemateriaal/principes/uitgangspunten.md#technologie-en-standaarden)).

**Taal.** Veldnamen en waarden in het Nederlands, met de Engelse of OEAPI-term tussen haakjes waar dat helpt.

## U8. Machine-interpreteerbaar, met leesbare weergaven

Elke payload heeft een **JSON Schema** (draft 2020-12) in de [informatie- en gegevensmodellen](../Informatie-en-gegevensmodellen/README.md) dat de vorm vastlegt: types, verplicht of optioneel, enums en patronen. Enumeraties horen daar, niet in een aparte tabel. De volwassenheid wordt op het schema zelf gemarkeerd (`$comment`), niet in de documenttitel of de doelstelling (zie U10).

Sluit aan op de uitgangspunten [machine-interpreteerbare formaten](../Referentiemateriaal/principes/uitgangspunten.md#technologie-en-standaarden) en [show don't tell](../Referentiemateriaal/principes/uitgangspunten.md#afstemming-en-beschrijvingswijze).

## U9. Scenario's en persona's

Documenten werken **leerroute 1** (regulier) uit aan de hand van persona **Jochem**, opleiding Apothekersassistent (SBB-kwalificatiedossier 23450, kwalificatie 27141). Leerroute 2 (temporiseren) en 3 (versnellen) volgen als **verschil** ten opzichte daarvan: de structuur blijft gelijk, een handvol attributen wijzigt.

De route en de persona staan volledig uitgewerkt in het [kaderscenario leerroute 1 — regulier](../Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md). Dat document is de kaderstellende basis waarop de koppelingen hier doorbouwen; het beschrijft per processtap wat er gebeurt en welke informatie beweegt. De overige leerroutes: [`kaderscenario's/`](../Referentiemateriaal/kaderscenario's/).

## U10. Scope- en documentdiscipline

- **Intra-instelling eerst.** Koppelingen worden eerst binnen één instelling uitgewerkt; federatie en cross-instelling volgen gefaseerd ([ADR 0008](../Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md)).
- **Scope sluit af.** Een document benoemt positief wat in scope is, noemt de afbakeningen die anders verwarring geven, en sluit af met de regel dat al het overige buiten het document valt. Een lezer hoeft dan niet te raden of iets vergeten of bewust weggelaten is.
- **Doel is toetsbaar.** Een document benoemt welke vragen het beantwoordt en wanneer het geslaagd is.
- **Geen statusaanduiding in de inhoud.** Woorden als "alpha" of "een eerste versie" horen niet in een titel, doel of scope. De volwassenheid van een artefact noteer je op dat artefact (bijvoorbeeld op het schema); de status van het werk staat in de pull request en de git-historie.
- **Geen metadatakop, geen issueverwijzingen.** Auteurschap en datums komen uit de git-historie; de weg waarlangs een document tot stand kwam staat in de pull requests. Deze documenten worden gereleased en moeten leesbaar zijn voor iemand die geen toegang heeft tot het werkproces erachter. Een verwijzing naar een issuenummer zegt zo'n lezer niets en veroudert bovendien: schrijf in plaats daarvan de **aanleiding** uit in de inleiding.
- **De inleiding is zelfdragend.** Ze benoemt de **aanleiding** (welk probleem of welke waarneming aanleiding gaf tot dit document), de **context** (waar het in de keten zit), het **doel** (welke vragen het beantwoordt) en de **scope** (wat er wel en niet in staat). Wie alleen de inleiding leest, weet of dit document zijn vraag beantwoordt.
- **Verwijzingen zijn links**, ook naar besluiten en naar andere documenten in deze map.

De bredere schrijfstijl staat in [`.cursor/rules/docs-style.mdc`](https://github.com/Npuls-OKx/meta/blob/d47bb0c74ec899a4384d06331692f74b9bd1db58/.cursor/rules/docs-style.mdc).

## Gerelateerde documenten

- [Instap voor nieuwkomers](README.md): ketenoverzicht, hoofdplaat, afkortingenlegenda en leesvolgorde.
- [OKx-architectuurprincipes](../Referentiemateriaal/principes/principes.md) en [OKx-uitgangspunten](../Referentiemateriaal/principes/uitgangspunten.md): de richting waarop deze uitgangspunten steunen.

## U11. Toekomstvaste endpoints: volledige structuur en delta

OKx definieert endpoints die ook toekomstige scenario's mogelijk maken. Waar een resource als structuur wordt ontsloten, biedt de eigenaar daarom beide vormen aan: de volledige structuur en de wijziging (delta). Een implementatie kiest zelf wat bij haar situatie past: een eenvoudige implementatie verwerkt de volledige structuur opnieuw, een rijkere implementatie verwerkt alleen de delta.

Waarom: de keten kent implementaties van verschillende volwassenheid, en scenario's die we nog niet kennen. Eén verplichte vorm dwingt óf onnodige complexiteit af (delta-berekening voor wie die niet nodig heeft) óf onnodig zwaar verkeer (volledige structuur voor wie alleen de wijziging wil). Twee vormen op dezelfde resource houden beide routes open zonder de semantiek te splitsen.

Zichtbaar in de koppeling [Onderwijsspecificatie ophalen](Koppelingen/onderwijsspecificatie-ophalen.md#specificatiewijziging-melden): de wijzigingsmelding is dun (conform U4), waarna de afnemer de volledige structuur of de delta ophaalt.
