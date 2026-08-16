# Afbakening

Waar dit pakket op staat, wat het moet kunnen en waar het ophoudt. De kaders leggen vast waarop de begrippen verankeren, de functionele eisen wat de keten van de koppelingen vraagt, en de scope wat er wel en niet in zit.

## 1. Kaders

De begrippen in dit pakket zijn niet vrij gekozen: elk conceptniveau heeft een bron in het kwalificatiekader van de sector, en sluit waar mogelijk aan op de Open Onderwijs API. Deze tabellen leggen die verankering vast.

### 1.1 Conceptniveaus van de onderwijsspecificatie

| Conceptniveau (`specificatieType`) | Bron in kwalificatiekader          | OEAPI-mapping (indicatief)        |
| ---------------------------------- | ---------------------------------- | --------------------------------- |
| `opleidingsspecificatie`           | Kwalificatiedossier                | EducationSpecification (program)  |
| `opleidingsprogrammaspecificatie`  | Kwalificatie                       | Programme                         |
| `onderwijseenheidspecificatie`     | Kerntaak                           | Course                            |
| `leeronderdeelspecificatie`        | Werkproces                         | LearningComponent                 |
| `keuzedeelruimtespecificatie`      | ruimte binnen kwalificatie         | (afgeleid, geen 1:1 OEAPI-object) |
| `toetsonderdeelspecificatie`       | toetsing                           | TestComponent                     |
| `examenplanspecificatie`           | OER, summatieve resultaatstructuur | (aparte uitwerking)               |
| `resultaateenheidspecificatie`     | groepering binnen het examenplan   | (aparte uitwerking)               |
| `lesspecificatie` (buiten scope)   | beleid instelling                  | LearningComponent (lesson)        |

De **kwalificatie ligt niet op root-niveau**: de `opleidingsspecificatie` verankert op de leeruitkomst van het kwalificatiedossier (23450), de `opleidingsprogrammaspecificatie` op die van de kwalificatie (27141).

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

| Conceptniveau (`specificatieType`) | Rol | OEAPI-mapping (indicatief) |
|---|---|---|
| `examenplanspecificatie` | Wortel (OER). Scope, aggregatie richting diploma | (geen 1:1 OEAPI-object) |
| `resultaateenheidspecificatie` | Groepering, meestal per kerntaak. Draagt weging en aggregatie | (geen 1:1 OEAPI-object) |
| `toetsonderdeelspecificatie` | Blad. Het concrete toets- of examenonderdeel | TestComponent |

## 2. Eisen aan de keten

Wat de keten moet kunnen, los van een koppeling en los van een oplossing. Deze eisen geven de context: zij gelden voor elke koppeling die de onderwijscatalogus met een afnemend systeem verbindt. De scherpere, per koppeling geformuleerde functionele eisen zijn hiervan afgeleid en staan bij het interactiepatroon dat ze uitwerkt, zodat de keten eis → interactiepatroon → endpoint bij elkaar blijft.

### 2.1 K1. Een vastgestelde specificatie bereikt elk systeem dat ermee werkt

De onderwijscatalogus is het distributiepunt: drie systemen zetten het onderwijs klaar en hebben elk een ander deel van dezelfde specificatie nodig. Zolang dat overzetten handwerk is, verschilt per instelling wat waar terechtkomt en is niet vast te stellen waarop een systeem zich heeft gebaseerd. De eis stuurt het patroon: de bezitter meldt, de afnemer haalt op wanneer het hem uitkomt ([U4](uitgangspunten.md#u4-notify-then-pull)).

Afgeleid: FR1 bij [planning en roostering](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eisen), FR1 bij [het studentinformatiesysteem](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eisen) en FR1 bij [het leermanagementsysteem](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eisen).

### 2.2 K2. Elk systeem meldt terug wat het met de specificatie heeft gedaan

Wie een gegeven bezit, bepaalt het ([U3](uitgangspunten.md#u3-resource-eigenaarschap)): de catalogus bezit de specificatie, maar niet het aanbod, niet de inrichting en niet de resultaten. Zonder terugmelding weet zij dus niet of het onderwijs klaarstaat, en kan zij niet naar het resultaat verwijzen. De terugmelding draagt daarom een referentie naar wat het afnemende systeem heeft gemaakt, en bij een mislukking de reden.

Afgeleid: FR1 en FR3 bij [planning en roostering](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eisen), FR1 bij [het studentinformatiesysteem](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eisen), FR1 en FR2 bij [het leermanagementsysteem](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eisen).

### 2.3 K3. Een wijziging werkt door zonder dat alles opnieuw wordt uitgewisseld

Een specificatie verandert nadat een afnemer zich erop heeft ingericht. De afnemer moet die wijziging kunnen volgen zonder dat de hele structuur opnieuw over de lijn gaat, en moet kunnen zien waarop hij zich baseerde: daar zijn de versionering en het manifest voor ([regels bij de schema's](Datamodelschema's/README.md#regels-bij-de-schemas)). Ook een statuswijziging die geen nieuwe versie oplevert hoort door te komen.

Afgeleid: FR2 en FR5 bij [planning en roostering](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eisen) en FR3 bij [het leermanagementsysteem](Interactiepatronen/onderwijscatalogus-leermanagementsysteem.md#functionele-eisen).

### 2.4 K4. Een wijziging raakt lopende uitvoering niet ongecontroleerd

Zodra een planning is afgerond of er verbintenissen lopen, is een wijziging niet meer vrijblijvend: er hangen roosters, inschrijvingen en resultaatafspraken aan. De keten moet zo'n wijziging langs een acceptatietoets leiden in plaats van hem stilzwijgend door te voeren. Voor het examenplan gelden de strengste regels, omdat het een contractuele afspraak met de student is.

Afgeleid: FR4 bij [planning en roostering](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eisen) en FR2 bij [het studentinformatiesysteem](Interactiepatronen/onderwijscatalogus-studentinformatiesysteem.md#functionele-eisen).

### 2.5 K5. Uitval kost geen informatie

Een bericht kan wegvallen. De keten moet daar tegen kunnen: de informatie moet alsnog op te halen zijn zonder op een herhaalde aflevering te wachten, en het afleveradres moet vastliggen voordat er iets wordt afgeleverd. Welke eigenschappen het afleverkanaal daarvoor moet hebben staat in [ADR 0018](../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md).

Afgeleid: FR6 en FR7 bij [planning en roostering](Interactiepatronen/onderwijscatalogus-planning-en-roostering.md#functionele-eisen). Voor de koppelingen met het studentinformatiesysteem en het leermanagementsysteem is deze eis nog niet in functionele eisen uitgewerkt; beide documenten stellen vast dat reconciliatie en abonnementenbeheer daar nog ontbreken.

## 3. Scope

In scope zijn de drie koppelingen vanuit de onderwijscatalogus: naar planning en roostering, naar het studentinformatiesysteem en naar het leermanagementsysteem. Alles is uitgewerkt binnen één instelling ([ADR 0008](../Referentiemateriaal/adr/0008-scope-planning-eerst-intra-instelling.md)), voor leerroute 1 tot en met 3, waarbij leerroute 1 is uitgewerkt en 2 en 3 als verschil daarop worden beschreven.

Daarbuiten vallen:

- **De koppelingen van het roostersysteem, het studentkeuzesysteem en de curriculum-ontwerptool.** Die systemen horen bij de keten en staan beschreven bij de [applicatiecomponenten](Applicatiecomponenten/README.md), maar dit pakket specificeert hun koppelingen niet.
- **Uitwisseling tussen instellingen.** Eerst de keten binnen één instelling.
- **Uitvoering en beoordeling**: afname, behaalde resultaten en het examendossier horen bij het examendomein OKE.
- **Het lesniveau.** De `lesspecificatie` leeft in het leermanagementsysteem en wordt hier niet gerealiseerd.
- **Generieke onderdelen** (taal, rekenen, burgerschap, Engels), die een eigen wettelijk regime kennen.
