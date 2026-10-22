# Koppelvlakdiensten

Een koppelvlakdienst is het contract waarmee een component een deel van zijn gedrag over een koppeling aanbiedt of afneemt. Diensten zijn de bouwstenen waaruit een [koppeling](../Koppelingen/README.md) wordt samengesteld. De dienst zegt wát er moet kunnen, niet welk systeem het doet: elk component kan hem implementeren, en een component implementeert er meestal meer dan één. Op elke dienstpagina is de handelende partij daarom het component dat de dienst implementeert, en niemand anders; waar die dienst voor dient blijkt uit de koppeling die hem inzet, onder **Gebruikt in**.

Een aanbieder zorgt dat hij een gegeven of een functionaliteit levert; een afnemer zorgt dat hij die kan afnemen. Dat zijn **twee losse diensten**, niet twee kanten van één, en op een pagina staan daarom alleen verplichtingen van één van beide richtingen. Een component dat onderwijsspecificaties publiceert implementeert `onderwijsspecificatiestructuur-aanbieder`; een component dat ze wil gebruiken implementeert `onderwijsspecificatiestructuur-afnemer`. Beide zijn zelfstandig te implementeren; een versie draagt alleen de koppeling die ze inzet ([release management §4.2](../release-management.md#42-een-koppeling-draagt-haar-eigen-versie)).

**Wie gegevens aanneemt, heeft een endpoint.** Krijgt een component gegevens toegestuurd, dan heeft het een endpoint nodig: de verzender moet ze ergens heen sturen. Een dienst zonder eigen endpoint neemt dus niets aan; het component haalt op of verstuurt alleen. Haalt het op, dan staat op de dienstpagina dat ophalen vereist is.

Met welk patroon een dienst wordt gebruikt is een keuze van de berichtstroom die hem inzet, niet een eigenschap van de dienst.

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
- Hoogstens twee gelijktijdig actieve majors per koppeling, zodat een afnemer tijd heeft om over te stappen.
- Het bericht ligt vast, het kanaal niet ([U5](../uitgangspunten.md#u5-bericht-versus-kanaal)).
