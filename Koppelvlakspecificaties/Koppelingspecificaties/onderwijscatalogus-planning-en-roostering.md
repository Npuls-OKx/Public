# Onderwijscatalogus naar planning en roostering

De koppeling tussen de onderwijscatalogus en het planningssysteem: welke informatie erover beweegt, in welke volgorde, en welk bericht dat draagt, met de sequentiediagrammen erbij. De functionele eisen die het proces aan deze koppeling stelt staan als vertrekpunt in de eerste tabel; het interactieoverzicht legt per interactie het bericht, het patroon en de foutafhandeling vast, en de endpoints staan bij de [applicatiecomponent](../Applicatiecomponenten/README.md) die ze serveert.

## Plek in de keten

![Koppeling onderwijscatalogus naar planning en roostering op de hoofdplaat](../src/highlight_oc_p_en_r_informatiestromen_hoofdplaat_v1_7.png)

De uitsnede komt uit de informatiestromen-hoofdplaat v1.7 (richtinggevend; de legenda draagt nog "concept"), met deze koppeling gemarkeerd. De koppelvlakken van beide componenten staan bij de [onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) en het [planningssysteem](../Applicatiecomponenten/planningssysteem.md).

## Stories

De stories uit de [requirementsboom](../../Referentiemateriaal/requirementsboom/README.md) die deze koppeling invult, met de berichtstroom die dat doet.

| Story | Ingevuld door |
|---|---|
| [story-0006](../../Referentiemateriaal/requirementsboom/stories.md#story-0006) | [Opleidingsaanbod aanmaken](#opleidingsaanbod-aanmaken) |
| [story-0007](../../Referentiemateriaal/requirementsboom/stories.md#story-0007) | [Opleidingsaanbod aanmaken](#opleidingsaanbod-aanmaken) en [Planning niet gelukt melden](#planning-niet-gelukt-melden) |
| [story-0030](../../Referentiemateriaal/requirementsboom/stories.md#story-0030) | [Opleidingsaanbod herplannen](#opleidingsaanbod-herplannen) |
| [story-0002](../../Referentiemateriaal/requirementsboom/stories.md#story-0002) | [Acceptatietoets bij late wijziging](#acceptatietoets-bij-late-wijziging) |
| [story-0032](../../Referentiemateriaal/requirementsboom/stories.md#story-0032) | [Specificatiestatus gewijzigd melden](#specificatiestatus-gewijzigd-melden) |
| [story-0011](../../Referentiemateriaal/requirementsboom/stories.md#story-0011) | [Reconciliatie na gemist event](#reconciliatie-na-gemist-event) |
| [story-0010](../../Referentiemateriaal/requirementsboom/stories.md#story-0010) | [Abonnement registreren](#abonnement-registreren) |

## Applicatiediensten

Deze koppeling zet de volgende [applicatiediensten](../Applicatiediensten/README.md) in. De tabel legt vast welk component welke dienst implementeert; welke stromen daarover lopen en in welke volgorde bepaalt de koppeling zelf.

| Applicatiedienst | Geïmplementeerd door |
|---|---|
| [onderwijsspecificatiestructuur-aanbieder](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md) | Onderwijscatalogus |
| [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md) | Planningssysteem |
| [planbaar-onderwijsaanbod-aanbieder](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md) | Planningssysteem |
| [planbaar-onderwijsaanbod-afnemer](../Applicatiediensten/planbaar-onderwijsaanbod-afnemer.md) | Onderwijscatalogus |
| [verwerkingsuitkomst-aanbieder](../Applicatiediensten/verwerkingsuitkomst-aanbieder.md) | Planningssysteem |
| [verwerkingsuitkomst-afnemer](../Applicatiediensten/verwerkingsuitkomst-afnemer.md) | Onderwijscatalogus |
| [afleverabonnement-aanbieder](../Applicatiediensten/afleverabonnement-aanbieder.md) | Onderwijscatalogus en planningssysteem |
| [afleverabonnement-afnemer](../Applicatiediensten/afleverabonnement-afnemer.md) | Onderwijscatalogus en planningssysteem |

## Interactiepatronen

Deze koppeling zet de volgende [interactiepatronen](../Interactiepatronen/README.md) in.

| Interactiepatroon | Waarvoor in deze koppeling |
|---|---|
| [Event Notification](../Interactiepatronen/event-notification.md) | Melden dat een specificatie planbaar is of is gewijzigd, en het ophalen van structuur, delta of aanbod-instantie dat daarop volgt |
| [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | De uitkomst van het planproces terugmelden, met een referentie naar het opleidingsaanbod |
| [Event-Carried State Transfer](../Interactiepatronen/event-carried-state-transfer.md) | Een statusovergang die los staat van een versie: het planningssysteem werkt zijn afgeleide status bij zonder op te halen |
| [Request-Reply](../Interactiepatronen/request-reply.md) | Herstel nadat een event in de dead letter channel is beland |
| [Subscription registration](../Interactiepatronen/subscription-registration.md) | Het afleveradres vastleggen waarop de meldingen landen |

## Procesbeeld

Twee gedeelde principes bepalen het verkeer over deze koppeling. **Resource-eigenaarschap** ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)): de onderwijscatalogus bezit de onderwijsspecificaties, het planningssysteem het onderwijsaanbod, het roostersysteem het rooster. **Event notification** ([U4](../uitgangspunten.md#u4-event-notification)): de onderwijscatalogus meldt, het planningssysteem haalt op wanneer het hem uitkomt.

```mermaid
flowchart LR
    CO["Curriculum-ontwerptool"] -- "onderwijsspecificatie" --> OC["Onderwijscatalogus<br/>bezit: specificaties"]
    subgraph KOP["deze koppeling: onderwijscatalogus naar planning en roostering"]
        OC -. "1: event specificatie planbaar" .-> P["Planningssysteem<br/>bezit: opleidingsaanbod"]
        OC -- "2: onderwijsspecificatiestructuur (pull door P)" --> P
        P -. "3: status + referentie opleidingsaanbod (uuid)" .-> OC
    end
    P -. "4: event planning beschikbaar<br/>(referentie naar aanbod en specificatie)" .-> R["Roostersysteem<br/>bezit: rooster"]
    R -. "5: event rooster bekend (referentie)" .-> OC
    R -. "5: event rooster bekend (referentie)" .-> P
```

Wat het diagram niet toont: het planningssysteem bouwt de planning **asynchroon** op, binnen de regels uit de specificatie (voorwaarden vooraf, locatie, periode). De uitkomst, gelukt of niet gelukt, komt terug als status met een referentie naar het `opleidingsaanbod`; de aanbod-instantie zelf blijft bij planning en wordt alleen opgehaald als de catalogus die wil inzien. Stap 4 en 5 liggen buiten deze koppeling en staan er ter illustratie van hetzelfde patroon.

## Berichtstromen

## Opleidingsaanbod aanmaken

Doel: een gepubliceerde specificatie omzetten in een planbaar `opleidingsaanbod`, met een referentie terug naar de onderwijscatalogus. Trigger: onderwijsspecificatie krijgt status `gepubliceerd`. Initiator: Onderwijscatalogus.

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Event Notification](../Interactiepatronen/event-notification.md), [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md), [onderwijsspecificatiestructuur-aanbieder](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md), [verwerkingsuitkomst-afnemer](../Applicatiediensten/verwerkingsuitkomst-afnemer.md), [planbaar-onderwijsaanbod-aanbieder](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md) |

Endpoints:

- [webhook `specificatie-planbaar`](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)
- [`GET /onderwijsspecificaties/{id}`](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md)
- [webhook `verwerkingsstatus`](../Applicatiediensten/verwerkingsuitkomst-afnemer.md)
- [`GET /onderwijsaanbod/{id}` (optioneel)](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus: opleidingsprogrammaspecificatie krijgt status gepubliceerd
    Onderwijscatalogus-)Planningssysteem: [specificatie-planbaar] Event: specificatie planbaar (id + versie)
    Planningssysteem->>Onderwijscatalogus: [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, versie)
    Onderwijscatalogus-->>Planningssysteem: Momentopname met onderwijsspecificaties en regelsets<br/>(manifest legt versies vast)
    alt Structuur valide
        Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status: ontvangen, planproces gestart (asynchroon)
        Note over Planningssysteem: Grofmazige planning, van specificatie naar opleidingsaanbod,<br/>binnen de regels (voorwaarden vooraf, locatie, periode)
        alt Planning gelukt
            Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status gelukt, met referentie naar opleidingsaanbod (uuid)
            opt de onderwijscatalogus wil het aanbod inzien
                Onderwijscatalogus->>Planningssysteem: [GET /onderwijsaanbod/{id}] opleidingsaanbod (uuid)
                Planningssysteem-->>Onderwijscatalogus: opleidingsaanbod-instantie (zie paragraaf 6)
            end
        else Planning niet gelukt
            Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status niet gelukt, met referentie naar opleidingsaanbod<br/>(instantie draagt status en reden, zie 5.3)
        end
    else Structuur niet valide
        Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status afgekeurd (validatiefout, met foutmodel)
    end
```

## Opleidingsaanbod herplannen

Doel: een lopende planning laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor de ontvanger. Trigger: nieuwe versie van een specificatie die al in een manifest is vastgelegd. Initiator: Onderwijscatalogus.

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Event Notification](../Interactiepatronen/event-notification.md), [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [onderwijsspecificatiestructuur-aanbieder](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md), [verwerkingsuitkomst-afnemer](../Applicatiediensten/verwerkingsuitkomst-afnemer.md), [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md) |

Endpoints:

- [`GET /onderwijsspecificaties/{id}/delta` of `GET /onderwijsspecificaties/{id}`](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md)
- [webhook `verwerkingsstatus`](../Applicatiediensten/verwerkingsuitkomst-afnemer.md)
- [webhook `specificatie-gewijzigd`](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus: Nieuwe versie van een specificatie<br/>die in een manifest is vastgelegd
    Onderwijscatalogus-)Planningssysteem: [specificatie-gewijzigd] Event: specificatie gewijzigd<br/>(object-id, oude versie, nieuwe versie, wijzigingsklasse)
    Note over Planningssysteem: Wat het planningssysteem met de wijziging doet is applicatiefunctionaliteit,<br/>buiten deze specificatie
    alt het planningssysteem haalt de delta op
        Planningssysteem->>Onderwijscatalogus: [GET /onderwijsspecificaties/{id}/delta] delta tussen versies (JSON Patch, RFC 6902)
        Onderwijscatalogus-->>Planningssysteem: Delta tussen oude en nieuwe versie
    else het planningssysteem haalt de volledige structuur op
        Planningssysteem->>Onderwijscatalogus: [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, nieuwe versie)
        Onderwijscatalogus-->>Planningssysteem: Momentopname (nieuwe versie)
    end
    Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status: ontvangen, herplanproces gestart
    Note over Planningssysteem: Herplannen (asynchroon)
    Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status voltooid of mislukt, met referentie naar opleidingsaanbod
```

## Planning niet gelukt melden

Doel: de onderwijscatalogus in kennis stellen dat een specificatie voor een of meer cohorten niet planbaar blijkt, met referentie en knelpunten, zonder de aanroep te blokkeren. Trigger: planproces bij het planningssysteem vindt geen geldige planning. Initiator: Planningssysteem.

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [verwerkingsuitkomst-afnemer](../Applicatiediensten/verwerkingsuitkomst-afnemer.md), [planbaar-onderwijsaanbod-aanbieder](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md) |

Endpoints:

- [webhook `verwerkingsstatus`](../Applicatiediensten/verwerkingsuitkomst-afnemer.md)
- [`GET /onderwijsaanbod/{id}` (optioneel)](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md)

```mermaid
sequenceDiagram
    autonumber
    actor Planner
    participant Planningssysteem
    participant Onderwijscatalogus

    Note over Planningssysteem: Planproces vindt geen geldige planning<br/>(bv. capaciteit of expertise ontoereikend)
    Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status niet gelukt, met referentie naar opleidingsaanbod
    Planningssysteem-->>Planner: Signaal niet realiseerbaar, met knelpunten
    opt de onderwijscatalogus wil de reden inzien
        Onderwijscatalogus->>Planningssysteem: [GET /onderwijsaanbod/{id}] opleidingsaanbod (uuid)
        Planningssysteem-->>Onderwijscatalogus: opleidingsaanbod-instantie met status en knelpunten
    end
    Note over Onderwijscatalogus: Specificatie blijft gepubliceerd,<br/>geen planbaar aanbod voor dit cohort
    Note over Onderwijscatalogus,Planningssysteem: Vervolg is ketenafstemming buiten deze koppeling,<br/>specificatie aanpassen (curriculum-ontwerptool), capaciteit uitbreiden of cohort uitstellen
```

## Acceptatietoets bij late wijziging

Doel: een afgeronde planning beschermen tegen een wijziging die er ongecontroleerd doorheen breekt. Trigger: specificatiewijziging terwijl de planning al is afgerond. Initiator: Onderwijscatalogus.

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Event Notification](../Interactiepatronen/event-notification.md), [Asynchronous Request-Reply](../Interactiepatronen/asynchronous-request-reply.md) | [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md), [verwerkingsuitkomst-afnemer](../Applicatiediensten/verwerkingsuitkomst-afnemer.md) |

Endpoints:

- [webhook `specificatie-gewijzigd`](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)
- [webhook `verwerkingsstatus`](../Applicatiediensten/verwerkingsuitkomst-afnemer.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus,Planningssysteem: Planning is afgerond, referentie naar opleidingsaanbod is bekend
    Onderwijscatalogus-)Planningssysteem: [specificatie-gewijzigd] Event: specificatie gewijzigd (object-id, wijzigingsklasse)
    Note over Planningssysteem: Toets aan acceptatieregels (lifecycle),<br/>wijziging na planning alleen bij uitzondering
    alt Niet-brekend, geen planimpact
        Planningssysteem->>Planningssysteem: Werk versieverwijzing in het manifest bij, planning blijft staan
        Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status: versieverwijzing bijgewerkt, geen herplanning
    else Brekend of planimpact
        Planningssysteem-)Onderwijscatalogus: [verwerkingsstatus] Status: wijziging niet verwerkt, ketenafstemming vereist
        Note over Onderwijscatalogus,Planningssysteem: Besluit buiten deze koppeling (memo van Niels),<br/>uitzonderlijk accepteren en herplannen, of terugdraaien
    end
```

## Specificatiestatus gewijzigd melden

Doel: de onderwijscatalogus een statuswijziging laten melden die los staat van een nieuwe versie, zodat het planningssysteem zijn afgeleide status kan bijwerken zonder herplanronde. Trigger: specificatie krijgt een nieuwe status buiten een versiewijziging om (bv. `gepubliceerd` naar `gedeactiveerd`, [regels bij de schema's](../Datamodelschema's/README.md#regels-bij-de-schemas)). Initiator: Onderwijscatalogus. Voorbeeldgeval: een opleiding die voor een ouder cohort bewust niet meer wordt aangeboden is nog wel planbaar, maar wordt niet meer gepland; dat is deze statuswijziging (met archivering als vervolg), geen planningsfout uit de melding hierboven.

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Event-Carried State Transfer](../Interactiepatronen/event-carried-state-transfer.md) | [onderwijsspecificatiestructuur-afnemer](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md) |

Endpoints:

- [webhook `specificatie-status-gewijzigd`](../Applicatiediensten/onderwijsspecificatiestructuur-afnemer.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus: Specificatie krijgt een nieuwe status,<br/>los van de versie (bv. gepubliceerd naar gedeactiveerd)
    Onderwijscatalogus-)Planningssysteem: [specificatie-status-gewijzigd] Event: specificatiestatus gewijzigd<br/>(object-id, oude status, nieuwe status)
    Note over Planningssysteem: Wat het planningssysteem met de statuswijziging doet is applicatiefunctionaliteit,<br/>buiten deze specificatie
```

## Reconciliatie na gemist event

Doel: de gemiste informatie via een gewone opvraag herstellen na een event dat in de Dead Letter Channel is beland, zonder op een herhaalde aflevering te wachten. Trigger: een event is niet aangekomen. Initiator: Onderwijscatalogus of Planningssysteem.

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Request-Reply](../Interactiepatronen/request-reply.md) | [onderwijsspecificatiestructuur-aanbieder](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md), [planbaar-onderwijsaanbod-aanbieder](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md) |

Endpoints:

- [`GET /onderwijsspecificaties` (op OC)](../Applicatiediensten/onderwijsspecificatiestructuur-aanbieder.md)
- [`GET /onderwijsaanbod` (op P)](../Applicatiediensten/planbaar-onderwijsaanbod-aanbieder.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus,Planningssysteem: Een event is in de Dead Letter Channel beland
    alt het planningssysteem heeft een event gemist
        Planningssysteem->>Onderwijscatalogus: [GET /onderwijsspecificaties] onderwijsspecificaties (gewijzigdSinds, status=gepubliceerd)
        Onderwijscatalogus-->>Planningssysteem: Lijst specificatie-id's met laatste versie
    else de onderwijscatalogus heeft een verwerkingsstatus gemist
        Onderwijscatalogus->>Planningssysteem: [GET /onderwijsaanbod] onderwijsaanbod (specificatieId, versie optioneel)
        Planningssysteem-->>Onderwijscatalogus: aanbodInstanties die deze specificatie instantieert
    end
```

## Abonnement registreren

Doel: elke partij een callback-URL laten vastleggen voor de events die zij van de ander ontvangt, als voorwaarde voor de event-gedreven stromen. Trigger: inrichting van de koppeling, of wijziging van de callback-URL. Initiator: Onderwijscatalogus en Planningssysteem (over en weer, elk voor de events die de ander van hem ontvangt).

| Versie | Interactiepatronen | Applicatiediensten |
|---|---|---|
| 1.0 | [Subscription registration](../Interactiepatronen/subscription-registration.md) | [afleverabonnement-aanbieder](../Applicatiediensten/afleverabonnement-aanbieder.md) |

Endpoints:

- [`POST /abonnementen` (op OC en op P)](../Applicatiediensten/afleverabonnement-aanbieder.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Planningssysteem->>Onderwijscatalogus: [POST /abonnementen] abonnement (callbackUrl, de meldingen over specificaties)
    Onderwijscatalogus-->>Planningssysteem: Abonnement-id
    Onderwijscatalogus->>Planningssysteem: [POST /abonnementen] abonnement (callbackUrl, de verwerkingsstatus)
    Planningssysteem-->>Onderwijscatalogus: Abonnement-id
    Note over Onderwijscatalogus,Planningssysteem: Herregistratie op dezelfde callback-URL + event-type overschrijft,<br/>geen dubbele aflevering (idempotent)
```

## Context: doorwerking naar het roostersysteem

Buiten deze koppeling, en niet als vastgelegde interactie: het roostersysteem plaatst het geplande aanbod in tijd en ruimte. Het planningssysteem meldt dat de planning beschikbaar is, het roostersysteem haalt het aanbod op en meldt het rooster terug aan zowel planning als catalogus. Hetzelfde patroon van referentie plus event dus, opgenomen om te tonen dat de lijn doorloopt tot voorbij wat dit pakket specificeert. Het [roostersysteem](../Applicatiecomponenten/roostersysteem.md) draagt daarom geen endpoints.

```mermaid
sequenceDiagram
    autonumber
    participant P as Planningssysteem
    participant R as Roostersysteem
    participant OC as Onderwijscatalogus

    P-)R: Event: planning beschikbaar<br/>(referentie naar opleidingsaanbod en naar specificatie)
    R->>P: GET opleidingsaanbod (uuid)
    P-->>R: opleidingsaanbod-instantie
    Note over R: Roosteren (asynchroon)
    R-)P: Event: rooster bekend (referentie, bij dit aanbod)
    R-)OC: Event: rooster bekend (zelfde referentie, bij deze specificatie)
    opt OC wil het rooster inzien
        OC->>R: GET rooster (uuid)
        R-->>OC: rooster-instantie
    end
```
