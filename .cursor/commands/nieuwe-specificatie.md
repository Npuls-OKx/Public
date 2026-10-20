Zet een nieuwe koppeling op. $ARGUMENTS

## Voorbereiden

Lees eerst, in deze volgorde:

1. [`Koppelvlakspecificaties/uitgangspunten.md`](../../Koppelvlakspecificaties/uitgangspunten.md) — U1 tot en met U11, de aannames die voor alles gelden
2. [`Koppelvlakspecificaties/Koppelingen/README.md`](../../Koppelvlakspecificaties/Koppelingen/README.md) — wat een koppeling is, de ontwerpregels en het overzicht
3. [`Koppelvlakspecificaties/release-management.md`](../../Koppelvlakspecificaties/release-management.md) §4.2 — wanneer een koppeling een versie krijgt
4. Het [kaderscenario](../../Referentiemateriaal/kaderscenario's/) van de leerroute waar je in werkt
5. Een bestaande koppeling, als spiegel

Vraag de gebruiker welke applicatiedienst de koppeling uitwerkt, wie aanbieder en afnemer zijn, en welke leerroute het scenario is.

## Opzetten

Er is geen template; neem een bestaande koppeling als model. De bestandsnaam is de naam van de koppeling, gelijk aan haar OEAPI-profiel zonder `okx-`.

Een koppeling draagt een kenmerkentabel (Aanbieder, Afnemer, Afgeleid van, Versie, Vereist, OEAPI-profiel), de plaat op de hoofdplaat, de stories die zij invult, en per berichtstroom het doel, de trigger en de initiator, de interactiepatronen en koppelvlakdiensten, de endpoints en het sequentiediagram. De versie blijft `—` tot elke stroom endpoints heeft.

Daarbuiten werk je bij:

- het overzicht in [`Koppelingen/README.md`](../../Koppelvlakspecificaties/Koppelingen/README.md), de pagina's van aanbieder en afnemer in `Applicatiecomponenten/`, en **Gebruikt in** op de koppelvlakdienstpagina's;
- in `Koppelvlakspecificaties/model/`: de koppeling met haar stromen in `koppelingen.c4`, de relaties naar aanbieder, afnemer en applicatiedienst in `applicatiediensten.c4` met een view in `views-hoofdplaat.c4`, en per stroom een sequentiediagram in `views-sequenties.c4`; render daarna met `npm run diagrammen:render`;
- [`release.json`](../../Koppelvlakspecificaties/release.json): de koppeling in de sectie Koppelingen.

## Schrijven

Twee dingen die vaak misgaan:

**Herhaal de uitgangspunten niet.** Noem het uitgangspunt in één regel en link erheen. Dat scheelt herstructureerwerk zodra een uitgangspunt wijzigt, en voorkomt dat de redenering op twee plekken uit elkaar loopt.

**Begin de inleiding bij de aanleiding**, niet bij een beschrijving van het document. Welk probleem of welke waarneming maakte dit nodig? Verwijs daarbij niet naar een issue: dit wordt gereleased.

## Payloads

Een nieuwe payload is een JSON Schema in de [informatie- en gegevensmodellen](../../Informatie-en-gegevensmodellen/README.md), een eigen releasepakket. Enumeraties horen in het schema, niet in een aparte tabel; welke onderdelen een afnemer gebruikt, staat in de gebruiksprofielen daar.

## Afronden

Werk de index bij in de README van de bovenliggende map, en draai `/controleer-document`.
