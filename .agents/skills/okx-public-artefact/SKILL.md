---
name: okx-public-artefact
description: Gebruik deze skill bij het schrijven, wijzigen of reviewen van een document in de OKx Public-repository. Bevat de conventies voor gereleasde artefacten (geen issueverwijzingen, zelfdragende inleiding, gepinde verwijzingen naar meta) en de valkuilen die daarbij horen. Trigger op koppelingspecificatie, payload-specificatie, kaderscenario, ankertabel, referentiemateriaal, of overhevelen uit meta.
---

# Een artefact in OKx Public

Dit repository draagt **releaseartefacten**. Het verschil met een kennisbasis bepaalt alles: de lezer is een architect of ontwikkelaar bij een instelling of leverancier, die het document jaren later kan opslaan en er een implementatie op baseert. Hij heeft geen toegang tot issues, pull requests of de werksessie waar iets uit voortkwam.

## De vier conventies

**Geen issueverwijzingen.** Geen `#123`, geen `Relateert aan: #12`, geen `See also #TBD`. Wat zo'n verwijzing impliciet droeg is de *aanleiding*; die schrijf je uit. Issueverwijzingen in commit messages en pull requests zijn juist wél gewenst: die horen bij het werkproces.

**De inleiding is zelfdragend.** Aanleiding, context, doel en scope. De scope sluit af met wat er buiten valt, zodat een lezer niet hoeft te raden of iets vergeten of bewust weggelaten is.

**Geen metadatakop.** Geen status, datum of auteur bovenaan; die komen uit de git-historie. Uitzondering: overgenomen bronmateriaal in `Referentiemateriaal/` behoudt de vorm van de bron, want een ADR hoort een status te dragen.

**Verwijzingen naar meta zijn gepind** op een commit-SHA, nooit op een branch. Een gereleased document mag niet meebewegen met zijn onderbouwing.

## Valkuilen

Deze zijn allemaal een keer misgegaan.

**Een link die buiten de repository wijst, lijkt lokaal goed.** `../../README.md` vanuit een submap kan toevallig resolveren naar een bestand in een naburige map op je schijf, terwijl hij op GitHub altijd stuk is. `check-links.py` vangt dit als `ONTSNAPT`.

**Anchors met een em-streep krijgen een dubbele koppelstreep.** GitHub vervangt *elke* spatie afzonderlijk, dus `### AP05 — Naam` wordt `#ap05--naam`. Wie `\s+` gebruikt in plaats van `\s` concludeert ten onrechte dat de link stuk is.

**`main` en `dev` van meta zijn uiteengelopen.** Ze dragen verschillende inhoud en zelfs verschillende ADR's onder hetzelfde nummer. Ga nooit uit van "main is de stabiele lijn"; controleer per pad waar het staat en of het op de gekozen commit bestaat.

**`.cursor/skills/` in meta is een symlink.** GitHub volgt symlinks niet in blob-URL's, dus zo'n link is daar altijd dood. Pin op het echte pad, `.agents/skills/`.

**Een regel met een issueverwijzing draagt vaak meer.** Sta er ook "Terminologie: ADR 0021" of "Waarden in het voorbeeld zijn indicatief" op, dan verdwijnt die zin mee als je de hele regel schrapt. Zet hem terug op de plek waar hij hoort.

**Een document kan zichzelf verbergen.** Een niet-gesloten `<!--` loopt door tot de eerstvolgende `-->`, ook door code fences heen. In het consumer-profiel van meta verbergt dat 2.244 regels. Controleer de balans als je een extract uit een groter document neemt.

## De taal van het domein

Gebruik de begrippen uit de [ankertabel](../../../Referentiemateriaal/kaderscenario's/leerroute-1-regulier.md#betrokken-informatie-bij-proces), niet eigen termen: kader, beoogde leeruitkomst, specificatie, aanbod, verbintenis, resultaat. De leeruitkomst is de sleutel die de kolommen doorkruist; specificaties verankeren erop en resultaten worden erop behaald.

Een **koppeling** is de informatiestroom tussen twee referentiecomponenten. Een **koppelvlak** is de verzameling koppelingen die één component raken. Componenten benoem je als referentiecomponent, niet als product: OKx beschrijft wat een component doet en hoe het zich in de keten gedraagt, niet welke leverancier het invult.

## Voor je iets voorstelt

```bash
python3 scripts/check-links.py <pad>
python3 scripts/check-conventies.py <pad>
python3 scripts/json-tree.py --check <document>.md
```

Wat een script niet vangt: of de aanleiding echt een aanleiding is, of een diagram iets toevoegt boven de tekst, en of de scope werkelijk afsluit. Loop dat met de hand na, of gebruik `/controleer-document`.
