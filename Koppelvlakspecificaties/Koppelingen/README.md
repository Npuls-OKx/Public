# Koppelingen

Een koppeling is één of meer endpoint-interacties met één doel, tussen een aanbieder en een afnemer. Zij is afgeleid van een applicatiedienst uit de domeinarchitectuur: het gedrag dat de [informatiestromen-hoofdplaat](../src/informatiestromen_hoofdplaat_v1_7.png) in een component tekent, zoals *Periode planning* in het planningssysteem. Elke koppeling komt één op één overeen met een OEAPI-profiel, met dezelfde naam en dezelfde versie ([U2](../uitgangspunten.md#u2-koppeling-versus-koppelvlak), [release management §4.2](../release-management.md#42-een-koppeling-draagt-haar-eigen-versie)).

Een koppeling legt berichtstromen vast. Elke berichtstroom noemt het [interactiepatroon](../Interactiepatronen/README.md) en de [koppelvlakdiensten](../Koppelvlakdiensten/README.md) die hij inzet, en een koppelvlakdienst levert via endpoints. Een applicatiedienst en een koppelvlakdienst zijn daarmee verschillende dingen: de eerste is gedrag van een component zoals de domeinarchitectuur het benoemt, de tweede het contract waarmee een component een deel van dat gedrag over een koppeling aanbiedt of afneemt.

## Ontwerpregels

**Eén aanbieder.** Alle endpoints van een koppeling staan in het OpenAPI-document van één component: de paden die het serveert en de meldingen die het verstuurt. De afnemer roept die paden aan en ontvangt de meldingen op het adres dat hij heeft geregistreerd. Daardoor is een koppeling precies één OpenAPI-document en één OEAPI-profiel. Vraagt een uitwisseling aan beide kanten endpoints, dan zijn het twee koppelingen. De prijs is dat melden en terugmelden in twee koppelingen staan die naar elkaar verwijzen, zoals [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md) en [Opleidingsaanbod aanmaken](opleidingsaanbod-aanmaken.md).

**Vereist in plaats van herhaald.** Een koppeling noemt onder *Vereist* de koppelingen waarop zij steunt; wie haar implementeert, implementeert die ook. Elke koppeling met meldingen steunt op [Afleverabonnement registreren](afleverabonnement-registreren.md) en [Reconciliatie](reconciliatie.md). Een OEAPI-profiel kan niet naar een ander profiel verwijzen en moet op zichzelf staan; het profiel van een koppeling neemt daarom de endpoints op van wat zij vereist.

**Velden vereisen, niet verbieden.** Verschillende koppelingen zetten dezelfde koppelvlakdienst in, en daarmee hetzelfde endpoint. Een koppeling mag velden van dat endpoint verplicht stellen, maar niet verbieden: twee profielen met tegengestelde eisen aan hetzelfde endpoint kan één implementatie niet allebei halen. Verschil per afnemer loopt via een parameter van het endpoint.

**Beveiliging.** Voor elk endpoint van elke koppeling geldt de [auth-standaard](../auth-standaard.md).

## Overzicht

| Afgeleid van | Koppeling | Aanbieder | Afnemer |
|---|---|---|---|
| *Onderwijsspecificatie uitwerking* | [Onderwijsspecificatie ophalen](onderwijsspecificatie-ophalen.md) | Onderwijscatalogus | Planningssysteem, Studentinformatiesysteem (SVS), Leermanagementsysteem, Studentkeuzesysteem |
| *Onderwijsspecificatie uitwerking* | [Specificatiestatus volgen](specificatiestatus-volgen.md) | Onderwijscatalogus | Planningssysteem, Leermanagementsysteem |
| *Onderwijsspecificatie uitwerking* | [Resultaatstructuur ophalen](resultaatstructuur-ophalen.md) | Onderwijscatalogus | Studentinformatiesysteem (SVS) |
| *Onderwijsspecificatie uitwerking* | [Specificatie aanpassen op verzoek](specificatie-aanpassen-op-verzoek.md) | Onderwijscatalogus | Planningssysteem |
| *Onderwijsspecificatie uitwerking* | [Keuzeaanbod ontsluiten](keuzeaanbod-ontsluiten.md) | Onderwijscatalogus | Studentkeuzesysteem |
| *Onderwijsspecificatie uitwerking* | [Inschrijfbaar aanbod ontsluiten](inschrijfbaar-aanbod-ontsluiten.md) | Onderwijscatalogus | Studentinformatiesysteem (KRS), EduHub, CAMBO |
| *Nominale route meerjaar uitwerking* | [Specificatie ter vaststelling aanbieden](specificatie-ter-vaststelling-aanbieden.md) | Onderwijscatalogus | Curriculum-ontwerptool |
| *(Meer)jaar capaciteitsplanning* | [Opleidingsaanbod aanmaken](opleidingsaanbod-aanmaken.md) | Planningssysteem | Onderwijscatalogus |
| *(Meer)jaar capaciteitsplanning* | [Opleidingsaanbod herplannen](opleidingsaanbod-herplannen.md) | Planningssysteem | Onderwijscatalogus |
| *(Meer)jaar capaciteitsplanning* | [Late wijziging toetsen](late-wijziging-toetsen.md) | Planningssysteem | Onderwijscatalogus |
| *(Meer)jaar capaciteitsplanning* | [Planningselementen ontsluiten](planningselementen-ontsluiten.md) | Planningssysteem | Onderwijscatalogus |
| *Periode planning* | [Geplande leergelegenheden ontsluiten](geplande-leergelegenheden-ontsluiten.md) | Planningssysteem | Studentkeuzesysteem |
| *Periode planning* | [Planninggroepen ontsluiten](planninggroepen-ontsluiten.md) | Planningssysteem | Roostersysteem |
| *Inschrijving op opleidingsprogramma* | [Plaatsingsgroepen ontsluiten](plaatsingsgroepen-ontsluiten.md) | Studentinformatiesysteem (KRS) | Planningssysteem |
| *Inschrijving op opleidingsprogramma* | [Opleidingsprogrammaverbintenis ontsluiten](opleidingsprogrammaverbintenis-ontsluiten.md) | Studentinformatiesysteem (KRS) | Studentkeuzesysteem, Leermanagementsysteem |
| *Keuze aanvraag beheer* | [Animo doorgeven](animo-doorgeven.md) | Studentkeuzesysteem | Planningssysteem |
| *Verwerken van definitieve keuzes* | [Plaatsing op lesgelegenheid aanvragen](plaatsing-op-lesgelegenheid-aanvragen.md) | Roostersysteem | Studentkeuzesysteem |
| *Verwerken van definitieve keuzes* | [Keuzeverbintenis vastleggen](keuzeverbintenis-vastleggen.md) | Studentkeuzesysteem | Studentinformatiesysteem (KRS) |
| *Verwerken van definitieve keuzes* | [Onderwijseenheidverbintenis doorgeven](onderwijseenheidverbintenis-doorgeven.md) | Studentkeuzesysteem | Studentinformatiesysteem (SVS) |
| *Verwerken van definitieve keuzes* | [Verbintenis en planninggroep doorgeven](verbintenis-en-planninggroep-doorgeven.md) | Studentkeuzesysteem | Leermanagementsysteem |
| Geen (roostersysteem) | [Leergelegenheden roosteren](leergelegenheden-roosteren.md) | Roostersysteem | Planningssysteem |
| Geen (roostersysteem) | [Geroosterde leergelegenheden ontsluiten](geroosterde-leergelegenheden-ontsluiten.md) | Roostersysteem | Studentkeuzesysteem |
| Geen (roostersysteem) | [Planninggroepen met studenten ontsluiten](planninggroepen-met-studenten-ontsluiten.md) | Roostersysteem | Studentinformatiesysteem (KRS) |
| Geen (leermanagementsysteem) | [Leeromgeving inrichten](leeromgeving-inrichten.md) | Leermanagementsysteem | Onderwijscatalogus |
| Geen (leermanagementsysteem) | [Leeromgeving bijwerken](leeromgeving-bijwerken.md) | Leermanagementsysteem | Onderwijscatalogus |
| Geen (leermanagementsysteem) | [Toetsresultaat doorgeven](toetsresultaat-doorgeven.md) | Leermanagementsysteem | Studentinformatiesysteem (SVS) |
| Geen (studentvolgsysteem) | [Nominaal template inrichten](nominaal-template-inrichten.md) | Studentinformatiesysteem (SVS) | Onderwijscatalogus |
| Geen (studentvolgsysteem) | [Examenplanwijziging toetsen](examenplanwijziging-toetsen.md) | Studentinformatiesysteem (SVS) | Onderwijscatalogus |
| Geen (ondersteunend) | [Afleverabonnement registreren](afleverabonnement-registreren.md) | Wie meldt | Wie ontvangt |
| Geen (ondersteunend) | [Reconciliatie](reconciliatie.md) | Wie meldde | Wie miste |
