# Keuzeregelset-aanbieder

Het implementerende component publiceert de regelsets waarmee keuzeruimte wordt begrensd, los van de items waarop ze van toepassing zijn. Aan de andere kant staat een component dat [keuzeregelset-afnemer](keuzeregelset-afnemer.md) implementeert.

## Verplichtingen

Een component dat deze dienst implementeert:

- serveert regelsets als eigen resource, los opvraagbaar van de items waarop ze slaan.
- drukt keuzeregels uit als minimum en maximum per benoemd bereik.
- versioneert elke regelset zelfstandig, en houdt een eerder gebruikte versie opvraagbaar voor verantwoording achteraf.
- gebruikt leeruitkomst-id's als verbindende sleutel, zonder de inhoud van de leeruitkomst mee te leveren.
- meldt een wijziging aan wie zich heeft geabonneerd.

### Endpoints

De endpoints die het component implementeert om deze dienst te leveren.

Dit contract is nog niet uitgewerkt. De dienst volgt uit de requirements; welke endpoints hem dragen ligt nog niet vast.

## Gebruikt in

Nog niet gebruikt in een koppeling in dit pakket.
