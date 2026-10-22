# Afleverabonnement-afnemer

Het implementerende component legt zijn afleveradres vast bij het component waarvan het meldingen wil ontvangen. Dat andere component implementeert [afleverabonnement-aanbieder](afleverabonnement-aanbieder.md).

## Verplichtingen

Een component dat deze dienst implementeert:

- legt afleveradres en soorten meldingen vast voordat er meldingen worden verwacht.
- verwerkt een herregistratie als vervanging van de vorige, niet als een extra.
- houdt de bevestigde identiteit vast, zodat de registratie te wijzigen of in te trekken is.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Geen eigen endpoint: het component verstuurt alleen, met `POST /abonnementen` bij [afleverabonnement-aanbieder](afleverabonnement-aanbieder.md). De meldingen zelf neemt het aan op de endpoints van de afnemerdienst waarop het abonnement slaat, zoals `specificatie-beschikbaar` bij [onderwijsspecificatiestructuur-afnemer](onderwijsspecificatiestructuur-afnemer.md); de `callbackUrl` wijst naar zo'n endpoint.

## Gebruikt in

- [Afleverabonnement registreren](../Koppelingen/afleverabonnement-registreren.md)
