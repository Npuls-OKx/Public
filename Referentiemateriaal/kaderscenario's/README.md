# Kaderscenario's

Per **Npuls-leerroute** één document dat de route uitwerkt tot een kaderstellend scenario: wat er in de keten gebeurt, wie welke rol speelt, welke informatie ontstaat en wat er tussen systemen moet bewegen. Deze documenten zijn de gedeelde basis waarop de koppelingspecificaties en latere uitwerkingen doorbouwen.

"Kaderstellend" betekent: beschrijvend en onderbouwend, niet voorschrijvend. Een kaderscenario legt niet op hoe een instelling haar onderwijs organiseert; het maakt zichtbaar welke informatie-uitwisseling nodig is om die route mogelijk te maken. Dat is dezelfde doelbinding als uitgangspunt U1 van de [koppelingspecificaties](../../Koppelvlakspecificaties/uitgangspunten.md).

## De reeks

| Kaderscenario | Route | Persona | Status |
| --- | --- | --- | --- |
| [Leerroute 1 — regulier](leerroute-1-regulier.md) | De nominale route: de student volgt de vooraf ontworpen opleiding in het bedoelde tempo | Jochem, opleiding Apothekersassistent | Uitgewerkt |
| Leerroute 2 — temporiseren | Dezelfde opleiding, bewust gespreid en gepersonaliseerd vanaf dag één | Larissa, topsporter, opleiding Software Developer | Nog over te brengen |
| Leerroute 3 — versnellen | Dezelfde opleiding, versneld op basis van eerder verworven competenties | Linda, met horeca-ervaring | Nog over te brengen |

**Leerroute 1 is de baseline.** Leerroute 2 en 3 worden beschreven als *verschil* ten opzichte daarvan: de structuur blijft gelijk, een handvol aspecten wijzigt. Begin dus bij leerroute 1, ook als je route 2 of 3 zoekt.

De leerroutes 4 tot en met 9 (personaliseren binnen de instelling, buiten de instelling, over sectoren heen; en modulair studeren via vrije keuze, bundelen en stapelen) zijn nog niet uitgewerkt. Het overzicht van alle negen staat in [leerroute-1-regulier.md](leerroute-1-regulier.md#de-npuls-leerroutes).

## Het ecosysteem: welke componenten en welke stromen

Een kaderscenario beschrijft niet alleen wat een student en een instelling meemaken. Het maakt ook zichtbaar **welk ecosysteem** nodig is om die route te kunnen leveren: welke systemen erbij betrokken zijn, wat elk daarvan wel en niet doet, en welke informatie ertussen beweegt. Dat is de brug van verhaal naar koppelvlak.

Dat gebeurt in de taal van de **referentiearchitecturen**: [MORA](https://mora.mbodigitaal.nl/) voor het mbo, met HORA en FORA in het vizier voor ho en federatief. OKx stemt de beschrijvingswijze daarop af, maar blijft pragmatisch: voldoende beschrijven om de keten te begrijpen, niet overbeschrijven (zie [uitgangspunten](../principes/uitgangspunten.md#afstemming-en-beschrijvingswijze)).

Componenten worden benoemd als **referentiecomponent**, niet als product. Een referentiecomponent beschrijft *wat* iets doet en *hoe* het zich gedraagt in de keten — Onderwijscatalogus, planningssysteem, roostersysteem, LMS, KRS, SVS, SKS, intakesysteem — onafhankelijk van welke leverancier het invult. Leveranciers mappen hun eigen applicaties op één of meer van die componenten en houden volledige vrijheid in hoe ze dat intern realiseren. Zie [OKx-AP05](../principes/principes.md#okx-ap05--referentiecomponenten-als-gedeeld-referentiekader).

Elk kaderscenario levert daarom vier dingen op over het ecosysteem:

| Wat | Waarom het nodig is |
| --- | --- |
| **Welke referentiecomponenten** de route raken | Zonder gedeelde componentbenoeming is semantische overeenstemming op een koppelvlak onbereikbaar |
| **Wat elk component wél en niet doet** | De rolafbakening voorkomt dat twee systemen dezelfde verantwoordelijkheid claimen |
| **Wie bron is van welk informatie-object** | Eén feit, één bron: dit voorkomt schaduwkopieën en tegenstrijdige gegevens ([OKx-AP13](../principes/principes.md#okx-ap13--source-system-ownership-en-doelbinding-per-referentiecomponent)) |
| **Welke informatiestromen ertussen lopen** | De stromen zijn de kandidaat-koppelingen; de som ervan levert het koppelvlak per component op |

Die laatste stap is de overgang naar [`Koppelvlakspecificaties/`](../../Koppelvlakspecificaties/): een informatiestroom die hier conceptueel is beschreven, wordt daar een gestandaardiseerde koppeling met berichten, patronen en payloads. Het kaderscenario zegt *dat* en *waarom* er iets beweegt; de koppelingspecificatie zegt *wat* er precies in het bericht staat.

De componenten en stromen blijven in een kaderscenario bewust **conceptueel**. Er staan geen endpoints, berichtformaten of API-details in; die horen bij een latere AMIGO-stap.

## Opbouw van een kaderscenario

Elk document volgt dezelfde indeling, zodat je routes naast elkaar kunt leggen:

1. **Doel en scope** — welke vragen het beantwoordt en wat er buiten valt
2. **De studentbeleving** — de route vanuit de lerende, met de keuzemomenten
3. **De instellingsbeleving** — wie ontwerpt, plant, roostert, begeleidt en examineert
4. **Het ecosysteem** — de betrokken referentiecomponenten, hun rolafbakening, de bronrollen per informatie-object en de informatiestromen ertussen
5. **Procesfasen en informatiestromen** — per fase welke informatie ontstaat en beweegt, met de informatiestromenplaat als kaart
6. **De ankertabel** — de informatie-objecten per niveau van het kwalificatiekader, van kader via leeruitkomst en specificatie naar aanbod, verbintenis en resultaat
7. **Concept-informatiemodel** — de objecten en hun samenhang

De persona hoort bij het kaderscenario maar staat als eigen document in [`persona's/`](../persona's/), zodat meerdere documenten ernaar kunnen verwijzen zonder de tekst te dupliceren.

## Herkomst

Deze documenten zijn extracten uit het [OKx OEAPI consumer-profiel](https://github.com/Npuls-OKx/meta/blob/d47bb0c74ec899a4384d06331692f74b9bd1db58/architecture/docs/specificatie/okx-oeapi-consumer-profiel/doc/20260501_Specificatie_document_OKx_OEAPI_profiel.md) in de meta-repository. Het brondocument blijft in meta doorontwikkelen; wat hier staat is gepind op meta-commit [`d47bb0c`](https://github.com/Npuls-OKx/meta/tree/d47bb0c74ec899a4384d06331692f74b9bd1db58).
