# Onderwijsaanbod als JSON-payload

## Inhoudsopgave

1. [Inleiding](#1-inleiding) (aanleiding, context, doel, scope)
2. [Payload](#2-payload)
3. [Toelichting bij de keuzes](#3-toelichting-bij-de-keuzes)

## 1. Inleiding

### 1.1 Aanleiding en context

**Aanleiding.** De koppelingspecificatie OC naar P&R legt vast dat het planningssysteem het aanbod bezit en over de koppeling alleen een referentie meldt. Daarmee bleef open wat een opvrager terugkrijgt zodra hij dat aanbod daadwerkelijk ophaalt. Dit document beschrijft die inhoud, zodat de afspraak over de koppeling ook uitvoerbaar is.

Het planningssysteem vertaalt een gepubliceerde onderwijsspecificatie naar **onderwijsaanbod**: wanneer wordt het onderwijs gegeven, waar, met welke groepen en door welk team. De [koppelingspecificatie onderwijscatalogus naar planning en roostering](onderwijscatalogus-planning-en-roostering.md) legt vast dat het planningssysteem dat aanbod bezit en alleen een referentie (uuid) over de koppeling meldt. Dit document beschrijft wat een opvrager terugkrijgt wanneer die het aanbod vervolgens ophaalt.

Het aanbod is de vierde begrippenfamilie uit de ankertabel: de specificatie zegt wat we organiseren, het aanbod zegt wanneer en met wie. Elke aanbod-instantie instantieert precies één onderwijsspecificatie en verwijst via `specificatieVerwijzing` (specificatieId plus versie) naar de exacte versie waarop de planning is gebaseerd.

| Aanbodniveau (`aanbodType`) | Instantieert (specificatie) |
|---|---|
| `opleidingsaanbod` | `opleidingsspecificatie` |
| `opleidingsprogramma-aanbod` | `opleidingsprogrammaspecificatie` |
| `onderwijseenheid-aanbod` | `onderwijseenheidspecificatie` |
| `leergelegenheid` | `leeronderdeelspecificatie` |

Scenario is leerroute 1 (regulier), persona [Jochem](https://github.com/Npuls-OKx/meta/blob/d47bb0c74ec899a4384d06331692f74b9bd1db58/architecture/docs/specificatie/okx-oeapi-consumer-profiel/doc/persona_jochem.md). Ketenoverzicht en begrippen: de [instap in de README](../../README.md#context).

### 1.2 Doel

Dit document beantwoordt drie vragen:

- Welke velden draagt een aanbod-instantie, en hoe verwijst die naar de onderliggende specificatie?
- Hoe leggen we locatie en organisatie vast zonder per organisatievorm een eigen model te maken?
- Hoe meldt het planningssysteem dat een planning niet realiseerbaar is, en waarom?

Geslaagd wanneer een leverancier de payload kan bouwen en lezen zonder aanvullende uitleg, en wanneer de knelpuntcodes een planner voldoende houvast geven om te weten wat er misgaat.

De payload is indicatief en onderbouwend, geen voorschrift aan de sector ([uitgangspunt U1](../../uitgangspunten.md#u1-indicatief-en-onderbouwend-niet-voorschrijvend)).

### 1.3 Scope

In scope is het aanbod op **planniveau**: periodes, locaties, groepen, uitvoerend team, en de uitkomst van het planproces. Uitgewerkt voor leerroute 1; leerroute 2 en 3 volgen als verschil ten opzichte daarvan.

Twee afbakeningen die anders verwarring geven:

- **Roosterniveau** (dag, tijdstip, lokaaltoewijzing per les) hoort bij het roostersysteem, niet bij dit document.
- **Personen** komen alleen als verwijzing (uuid) voor. Namen, inzet en beschikbaarheid horen in de personeelssystemen; dataminimalisatie is hier dus een ontwerpeis en geen open kwestie.

Al het overige valt buiten dit document.

## 2. Payload

Het bijbehorende [informatiemodel](../../Datamodelschema's/README.md#onderwijsaanbod) en de [voorbeeldpayload](../../Datamodelschema's/README.md#voorbeeld-onderwijsaanbod) staan bij de datamodelschema's. De knelpuntcodes staan toegelicht in [§3.4](#34-knelpunten-plannen-als-constraint-satisfaction-problem).

Het schema legt de exacte vorm vast: welke velden er zijn, welke verplicht zijn en welke waarden een veld mag dragen. Het is **alfa en indicatief** en verandert mee zolang de payload nog niet vaststaat.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://okx.npuls.nl/schema/onderwijsaanbod/alfa",
  "title": "Onderwijsaanbod",
  "$comment": "Alfa en indicatief. Deze vorm onderbouwt welke velden het koppelvlak nodig heeft en kan wijzigen zolang de payload niet is vastgesteld.",
  "type": "object",
  "required": ["aanbodInstanties"],
  "properties": {
    "aanbodInstanties": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "aanbodType", "versie", "bovenliggendAanbodId", "specificatieVerwijzing", "naam", "status"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "aanbodType": { "enum": ["opleidingsaanbod", "opleidingsprogramma-aanbod", "onderwijseenheid-aanbod", "leergelegenheid"] },
          "versie": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" },
          "bovenliggendAanbodId": { "type": ["string", "null"], "format": "uuid" },
          "specificatieVerwijzing": {
            "type": "object",
            "required": ["specificatieId", "versie"],
            "properties": {
              "specificatieId": { "type": "string", "format": "uuid" },
              "versie": { "type": "string" }
            }
          },
          "naam": { "type": "string" },
          "status": { "enum": ["inPlanning", "gepland", "nietRealiseerbaar", "geannuleerd"] },
          "knelpunten": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["code", "omschrijving"],
              "properties": {
                "code": { "type": "string" },
                "omschrijving": { "type": "string" },
                "betrokkenSpecificatieIds": { "type": "array", "items": { "type": "string" } }
              }
            }
          },
          "cohort": { "type": "string" },
          "periode": {
            "type": "object",
            "properties": {
              "start": { "type": "string", "format": "date" },
              "eind": { "type": "string", "format": "date" }
            }
          },
          "minAantalStudenten": { "type": "integer" },
          "maxAantalStudenten": { "type": "integer" },
          "locatieId": { "type": "string", "format": "uuid" },
          "uitvoerendTeamId": { "type": "string", "format": "uuid" },
          "groepen": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["id", "naam"],
              "properties": {
                "id": { "type": "string", "format": "uuid" },
                "naam": { "type": "string" },
                "capaciteit": { "type": "integer" }
              }
            }
          }
        }
      }
    },
    "locaties": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "locatieType", "naam"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "locatieType": { "enum": ["campus", "vestiging", "gebouw", "ruimte", "balie", "adres", "geopunt", "virtueel"] },
          "naam": { "type": "string" },
          "valtBinnenLocatieId": { "type": ["string", "null"], "format": "uuid" },
          "adres": { "type": "object" },
          "geolocatie": { "type": "object" },
          "verdieping": { "type": "string" },
          "vleugel": { "type": "string" },
          "url": { "type": "string" },
          "codes": { "type": "array", "items": { "type": "object" } }
        }
      }
    },
    "organisatieEenheden": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "eenheidType", "naam"],
        "properties": {
          "id": { "type": "string", "format": "uuid" },
          "eenheidType": { "type": "string", "$comment": "open lijst: instelling, sector, college, afdeling, onderwijsteam" },
          "naam": { "type": "string" },
          "bovenliggendeEenheidId": { "type": ["string", "null"], "format": "uuid" },
          "professionalIds": { "type": "array", "items": { "type": "string", "format": "uuid" } }
        }
      }
    }
  }
}
```

De knelpuntcodes staan toegelicht in [§3.4](#34-knelpunten-plannen-als-constraint-satisfaction-problem).

## 3. Toelichting bij de keuzes

### 3.1 Ontwerpkeuzes

- **Volledig Nederlands.** Veldnamen volgen het semantisch kader. De binding met de Open Onderwijs API is een aparte stap.
- **Plat met verwijzingen.** De objecten staan in platte lijsten (`aanbodInstanties`, `locaties`, `organisatieEenheden`) en de samenhang loopt via id-verwijzingen (`bovenliggendAanbodId`, `locatieId`, `uitvoerendTeamId`, `valtBinnenLocatieId`, `bovenliggendeEenheidId`) in plaats van via fysieke nesting. Dat maakt elk object los adresseerbaar en los te versioneren, en voorkomt dat je een halve boom moet meesturen om één les te wijzigen. De prijs is dat de hiërarchie niet meer uit de JSON zelf blijkt; daarom staat er een instantieboom bij.
- **Zelfde mechaniek als de specificatie-payload.** Uuid's, `versie` (semver), identiteit los van versie, en dezelfde recursie via een ouder-verwijzing.
- **Status en knelpunten op de instantie.** De uitkomst van het planproces leeft op de aanbod-instantie zelf, met knelpuntcodes (§3.4).
- **Groepen als koppeling.** Een groep hangt aan een `leergelegenheid` of `onderwijseenheid-aanbod` en maakt de combinatie specificatie, locatie en periode herkenbaar.

### 3.2 Locatiemodel

Geïnspireerd op het voorstel voor betere locatie-ondersteuning in de Open Onderwijs API ([issue 635](https://github.com/open-education-api/specification/issues/635)), hier uitgedrukt in het eigen semantisch kader:

- **Eén locatietype voor elke korrelgrootte.** Eén object `locatie` met een `locatieType`: van campus tot ruimte, en ook virtueel. Geen apart model per niveau.
- **Recursieve plaatsing via verwijzing.** `valtBinnenLocatieId` drukt de ruimtelijke hiërarchie uit: ruimte binnen gebouw, gebouw binnen vestiging, vestiging binnen campus.
- **Adres en geopunt naast elkaar.** Een locatie kan een adres dragen en daarnaast, onafhankelijk, een geografisch punt.
- **Virtuele locaties zijn volwaardig.** Een online leeromgeving of videoles krijgt `locatieType: virtueel` met een `url`.
- **Codes voor herkenbaarheid.** `codes` draagt externe identificaties, bijvoorbeeld een vestigingscode.

### 3.3 Organisatie-inrichting

Een aanbod wordt uitgevoerd door een team, en planning heeft dat team nodig om te weten of het aanbod haalbaar is. Daarom draagt de payload een minimale organisatiestructuur, met het organogram uit het OEAPI consumer-profiel als indicatie: instelling, daarbinnen sectoren of colleges, daarbinnen onderwijsteams.

- `organisatieEenheden` is een platte lijst met `eenheidType` en `bovenliggendeEenheidId`, hetzelfde recursiepatroon als de rest.
- Een aanbod-instantie verwijst via `uitvoerendTeamId` naar het team dat het aanbod draagt.
- Professionals hangen aan het team als `professionalIds`, alleen uuid's. Inzet, beschikbaarheid en competenties leven in het plan-van-inzetsysteem, buiten deze koppeling.

### 3.4 Knelpunten: plannen als constraint satisfaction problem

Plannen is op te vatten als een constraint satisfaction problem (CSP): variabelen (leergelegenheden maal periodes maal middelen) krijgen een waarde binnen randvoorwaarden (constraints) uit de specificatie (studielast, tijdsverdeling, voorwaarden vooraf, keuzeregels), de organisatie (teamcapaciteit, expertise), de infrastructuur (ruimtetypen, locaties) en de kalender (lesweken, urennorm). "Niet realiseerbaar" betekent: een of meer constraints zijn onvervulbaar. De knelpuntcode benoemt de geschonden constraint-categorie, met de betrokken specificaties erbij.

Eerste aanzet voor de codes (concept):

| Code | Geschonden constraint | Voorbeeld |
|---|---|---|
| `capaciteitTekort` | Inzetbare uren van team of professionals | 4 groepen vragen 960 contacturen, 666 beschikbaar |
| `expertiseTekort` | Vereist expertiseprofiel ontbreekt | Geen docent met profiel farmaceutische zorg |
| `ruimteTekort` | Ruimtetype of ruimtecapaciteit ontoereikend | Geen praktijklokaal beschikbaar in de periode |
| `locatieConflict` | Zelfde ruimte gelijktijdig dubbel nodig | Twee opleidingen claimen lokaal 2.14 in dezelfde weken |
| `volgordeConflict` | Voorwaarde vooraf past niet in de periodes | Wiskunde 1 en Ruimtelijk inzicht passen niet na elkaar binnen het jaar |
| `regelConflict` | Keuzeregels (regelset) onvervulbaar | De regelset sluit alle kiesbare keuzedelen uit |
| `groepsgrootteConflict` | Minimum of maximum aantal studenten | Prognose blijft onder het minimum |
| `kalenderConflict` | Urennorm of lesweken passen niet | Vereiste begeleide uren passen niet in de beschikbare weken |

Deze tabel is een aanzet; de genormeerde codelijst met foutmodel (structuur, ernst, herstelacties) staat als open punt in §4.
