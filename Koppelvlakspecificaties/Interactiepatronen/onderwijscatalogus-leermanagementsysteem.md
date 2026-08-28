# Interactiepatroon: onderwijscatalogus naar leermanagementsysteem

Het interactiepatroon van deze koppeling: de systeem-naar-systeemberichten (machine-to-machine) tussen de onderwijscatalogus en het leermanagementsysteem, met de sequentiediagrammen. Doel: per patroon laten zien welk berichtenpatroon het technisch implementeert en wat het oplevert, zonder de koppelingspecificatie te herhalen. De functionele eisen die het proces aan deze koppeling stelt staan als vertrekpunt in de eerste tabel; het interactieoverzicht legt per interactie het bericht, het patroon en de foutafhandeling vast, en de endpoints staan bij de [applicatiecomponent](../Applicatiecomponenten/README.md) dat ze serveert.

## Plek in de keten

![Koppeling onderwijscatalogus naar het leermanagementsysteem op de hoofdplaat](../src/highlight_oc_lms_informatiestromen_hoofdplaat_v1_7.png)

De uitsnede komt uit de informatiestromen-hoofdplaat v1.7 (richtinggevend; de legenda draagt nog "concept"), met deze koppeling gemarkeerd. De koppelvlakken van beide componenten staan bij de [onderwijscatalogus](../Applicatiecomponenten/onderwijscatalogus.md) en het [leermanagementsysteem](../Applicatiecomponenten/leermanagementsysteem.md).

## Functionele eisen

| Id | Functionele eis | Interactiepatroon | Story |
|---|---|---|---|
| <a id="functionele-eis-0010"></a>functionele-eis-0010 | De onderwijscatalogus moet het leermanagementsysteem kunnen laten weten dat een specificatie beschikbaar is om de leeromgeving op in te richten, en het leermanagementsysteem moet daarop een inrichtingsstatus met referentie kunnen terugleveren | [Notify-then-pull: leeromgeving inrichten en leermiddelkoppeling melden](#notify-then-pull-leeromgeving-inrichten-en-leermiddelkoppeling-melden) | geen |
| <a id="functionele-eis-0011"></a>functionele-eis-0011 | Het leermanagementsysteem moet een leermiddelkoppeling die het heeft gelegd aan de onderwijscatalogus kunnen melden, zodat die de leermiddelen bij het aanbod kan tonen | [Notify-then-pull: leeromgeving inrichten en leermiddelkoppeling melden](#notify-then-pull-leeromgeving-inrichten-en-leermiddelkoppeling-melden) | [story-0003](../../Referentiemateriaal/requirementsboom/stories.md#story-0003) |
| <a id="functionele-eis-0012"></a>functionele-eis-0012 | Het leermanagementsysteem moet zijn inrichting kunnen bijwerken wanneer een specificatie wijzigt, zonder verplicht de volledige structuur opnieuw te ontvangen | [Notify-then-pull: inrichting bijwerken na wijziging](#notify-then-pull-inrichting-bijwerken-na-wijziging) | geen |

## Procesbeeld

**Resource-eigenaarschap** ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)): de onderwijscatalogus bezit de specificaties, de leeromgeving haar inrichting en de leermiddelkoppeling. **Notify-then-pull** ([U4](../uitgangspunten.md#u4-notify-then-pull)) geldt in beide richtingen.

```mermaid
flowchart LR
    OC["Onderwijscatalogus<br/>bezit: specificaties"]
    subgraph KOP["deze koppeling: onderwijscatalogus naar leermanagementsysteem"]
        OC -. "1: event specificatie beschikbaar" .-> LMS["LMS<br/>bezit: leeromgeving-inrichting en leermiddelkoppeling"]
        OC -- "2: onderwijsspecificatiestructuur (pull door LMS)" --> LMS
        LMS -. "3: status inrichting + referentie" .-> OC
        LMS -. "4: event leermiddelkoppeling beschikbaar (referentie)" .-> OC
        LMS -- "5: leermiddelkoppeling (pull door OC)" --> OC
    end
```

Wat het diagram niet toont: de leeromgeving richt zich in tot op **leeronderdeelniveau** en vult daaronder haar eigen lesniveau in, waar de catalogus buiten staat. De leermiddelkoppeling gaat de andere kant op zodra de leeromgeving die heeft gelegd; de catalogus haalt hem op wanneer die de leermiddelen bij het aanbod wil tonen. Wijzigt een specificatie, dan volgt een nieuw event en haalt de leeromgeving het verschil of de volledige structuur opnieuw op.

## Interactieoverzicht

De interacties op deze koppeling, met per interactie het messaging-patroon, in dezelfde patroontaal als de koppeling met planning ([Enterprise Integration Patterns, Messaging](https://www.enterpriseintegrationpatterns.com/patterns/messaging/)).
Wat hier wordt vastgelegd is het **bericht**, niet het **kanaal**: hoe het bericht bij de ontvanger komt is een inrichtingskeuze van instelling en leverancier, binnen de vier eigenschappen die [ADR 0018](../../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md) eist. Zie [uitgangspunt U5](../uitgangspunten.md#u5-bericht-versus-kanaal).

| # | Interactie | Initiator | Patroon | Synchroniciteit | Gedrag bij dubbele ontvangst | Foutafhandeling |
|---|---|---|---|---|---|---|
| L1 | Specificatie beschikbaar melden | OC | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (id + versie) | Asynchroon | Geen effect: event-id ([Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html)) | [Guaranteed Delivery](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedDelivery.html); [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |
| L2 | Onderwijsspecificatiestructuur of delta ophalen | LMS | [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html) (GET, alleen-lezen) | Synchroon | Geen effect (alleen-lezen) | HTTP-foutcodes, client bepaalt retry |
| L3 | Inrichtingsstatus melden, met referentie | LMS | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (status: ontvangen/gestart, afgekeurd, ingericht, niet ingericht) | Asynchroon | Geen effect: status-id | Retry met backoff, daarna [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |
| L4 | Leermiddelkoppeling beschikbaar melden | LMS | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (referentie + specificatie-id en versie) | Asynchroon | Geen effect: event-id | [Guaranteed Delivery](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedDelivery.html); [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |
| L5 | Leermiddelkoppeling ophalen | OC | [Request-Reply](https://www.enterpriseintegrationpatterns.com/patterns/messaging/RequestReply.html) op referentie (GET uuid, alleen-lezen) | Synchroon | Geen effect (alleen-lezen) | HTTP-foutcodes |
| L6 | Specificatiewijziging melden | OC | [Event Message](https://www.enterpriseintegrationpatterns.com/patterns/messaging/EventMessage.html) (object-id, oude en nieuwe versie, wijzigingsklasse) | Asynchroon | Geen effect: event-id | [Guaranteed Delivery](https://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedDelivery.html); [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html) |

## Berichtgedrag

Dat is een voorbeeld van een kanaal, geen voorschrift: een bus, broker of cloud-pubsubdienst mag het vervangen zolang die de vier eigenschappen uit §3 levert. Het bericht blijft in alle gevallen gelijk.

- Alle GET's zijn alleen-lezen en zonder neveneffect; herhaald aanroepen geeft hetzelfde resultaat.
- Event-aflevering: ontvanger bevestigt met 200; bij uitblijven daarvan herhaalt de verzender met backoff en daarna [Dead Letter Channel](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html). Dubbele aflevering is onschadelijk door het event-id ([Idempotent Receiver](https://www.enterpriseintegrationpatterns.com/patterns/messaging/IdempotentReceiver.html)).
- Registratie van een callback-URL, zoals `POST /abonnementen` bij de koppeling met planning (I8), is voor deze koppeling nog geen eigen interactie in §3; zolang die er niet is, is het afleveradres een inrichtingskeuze tussen OC en LMS, buiten dit document.
- Mogelijke uitbreidingen (v-next): paginering bij grote structuren, filter op deelstructuur-selectie bij het ophalen van de structuur.

## Interactiepatronen

| Interactiepatroon | Doel | Trigger | Initiator | Interacties (§3) | Endpoints (§7) | Sequentiediagram |
|---|---|---|---|---|---|---|
| Notify-then-pull: leeromgeving inrichten en leermiddelkoppeling melden | Een gepubliceerde specificatie omzetten in een ingerichte leeromgeving, met een leermiddelkoppeling terug naar de onderwijscatalogus | Onderwijsspecificatie krijgt status `gepubliceerd` | Onderwijscatalogus | L1, L2, L3, L4, (L5) | webhook `specificatie-beschikbaar`; `GET /onderwijsspecificaties/{id}`; webhook `inrichtingsstatus`; webhook `leermiddelkoppeling-beschikbaar`; (`GET /leermiddelkoppelingen/{id}`) | [hieronder](#notify-then-pull-leeromgeving-inrichten-en-leermiddelkoppeling-melden) |
| Notify-then-pull: inrichting bijwerken na wijziging | Een bestaande inrichting laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor het leermanagementsysteem | Nieuwe versie van een specificatie waarop het leermanagementsysteem is ingericht | Onderwijscatalogus | L2, L3, L6 | `GET /onderwijsspecificaties/{id}/delta` of `GET /onderwijsspecificaties/{id}`; webhook `inrichtingsstatus`; webhook `specificatie-gewijzigd` | [hieronder](#notify-then-pull-inrichting-bijwerken-na-wijziging) |

## Notify-then-pull: leeromgeving inrichten en leermiddelkoppeling melden

Doel: een gepubliceerde specificatie omzetten in een ingerichte leeromgeving, met een leermiddelkoppeling terug naar de onderwijscatalogus. Trigger: onderwijsspecificatie krijgt status `gepubliceerd`. Initiator: Onderwijscatalogus. Interacties: L1, L2, L3, L4, (L5).

Endpoints:

- [webhook `specificatie-beschikbaar` (L1)](../Applicatiecomponenten/leermanagementsysteem.md)
- [`GET /onderwijsspecificaties/{id}` (L2)](../Applicatiecomponenten/onderwijscatalogus.md)
- [webhook `inrichtingsstatus` (L3)](../Applicatiecomponenten/onderwijscatalogus.md)
- [webhook `leermiddelkoppeling-beschikbaar` (L4)](../Applicatiecomponenten/onderwijscatalogus.md)
- [`GET /leermiddelkoppelingen/{id}` (L5, optioneel)](../Applicatiecomponenten/leermanagementsysteem.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant LMS

    Note over Onderwijscatalogus: opleidingsprogrammaspecificatie krijgt status gepubliceerd
    Onderwijscatalogus-)LMS: L1 [specificatie-beschikbaar] Event: specificatie beschikbaar (id + versie)
    LMS->>Onderwijscatalogus: L2 [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, versie)
    Onderwijscatalogus-->>LMS: Momentopname (manifest legt versies vast)
    LMS-)Onderwijscatalogus: L3 [inrichtingsstatus] Status: ontvangen, inrichting gestart (asynchroon)
    Note over LMS: Leeromgeving inrichten op leeronderdeelniveau,<br/>leermiddel(groep)en koppelen aan specificaties
    LMS-)Onderwijscatalogus: L3 [inrichtingsstatus] Status ingericht, met referentie naar inrichting (uuid)
    LMS-)Onderwijscatalogus: L4 [leermiddelkoppeling-beschikbaar] Event: leermiddelkoppeling beschikbaar (referentie, specificatie-id + versie)
    opt de onderwijscatalogus toont leermiddelen bij het aanbod
        Onderwijscatalogus->>LMS: L5 [GET /leermiddelkoppelingen/{id}] leermiddelkoppeling (uuid)
        LMS-->>Onderwijscatalogus: Leermiddelkoppeling (leermiddelgroepen per specificatie)
    end
```

## Notify-then-pull: inrichting bijwerken na wijziging

Doel: een bestaande inrichting laten volgen op een nieuwe specificatieversie, met delta of volledige structuur als keuze voor het leermanagementsysteem. Trigger: nieuwe versie van een specificatie waarop het leermanagementsysteem is ingericht. Initiator: Onderwijscatalogus. Interacties: L2, L3, L6.

Endpoints:

- [`GET /onderwijsspecificaties/{id}/delta` of `GET /onderwijsspecificaties/{id}` (L2)](../Applicatiecomponenten/onderwijscatalogus.md)
- [webhook `inrichtingsstatus` (L3)](../Applicatiecomponenten/onderwijscatalogus.md)
- [webhook `specificatie-gewijzigd` (L6)](../Applicatiecomponenten/leermanagementsysteem.md)

```mermaid
sequenceDiagram
    autonumber
    participant Onderwijscatalogus
    participant LMS

    Note over Onderwijscatalogus: Nieuwe versie van een specificatie<br/>waarop het leermanagementsysteem is ingericht
    Onderwijscatalogus-)LMS: L6 [specificatie-gewijzigd] Event: specificatie gewijzigd<br/>(object-id, oude versie, nieuwe versie, wijzigingsklasse)
    Note over LMS: Wat het leermanagementsysteem met de wijziging doet is applicatiefunctionaliteit,<br/>buiten deze specificatie
    alt het leermanagementsysteem haalt de delta op
        LMS->>Onderwijscatalogus: L2 [GET /onderwijsspecificaties/{id}/delta] delta tussen versies (JSON Patch, RFC 6902)
        Onderwijscatalogus-->>LMS: Delta tussen oude en nieuwe versie
    else het leermanagementsysteem haalt de volledige structuur op
        LMS->>Onderwijscatalogus: L2 [GET /onderwijsspecificaties/{id}] onderwijsspecificatiestructuur (id, nieuwe versie)
        Onderwijscatalogus-->>LMS: Momentopname (nieuwe versie)
    end
    LMS-)Onderwijscatalogus: L3 [inrichtingsstatus] Status: inrichting bijgewerkt, of afstemming nodig
```
