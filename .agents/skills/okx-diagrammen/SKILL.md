---
name: okx-diagrammen
description: Gebruik deze skill bij het maken of wijzigen van een structuurdiagram in de OKx Public-repository: koppelvlakken, applicatiecomponenten, ketenbeelden. Legt vast dat die uit een LikeC4-model komen in plaats van uit een losse tekening, met de modelleerconventies, de rendervolgorde en de valkuilen van het gereedschap. Trigger op diagram, plaat, koppelvlak tekenen, LikeC4, c4-model, architectuurplaat.
---

# Structuurdiagrammen in OKx Public

Een structuurdiagram is hier geen tekening maar een **afgeleide van een model**. De bron is `.c4`: platte tekst, diffbaar, reviewbaar in een pull request. Daaruit komt de PNG die in de documenten staat, en daaruit komt ook JSON, Mermaid, D2, PlantUML en draw.io als iemand het anders wil gebruiken. Een lezer krijgt dus niet alleen een plaat maar de inhoud erachter; `release.json` levert het model daarom mee.

Wat hier **niet** uit een model komt: de sequentiediagrammen in de koppelingspecificaties. Die blijven mermaid in de markdown. LikeC4 kan ze wel, maar een dynamische view rendert in markdown als stroomdiagram zonder stapnummers, en dat is een verslechtering. Gebruik LikeC4 voor wat er ís, mermaid voor wat er gebeurt.

## Waar het staat en hoe je het draait

| Waar | Wat |
|---|---|
| `Koppelvlakspecificaties/model/` | De bron. `spec.c4` draagt de elementsoorten, de relatiesoorten en de gedeelde stijlgroep; `componenten.c4` de keten; `bouwblokken.c4` de berichtstromen, patronen en schema's; `release.c4`, `migratie.c4`, `situaties.c4` en `paden.c4` het versiescenario; `staalkaart.c4` de overzichten van wat LikeC4 biedt. De views staan in `views-*.c4` |
| `Koppelvlakspecificaties/src/diagrammen/` | De gerenderde platen, in een map per categorie. **Gegenereerd**: render opnieuw, wijzig ze niet |
| `scripts/likec4-render.sh` | Valideert, rendert, zet de marges eromheen en deelt de platen in |
| `scripts/likec4-layout.py` | Berekent de plaatsing van views zonder relaties |
| `scripts/likec4-marge.py` | Zet de platen op een witte ondergrond met lucht eromheen |
| `scripts/likec4-plaatsen.py` | Zet elke plaat in de map van zijn categorie, met een naam uit de titel |

```bash
npm install                    # eenmalig
npm run diagrammen:controle    # syntax en semantiek, plus layout drift
npm run diagrammen:preview     # interactieve preview op localhost
npm run diagrammen:render      # alles opnieuw naar src/
```

**De titel bepaalt waar de plaat landt.** Een view heet `Categorie / Naam`, en daaruit volgt het pad: `Referentie / Koppelvlak van de onderwijscatalogus` wordt `src/diagrammen/referentie/koppelvlak-van-de-onderwijscatalogus.png`. De categorieën zijn `Referentie` (de keten en de koppelvlakken), `Bouwblokken` (waar de versies zitten en hoe ver een wijziging reikt), `Versiescenario`, `Situaties` en `Staalkaart`. Een nieuwe plaat hoeft dus alleen een goede titel te krijgen; map en bestandsnaam volgen vanzelf en hoeven nergens apart te worden bijgehouden.

## Modelleerconventies

**De elementsoorten volgen de begrippen, niet de tekening.** Een `systeem` is een applicatiecomponent uit de keten, een `koppelvlak` de optelsom van de koppelingen die het raken, een `dienst` een applicatiedienst die het component claimt, en een `endpoint` het endpoint waarmee het die dienst levert. Die vier komen één op één uit [`Applicatiecomponenten/`](../../../Koppelvlakspecificaties/Applicatiecomponenten/) en [`Applicatiediensten/`](../../../Koppelvlakspecificaties/Applicatiediensten/). Verzin er niets bij: wijzigt een dienstpagina, dan wijzigt het model mee.

**Elke dienst is een container, ook zonder endpoint.** Levert een dienst zelf niets — de afnemer die ophaalt, de aanbieder die meldt — geef hem dan een blok van de soort `gedrag` dat benoemt wát hij doet: "Haalt het opleidingsaanbod op bij de aanbieder", "Meldt de uitkomst van het planproces". Zonder dat blok rendert dezelfde elementsoort op twee manieren, als omlijnde groep én als vol blok, en dan denkt de lezer dat het om twee verschillende dingen gaat.

**Relaties hangen aan het gedrag, niet aan de dienst.** Het is het ophalen dat aanroept en het melden dat meldt. Gebruik de relatiesoorten: `-[melding]->` voor een dun event met een verwijzing ([U4](../../../Koppelvlakspecificaties/uitgangspunten.md#u4-event-notification)), `-[aanroep]->` voor een synchrone aanroep met antwoord. Let op dat ook de aanbieder van een structuur een gedragsblok heeft: bekendmaken dat er iets is gewijzigd vraagt geen endpoint van hem.

**Maten zet je per elementsoort, niet per element.** Een enkel blok groter maken omdat zijn titel afkapt, verplaatst het probleem naar de uitlijning: binnen dezelfde groep worden de blokken dan ongelijk. Kies de maat die het langste label aankan en geef die aan de hele soort.

## Wat een plaat leesbaar houdt

Richt op ongeveer **1400 pixels paginabreedte**. LikeC4 rendert op 2×, dus een bestand van 3500 tot 4600 pixels breed komt daarop uit op tekst die je nog leest. Dat haal je niet met layoutinstellingen maar met de indeling van de views: één plaat per component in plaats van alles op één plaat. De legenda (`--notation`) staat aan zodat een plaat ook los van het document te lezen is; hij kost ongeveer 700 pixels breedte.

Twee instellingen ruimen loze ruimte op. `autoLayout TopBottom 40 40` zet de afstand tussen rangen en knopen op 40 pixels tegen de standaard 120 en 110. En `padding sm` verkleint de blokken zonder de tekst te verkleinen — let er dan op dat de `technology`-regel bij die maat niet meer wordt getoond en de `description`-regel wél, dus zet de schemanaam van een endpoint in `description`.

## Valkuilen van het gereedschap

**Views zonder relaties krijgen hun plaatsing van `likec4-layout.py`.** Graphviz rijgt de groepen dan aan elkaar met onzichtbare edges van een knoop in de ene groep naar een knoop in de volgende, waardoor een groep onder dát punt hangt in plaats van onder de linkerrand van zijn voorganger. Er blijft ruimte leeg en de volgorde is niet te sturen. Het script rekent die platen daarom zelf uit en legt het resultaat vast als snapshot in `model/.likec4/`. Die map staat naast de bron, niet in de projectroot, en LikeC4 zegt niets als hij er niets vindt. De snapshots bestaan alleen tijdens de rit: de renderstap maakt ze aan voor de export en gooit ze daarna weg. Dat houdt ze een afgeleide, en het voorkomt dat ze meegaan in een release die de modelmap meelevert.

**`likec4 validate` meldt een achtergebleven snapshot als "layout drift".** Normaal zie je dat niet, want de renderstap ruimt ze op. Zie je het toch, dan is een rit afgebroken: gooi `model/.likec4/` weg en render opnieuw.

**`rank same` werkt alleen op knopen.** Een groep is een cluster en krijgt geen rang, dus een rangblok op containers verdwijnt geruisloos uit de gegenereerde graphviz. `rank min` en `rank max` doen binnen een container helemaal niets.

**Een kleur op een tag kleurt alleen de tag-badge.** Wil je een element kleuren op grond van een tag, dan heb je `style element.tag = #x` nodig. Die stijlregels worden op volgorde toegepast, dus een element met twee tags krijgt de kleur van de laatste regel die past.

**Er is geen SVG-export**, alleen PNG en JPG. En een relatie die niet op het niveau van de view is gedeclareerd toont als `[...]`; dat los je op met een samenvattende relatie of een `exclude` per paar.

## Voor je iets voorstelt

```bash
npm run diagrammen:controle
npm run diagrammen:render
python3 scripts/check-links.py <pad>
python3 -m unittest discover -s tests
```

Wat geen script vangt: of de plaat iets toevoegt boven de tekst, en of de begrippen erop dezelfde zijn als in de dienstpagina's. Loop dat met de hand na.
