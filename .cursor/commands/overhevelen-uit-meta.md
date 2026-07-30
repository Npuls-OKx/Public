Hevel een artefact over uit de meta-repository naar dit repository. $ARGUMENTS

Materiaal rijpt in meta en komt hierheen zodra het releasebaar is. Overhevelen is geen kopieeractie: de inhoud verandert van karakter, van werkdocument naar releaseartefact, en dat vraagt zeven stappen. Sla er geen over.

## 1. Bepaal wat er meegaat en waarop je pint

Vraag de gebruiker welk artefact mee moet en of de onderbouwing (ADR's, principes, scenario's) meeverhuist of gepind wordt aangehaald.

Bepaal daarna de **commit** waarop je pint, en controleer of die het materiaal draagt:

```bash
git -C <meta> log -1 --format=%H <branch>
git -C <meta> cat-file -e <sha>:<pad>        # per pad dat je gaat aanhalen
```

Let op: `main` en `dev` van meta zijn uiteengelopen. Ze dragen verschillende inhoud en zelfs verschillende ADR's onder hetzelfde nummer. Ga niet uit van "main is de stabiele lijn": controleer per pad waar het staat.

## 2. Kies de plek

Volg de containers uit de rule over repo-structuur. Bepaal per bestand of het **Source Material** is (het releasepakket) of **Reference Material** (onderbouwing). Bij twijfel: kan een afnemer hiermee bouwen, dan is het Source Material.

## 3. Schoon de bestandsnamen op

Weg met datum- en versieprefixen. `20260723_1156_okx-lr1-koppelingspecificatie-oc-p-en-r.md` wordt `koppelingspecificatie-oc-p-en-r.md`. Die prefixen zijn een werkproces-conventie uit meta en horen niet in een releaseartefact.

## 4. Herschrijf alle verwijzingen

Dit is het meeste werk. Inventariseer eerst:

```bash
grep -rhoP '\]\((?!http|#)[^)]+\)' <map> | sort -u
```

Per link drie mogelijkheden:

- **Doel verhuist mee** → relatief pad naar de nieuwe plek.
- **Doel blijft in meta** → absolute URL, gepind op de commit uit stap 1.
- **Doel is een symlink in meta** (`.cursor/skills/`) → pin op het echte pad (`.agents/skills/`), want GitHub volgt symlinks niet in blob-URL's.

Let op verwijzingen die het brondocument zelf al kapot had; repareer die en meld ze terug aan meta.

## 5. Haal de issueverwijzingen eruit

Weg met `Relateert aan: #...`, `- Issues: ...`, `See also #TBD` en kale nummers in lopende tekst.

Inline verwijzingen **herschrijf** je met behoud van betekenis, je schrapt ze niet: "wordt uitgewerkt in #84" wordt "wordt in een aparte uitwerking behandeld".

Kijk uit: een `Relateert aan`-regel draagt vaak méér dan issuenummers. Sta er ook "Terminologie: ADR 0021" of "Waarden in het voorbeeld zijn indicatief" op, zet die zin dan terug op de plek waar hij hoort.

## 6. Maak de inleiding zelfdragend

Wat de issueverwijzing impliciet droeg is de **aanleiding**. Schrijf die uit: welk probleem of welke waarneming maakte dit document nodig? Leid dat af uit het document zelf, verzin geen geschiedenis. Controleer daarna dat context, doel en scope er ook staan.

## 7. Verifieer

```bash
python3 scripts/check-links.py
python3 scripts/check-conventies.py
python3 scripts/json-tree.py --check <document>.md    # payload-documenten
```

Controleer daarnaast met de hand:

- Bestaan alle gepinde meta-paden op de gekozen commit?
- Staan alle afbeeldingen in de nieuwe `img/`, en zijn ze allemaal in gebruik?
- Zijn code fences en HTML-comment-markers in balans, als je een extract uit een groter document hebt genomen?

Meld in de pull request wat je in de bron bent tegengekomen dat daar aandacht vraagt.
