# Lifecycle en versionering van onderwijsspecificaties

## Inhoudsopgave

1. [Inleiding](#1-inleiding) (aanleiding, context, doel, scope)
2. [Uitgangspunten](#2-uitgangspunten)
3. [Versioneringsmechaniek](#3-versioneringsmechaniek)
4. [Classificatie van wijzigingen](#4-classificatie-van-wijzigingen)

## 1. Inleiding

### 1.1 Aanleiding en context

**Aanleiding.** Bij het beschrijven van de centrale payload bleef één vraag onbeantwoord: wat gebeurt er als een specificatie wijzigt terwijl studenten al zijn ingeschreven en planning het aanbod al heeft klaargezet? Zonder afspraak daarover weet een afnemer niet waarop hij plant, en kan dezelfde specificatie bij twee systemen een andere betekenis krijgen. De memo "Onderwijs PDCA-cyclus" van Niels leverde de invoer over hoe een instelling haar onderwijs cyclisch herziet.

Onderwijs staat niet stil. Een kerntaak wordt herzien, een keuzedeel vervangen, een examenplan aangescherpt, en dat gebeurt terwijl studenten al aan een opleiding zijn begonnen en planning het aanbod al heeft klaargezet. De vraag is dus niet óf specificaties wijzigen, maar hoe een afnemer weet waarop hij plant of inricht, en wat er gebeurt met wat er al staat.

De [onderwijsspecificatie-payload](payload-onderwijsspecificatie.md) zet daarom een `versie` (semver) op elk niveau en houdt de identiteit van een specificatie los van die versie. Dit document legt uit waarom, en wat dat betekent voor de keten. Ketenoverzicht en begrippen: de [instap in de README](../../README.md#context).

De memo "Onderwijs PDCA-cyclus" van Niels is de invoer: die beschrijft hoe een instelling haar onderwijs cyclisch herziet. De uitgangspunten daaruit staan in [§2](#2-uitgangspunten), vertaald naar wat ze voor de oplossing betekenen.

**Twee dingen die op elkaar lijken maar het niet zijn.** Dit document gaat over de lifecycle van **onderwijsspecificaties**: de inhoud die over de koppeling gaat. Dat is iets anders dan het release-management van de **koppelvlakspecificatie** zelf, dus van de standaard en haar documenten; dat staat in [`doc/OKx_Release-management-en-versionering.md`](https://github.com/Npuls-OKx/meta/blob/d47bb0c74ec899a4384d06331692f74b9bd1db58/doc/OKx_Release-management-en-versionering.md). Een instelling die haar kerntaak herziet raakt het eerste, niet het tweede.

### 1.2 Doel

Dit document beantwoordt drie vragen:

- Wanneer leidt een wijziging tot een nieuwe versie, en wanneer tot een heel nieuwe specificatie?
- Hoe weet een afnemer welke versies bij elkaar horen, en wat er verandert als er één wijzigt?
- Tot welk moment in het proces is een wijziging nog te accepteren?

Geslaagd wanneer een onderwijscatalogus en een afnemer bij dezelfde wijziging tot hetzelfde oordeel komen over wat er moet gebeuren.

Deze uitwerking is indicatief en onderbouwend, net als de koppelingspecificaties die erop steunen ([uitgangspunt U1](../../uitgangspunten.md#u1-indicatief-en-onderbouwend-niet-voorschrijvend)).

Wat dit document nog niet doet: de publicatiegebeurtenis waarmee een catalogus een samenhangende versie van de hele boom vrijgeeft, en de uitgewerkte voorbeelden van gelijktijdig actieve versies over cohorten heen.

### 1.3 Scope

In scope is de lifecycle van onderwijsspecificaties: versienummering, identiteit, geldigheid, status, en de classificatie van wijzigingen. Dit gaat over beleid, niet over techniek. Geldt voor leerroute 1 tot en met 3.

Twee afbakeningen die anders verwarring geven:

- De **techniek** (hoe een wijziging als bericht over de koppeling gaat) staat in de koppelingspecificaties, niet hier.
- Het **release-management van de standaard zelf** is een eigen document, zie §1.1.

Al het overige valt buiten dit document.

## 2. Uitgangspunten

Uit de memo van Niels, met per uitgangspunt wat het voor de oplossing betekent.

| Uitgangspunt | Wat het betekent voor de oplossing |
|---|---|
| Onderdelen hebben een eigen lifecycle | Elke specificatie draagt een eigen `versie`. Een herziene onderwijseenheid dwingt geen nieuwe versie van de hele opleiding af; de opleiding pint alleen een ander versienummer in haar manifest. |
| Identificerende codering en versionering strikt scheiden | Harde eis aan de payload: het id van een specificatie verandert nooit door een inhoudelijke wijziging. Verwijzingen van planning, leeromgeving en studentinformatiesysteem blijven daardoor geldig. |
| Specificaties met aanbod worden gedeactiveerd, niet verwijderd | Zodra er aanbod of een verbintenis aan hangt, is verwijderen geen optie: een lopende student moet herleidbaar blijven tot de versie waarop hij is ingeschreven. Vandaar de status `gedeactiveerd` en de geldigheidsvelden. Geldt voor elke specificatie waaraan aanbod, verbintenis of resultaat hangt. |
| Het examenplan kent de strengste acceptatieregels | Het examenplan is een contractuele afspraak met de student. Elke wijziging vraagt expliciete impactanalyse en besluitvorming, ook wanneer die technisch niet-brekend lijkt. |
| De onderwijscatalogus is verantwoordelijk voor versionering | Er is één partij die versienummers uitgeeft en publiceert, zodat afnemers niet elk hun eigen waarheid opbouwen. Dit gaat over de inhoud, niet over de release van de standaard (§1.1). |

## 3. Versioneringsmechaniek

De payload-kant hiervan (het manifest, met een uitgewerkt voorbeeld) staat in [§3.3 van de onderwijsspecificatie-payload](payload-onderwijsspecificatie.md). Hier het beleid eromheen.

- **Semver per specificatie** (`MAJOR.MINOR.PATCH`): MAJOR is brekend binnen dezelfde identiteit, MINOR is additief, PATCH is een correctie.
- **Identiteit los van versie.** Een fundamentele wijziging, bijvoorbeeld een nieuw kwalificatiedossier of gewijzigde wettelijke eisen, is een **nieuwe specificatie** met een nieuw id, niet een MAJOR-ophoging.
- **Versie als manifest, op elk niveau.** Elke specificatie met onderdelen pint de versies daarvan vast. Zo is een gepubliceerde boom altijd een samenhangend geheel, ook als de onderdelen intussen verder zijn.
- **Impact-gedreven propagatie.** Een MAJOR-ophoging van een onderdeel werkt niet automatisch door naar de opleiding. Dat gebeurt alleen als de afhankelijkheid breekt, dus wanneer leeruitkomsten, weging of het recht op een waardedocument veranderen. Anders is het enkel een nieuwe pin in het manifest.
- **Status-lifecycle**: `concept`, `vastgesteld`, `gepubliceerd`, `gedeactiveerd`, `gearchiveerd`, en `vervallen` waar van toepassing.
- **Geldigheid.** `geldigVanaf` en `geldigTot` maken meerdere gelijktijdig actieve versies mogelijk: de oude versie voor lopende studenten, de nieuwe voor nieuwe instroom.

## 4. Classificatie van wijzigingen

| Type wijziging | Casus | Gevolg |
|---|---|---|
| Fundamenteel | Nieuw kwalificatiedossier, gewijzigde wettelijke eisen, nieuwe onderwijsvisie | Nieuwe specificatie met een nieuw id; meestal alleen voor nieuwe instroom |
| Examenplan | Aanpassing van de summatieve resultaatstructuur | Alleen na expliciete impactanalyse en besluit |
| Onderdeel | Update van een onderwijseenheid- of leeronderdeelspecificatie | Nieuwe versie van het onderdeel; de bovenliggende specificatie volgt alleen bij een brekende afhankelijkheid |
| Niet-brekend | Actualisatie van lessen, materiaal of uitvoeringsvorm | PATCH of MINOR binnen dezelfde identiteit |
| Na planning of roostering | Wijziging nadat aanbod of rooster is gepubliceerd | Alleen bij uitzondering en na ketenafstemming |
