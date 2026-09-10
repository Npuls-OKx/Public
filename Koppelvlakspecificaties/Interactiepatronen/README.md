# Interactiepatronen

Een interactiepatroon beschrijft hoe twee partijen informatie uitwisselen, los van welke partijen dat zijn en welke informatie het betreft. De [koppelingspecificaties](../Koppelingspecificaties/) kiezen per interactie een patroon en vullen het in met de systemen, de berichten en de payloads van die koppeling; het patroon zelf staat hier één keer, in rollen in plaats van systeemnamen.

Die rollen worden vervuld door [applicatiecomponenten](../Applicatiecomponenten/). Welke component welke rol heeft volgt uit resource-eigenaarschap ([U3](../uitgangspunten.md#u3-resource-eigenaarschap)): het component dat de resource bezit is de **bezitter**, het component dat hem afneemt de **consument**. Dat wisselt per resource, ook binnen één koppeling — de onderwijscatalogus is bezitter van de onderwijsspecificaties en consument van het opleidingsaanbod dat planning bezit.

Alle vijf komen uit bestaande catalogi en dragen de naam die daar geldt; per patroon staat de keuze om het te gebruiken en de beperking die OKx eroverheen legt. De eisen aan aflevering, idempotentie, foutafhandeling en volgorde gelden voor elk asynchroon bericht in dit pakket en staan in [ADR 0018](../../Referentiemateriaal/adr/0018-enterprise-messaging-patronen-voor-betrouwbare-koppelvlakken.md); hoe een bericht bij de ontvanger komt is een inrichtingskeuze ([U5](../uitgangspunten.md#u5-bericht-versus-kanaal)).

| Patroon | Waarvoor | Naam uit |
|---|---|---|
| [Event Notification](event-notification.md) | De bezitter meldt dat er iets is, de consument haalt het op wanneer het hem uitkomt | Fowler |
| [Event-Carried State Transfer](event-carried-state-transfer.md) | Het event draagt de wijziging zelf, de ontvanger hoeft niets op te halen | Fowler |
| [Asynchronous Request-Reply](asynchronous-request-reply.md) | De verwerking duurt; de uitkomst komt terug als apart bericht | Azure Cloud Design Patterns, AIP-151 |
| [Request-Reply](request-reply.md) | De afnemer vraagt zelf op, zonder voorafgaand event | Enterprise Integration Patterns |
| [Subscription registration](subscription-registration.md) | Vastleggen waar events afgeleverd mogen worden | WebSub, CloudEvents Subscriptions |

Twee onderscheidingen bepalen de keuze. Of het event genoeg draagt om zonder opvraag te handelen scheidt de eerste twee. Wie begint scheidt de derde van de vierde: bij Asynchronous Request-Reply komt de uitkomst ongevraagd terug op iets dat de ander startte, bij Request-Reply vraagt de afnemer zelf.
