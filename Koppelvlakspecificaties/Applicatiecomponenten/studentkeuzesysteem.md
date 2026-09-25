# Studentkeuzesysteem (SKS)

Het studentkeuzesysteem is de component waar de student zijn keuzes maakt. Het is bewust als **zelfstandige** referentiecomponent belegd en niet verspreid over portaal, catalogus of leeromgeving, zodat de keuze-interactie expliciet wordt in plaats van verborgen ([ADR 0005](../../Referentiemateriaal/adr/0005-student-keuze-systeem-zelfstandige-referentiecomponent.md)). Het draagt de keuze-interacties van de student; het studentvolgsysteem blijft bij resultaat en voortgang, en de inschrijving blijft bij het kernregistratiesysteem ([ADR 0009](../../Referentiemateriaal/adr/0009-sks-svs-rollenverdeling-keuze-vs-resultaat-voortgang.md), [ADR 0014](../../Referentiemateriaal/adr/0014-splitsing-inschrijving-rodkrs-en-studentkeuze-sks.md)).

Het systeem komt in de procesbeelden voor als de partij die keuzes aan het studentinformatiesysteem levert; die koppeling is een eigen uitwerking en valt buiten de drie koppelingen vanuit de catalogus die hier zijn uitgewerkt.

## Koppelvlak

![Koppelvlak van het studentkeuzesysteem op de hoofdplaat v1.7](../src/koppelvlak_sks_view_ihp_v1_7.png)

De view toont het koppelvlak van het studentkeuzesysteem: de optelsom van zijn koppelingen op de informatiestromen-hoofdplaat v1.7.

## Applicatiediensten

Dit pakket belegt nog geen applicatiedienst bij het studentkeuzesysteem. De requirements wijzen [kiesbaarheidsbepaling-aanbieder](../Applicatiediensten/kiesbaarheidsbepaling-aanbieder.md), [onderwijsaanbod-zoekvraag-afnemer](../Applicatiediensten/onderwijsaanbod-zoekvraag-afnemer.md) en [onderwijsaanbod-haalbaarheidstoets-afnemer](../Applicatiediensten/onderwijsaanbod-haalbaarheidstoets-afnemer.md) aan als de diensten die hier horen.
