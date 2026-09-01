## Requirementsboom als koppeling tussen business en techniek

Status: Voorstel

Datum: 2026-08-06

### Context

De businesskant (persona's, kaderscenario's, principes, besluiten) en de techniekkant (koppelingspecificaties, payloads, datamodellen, endpointtabellen) staan in de OKx-repositories naast elkaar zonder mechanisme dat ze aan elkaar bindt. Een wijziging in een kaderscenario maakt niet zichtbaar welke specificatie meebeweegt, en een endpoint is niet herleidbaar naar de eis waar het uit voortkomt.

Onderzoek in de meta-repository (drie verslagen plus synthese, zie Relaties) vergeleek hoe HL7 FHIR, TM Forum, SEMIC, Logius, VNG Realisatie en Haal Centraal dit oplossen, wat AMIGO v1.1.0 voorschrijft en welk gereedschap past. Een sparsessie op 5 augustus 2026 bracht daar de vorm bij die functionele en businessstakeholders wél kunnen dragen.

### Beslissing

1. **De requirementsboom is de getoonde koppeling tussen business en techniek**: een gelaagde breakdown van opdracht (Leren zonder Drempels) via epics en features naar stories, met één document per laag en een index, in deze repository onder `Referentiemateriaal/requirementsboom/`, naast de koppelvlakspecificaties die de stories aanwijzen.
2. **Elke rij draagt een bron** (vastgesteld document, ADR of meetingverslag); wat niet herleidbaar is staat op een parkeerlijst, niet in de boom.
3. **Stories eindigen bij de techniek**: een story noemt de interactie in een koppelingspecificatie en het systeem dat eigenaar wordt van de bijbehorende endpoint-set. De redenering is: wie deze featureset wil ondersteunen, wordt eigenaar van deze endpoints; hoe een leverancier dat intern oplost valt buiten de standaard.
4. **Eis-identificatienummers en uitvoerbare scenario's zijn achtergrondmechaniek**, niet de getoonde koppeling. Ze worden gefaseerd ingevoerd zodra de boom zich bewezen heeft, te beginnen met een proef op één koppelingspecificatie.
5. **De boom in git is de bron voor planning**: een agent-omzetting vertaalt de vastgestelde boom naar milestones en issues (epic wordt milestone, feature en story worden issues met terugverwijzing), zodat de product owner in issues werkt zonder de boom te bewerken.

### Alternatieven

- **Het identificatienummer draagt de koppeling** (Logius API Design Rules, OpenFastTrace-notatie). Sterkste traceerbaarheid per regel notatie, maar te technisch als primaire laag: functionele en businessstakeholders herkennen "ID gekoppeld aan ID op de implementatielaag" niet, en volledige synchronisatie blijkt in de praktijk niet vol te houden (FHIR heeft het veld `Requirements.statement.satisfiedBy` en nul invullingen tegenover 6760 profielen). Blijft als achtergrondmechaniek in beeld (beslispunt 4).
- **Het model draagt de koppeling** (AMIGO paragraaf 5.4: technische modellen gegenereerd uit logische modellen). Volledig methodiek-conform, maar vraagt een generatieketen en toolbezit die er nu niet zijn; SEMIC laat zien hoe een expressief bronformaat samengaat met een verschraalde praktijk. AMIGO-principe I1 staat gefaseerde invoering toe; dit blijft de stip op de horizon voor de gegevensanalyse.
- **De test draagt de koppeling** (Haal Centraal: het scenario is specificatie, test en publicatie tegelijk). Sterkste borging dat een eis blijft werken, maar toont de businesslaag niet als leesbare ingang en vraagt een implementatie om tegen te draaien. Volgt gefaseerd samen met de identificatienummers (beslispunt 4).
- **ArchiMate-relaties tussen businesslaag en implementatie.** Afgewezen als koppelmechanisme: het onderzoek laat zien dat dit patroon in de praktijk doodbloedt zodra de synchronisatielast stijgt, en het model is voor niet-architecten onleesbaar.

### Consequenties

- Deze repository draagt onder `Referentiemateriaal/requirementsboom/` zes documenten met harde omvangslimieten (overzicht boven volledigheid); uitbreiding gebeurt vanuit de parkeerlijst, per pull request, bewaakt door de navigatiecontrole in de CI (`scripts/validate-requirementsboom-navigatie.py`).
- De product owner leest de bovenste twee lagen (opdracht en epics); de technische werkgroep en leveranciers lezen features en stories met de koppelvlakverwijzingen.
- De koppelvlakspecificaties worden vanuit stories aangewezen én wijzen terug: elke functionele eis draagt een Story-kolom met de stories die hem dragen. Nieuwe interacties horen vanaf nu een story als tegenhanger te hebben.
- Open beheervraag, belegd bij het kernteam: wie onderhoudt de boom na de proof of concept, en kan de business de doorverwijzingen (interacties, later eis-identificatienummers) zelf definiëren en bijhouden? De agent-omzetting naar milestones en issues (beslispunt 5) is het voorstel, nog geen besluit.
- Richting AMIGO geldt comply or explain: de traceerbaarheidsrelaties uit paragraaf 5.4 worden deels ingevuld door de boom met bronplicht; de generatie uit logische modellen is uitgesteld en hier uitgelegd.
- Geen wijziging aan `architecture/model/model.archimate` in de meta-repository; de boom staat bewust los van het model.

### Relaties en links

- Issue: [meta-issue 130](https://github.com/Npuls-OKx/meta/issues/130) (onderzoek en proof of concept), [meta-issue 135](https://github.com/Npuls-OKx/meta/issues/135) (identificatienummer-conventie, geparkeerd als achtergrondmechaniek)
- PR: [meta-PR 131](https://github.com/Npuls-OKx/meta/pull/131) (onderzoek, synthese en de requirementsboom zelf)
- Overheveling: [Public-issue 33](https://github.com/Npuls-OKx/Public/issues/33) — de boom van de meta-repository naar `Referentiemateriaal/requirementsboom/`, met terugleiding van de functionele eisen en de navigatiecontrole in de CI
- Onderzoek: de drie verslagen en de synthese onder `architecture/agent-artifacts/research/` in de meta-repository (via meta-PR 131), waaronder de vergelijking van de drie koppelmechanismen en de AMIGO-toets
- Meetings: sparsessie 5 augustus 2026 (vastgelegd in de extractieverantwoording bij meta-PR 131); meetingverslagen maart tot en met juli in `architecture/meetings/` (meta)
- ArchiMate-model: `architecture/model/model.archimate` (meta), geen wijziging
- OKx-docs: `Koppelvlakspecificaties/` (interacties en endpoint-sets waar stories naar verwijzen), `Referentiemateriaal/kaderscenario's/`
