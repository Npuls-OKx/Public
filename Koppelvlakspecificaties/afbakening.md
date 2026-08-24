# Afbakening

Waar dit pakket op staat, wat het moet kunnen en waar het ophoudt. De kaders leggen vast waarop de begrippen verankeren, de functionele eisen wat de keten van de koppelingen vraagt, en de scope wat er wel en niet in zit.

## 1. Kaders

De begrippen in dit pakket zijn niet vrij gekozen: elk conceptniveau verankert op het kwalificatiekader van de sector.

### 1.1 Ankertabel

De ankertabel zet de zes begrippenfamilies naast elkaar per niveau van het kwalificatiekader. Zij bepaalt welk begrip op welk niveau hoort en hoe de families zich tot elkaar verhouden: een specificatie beschrijft wat een instelling organiseert, een aanbod plaatst dat in tijd en met wie, een verbintenis bindt er een student aan, en een resultaat legt vast wat die student heeft behaald. Bron: [consumer-profiel](https://github.com/Npuls-OKx/meta/blob/d47bb0c74ec899a4384d06331692f74b9bd1db58/architecture/docs/specificatie/okx-oeapi-consumer-profiel/README.md), §3.2.6.

| 1. Kwalificatiekader | 2. Beoogde leeruitkomst | 3. Onderwijsspecificatie | 4. Onderwijsaanbod | 5. Onderwijsverbintenis | 6. Onderwijsresultaat |
|---|---|---|---|---|---|
| Kwalificatiedossier | N.v.t. op dit niveau: leeruitkomsten hangen lager in de boom | Opleidingsspecificatie | Opleidingsaanbod | Opleidingsverbintenis | Opleidingsverbintenis-resultaat |
| Kwalificatie | N.v.t. op dit niveau: aggregatie van onderliggende leeruitkomsten | Opleidingsprogramma-specificatie | Opleidingsprogramma-aanbod | Opleidingsprogramma-verbintenis | Opleidingsprogramma-verbintenis-resultaat |
| Kerntaak | Collectie van leeruitkomst-collecties, één per onderliggend werkproces | Onderwijseenheid-specificatie | Onderwijseenheid-aanbod | Onderwijseenheid-verbintenis | Onderwijseenheid-verbintenis-resultaat |
| Werkproces | Leeruitkomst-collectie | Leeronderdeel-specificatie | Leergelegenheid | Leergelegenheid-verbintenis | Leergelegenheid-verbintenis-resultaat |
| N.v.t. binnen het kwalificatiekader: eigen beleid van de instelling | Lesuitkomst, formatief, hangt onder een leeruitkomst | Lesspecificatie | Lesgelegenheid | Lesgelegenheid-verbintenis | Lesgelegenheid-verbintenis-resultaat |
| N.v.t. binnen het kwalificatiekader: toetsing | Scope van toetsing: een set leeruitkomsten en lesuitkomsten | Toetsonderdeel-specificatie | Toetsgelegenheid | Toetsgelegenheid-verbintenis | Toetsgelegenheid-verbintenis-resultaat |
| Doorgaand werkproces | Te behalen set leeruitkomsten, vastgesteld door de examencommissie | Examenonderdeel-specificatie | Examengelegenheid | Examengelegenheid-verbintenis | Examengelegenheid-verbintenis-resultaat |

Niet elk niveau uit deze tabel is in dit pakket uitgewerkt. De `specificatieType`-waarden die de schema's kennen, staan in [education-specification.json](Datamodelschema's/education-specification.json); de lesspecificatie valt buiten de scope (§3).

### 1.2 Aanbodniveaus

Elke aanbod-instantie instantieert precies één onderwijsspecificatie en verwijst via `specificatieVerwijzing` (specificatieId plus versie) naar de exacte versie waarop de planning is gebaseerd.

| Aanbodniveau (`aanbodType`) | Instantieert (specificatie) |
|---|---|
| `opleidingsaanbod` | `opleidingsspecificatie` |
| `opleidingsprogramma-aanbod` | `opleidingsprogrammaspecificatie` |
| `onderwijseenheid-aanbod` | `onderwijseenheidspecificatie` |
| `leergelegenheid` | `leeronderdeelspecificatie` |

### 1.3 Typen in de resultaatstructuur

De resultaatstructuur gebruikt dezelfde specificatiefamilie als de onderwijsspecificatie. Drie typen:

| Conceptniveau (`specificatieType`) | Rol |
|---|---|
| `examenplanspecificatie` | Wortel (OER). Scope, aggregatie richting diploma |
| `resultaateenheidspecificatie` | Groepering, meestal per kerntaak. Draagt weging en aggregatie |
| `toetsonderdeelspecificatie` | Blad. Het concrete toets- of examenonderdeel |

## 2. Eisen aan de keten

Wat de keten moet kunnen, los van een koppeling en los van een oplossing. Deze eisen geven de context: zij gelden voor elke koppeling die de onderwijscatalogus met een afnemend systeem verbindt. De scherpere, per koppeling geformuleerde functionele eisen zijn hiervan afgeleid en staan bij het interactiepatroon dat ze uitwerkt, zodat de keten eis → interactiepatroon → endpoint bij elkaar blijft. De functionele eisen zijn doorlopend genummerd over de koppelingen heen (`functionele-eis-0001` en verder), zodat elke eis één vaste verwijzing heeft. Ook de keten-eisen zelf dragen een id (`keten-eis-0001` tot en met `keten-eis-0005`) — een eigen soort naast de functionele eisen, omdat het een andere laag is: keten-breed in plaats van per koppeling. De tabel toont per keten-eis de afgeleide functionele eisen per koppeling; een cel "nog niet uitgewerkt" is een gat dat nog uitwerking vraagt.

| Id | Keten-eis | [Planning en roostering](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md) | [Studentinformatiesysteem](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md) | [Leermanagementsysteem](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md) |
|---|---|---|---|---|
| keten-eis-0001 | [Een vastgestelde specificatie bereikt elk systeem dat ermee werkt](#keten-eis-0001) | [functionele-eis-0001](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0001) | [functionele-eis-0008](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eis-0008) | [functionele-eis-0010](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0010) |
| keten-eis-0002 | [Elk systeem meldt terug wat het met de specificatie heeft gedaan](#keten-eis-0002) | [functionele-eis-0001](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0001) en [functionele-eis-0003](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0003) | [functionele-eis-0008](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eis-0008) | [functionele-eis-0010](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0010) en [functionele-eis-0011](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0011) |
| keten-eis-0003 | [Een wijziging werkt door zonder dat alles opnieuw wordt uitgewisseld](#keten-eis-0003) | [functionele-eis-0002](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0002) en [functionele-eis-0005](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0005) | nog niet uitgewerkt | [functionele-eis-0012](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0012) |
| keten-eis-0004 | [Een wijziging raakt lopende uitvoering niet ongecontroleerd](#keten-eis-0004) | [functionele-eis-0004](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0004) | [functionele-eis-0009](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eis-0009) | nog niet uitgewerkt |
| keten-eis-0005 | [Uitval kost geen informatie](#keten-eis-0005) | [functionele-eis-0006](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0006) en [functionele-eis-0007](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0007) | nog niet uitgewerkt | nog niet uitgewerkt |

<a id="keten-eis-0001"></a>

### 2.1 keten-eis-0001. Een vastgestelde specificatie bereikt elk systeem dat ermee werkt

De onderwijscatalogus is het distributiepunt: drie systemen zetten het onderwijs klaar en hebben elk een ander deel van dezelfde specificatie nodig. Zolang dat overzetten handwerk is, verschilt per instelling wat waar terechtkomt en is niet vast te stellen waarop een systeem zich heeft gebaseerd. De eis stuurt het patroon: de bezitter meldt, de afnemer haalt op wanneer het hem uitkomt ([U4](uitgangspunten.md#u4-notify-then-pull)).

Afgeleid: [functionele-eis-0001](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0001) bij planning en roostering, [functionele-eis-0008](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eis-0008) bij het studentinformatiesysteem en [functionele-eis-0010](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0010) bij het leermanagementsysteem.

<a id="keten-eis-0002"></a>

### 2.2 keten-eis-0002. Elk systeem meldt terug wat het met de specificatie heeft gedaan

Wie een gegeven bezit, bepaalt het ([U3](uitgangspunten.md#u3-resource-eigenaarschap)): de catalogus bezit de specificatie, maar niet het aanbod, niet de inrichting en niet de resultaten. Zonder terugmelding weet zij dus niet of het onderwijs klaarstaat, en kan zij niet naar het resultaat verwijzen. De terugmelding draagt daarom een referentie naar wat het afnemende systeem heeft gemaakt, en bij een mislukking de reden.

Afgeleid: [functionele-eis-0001](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0001) en [functionele-eis-0003](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0003) bij planning en roostering, [functionele-eis-0008](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eis-0008) bij het studentinformatiesysteem, [functionele-eis-0010](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0010) en [functionele-eis-0011](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0011) bij het leermanagementsysteem.

<a id="keten-eis-0003"></a>

### 2.3 keten-eis-0003. Een wijziging werkt door zonder dat alles opnieuw wordt uitgewisseld

Een specificatie verandert nadat een afnemer zich erop heeft ingericht. De afnemer moet die wijziging kunnen volgen zonder dat de hele structuur opnieuw over de lijn gaat, en moet kunnen zien waarop hij zich baseerde: daar zijn de versionering en het manifest voor ([regels bij de schema's](Datamodelschema's/README.md#regels-bij-de-schemas)). Ook een statuswijziging die geen nieuwe versie oplevert hoort door te komen.

Afgeleid: [functionele-eis-0002](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0002) en [functionele-eis-0005](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0005) bij planning en roostering en [functionele-eis-0012](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eis-0012) bij het leermanagementsysteem.

<a id="keten-eis-0004"></a>

### 2.4 keten-eis-0004. Een wijziging raakt lopende uitvoering niet ongecontroleerd

Zodra een planning is afgerond of er verbintenissen lopen, is een wijziging niet meer vrijblijvend: er hangen roosters, inschrijvingen en resultaatafspraken aan. De keten moet zo'n wijziging langs een acceptatietoets leiden in plaats van hem stilzwijgend door te voeren. Voor het examenplan gelden de strengste regels, omdat het een contractuele afspraak met de student is.

Afgeleid: [functionele-eis-0004](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0004) bij planning en roostering en [functionele-eis-0009](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eis-0009) bij het studentinformatiesysteem.

<a id="keten-eis-0005"></a>

### 2.5 keten-eis-0005. Uitval kost geen informatie

Een bericht kan wegvallen. De keten moet daar tegen kunnen: de informatie moet alsnog op te halen zijn zonder op een herhaalde aflevering te wachten, en het afleveradres moet vastliggen voordat er iets wordt afgeleverd. Welke eigenschappen het afleverkanaal daarvoor moet hebben staat in [ADR 0018](../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md).

Afgeleid: [functionele-eis-0006](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0006) en [functionele-eis-0007](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eis-0007) bij planning en roostering. Voor de koppelingen met het studentinformatiesysteem en het leermanagementsysteem is deze eis nog niet in functionele eisen uitgewerkt; beide documenten stellen vast dat reconciliatie en abonnementenbeheer daar nog ontbreken.

## 3. Scope

In scope zijn de drie koppelingen vanuit de onderwijscatalogus: naar planning en roostering, naar het studentinformatiesysteem en naar het leermanagementsysteem. Alles is uitgewerkt binnen één instelling ([ADR 0008](../Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md)), voor leerroute 1 tot en met 3, waarbij leerroute 1 is uitgewerkt en 2 en 3 als verschil daarop worden beschreven.

Daarbuiten vallen:

- **De koppelingen van het roostersysteem, het studentkeuzesysteem en de curriculum-ontwerptool.** Die systemen horen bij de keten en staan beschreven bij de [applicatiecomponenten](Applicatiecomponenten/README.md), maar dit pakket specificeert hun koppelingen niet.
- **Uitwisseling tussen instellingen.** Eerst de keten binnen één instelling.
- **Uitvoering en beoordeling**: afname, behaalde resultaten en het examendossier horen bij het examendomein OKE.
- **Het lesniveau.** De `lesspecificatie` leeft in het leermanagementsysteem en wordt hier niet gerealiseerd.
- **Generieke onderdelen** (taal, rekenen, burgerschap, Engels), die een eigen wettelijk regime kennen.
