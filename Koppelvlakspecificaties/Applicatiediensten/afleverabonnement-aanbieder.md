# Afleverabonnement-aanbieder

Het implementerende component stelt de mogelijkheid beschikbaar om vast te leggen waar en waarvoor een ander component meldingen wil ontvangen. Elk component dat meldingen doet kan deze dienst implementeren; aan de andere kant staat een component dat [afleverabonnement-afnemer](afleverabonnement-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- neemt een registratie aan met een afleveradres en de soorten meldingen waarvoor die geldt.
- maakt herregistratie idempotent op de combinatie van adres en soort: de vorige wordt overschreven, er ontstaat geen dubbele aflevering.
- bevestigt met een identiteit waarmee de registratie later te wijzigen of in te trekken is.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

| Endpoint | Methode | Parameters | Request | Response | Statuscodes |
|---|---|---|---|---|---|
| `/abonnementen` | POST | — | [subscription.json](../../Informatie-en-gegevensmodellen/schemas/subscription.json): `callbackUrl` en de soorten meldingen | Abonnement-id | 201, 400 |

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)
