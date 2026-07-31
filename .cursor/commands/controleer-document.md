Controleer een document voordat het als pull request wordt voorgesteld. $ARGUMENTS

Zonder pad: controleer alles wat op deze branch is gewijzigd ten opzichte van `dev`.

## Machinaal

Draai vanuit de repo-root en los op wat eruit komt:

```bash
python3 scripts/check-links.py <pad>
python3 scripts/check-conventies.py <pad>
python3 scripts/json-tree.py --check <pad>    # alleen payload-documenten
```

Repareer, draai opnieuw, en meld het resultaat feitelijk. Een melding wegpoetsen door de controle te versoepelen is geen oplossing.

## Met de hand

De volgende dingen vangt geen script. Loop ze langs en meld per punt of het klopt.

**De inleiding is zelfdragend.** Kan iemand die de keten niet kent na alleen de inleiding zeggen of dit document zijn vraag beantwoordt? Staan aanleiding, context, doel en scope er alle vier, en sluit de scope af met wat er buiten valt?

**De aanleiding is echt een aanleiding.** Niet "dit document beschrijft X" maar welk probleem of welke waarneming het nodig maakte.

**Eén drager per informatie-eenheid.** Zeggen een diagram, een tabel en een alinea hetzelfde? Kies er één.

**Verwijzingen zijn links**, ook in tabellen en ook naar besluiten. Geen kale "zie ADR 0021".

**Afkortingen** staan voluit bij eerste gebruik of in een legenda.

**Geen statusaanduiding** in titel, doel of scope. De volwassenheid van een schema noteer je op dat schema.

**De README van de bovenliggende map** noemt dit document, als het nieuw is.

**Afbeeldingen** staan in de `img/` naast het document, en er staan er geen ongebruikte.

## Melden

Geef de uitkomst per controle, met het aantal gevonden en opgeloste problemen. Zeg expliciet wat je niet hebt kunnen controleren en waarom.
