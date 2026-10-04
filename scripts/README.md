# Scripts

Gereedschap om te controleren wat machinaal te controleren is, en om het releasepakket te bouwen. Draai ze vanuit de repo-root.

| Script | Wat het doet |
|---|---|
| [`check-links.py`](check-links.py) | Vangt dode links, links die buiten de repository wijzen, links door een symlink heen, dode anchors |
| [`check-conventies.py`](check-conventies.py) | Vangt issueverwijzingen, metadatakoppen, datumprefixen, links naar een meta-branch in plaats van een commit, onvolledige inleidingen |
| [`json-tree.py`](json-tree.py) | Vangt drift tussen de JSON, het schema en de gegenereerde bomen in een payload-document |
| [`build-release.py`](build-release.py) | Bouwt het releasepakket: docx-documenten uit de markdown-bronnen |
| [`validate-requirementsboom-navigatie.py`](validate-requirementsboom-navigatie.py) | Vangt gebroken navigatie in de requirementsboom: dode ankers, eenzijdige laagverwijzingen, terugleiding die niet spoort met de stories |
| [`likec4-render.sh`](likec4-render.sh) | Rendert de LikeC4-views van een pakket naar PNG: valideren, plaatsing berekenen, exporteren, marge eromheen |
| [`likec4-layout.py`](likec4-layout.py) | Berekent de plaatsing van views zonder relaties, waar graphviz geen bruikbare oplevert |
| [`likec4-marge.py`](likec4-marge.py) | Zet een geëxporteerde plaat op een witte ondergrond met lucht eromheen |
| [`likec4-plaatsen.py`](likec4-plaatsen.py) | Zet elke plaat in de map van zijn categorie, met een bestandsnaam uit de titel van de view |

```bash
python3 scripts/check-links.py                    # hele repository
python3 scripts/check-conventies.py <pad>         # of alleen een map of bestand
python3 scripts/json-tree.py --check <doc>.md     # controleren
python3 scripts/json-tree.py --write <doc>.md     # bomen bijwerken
python3 scripts/validate-requirementsboom-navigatie.py   # requirementsboom
python3 -m unittest discover -s tests             # testgevallen van de scripts

python3 scripts/build-release.py Koppelvlakspecificaties --uit dist
python3 scripts/build-release.py "Informatie-en-gegevensmodellen" --alleen-controle

npm run diagrammen:controle                       # LikeC4-model valideren
npm run diagrammen:render                         # de platen opnieuw renderen
```

De vier `likec4`-scripts horen bij elkaar en worden via `npm run diagrammen:render` in de goede volgorde gedraaid; zie [`.agents/skills/okx-diagrammen/`](../.agents/skills/okx-diagrammen/SKILL.md) voor wat ze doen en waarom de plaatsing apart wordt berekend.

De controlescripts geven exitcode 1 bij een probleem, zodat ze in een pre-commit hook of workflow passen.

## Testgevallen

Elk script draagt expliciete, naloopbare testgevallen in [`tests/`](../tests/) (`tests/test_<naam>.py`, standaardbibliotheek `unittest`, draaibaar met `python3 -m unittest discover -s tests`). Elk geval volgt de given-when-then-conventie in methodenaam en teststructuur, met onafhankelijke verwachtingen (geen hardgecodeerde momentopnamen van repo-inhoud). Een pull request die een script toevoegt of wijzigt, rapporteert per testgeval wat er gedraaid is en wat het resultaat was; "getest" zonder naloopbare gevallen telt niet als verificatie. De testrun draait mee in de CI (`validatie.yml`).

## Waarom deze controles bestaan

Elk van deze checks vangt een fout die een keer is gemaakt.

`check-links.py` lost paden **lexicaal** op in plaats van ze te resolven, precies zoals GitHub dat doet. Daardoor vangt hij twee dingen die een gewone bestandscontrole mist: een link die met genoeg `../` *buiten* de repository wijst en lokaal toevallig resolveert naar een bestand in een naburige map, en een link die door een **symlink** heen loopt. Beide werken op je eigen schijf en zijn stuk in de webweergave.

Het anchor-algoritme volgt dat van GitHub, waar elke spatie afzonderlijk een koppelstreep wordt: een em-streep in een kop levert daardoor een dubbele koppelstreep op.

## Het releasepakket bouwen

`build-release.py` schrijft het gebundelde document eerst als markdown in de pakketmap ([`Koppelvlakspecificaties/koppelvlakspecificatie.md`](../Koppelvlakspecificaties/koppelvlakspecificatie.md)) en bouwt de artefacten daaruit. Dat bestand is gegenereerd; `--alleen-controle` faalt wanneer het niet meer overeenkomt met de bronnen, zodat een wijziging met de hand opvalt. Verder maakt `build-release.py` van de markdown-bronnen twee artefacten: één gebundeld document met alle documenten in leesvolgorde, en de documenten los in een zip met de mapstructuur erbij. Welke documenten meegaan, in welke volgorde, en onder welke versie staat in het manifest van het pakket: [`Koppelvlakspecificaties/release.json`](../Koppelvlakspecificaties/release.json). Documenten die bij elkaar horen kun je daar als **sectie** opnemen (`{"sectie", "inleiding", "documenten"}`); ze worden dan subhoofdstukken onder één kop, zoals de applicatiecomponenten. In de losse documenten verandert dat niets. Een nieuw pakket krijgt een eigen map met een eigen `release.json`; het script en de workflow werken dan zonder aanpassing, want die zoeken de pakketmappen zelf op.

Bouwt een pakket op een ander, dan noemt zijn manifest dat onder `afhankelijkheden`, met de versie erbij — de koppelvlakspecificatie doet dat voor de informatie- en gegevensmodellen. Verwijzingen die in zo'n pakket landen krijgen de tag van díe versie in plaats van de ref die nu gebouwd wordt; anders zou een verwijzing stilzwijgend meebewegen met wat er later in het andere pakket landt. Staat dat pakket inmiddels op een hogere versie, dan faalt de bouw met de vraag vast te stellen of de wijziging hier doorwerkt.

Drie dingen doet het script die pandoc alleen niet doet.

**Mermaid renderen.** De specificaties dragen tientallen mermaid-diagrammen. Pandoc kent mermaid niet en zou die codeblokken als letterlijke tekst afdrukken. Elk blok gaat daarom eerst door mermaid-cli naar een PNG.

**Verwijzingen herschrijven.** In een docx bestaat `../Koppelingspecificaties/...md#anchor` niet. In het gebundelde document worden verwijzingen tussen documenten interne verwijzingen; in de losse documenten, en voor alles buiten het pakket zoals `Referentiemateriaal/`, worden het GitHub-URL's op de gebouwde ref. Die blijven altijd werken, ook als iemand het document jaren later opent.

**Botsende anchors voorkomen.** Meerdere documenten dragen een kop `## 3. Interactieoverzicht`. Gebundeld levert dat dubbele id's op, en dan landt een verwijzing stilzwijgend in het verkeerde hoofdstuk. Elke kop krijgt daarom een id met het document als voorvoegsel.

Lokaal bouwen vraagt `pandoc`, `node` en `npx`. In de workflow staat pandoc op een vaste versie: een releaseartefact hoort reproduceerbaar te zijn, en de pandoc uit apt verschilt per runner-image.

## Wat er in CI draait

| Workflow | Wanneer | Wat |
|---|---|---|
| [`validatie.yml`](../.github/workflows/validatie.yml) | pull request, push naar `dev` | De drie controlescripts, plus een bouwcontrole die bewijst dat elk pakket nog te bouwen is |
| [`release.yml`](../.github/workflows/release.yml) | push naar `release-*` | Bouwt elk pakket en zet het klaar als **concept**-release, elk onder een eigen tag |

Het publiceren van een concept-release blijft handwerk. Dat is met opzet: het [releaseproces](../Algemeen/release-management/Release-management-algemeen.md#6-releaseproces) legt de kwaliteitstoets bij de Tester, en een workflow die zelf publiceert zou die stap overslaan.

De versie komt uit `release.json`, niet uit een tag: de bron bepaalt welke versie hij draagt, de tag is het gevolg. De workflow zet die tag bij het bouwen en bouwt er ook mee, zodat de verwijzingen in de uitgeleverde documenten naar de tag wijzen en niet naar de release branch. Staat er een versie in die al gepubliceerd is, dan faalt de workflow met de vraag om de versie te verhogen. De tag draagt de pakketnaam (`koppelvlakspecificatie-v1.2.0`), omdat deze repository meerdere releasepakketten bevat en een kale `v1.2.0` dan niet zegt waarover het gaat.
