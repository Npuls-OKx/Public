# OKx Public — instructies voor agents

Dit is **Public source** van OKx (Onderwijskoppelingen): de publieke bron van de **releaseartefacten**. Geen kennisbasis en geen werkomgeving. Wat hier staat wordt gepubliceerd en door instellingen en leveranciers gebruikt om koppelvlakken te bouwen.

Dat ene feit stuurt alles. De lezer van een document hier is een architect of ontwikkelaar bij een instelling of leverancier, die het jaren later kan opslaan en er een implementatie op baseert. Hij heeft geen toegang tot issues, pull requests of de werksessie waar iets uit voortkwam.

## Lees dit eerst

| Waar | Wat je eruit haalt |
|---|---|
| [`README.md`](README.md) | Wat er in dit repository staat en in welke container |
| [`.cursor/rules/`](.cursor/rules/) | De conventies: governance, structuur, documenten, verwijzingen, stijl |
| [`Koppelvlakspecificaties/uitgangspunten.md`](Koppelvlakspecificaties/uitgangspunten.md) | U1 tot en met U10, de aannames onder alle specificaties |
| [`.agents/skills/okx-public-artefact/`](.agents/skills/okx-public-artefact/) | Hoe je hier een document schrijft, en welke valkuilen erbij horen |

Ga je serieus aan de slag, draai dan eerst `/prep-repo-context`.

## De vijf regels die het vaakst misgaan

1. **Geen issueverwijzingen in documenten.** Geen `#123`, geen `Relateert aan: #12`. Wat zo'n verwijzing droeg is de *aanleiding*; die schrijf je uit in de inleiding. In commit messages en pull requests horen issueverwijzingen juist wél.
2. **De inleiding is zelfdragend**: aanleiding, context, doel en scope, en de scope sluit af met wat er buiten valt.
3. **Verwijzingen naar de meta-repository zijn gepind op een commit**, nooit op een branch. Een gereleased document mag niet meebewegen met zijn onderbouwing.
4. **Geen metadatakop en geen datumprefix in bestandsnamen.** Auteur en datum komen uit de git-historie. Uitzondering: overgenomen bronmateriaal in `Referentiemateriaal/` behoudt de vorm van de bron.
5. **Werk op een feature branch vanaf `dev`.** Nooit rechtstreeks committen op `dev` of een release branch.

## Controleer voordat je iets voorstelt

```bash
python3 scripts/check-links.py        # dode links, ontsnappingen buiten de repo, dode anchors
python3 scripts/check-conventies.py   # issueverwijzingen, metadatakoppen, branchlinks, inleiding
python3 scripts/json-tree.py --check <document>.md    # payload-documenten
```

Alle drie geven exitcode 1 bij een probleem. Een melding wegpoetsen door de controle te versoepelen is geen oplossing; los op wat eruit komt of leg uit waarom het geen probleem is.

Wat geen script vangt: of de aanleiding echt een aanleiding is, of een diagram iets toevoegt boven de tekst, en of de scope werkelijk afsluit. Loop dat met de hand na met `/controleer-document`.

## Commands

`/prep-repo-context`, `/nieuwe-specificatie`, `/overhevelen-uit-meta`, `/controleer-document`, `/release-voorbereiden`, `/commit-message-nl`. Zie [`.cursor/commands/`](.cursor/commands/).

## Waar de skills staan

De inhoud staat in [`.agents/skills/`](.agents/skills/); `.claude/skills` en `.cursor/skills` zijn symlinks daarheen zodat beide tools ze vinden. **Verwijs altijd naar het `.agents/`-pad**: GitHub volgt symlinks niet in blob-URL's, dus een link naar `.claude/skills/...` of `.cursor/skills/...` is in de webweergave dood.

## Wat hier niet thuishoort

Kaderstelling en materiaal dat nog in beweging is rijpen in [`Npuls-OKx/meta`](https://github.com/Npuls-OKx/meta) en komen hierheen zodra ze releasebaar zijn. **Architectuurbesluiten leven hier**, in [`Referentiemateriaal/adr/`](Referentiemateriaal/adr/). De OpenAPI-specificatie leeft in [`Npuls-OKx/specification`](https://github.com/Npuls-OKx/specification). Twijfel je of iets hier hoort: kan een afnemer ermee bouwen, of onderbouwt het iets waarmee hij bouwt? Zo niet, dan hoort het in meta.
