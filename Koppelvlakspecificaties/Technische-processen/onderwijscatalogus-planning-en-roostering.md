# Technisch proces: onderwijscatalogus naar planning en roostering

Het technisch proces van deze koppeling: de systeem-naar-systeemberichten tussen de onderwijscatalogus en het planningssysteem, met de sequentiediagrammen. Doel: per proces laten zien welk berichtenpatroon het technisch implementeert en wat het oplevert, zonder de koppelingspecificatie te herhalen. Voor I1 tot en met I5 zijn de sequentiediagrammen overgenomen uit [§5](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#5-sequentiediagrammen) van de koppelingspecificatie; I6 tot en met I8 hebben daar geen eigen diagram (ze volgen het patroon van resp. I4 en I2/I5) en zijn hier opgebouwd uit [§3](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#3-interactieoverzicht) en [§7](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest). Voor het bericht, het patroon en de foutafhandeling per interactie blijft §3 leidend, voor de endpoint(s) die het bericht draagt §7. Elk technisch proces hieronder draagt zo de keten functionele eis → technisch proces → endpoint(s). Het functionele proces dat deze koppeling ondersteunt (onderwijsontwikkeling en planvorming) valt buiten dit document; de functionele eisen die dat proces aan deze koppeling stelt staan als vertrekpunt in de eerste tabel.

## Functionele eisen

| # | Functionele eis | Technisch proces |
|---|---|---|
| FR1 | De onderwijscatalogus moet het planningssysteem kunnen laten weten dat een specificatie gereed is om te plannen, en het planningssysteem moet daarop een opleidingsaanbod met referentie kunnen terugleveren | [Notify-then-pull: opleidingsaanbod aanmaken](#notify-then-pull-opleidingsaanbod-aanmaken) |
| FR2 | Het planningssysteem moet de planning kunnen bijwerken wanneer een specificatie wijzigt, zonder verplicht de volledige structuur opnieuw te ontvangen | [Notify-then-pull: opleidingsaanbod herplannen](#notify-then-pull-opleidingsaanbod-herplannen) |
| FR3 | De onderwijscatalogus moet kunnen weten wanneer een cohort niet planbaar is, inclusief de reden | [Asynchrone statusmelding: planning niet gelukt](#asynchrone-statusmelding-planning-niet-gelukt) |
| FR4 | Een afgeronde planning moet beschermd zijn tegen een specificatiewijziging die er ongecontroleerd doorheen breekt | [Acceptatietoets bij late wijziging](#acceptatietoets-bij-late-wijziging) |
| FR5 | De onderwijscatalogus moet een statuswijziging kunnen melden die niet aan een nieuwe versie hangt, los van het wijzigingsproces | [Asynchrone statusmelding: specificatiestatus gewijzigd](#asynchrone-statusmelding-specificatiestatus-gewijzigd) |
| FR6 | Beide partijen moeten na een gemist event de informatie alsnog kunnen ophalen | [Reconciliatie na gemist event](#reconciliatie-na-gemist-event) |
| FR7 | Beide partijen moeten een afleveradres kunnen vastleggen voordat events afgeleverd worden | [Abonnement registreren](#abonnement-registreren) |

## Technische processen

| Technisch proces | Doel | Trigger | Initiator | Interacties (§3) | Endpoints (§7) | Sequentiediagram |
|---|---|---|---|---|---|---|
| Notify-then-pull: opleidingsaanbod aanmaken | Een gepubliceerde specificatie omzetten in een planbaar `opleidingsaanbod`, met een referentie terug naar de onderwijscatalogus | Onderwijsspecificatie krijgt status `gepubliceerd` | Onderwijscatalogus | I1, I2, I3, (I5) | webhook `specificatie-planbaar`; `GET /onderwijsspecificaties/{id}`; webhook `verwerkingsstatus`; (`GET /onderwijsaanbod/{id}`) | [hieronder](#notify-then-pull-opleidingsaanbod-aanmaken) |
| Notify-then-pull: opleidingsaanbod herplannen | Een lopende planning laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor de ontvanger | Nieuwe versie van een specificatie die al in een manifest is vastgelegd | Onderwijscatalogus | I2, I3, I4 | `GET /onderwijsspecificaties/{id}/delta` of `GET /onderwijsspecificaties/{id}`; webhook `verwerkingsstatus`; webhook `specificatie-gewijzigd` | [hieronder](#notify-then-pull-opleidingsaanbod-herplannen) |
| Asynchrone statusmelding: planning niet gelukt | De onderwijscatalogus in kennis stellen dat een cohort niet planbaar is, met referentie en knelpunten, zonder de aanroep te blokkeren | Planproces bij het planningssysteem vindt geen geldige planning | Planningssysteem | I3, (I5) | webhook `verwerkingsstatus`; (`GET /onderwijsaanbod/{id}`) | [hieronder](#asynchrone-statusmelding-planning-niet-gelukt) |
| Acceptatietoets bij late wijziging | Een afgeronde planning beschermen tegen een wijziging die er ongecontroleerd doorheen breekt | Specificatiewijziging terwijl de planning al is afgerond | Onderwijscatalogus | I3, I4 | webhook `specificatie-gewijzigd`; webhook `verwerkingsstatus` | [hieronder](#acceptatietoets-bij-late-wijziging) |
| Asynchrone statusmelding: specificatiestatus gewijzigd | De onderwijscatalogus een statuswijziging laten melden die los staat van een nieuwe versie, zodat het planningssysteem zijn afgeleide status kan bijwerken zonder herplanronde | Specificatie krijgt een nieuwe status buiten een versiewijziging om (bv. `gepubliceerd` naar `gedeactiveerd`) | Onderwijscatalogus | I6 | webhook `specificatie-status-gewijzigd` | [hieronder](#asynchrone-statusmelding-specificatiestatus-gewijzigd) |
| Reconciliatie na gemist event | De gemiste informatie via een gewone opvraag herstellen na een event dat in de Dead Letter Channel is beland | Een I1-, I3-, I4- of I6-event is niet aangekomen | Onderwijscatalogus of Planningssysteem | I7 | `GET /onderwijsspecificaties` (op OC); `GET /onderwijsaanbod` (op P) | [hieronder](#reconciliatie-na-gemist-event) |
| Abonnement registreren | Elke partij een callback-URL laten vastleggen voor de events die zij van de ander ontvangt, als voorwaarde voor I1, I3, I4 en I6 | Inrichting van de koppeling, of wijziging van de callback-URL | Onderwijscatalogus en Planningssysteem | I8 | `POST /abonnementen` (op OC en op P) | [hieronder](#abonnement-registreren) |

## Notify-then-pull: opleidingsaanbod aanmaken

Doel: een gepubliceerde specificatie omzetten in een planbaar `opleidingsaanbod`, met een referentie terug naar de onderwijscatalogus. Trigger: onderwijsspecificatie krijgt status `gepubliceerd`. Initiator: Onderwijscatalogus. Interacties: I1, I2, I3, (I5).

Endpoints:

- [webhook `specificatie-planbaar` (I1)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [`GET /onderwijsspecificaties/{id}` (I2)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [webhook `verwerkingsstatus` (I3)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [`GET /onderwijsaanbod/{id}` (I5, optioneel)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus: opleidingsprogrammaspecificatie krijgt status gepubliceerd
    Onderwijscatalogus-)Planningssysteem: I1 [specificatie-planbaar] Event: specificatie planbaar (id + versie)
    Planningssysteem->>Onderwijscatalogus: I2 [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, versie)
    Onderwijscatalogus-->>Planningssysteem: Momentopname met onderwijsspecificaties en regelsets<br/>(manifest legt versies vast)
    alt Structuur valide
        Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status: ontvangen, planproces gestart (asynchroon)
        Note over Planningssysteem: Grofmazige planning, van specificatie naar opleidingsaanbod,<br/>binnen de regels (voorwaarden vooraf, locatie, periode)
        alt Planning gelukt
            Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status gelukt, met referentie naar opleidingsaanbod (uuid)
            opt de onderwijscatalogus wil het aanbod inzien
                Onderwijscatalogus->>Planningssysteem: I5 [GET /onderwijsaanbod/{id}] opleidingsaanbod (uuid)
                Planningssysteem-->>Onderwijscatalogus: opleidingsaanbod-instantie (zie paragraaf 6)
            end
        else Planning niet gelukt
            Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status niet gelukt, met referentie naar opleidingsaanbod<br/>(instantie draagt status en reden, zie 5.3)
        end
    else Structuur niet valide
        Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status afgekeurd (validatiefout, met foutmodel)
    end
```

## Notify-then-pull: opleidingsaanbod herplannen

Doel: een lopende planning laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor de ontvanger. Trigger: nieuwe versie van een specificatie die al in een manifest is vastgelegd. Initiator: Onderwijscatalogus. Interacties: I2, I3, I4.

Endpoints:

- [`GET /onderwijsspecificaties/{id}/delta` of `GET /onderwijsspecificaties/{id}` (I2)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [webhook `verwerkingsstatus` (I3)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [webhook `specificatie-gewijzigd` (I4)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus: Nieuwe versie van een specificatie<br/>die in een manifest is vastgelegd
    Onderwijscatalogus-)Planningssysteem: I4 [specificatie-gewijzigd] Event: specificatie gewijzigd<br/>(object-id, oude versie, nieuwe versie, wijzigingsklasse)
    Note over Planningssysteem: Wat het planningssysteem met de wijziging doet is applicatiefunctionaliteit,<br/>buiten deze specificatie
    alt het planningssysteem haalt de delta op
        Planningssysteem->>Onderwijscatalogus: I2 [GET /onderwijsspecificaties/{id}/delta] delta tussen versies (JSON Patch, RFC 6902)
        Onderwijscatalogus-->>Planningssysteem: Delta tussen oude en nieuwe versie
    else het planningssysteem haalt de volledige structuur op
        Planningssysteem->>Onderwijscatalogus: I2 [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, nieuwe versie)
        Onderwijscatalogus-->>Planningssysteem: Momentopname (nieuwe versie)
    end
    Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status: ontvangen, herplanproces gestart
    Note over Planningssysteem: Herplannen (asynchroon)
    Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status voltooid of mislukt, met referentie naar opleidingsaanbod
```

## Asynchrone statusmelding: planning niet gelukt

Doel: de onderwijscatalogus in kennis stellen dat een cohort niet planbaar is, met referentie en knelpunten, zonder de aanroep te blokkeren. Trigger: planproces bij het planningssysteem vindt geen geldige planning. Initiator: Planningssysteem. Interacties: I3, (I5).

Endpoints:

- [webhook `verwerkingsstatus` (I3)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [`GET /onderwijsaanbod/{id}` (I5, optioneel)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

```mermaid
sequenceDiagram
    autonumber
    actor Planner
    participant Planningssysteem
    participant Onderwijscatalogus

    Note over Planningssysteem: Planproces vindt geen geldige planning<br/>(bv. capaciteit of expertise ontoereikend)
    Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status niet gelukt, met referentie naar opleidingsaanbod
    Planningssysteem-->>Planner: Signaal niet realiseerbaar, met knelpunten
    opt de onderwijscatalogus wil de reden inzien
        Onderwijscatalogus->>Planningssysteem: I5 [GET /onderwijsaanbod/{id}] opleidingsaanbod (uuid)
        Planningssysteem-->>Onderwijscatalogus: opleidingsaanbod-instantie met status en knelpunten
    end
    Note over Onderwijscatalogus: Specificatie blijft gepubliceerd,<br/>geen planbaar aanbod voor dit cohort
    Note over Onderwijscatalogus,Planningssysteem: Vervolg is ketenafstemming buiten deze koppeling,<br/>specificatie aanpassen (curriculum-ontwerptool), capaciteit uitbreiden of cohort uitstellen
```

## Acceptatietoets bij late wijziging

Doel: een afgeronde planning beschermen tegen een wijziging die er ongecontroleerd doorheen breekt. Trigger: specificatiewijziging terwijl de planning al is afgerond. Initiator: Onderwijscatalogus. Interacties: I3, I4.

Endpoints:

- [webhook `specificatie-gewijzigd` (I4)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [webhook `verwerkingsstatus` (I3)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus,Planningssysteem: Planning is afgerond, referentie naar opleidingsaanbod is bekend
    Onderwijscatalogus-)Planningssysteem: I4 [specificatie-gewijzigd] Event: specificatie gewijzigd (object-id, wijzigingsklasse)
    Note over Planningssysteem: Toets aan acceptatieregels (lifecycle),<br/>wijziging na planning alleen bij uitzondering
    alt Niet-brekend, geen planimpact
        Planningssysteem->>Planningssysteem: Werk versieverwijzing in het manifest bij, planning blijft staan
        Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status: versieverwijzing bijgewerkt, geen herplanning
    else Brekend of planimpact
        Planningssysteem-)Onderwijscatalogus: I3 [verwerkingsstatus] Status: wijziging niet verwerkt, ketenafstemming vereist
        Note over Onderwijscatalogus,Planningssysteem: Besluit buiten deze koppeling (memo van Niels),<br/>uitzonderlijk accepteren en herplannen, of terugdraaien
    end
```

## Asynchrone statusmelding: specificatiestatus gewijzigd

Doel: de onderwijscatalogus een statuswijziging laten melden die los staat van een nieuwe versie, zodat het planningssysteem zijn afgeleide status kan bijwerken zonder herplanronde. Trigger: specificatie krijgt een nieuwe status buiten een versiewijziging om (bv. `gepubliceerd` naar `gedeactiveerd`, [lifecycle-uitwerking §3](../Koppelingspecificaties/gedeeld/lifecycle-en-versionering.md#3-versioneringsmechaniek)). Initiator: Onderwijscatalogus. Interacties: I6.

Endpoints:

- [webhook `specificatie-status-gewijzigd` (I6)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

Geen apart sequentiediagram in de koppelingspecificatie; I6 spiegelt daar het patroon van I4. Opgebouwd uit de interactiebeschrijving in §3.

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus: Specificatie krijgt een nieuwe status,<br/>los van de versie (bv. gepubliceerd naar gedeactiveerd)
    Onderwijscatalogus-)Planningssysteem: I6 [specificatie-status-gewijzigd] Event: specificatiestatus gewijzigd<br/>(object-id, oude status, nieuwe status)
    Note over Planningssysteem: Wat het planningssysteem met de statuswijziging doet is applicatiefunctionaliteit,<br/>buiten deze specificatie
```

## Reconciliatie na gemist event

Doel: de gemiste informatie via een gewone opvraag herstellen na een event dat in de Dead Letter Channel is beland, zonder op een herhaalde aflevering te wachten. Trigger: een I1-, I3-, I4- of I6-event is niet aangekomen. Initiator: Onderwijscatalogus of Planningssysteem. Interacties: I7.

Endpoints:

- [`GET /onderwijsspecificaties` (op OC)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)
- [`GET /onderwijsaanbod` (op P)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

Geen apart sequentiediagram in de koppelingspecificatie; I7 spiegelt daar het patroon van I2/I5. Opgebouwd uit de interactiebeschrijving in §3 en de endpoints in §7.

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Note over Onderwijscatalogus,Planningssysteem: Een event (I1, I3, I4 of I6) is in de Dead Letter Channel beland
    alt het planningssysteem heeft een event gemist
        Planningssysteem->>Onderwijscatalogus: I7 [GET /onderwijsspecificaties] onderwijsspecificaties (gewijzigdSinds, status=gepubliceerd)
        Onderwijscatalogus-->>Planningssysteem: Lijst specificatie-id's met laatste versie
    else de onderwijscatalogus heeft een I3-event gemist
        Onderwijscatalogus->>Planningssysteem: I7 [GET /onderwijsaanbod] onderwijsaanbod (specificatieId, versie optioneel)
        Planningssysteem-->>Onderwijscatalogus: aanbodInstanties die deze specificatie instantieert
    end
```

## Abonnement registreren

Doel: elke partij een callback-URL laten vastleggen voor de events die zij van de ander ontvangt, als voorwaarde voor de event-gedreven interacties (I1, I3, I4, I6). Trigger: inrichting van de koppeling, of wijziging van de callback-URL. Initiator: Onderwijscatalogus en Planningssysteem (over en weer, elk voor de events die de ander van hem ontvangt). Interacties: I8.

Endpoints:

- [`POST /abonnementen` (op OC en op P)](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#7-endpointbeschrijvingen-rest)

Geen apart sequentiediagram in de koppelingspecificatie; I8 spiegelt daar het patroon van I2/I5. Opgebouwd uit de endpoints in §7.

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant Planningssysteem

    Planningssysteem->>Onderwijscatalogus: I8 [POST /abonnementen] abonnement (callbackUrl, events: I1, I4, I6)
    Onderwijscatalogus-->>Planningssysteem: Abonnement-id
    Onderwijscatalogus->>Planningssysteem: I8 [POST /abonnementen] abonnement (callbackUrl, events: I3)
    Planningssysteem-->>Onderwijscatalogus: Abonnement-id
    Note over Onderwijscatalogus,Planningssysteem: Herregistratie op dezelfde callback-URL + event-type overschrijft,<br/>geen dubbele aflevering (idempotent)
```
