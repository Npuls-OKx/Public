Bereid een release van een pakket in dit repository voor. $ARGUMENTS

Een release is het besluit om een vastgelegde inhoud beschikbaar te stellen aan afnemers. Niet elke merge is een release.

## 1. Bepaal het pakket en de scope

Welk releasepakket gaat eruit, en welke wijzigingen zitten erin sinds de vorige versie?

```bash
git log --oneline <vorige-tag>..dev -- <pakketmap>
```

## 2. Bepaal de bump

SemVer, en de **zwaarste wijziging wint**: één breaking change maakt de hele release major.

| Bump | Wanneer |
|---|---|
| **MAJOR** | Niet-backward-compatibel. Bestaande implementaties of interpretaties worden ongeldig: een begrip of een rij of kolom in de ankertabel wijzigt waardoor eerdere mapping niet meer klopt, een cardinaliteit verandert, of iets dat optioneel was wordt verplicht |
| **MINOR** | Nieuwe, niet-breaking mogelijkheid: nieuw optioneel veld, nieuw scenario, nieuwe koppeling, nieuwe enum-waarde |
| **PATCH** | Correctie zonder semantische wijziging: typefix, verduidelijking, gerepareerde link of voorbeeld |

Twijfel je tussen minor en major, dan is het major. Een breaking change hoort al tijdens refinement helder te zijn, niet pas bij de release.

## 3. Controleer de baseline

Draai over de volledige pakketmap:

```bash
python3 scripts/check-links.py <pakketmap>
python3 scripts/check-conventies.py <pakketmap>
python3 scripts/json-tree.py --check <elk payload-document>
```

Loop daarnaast langs: staat er nog een open punt in dat de release blokkeert, en klopt elke README-index?

## 4. Stel de release notes samen

Per wijziging: wat is er veranderd, wat is de impact, en welke actie moet een afnemer ondernemen. Bij een major: een migratiehandleiding met wat er breekt, wat te doen en welk migratievenster geldt.

Patches krijgen een korte feitelijke regel; minor en major een uitgebreidere toelichting.

## 5. Leg het voor

Een release vraagt bekrachtiging door het eigenaar-team en communicatie via de standaardroute. Stel de bump en de notes voor; het besluit is niet aan de agent.

Draai geen `git tag` en publiceer geen release zonder expliciete opdracht.
