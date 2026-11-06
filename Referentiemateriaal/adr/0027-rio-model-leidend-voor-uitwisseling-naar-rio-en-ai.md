## Het RIO-model leidend voor de uitwisseling naar RIO en Aanmelden en Inschrijven

Status: Voorstel

Datum: 2026-11-04

### Context

Een instelling meldt haar onderwijsaanbod aan bij het Register Instellingen en Opleidingen (RIO) en stelt het beschikbaar voor Aanmelden, Intekenen en Inschrijven (AII) of het huidige CAMBO. Vandaag wordt die informatie in de praktijk samengesteld vanuit het studentinformatiesysteem: dat systeem staat centraal in het landschap, en de koppelingen naar RIO en CAMBO worden daaruit gerealiseerd. De vorm van wat er uitgaat volgt dan de interne structuur van die leverancier, en elke instelling krijgt een eigen vertaling tussen haar aanbod en wat het register verwacht.

De onderwijscatalogus is in het OKx-landschap de plek waar het onderwijsaanbod ontstaat en waar het aanmeld- en inschrijfbare aanbod vandaan komt. Dat de catalogus bron is voor de kernregistratie bestaat vandaag nog niet; OKx introduceert dat. Daarmee ligt de vraag open welke vorm het aanbod krijgt op weg naar RIO en AI, en wie die vorm bepaalt.

RIO is zelf een uitwisselingsstandaard. Er ligt dus al een vastgestelde, landelijk beheerde beschrijving van wat een opleiding, een aanbod en een locatie zijn.

Relateert aan [meta-issue 513](https://github.com/Npuls-OKx/meta/issues/513) en [meta-issue 436](https://github.com/Npuls-OKx/meta/issues/436).

### Beslissing

1. **Het RIO-model is leidend** voor de gegevensuitwisseling richting RIO en richting Aanmelden en Inschrijven. OKx beschrijft die uitwisseling in de begrippen en de structuur van RIO, en niet in een eigen vorm die daarna vertaald moet worden.
2. **De onderwijscatalogus levert die informatie aan.** Het aanbod ontstaat daar, en daarmee is de catalogus de bron voor wat naar het register gaat. Het studentinformatiesysteem blijft de bron voor de persoon, de verbintenis en de bekostigingsverantwoording.
3. **Waar een OKx-begrip en een RIO-begrip uiteenlopen, is dat een signalering richting RIO** en geen eigen afwijking in de uitwisseling. Dat volgt de lijn die OKx ook richting de Open Education API hanteert.

De onderbouwing is dat een interne vorm gebruiken onlogisch is zolang er een correcte implementatie voor uitwisseling bestaat. Elke eigen vorm levert een vertaalslag op die per instelling en per leverancier anders uitpakt, en die vertaalslag is precies wat OKx wil wegnemen.

### Alternatieven

- **Het studentinformatiesysteem blijft samenstellen, zoals vandaag.** Dat vraagt geen verandering van de praktijk en houdt de bestaande koppelingen intact. Het houdt echter in stand dat de vorm per leverancier verschilt, en het legt de verantwoordelijkheid voor het aanbod bij een systeem dat het aanbod niet maakt.
- **OKx beschrijft een eigen uitwisselingsvorm en vertaalt die naar RIO.** Dat geeft ruimte om begrippen te gebruiken die binnen de keten al zijn vastgelegd. Het levert een tweede model op dat onderhouden moet worden, en bij elke wijziging van RIO een vertaling die kan verschuiven.

### Consequenties

- De koppeling van de onderwijscatalogus richting RIO en AI wordt beschreven in RIO-begrippen. Dat raakt de interactieketen onderwijsaanbod en de bijbehorende payload.
- CAMBO wordt uitgefaseerd en vervangen door Aanmelden en Inschrijven. RIO blijft bestaan voor het registreren van onderwijsaanbod en locaties. De hoofdplaat informatiestromen toont die drie vandaag nog als een groep; die groep beweegt mee met die uitfasering.
- De aanmeldmodule heeft meer nodig dan de kernregistratie: daar speelt capaciteit wel een rol. Die informatie loopt via dezelfde lijn naar RIO en AI, en niet via de kernregistratie.
- Een instelling die haar aanbod vandaag vanuit het studentinformatiesysteem aanmeldt, verlegt die route naar de onderwijscatalogus. Dat is een migratie, geen configuratie.
- Een leverancier van een onderwijscatalogus krijgt er een uitgaande koppeling bij; een leverancier van een studentinformatiesysteem verliest er een.

### Relaties en links

- Issues: [meta 513](https://github.com/Npuls-OKx/meta/issues/513), [meta 436](https://github.com/Npuls-OKx/meta/issues/436), [meta 314](https://github.com/Npuls-OKx/meta/pull/314)
- Herkomst: sparsessie PR 314, deel 2, OKx-interactieketens en gegevensuitwisseling, 4 november 2026
- Verwante besluiten: [ADR 0008](0008-scope-planning-eerst-intra-instelling.md) over de fasering tussen instellingen
