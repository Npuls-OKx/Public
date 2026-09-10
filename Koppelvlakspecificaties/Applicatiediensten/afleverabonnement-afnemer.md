# Afleverabonnement-afnemer

Kan zijn afleveradres vastleggen bij een partij van wie hij meldingen wil ontvangen.

## Doel

Er gaan geen meldingen verloren omdat de afzender niet weet waar hij ze kwijt kan.

## Verplichtingen

Een component dat deze dienst implementeert:

- legt afleveradres en soorten meldingen vast voordat er meldingen worden verwacht.
- verwerkt een herregistratie als vervanging van de vorige, niet als een extra.
- houdt de bevestigde identiteit vast, zodat de registratie te wijzigen of in te trekken is.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Geen. Deze dienst vraagt geen eigen endpoints: de afnemer registreert zich bij de aanbieder en stelt zelf niets beschikbaar.

## Gebruikt in

- [Onderwijscatalogus naar planning en roostering](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering.md)

## Tegenhanger

[Afleverabonnement-aanbieder](afleverabonnement-aanbieder.md)
