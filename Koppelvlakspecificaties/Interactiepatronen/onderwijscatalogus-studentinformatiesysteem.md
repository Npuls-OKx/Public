# Interactiepatroon: onderwijscatalogus naar studentinformatiesysteem

Het interactiepatroon van deze koppeling: de systeem-naar-systeemberichten (machine-to-machine) tussen de onderwijscatalogus en het studentinformatiesysteem, met de sequentiediagrammen. Doel: per patroon laten zien welk berichtenpatroon het technisch implementeert en wat het oplevert, zonder de koppelingspecificatie te herhalen. De functionele eisen die het proces aan deze koppeling stelt staan als vertrekpunt in de eerste tabel; het interactieoverzicht legt per interactie het bericht, het patroon en de foutafhandeling vast, en de endpoints staan bij de [applicatiecomponent](../Applicatiecomponenten/README.md) dat ze serveert.

## Plek in de keten

![Koppeling onderwijscatalogus naar het studentinformatiesysteem op de hoofdplaat](../src/highlight_oc_sis_informatiestromen_hoofdplaat_v1_7.png)

De uitsnede komt uit de informatiestromen-hoofdplaat v1.7 (richtinggevend; de legenda draagt nog "concept"), met deze koppeling gemarkeerd. De koppelvlakken van beide componenten staan bij de [onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) en het [studentinformatiesysteem](../Applicatiecomponenten/studentinformatiesysteem.md).

## Functionele eisen

| Id | Functionele eis | Interactiepatroon | Story |
|---|---|---|---|
| <a id="functionele-eis-0008"></a>functionele-eis-0008 | De onderwijscatalogus moet het studentinformatiesysteem kunnen laten weten dat een specificatie en resultaatstructuur beschikbaar zijn om het nominale template en de resultaatstructuur op in te richten, en het studentinformatiesysteem moet daarop een inrichtingsstatus met referentie kunnen terugleveren | [Notify-then-pull: nominaal template en resultaatstructuur inrichten](#notify-then-pull-nominaal-template-en-resultaatstructuur-inrichten) | [story-0022](../../Referentiemateriaal/requirementsboom/stories.md#story-0022); [story-0023](../../Referentiemateriaal/requirementsboom/stories.md#story-0023) |
| <a id="functionele-eis-0009"></a>functionele-eis-0009 | Een ingerichte resultaatstructuur waarop al verbintenissen lopen moet beschermd zijn tegen een examenplanwijziging die er ongecontroleerd doorheen breekt | [Acceptatietoets bij wijziging examenplan](#acceptatietoets-bij-wijziging-examenplan) | [story-0020](../../Referentiemateriaal/requirementsboom/stories.md#story-0020) |

## Procesbeeld

**Resource-eigenaarschap** ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)): de onderwijscatalogus bezit de specificaties en de resultaatstructuren, het studentinformatiesysteem de verbintenissen, individuele structuren, voortgang en resultaten. **Notify-then-pull** ([U4](../uitgangspunten.md#u4-notify-then-pull)): de catalogus meldt, het studentinformatiesysteem haalt op.

```mermaid
flowchart LR
    OC["Onderwijscatalogus<br/>bezit: specificaties en resultaatstructuren"]
    subgraph KOP["deze koppeling: onderwijscatalogus naar studentinformatiesysteem"]
        OC -. "1: event specificatie beschikbaar" .-> SIS["SIS (KRS/SVS)<br/>bezit: verbintenissen, individuele structuren, resultaten"]
        OC -- "2: onderwijsspecificatiestructuur (pull door SIS)" --> SIS
        OC -- "3: resultaatstructuur (pull door SIS)" --> SIS
        SIS -. "4: status inrichting + referentie" .-> OC
    end
    SKS["Student Keuze Systeem"] -. "keuzes (eigen koppeling, buiten scope)" .-> SIS
```

Wat het diagram niet toont: het studentinformatiesysteem haalt twee dingen op, de specificatiestructuur en de resultaatstructuur, en richt daarmee het **nominale template** in plus de mapping van welke toetsonderdeelresultaten welke leeruitkomsten afdichten ([ADR 0022](../../Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md)). Bij een wijziging draagt het event een wijzigingsklasse mee. Voor het examenplan gelden daarbij de strengste acceptatieregels: lopende verbintenissen mogen niet ongecontroleerd geraakt worden.

## Interactieoverzicht

De interacties op deze koppeling, met per interactie het messaging-patroon, in dezelfde patroontaal als de koppeling met planning ([Enterprise Integration Patterns, Messaging](https://www.enterpriseintegrationpatterns.com/patterns/messaging/)).
Wat hier wordt vastgelegd is het **bericht**, niet het **kanaal**: hoe het bericht bij de ontvanger komt is een inrichtingskeuze van instelling en leverancier, binnen de vier eigenschappen die [ADR 0018](../../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md) eist. Zie [uitgangspunt U5](../uitgangspunten.md#u5-bericht-versus-kanaal).

| # | Interactie | Initiator | Patroon | Synchroniciteit | Gedrag bij dubbele ontvangst | Foutafhandeling |
|---|---|---|---|---|---|---|
| S1 | Specificatie en resultaatstructuur beschikbaar melden | OC | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (id + versie) | Asynchroon | Geen effect: event-id ([Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html)) | [Guaranteed Delivery](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedDelivery.html); [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |
| S2 | Onderwijsspecificatiestructuur of delta ophalen | SIS | [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html) (GET, alleen-lezen) | Synchroon | Geen effect (alleen-lezen) | HTTP-foutcodes, client bepaalt retry |
| S3 | Resultaatstructuur ophalen | SIS | [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html) (GET, alleen-lezen) | Synchroon | Geen effect (alleen-lezen) | HTTP-foutcodes |
| S4 | Inrichtingsstatus melden, met referentie naar de inrichting | SIS | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (status: ontvangen/gestart, afgekeurd, ingericht, niet ingericht) | Asynchroon | Geen effect: status-id | Retry met backoff, daarna [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |
| S5 | Wijziging specificatie of resultaatstructuur melden | OC | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (object-id, oude en nieuwe versie, wijzigingsklasse) | Asynchroon | Geen effect: event-id | [Guaranteed Delivery](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedDelivery.html); [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |

## Berichtgedrag

Dat is een voorbeeld van een kanaal, geen voorschrift: een bus, broker of cloud-pubsubdienst mag het vervangen zolang die de vier eigenschappen uit §3 levert. Het bericht blijft in alle gevallen gelijk.

- Alle GET's zijn alleen-lezen en zonder neveneffect; herhaald aanroepen geeft hetzelfde resultaat.
- Event-aflevering: ontvanger bevestigt met 200; bij uitblijven daarvan herhaalt de verzender met backoff en daarna [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html). Dubbele aflevering is onschadelijk door het event-id ([Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html)).
- Registratie van een callback-URL, zoals `POST /abonnementen` bij de koppeling met planning (I8), is voor deze koppeling nog geen eigen interactie in §3; zolang die er niet is, is het afleveradres een inrichtingskeuze tussen OC en SIS, buiten dit document.
- Mogelijke uitbreidingen (v-next): paginering bij grote structuren.

## Interactiepatronen

| Interactiepatroon | Doel | Trigger | Initiator | Interacties (§3) | Endpoints (§7) | Sequentiediagram |
|---|---|---|---|---|---|---|
| Notify-then-pull: nominaal template en resultaatstructuur inrichten | Een gepubliceerde specificatie en examenplanspecificatie omzetten in een ingericht nominaal template en resultaatstructuur bij het studentinformatiesysteem | Onderwijsspecificatie en examenplanspecificatie krijgen status `gepubliceerd` | Onderwijscatalogus | S1, S2, S3, S4 | webhook `specificatie-en-resultaatstructuur-beschikbaar`; `GET /onderwijsspecificaties/{id}`; `GET /examenplanspecificaties/{id}`; webhook `inrichtingsstatus` | [hieronder](#notify-then-pull-nominaal-template-en-resultaatstructuur-inrichten) |
| Acceptatietoets bij wijziging examenplan | Lopende verbintenissen beschermen tegen een examenplanwijziging die er ongecontroleerd doorheen breekt | Examenplanspecificatie wijzigt terwijl er al verbintenissen lopen | Onderwijscatalogus | S5 | webhook `examenplanspecificatie-gewijzigd`; webhook `inrichtingsstatus` | [hieronder](#acceptatietoets-bij-wijziging-examenplan) |

## Notify-then-pull: nominaal template en resultaatstructuur inrichten

Doel: een gepubliceerde specificatie en examenplanspecificatie omzetten in een ingericht nominaal template en resultaatstructuur bij het studentinformatiesysteem. Trigger: onderwijsspecificatie en examenplanspecificatie krijgen status `gepubliceerd`. Initiator: Onderwijscatalogus. Interacties: S1, S2, S3, S4.

Endpoints:

- [webhook `specificatie-en-resultaatstructuur-beschikbaar` (S1)](../Applicatiecomponenten/studentinformatiesysteem.md)
- [`GET /onderwijsspecificaties/{id}` (S2)](../Applicatiecomponenten/onderwijscatalogus.md)
- [`GET /examenplanspecificaties/{id}` (S3)](../Applicatiecomponenten/onderwijscatalogus.md)
- [webhook `inrichtingsstatus` (S4)](../Applicatiecomponenten/onderwijscatalogus.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant SIS

    Note over Onderwijscatalogus: opleidingsprogrammaspecificatie en examenplanspecificatie gepubliceerd
    Onderwijscatalogus-)SIS: S1 [specificatie-en-resultaatstructuur-beschikbaar] Event: beschikbaar (specificatie-id + versie, examenplan-id + versie)
    SIS->>Onderwijscatalogus: S2 [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, versie)
    Onderwijscatalogus-->>SIS: Momentopname (manifest legt versies vast)
    SIS->>Onderwijscatalogus: S3 [GET /examenplanspecificaties/{id}] resultaatstructuur (examenplan-id, versie)
    Onderwijscatalogus-->>SIS: Resultaatstructuur (weging, aggregatie, toetsonderdelen)
    SIS-)Onderwijscatalogus: S4 [inrichtingsstatus] Status: ontvangen, inrichting gestart (asynchroon)
    Note over SIS: Inrichten nominaal template (leerroute, keuzeruimte)<br/>en resultaatstructuur (mapping toetsonderdeelresultaten naar leeruitkomsten)
    alt Inrichting gelukt
        SIS-)Onderwijscatalogus: S4 [inrichtingsstatus] Status ingericht, met referentie naar inrichting (uuid)
    else Inrichting niet gelukt
        SIS-)Onderwijscatalogus: S4 [inrichtingsstatus] Status niet ingericht (validatie- of inrichtingsfout)
    end
```

## Acceptatietoets bij wijziging examenplan

Doel: lopende verbintenissen beschermen tegen een examenplanwijziging die er ongecontroleerd doorheen breekt. Trigger: examenplanspecificatie wijzigt terwijl er al verbintenissen lopen. Initiator: Onderwijscatalogus. Interacties: S5.

Endpoints:

- [webhook `examenplanspecificatie-gewijzigd` (S5)](../Applicatiecomponenten/studentinformatiesysteem.md)
- [webhook `inrichtingsstatus` (S4)](../Applicatiecomponenten/onderwijscatalogus.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant SIS

    Note over SIS: Inrichting gereed, verbintenissen lopen (op aanbod)
    Onderwijscatalogus-)SIS: S5 [examenplanspecificatie-gewijzigd] Event: examenplanspecificatie gewijzigd (id, wijzigingsklasse)
    Note over SIS: Toets aan acceptatieregels,<br/>lopende verbintenissen mogen niet ongecontroleerd geraakt worden
    alt Geen lopende verbintenissen geraakt
        SIS->>SIS: Werk versieverwijzing bij, nieuwe instroom volgt nieuwe versie
        SIS-)Onderwijscatalogus: S4 [inrichtingsstatus] Status: verwerkt, oude versie blijft voor lopende verbintenissen
    else Lopende verbintenissen geraakt
        SIS-)Onderwijscatalogus: S4 [inrichtingsstatus] Status: niet verwerkt, expliciete impactanalyse en besluit vereist
        Note over Onderwijscatalogus,SIS: Besluit buiten deze koppeling,<br/>gelijktijdig actieve versies per cohort (lifecycle-uitwerking)
    end
```
