# Applicatiediensten

Een applicatiedienst is een capability: gedrag dat een applicatiecomponent kan implementeren. Diensten zijn de bouwstenen waaruit een [koppeling](../Koppelingspecificaties/) wordt samengesteld. De dienst zegt wát er moet kunnen en waarom, niet wie het doet — elk component kan hem claimen, en een component claimt er meestal meer dan één.

Een aanbieder zorgt dat hij een gegeven of een functionaliteit levert; een afnemer zorgt dat hij die kan afnemen. Dat zijn **twee losse diensten**, niet twee kanten van één, en op een pagina staan daarom alleen verplichtingen van één van beide richtingen. Een component dat onderwijsspecificaties publiceert implementeert `onderwijsspecificatiestructuur-aanbieder`; een component dat ze wil gebruiken implementeert `onderwijsspecificatiestructuur-afnemer`. Beide zijn zelfstandig te claimen en zelfstandig te versioneren.

Met welk patroon een dienst wordt gebruikt is een keuze van de [koppelingspecificatie](../Koppelingspecificaties/) die hem inzet, niet een eigenschap van de dienst.

| Aanbieder | Afnemer | Waarover |
|---|---|---|
| [onderwijsspecificatiestructuur](onderwijsspecificatiestructuur-aanbieder.md) | [onderwijsspecificatiestructuur](onderwijsspecificatiestructuur-afnemer.md) | De vastgestelde specificatiestructuur met haar versies |
| [onderwijsspecificatie-inname](onderwijsspecificatie-inname-aanbieder.md) | [onderwijsspecificatie-inname](onderwijsspecificatie-inname-afnemer.md) | Een elders ontworpen specificatie vaststellen en opnemen |
| [keuzeregelset](keuzeregelset-aanbieder.md) | [keuzeregelset](keuzeregelset-afnemer.md) | De regels die keuzeruimte begrenzen, los van de items |
| [planbaar-onderwijsaanbod](planbaar-onderwijsaanbod-aanbieder.md) | [planbaar-onderwijsaanbod](planbaar-onderwijsaanbod-afnemer.md) | Aanbod in het stadium tussen specificatie en rooster |
| [onderwijsaanbod-zoekvraag](onderwijsaanbod-zoekvraag-aanbieder.md) | [onderwijsaanbod-zoekvraag](onderwijsaanbod-zoekvraag-afnemer.md) | Aanbod doorzoeken op criteria uit de leervraag |
| [onderwijsaanbod-haalbaarheidstoets](onderwijsaanbod-haalbaarheidstoets-aanbieder.md) | [onderwijsaanbod-haalbaarheidstoets](onderwijsaanbod-haalbaarheidstoets-afnemer.md) | Een voorstel beoordelen vóór vastlegging |
| [geroosterd-onderwijsaanbod](geroosterd-onderwijsaanbod-aanbieder.md) | [geroosterd-onderwijsaanbod](geroosterd-onderwijsaanbod-afnemer.md) | Aanbod in het laatste stadium, per periode |
| [kiesbaarheidsbepaling](kiesbaarheidsbepaling-aanbieder.md) | [kiesbaarheidsbepaling](kiesbaarheidsbepaling-afnemer.md) | Wat een student op elk niveau mag kiezen |
| [verbintenistoestand](verbintenistoestand-aanbieder.md) | [verbintenistoestand](verbintenistoestand-afnemer.md) | De toestand van de onderwijsverbintenis per niveau |
| [resultaatstructuur](resultaatstructuur-aanbieder.md) | [resultaatstructuur](resultaatstructuur-afnemer.md) | Toetsonderdelen, weging en aggregatie |
| [behaalde-leeruitkomst](behaalde-leeruitkomst-aanbieder.md) | [behaalde-leeruitkomst](behaalde-leeruitkomst-afnemer.md) | Wat een student heeft behaald, met bewijsvoering |
| [leermiddelkoppeling](leermiddelkoppeling-aanbieder.md) | [leermiddelkoppeling](leermiddelkoppeling-afnemer.md) | De gelegde koppeling naar leermiddelen |
| [verwerkingsuitkomst](verwerkingsuitkomst-aanbieder.md) | [verwerkingsuitkomst](verwerkingsuitkomst-afnemer.md) | Wat een verwerking heeft opgeleverd, met referentie naar het aangemaakte |
| [afleverabonnement](afleverabonnement-aanbieder.md) | [afleverabonnement](afleverabonnement-afnemer.md) | Vastleggen waar en waarvoor een partij meldingen wil ontvangen |

## Wat op elke dienst drukt

Deze eisen gelden voor elke dienst in de tabel:

- Betrouwbare aflevering, idempotente verwerking, dead letter-afhandeling en volgorde waar die semantisch telt ([ADR 0018](../../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md)).
- Authenticatie via OAuth 2.0 Client Credentials, met een eigen token-endpoint per aanbieder ([auth-standaard](../auth-standaard.md)).
- Hoogstens twee gelijktijdig actieve major versies, zodat een afnemer tijd heeft om over te stappen.
- Het bericht ligt vast, het kanaal niet ([U5](../uitgangspunten.md#u5-bericht-versus-kanaal)).
