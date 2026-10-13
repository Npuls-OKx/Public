# Logisch gegevensmodel

Per begrippenfamilie de entiteiten, hun velden en hun onderlinge relaties, onafhankelijk van de techniek waarin ze worden uitgewisseld. Wat een diagram niet kan uitdrukken staat in [regels bij de schema's](regels.md); de technische vorm die hieruit volgt staat in de [schema's](schemas/).

## Onderwijsspecificatie

Alle specificaties zijn hetzelfde objecttype, gespecialiseerd via `specificatieType`. In het informatiemodel hieronder betekent `onderdeel_van` additief (de studielast telt op) en `variant_van` alternatief (een keuze tussen varianten, geen optelling). Elke entiteit draagt daarnaast `versie` (semver); dat is voor de leesbaarheid niet in elke box herhaald.

```mermaid
erDiagram
    OPLEIDINGSSPECIFICATIE ||--o{ OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG : variant_van
    OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG ||--o{ OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP : variant_van
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP ||--o{ ONDERWIJSEENHEIDSPECIFICATIE : onderdeel_van
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP ||--|| KEUZEDEELRUIMTESPECIFICATIE : bevat
    ONDERWIJSEENHEIDSPECIFICATIE ||--o{ LEERONDERDEELSPECIFICATIE : onderdeel_van
    KEUZEDEELRUIMTESPECIFICATIE }o--o{ REGELSET : regelsetVerwijzingen
    REGELSET }o--o{ KEUZEDEELPROGRAMMASPECIFICATIE : kiesbaar
    REGELSET }o--o{ LEERUITKOMST : "stelt deelname-voorwaarden in behaalde leeruitkomsten"
    KEUZEDEELPROGRAMMASPECIFICATIE ||--o{ ONDERWIJSEENHEIDSPECIFICATIE : onderdeel_van

    OPLEIDINGSSPECIFICATIE }o--|| LEERUITKOMST : "verankert op"
    OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG }o--|| LEERUITKOMST : "verankert op"
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP }o--|| LEERUITKOMST : "verankert op"
    ONDERWIJSEENHEIDSPECIFICATIE }o--|| LEERUITKOMST : "verankert op"
    LEERONDERDEELSPECIFICATIE }o--|| LEERUITKOMST : "verankert op"
    KEUZEDEELPROGRAMMASPECIFICATIE }o--|| LEERUITKOMST : "verankert op"
    LEERUITKOMST ||--o{ LEERUITKOMST : "aggregeert bottom-up en top-down"
    LEERUITKOMST {
        uuid id PK
        string versie "eigen lifecycle"
        string naam
        object bron "standaard (nu sbb-kwalificatiekader, later bv. competentnl) + type + code"
        uuid bovenliggendLeeruitkomstId FK "recursief, orde van grootte per niveau"
        string waardedocument "diploma, certificaat, later microcredential"
        array indicatieveOmvang "SBU en/of EC naast elkaar ([ADR 0004](../Referentiemateriaal/adr/0004-leeruitkomsten-sbu-ec-logistieke-containergrootte.md))"
        string omschrijving "optioneel, per gebruiksprofiel"
        string resultaat "optioneel"
        array gedrag "optioneel"
        int nlqfNiveau
    }
    OPLEIDINGSSPECIFICATIE {
        uuid id PK
        string specificatieType "opleidingsspecificatie"
        uuid bovenliggendSpecificatieId "null"
        uuid leeruitkomstId FK "sleutel naar leeruitkomst"
        string naam
        string curriculumtype
        string versie
        date geldigVanaf
        date geldigTot
        object studielast "waarde + SBU"
        array manifest "pins: id + version + relatie"
        string status
    }
    OPLEIDINGSPROGRAMMASPECIFICATIE_LEERWEG {
        uuid id PK
        string specificatieType "opleidingsprogrammaspecificatie"
        uuid bovenliggendSpecificatieId FK "opleiding"
        uuid leeruitkomstId FK "sleutel naar leeruitkomst"
        string programmaLaag "leerweg"
        string leerweg "BOL of BBL"
        string programmatype "diplomaprogramma"
        object studielast
    }
    OPLEIDINGSPROGRAMMASPECIFICATIE_DOELGROEP {
        uuid id PK
        string specificatieType "opleidingsprogrammaspecificatie"
        uuid bovenliggendSpecificatieId FK "leerweg-programma"
        uuid leeruitkomstId FK "sleutel naar leeruitkomst"
        string programmaLaag "doelgroep"
        string doelgroep "regulier, zijinstromer, hybride, organisatiespecifiek"
        string leerweg
        string curriculumtype
        object organisatie "optioneel, bv. Ziekenhuis 12"
        string cohort
        date startdatum
        date geldigVanaf
        date geldigTot
        object studielast
        array manifest "pins: id + version + relatie"
    }
    ONDERWIJSEENHEIDSPECIFICATIE {
        uuid id PK
        string specificatieType "onderwijseenheidspecificatie"
        uuid bovenliggendSpecificatieId FK "programma of keuzedeelprogramma"
        uuid leeruitkomstId FK "sleutel naar leeruitkomst"
        string naam
        object studielast
    }
    LEERONDERDEELSPECIFICATIE {
        uuid id PK
        string specificatieType "leeronderdeelspecificatie"
        uuid bovenliggendSpecificatieId FK "onderwijseenheid"
        uuid leeruitkomstId FK "sleutel naar leeruitkomst"
        string naam
        string tijdsverdeling "BOT of OOT"
        object studielast
    }
    KEUZEDEELRUIMTESPECIFICATIE {
        uuid id PK
        string specificatieType "keuzedeelruimtespecificatie"
        uuid bovenliggendSpecificatieId FK "doelgroep-programma"
        object studielast "keuzeruimte in SBU"
        array regelsetVerwijzingen FK "naar REGELSET"
    }
    KEUZEDEELPROGRAMMASPECIFICATIE {
        uuid id PK
        string specificatieType "opleidingsprogrammaspecificatie"
        uuid bovenliggendSpecificatieId "null, zelfstandig"
        uuid leeruitkomstId FK "sleutel naar leeruitkomst"
        string programmatype "keuzedeelprogramma"
        string keuzedeelKlasse "algemeen-verbredend of beroepsspecifiek-verdiepend"
        object studielast
    }
    REGELSET {
        uuid id PK
        string naam
        uuid vanToepassingOp FK "keuzedeelruimte"
        array regels "kiesbaar + voorwaardeVooraf in behaalde leeruitkomsten"
    }
```

Het model toont de relatie tussen specificatie en leeruitkomst als veel-op-veel. De payload implementeert dat voorlopig als één `leeruitkomstId` per specificatie; een array-vorm is nog niet uitgewerkt.

## Onderwijsaanbod

```mermaid
erDiagram
    AANBODINSTANTIE ||--o{ AANBODINSTANTIE : bovenliggendAanbodId
    AANBODINSTANTIE }o--|| ONDERWIJSSPECIFICATIE : specificatieVerwijzing
    AANBODINSTANTIE }o--o| LOCATIE : locatieId
    AANBODINSTANTIE }o--o| ORGANISATIE_EENHEID : uitvoerendTeamId
    AANBODINSTANTIE ||--o{ GROEP : groepen
    LOCATIE ||--o{ LOCATIE : valtBinnenLocatieId
    ORGANISATIE_EENHEID ||--o{ ORGANISATIE_EENHEID : bovenliggendeEenheidId

    AANBODINSTANTIE {
        uuid id PK
        string aanbodType "opleidingsaanbod tot leergelegenheid"
        string versie "semver"
        uuid bovenliggendAanbodId FK "null op root"
        object specificatieVerwijzing "specificatieId + versie"
        string naam
        string status
        array knelpunten "code + omschrijving (par. 3.4)"
        string cohort
        object periode "start + eind"
        int minAantalStudenten
        int maxAantalStudenten
        uuid locatieId FK
        uuid uitvoerendTeamId FK
    }
    GROEP {
        uuid id PK
        string naam
        int capaciteit
    }
    LOCATIE {
        uuid id PK
        string locatieType "campus tot ruimte, virtueel"
        string naam
        uuid valtBinnenLocatieId FK "recursief"
        object adres
        object geolocatie "breedtegraad + lengtegraad"
        string verdieping
        string vleugel
        string url "bij virtueel"
        array codes "externe identificaties"
    }
    ORGANISATIE_EENHEID {
        uuid id PK
        string eenheidType "instelling, sector, onderwijsteam"
        string naam
        uuid bovenliggendeEenheidId FK "recursief"
        array professionalIds "alleen uuid's"
    }
    ONDERWIJSSPECIFICATIE {
        uuid id PK
        string versie "gepinde versie, het object zelf staat in de onderwijsspecificatie-payload"
    }
```

## Resultaatstructuur en examenplan

```mermaid
erDiagram
    EXAMENPLANSPECIFICATIE ||--o{ RESULTAATEENHEIDSPECIFICATIE : onderdeel_van
    RESULTAATEENHEIDSPECIFICATIE ||--o{ TOETSONDERDEELSPECIFICATIE : onderdeel_van
    EXAMENPLANSPECIFICATIE }o--|| OPLEIDINGSPROGRAMMASPECIFICATIE : geldtVoor
    RESULTAATEENHEIDSPECIFICATIE }o--o{ REGELSET : regelsetVerwijzingen

    EXAMENPLANSPECIFICATIE {
        uuid id PK
        string specificatieType "examenplanspecificatie"
        uuid bovenliggendSpecificatieId "null"
        uuid geldtVoor FK "opleidingsprogrammaspecificatie"
        uuid leeruitkomstId FK "sleutel naar de leeruitkomst"
        object leeruitkomst "leesbaar: type=kwalificatie, code=27141"
        string aggregatie "allenVoldoende"
        object resultaatmodel "schaal, cesuur"
        string versie
        date geldigVanaf
        date geldigTot
        array manifest "pins: id + version + relatie"
        string status
    }
    RESULTAATEENHEIDSPECIFICATIE {
        uuid id PK
        string specificatieType "resultaateenheidspecificatie"
        uuid bovenliggendSpecificatieId FK "examenplanspecificatie"
        uuid leeruitkomstId FK "sleutel naar de leeruitkomst"
        object leeruitkomst "leesbaar: type=kerntaak"
        uuid beoordeelt FK "onderwijseenheid of keuzedeelruimte, optioneel"
        number weging "relatief binnen ouder"
        string aggregatie
        object resultaatmodel
        boolean verplicht
        array regelsetVerwijzingen FK "naar REGELSET"
        array manifest
    }
    TOETSONDERDEELSPECIFICATIE {
        uuid id PK
        string specificatieType "toetsonderdeelspecificatie"
        uuid bovenliggendSpecificatieId FK "resultaateenheidspecificatie"
        uuid leeruitkomstId FK "sleutel naar de leeruitkomst"
        object leeruitkomst "leesbaar: type=kerntaak of werkproces"
        string aard "summatief of formatief"
        string toetsvorm
        number weging
        object resultaatmodel
        boolean verplicht
    }
    REGELSET {
        uuid id PK
        string naam
        array regels "welke resultaten meetellen"
    }
    OPLEIDINGSPROGRAMMASPECIFICATIE {
        uuid id PK
        string versie "gepinde versie, het object zelf staat in de onderwijsspecificatie-payload"
    }
```

## Onderwijscatalogus naar planning en roostering

De begrippen uit het semantisch kader en hun relaties, in de context van dit proces. Links de wereld van OC (specificeren), rechts die van P (instantiëren); de koppeling verbindt ze via de verwijzing "instantieert".

```mermaid
erDiagram
    ONDERWIJSSPECIFICATIE ||--o{ ONDERWIJSSPECIFICATIE : "bestaat uit"
    ONDERWIJSSPECIFICATIE }o--o{ LEERUITKOMST : "verankert op"
    ONDERWIJSSPECIFICATIE }o--o{ REGELSET : "kent keuzeregels via"
    ONDERWIJSAANBOD }o--|| ONDERWIJSSPECIFICATIE : "instantieert (id en versie)"
    ONDERWIJSAANBOD ||--o{ ONDERWIJSAANBOD : "bestaat uit"
    ONDERWIJSAANBOD }o--o| LOCATIE : "vindt plaats op"
    ONDERWIJSAANBOD }o--o| ONDERWIJSTEAM : "wordt uitgevoerd door"
    ONDERWIJSAANBOD ||--o{ GROEP : "kent"
    ROOSTER }o--|| ONDERWIJSAANBOD : "plaatst in de tijd (context)"
```

## Onderwijscatalogus naar studentinformatiesysteem

Conform het ROSA Kernmodel Onderwijsinformatie (KOI) en [ADR 0022](../Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md): een onderwijsresultaat wordt behaald op leeruitkomsten, en meerdere toetsonderdeelresultaten leiden gewogen tot dat onderwijsresultaat. De verbintenis hoort bij het aanbod (ankertabel), niet bij de specificatie, en staat daarom niet in dit kernmodel.

```mermaid
erDiagram
    ONDERWIJSSPECIFICATIE ||--o{ ONDERWIJSSPECIFICATIE : "bestaat uit"
    ONDERWIJSSPECIFICATIE }o--o{ LEERUITKOMST : "verankert op"
    NOMINAAL_EXAMENPLAN }o--|| ONDERWIJSSPECIFICATIE : "geldt voor"
    NOMINAAL_EXAMENPLAN ||--o{ TOETSONDERDEEL : "weegt"
    KEUZEDEEL ||--o| KEUZEDEEL_EXAMENPLANDEEL : "kent eigen"
    KEUZEDEEL_EXAMENPLANDEEL ||--o{ TOETSONDERDEEL : "weegt"
    TOETSONDERDEEL }o--o{ LEERUITKOMST : "toetst"
    INDIVIDUELE_STRUCTUUR }o--|| ONDERWIJSSPECIFICATIE : "is kopie van nominaal template"
    INDIVIDUELE_STRUCTUUR }o--o{ KEUZEDEEL : "ingevuld met (keuze via SKS)"
    INDIVIDUEEL_EXAMENPLAN ||--|| INDIVIDUELE_STRUCTUUR : "hoort bij"
    INDIVIDUEEL_EXAMENPLAN }o--|| NOMINAAL_EXAMENPLAN : "samengesteld uit"
    INDIVIDUEEL_EXAMENPLAN }o--o{ KEUZEDEEL_EXAMENPLANDEEL : "plus delen van gekozen keuzedelen"
    TOETSONDERDEELRESULTAAT }o--|| TOETSONDERDEEL : "resultaat op"
    ONDERWIJSRESULTAAT }o--o{ TOETSONDERDEELRESULTAAT : "gewogen samengesteld uit"
    ONDERWIJSRESULTAAT }o--o{ LEERUITKOMST : "dicht af"
    ONDERWIJSRESULTAAT }o--|| INDIVIDUEEL_EXAMENPLAN : "telt mee in"
```

## Onderwijscatalogus naar leermanagementsysteem

```mermaid
erDiagram
    ONDERWIJSSPECIFICATIE ||--o{ ONDERWIJSSPECIFICATIE : "bestaat uit"
    ONDERWIJSSPECIFICATIE }o--o{ LEERUITKOMST : "verankert op"
    LEEROMGEVING_INRICHTING }o--|| ONDERWIJSSPECIFICATIE : "is ingericht naar (id en versie)"
    LEERMIDDELKOPPELING }o--|| ONDERWIJSSPECIFICATIE : "hoort bij (id en versie)"
    LEERMIDDELKOPPELING ||--o{ LEERMIDDELGROEP : "bundelt"
    LEERMIDDELGROEP ||--o{ LEERMIDDEL : "bevat"
```
