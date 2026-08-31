## Koppelvlak curriculumontwerp-onderwijscatalogus krijgt geen prioriteit

Status: Voorstel

Datum: 2026-08-28

### Context

De [curriculum-ontwerptool](../../Koppelvlakspecificaties/Applicatiecomponenten/curriculum-ontwerptool.md) staat als applicatiecomponent in de koppelvlakspecificaties: het is de plek waar onderwijsspecificaties ontworpen worden voordat de onderwijscatalogus ze ontsluit (prioriteitsketen, ADR 0002). Voor de koppeling tussen curriculumontwerp en de catalogus (CO-OC) is echter geen interactiepatroon gespecificeerd, en de vraag lag voor of dat alsnog moest gebeuren.

Twee waarnemingen bepalen het antwoord. Er is op dit moment **geen marktpartij** die een curriculumontwerp-systeem levert dat dit koppelvlak zou implementeren; instellingen ontwerpen curricula in de praktijk in uiteenlopende, vaak leverancierseigen of handmatige vormen. En de beproevingscapaciteit van OKx ligt bij de koppelingen waar wél implementerende partijen voor bestaan: onderwijscatalogus naar planning en roostering, studentinformatiesysteem en leermanagementsysteem.

### Beslissing

1. **Voor de koppeling curriculumontwerp-onderwijscatalogus wordt in de huidige scope geen interactiepatroon gespecificeerd.**
2. De curriculum-ontwerptool **blijft als applicatiecomponent benoemd** in de architectuur: de bron-rol van curriculumontwerp voor de catalogus blijft bestaan, ook als de aanlevering voorlopig buiten de gestandaardiseerde koppelvlakken om loopt.
3. **Herzieningsvoorwaarde**: dit besluit wordt heroverwogen zodra een marktpartij zich aandient die het koppelvlak wil implementeren, of een pilot er aantoonbaar om vraagt. Heroverweging loopt via een nieuw besluit of een amendement op dit besluit.

### Alternatieven

- **Het koppelvlak nu toch specificeren**: afgewezen. Een specificatie zonder implementerende partij kan niet beproefd worden, terwijl beproeven met pilots een kernonderdeel van de aanpak is; het document zou ongetoetst verouderen en schijnzekerheid bieden.
- **De component uit de architectuur schrappen**: afgewezen. De prioriteitsketen (ADR 0002) begint bij het curriculumontwerp als bron; die rol verdwijnt niet doordat het koppelvlak nog niet gestandaardiseerd is. Schrappen zou de herkomst van onderwijsspecificaties onzichtbaar maken.

### Consequenties

- Voor informatiemanagers van instellingen: de instroom van onderwijsspecificaties vanuit curriculumontwerp naar de catalogus valt buiten de huidige gestandaardiseerde koppelvlakken. Hoe die instroom nu verloopt (handmatig, leverancierseigen) is een instellingskeuze; de catalogus blijft wel de formeel vastgestelde bron voor de keten erachter.
- De koppelvlakspecificaties concentreren zich op de drie koppelingen met implementerende partijen; de requirementsboom en de releaseplanning volgen die prioriteit.
- Geen impact op het ArchiMate-model in de meta-repository; de component en zijn relaties blijven staan.

### Relaties en links

- ADR: [0002: prioriteitsketen catalogus](0002-prioriteitsketen-catalogus-drielagen-fundament.md)
- Applicatiecomponent: [curriculum-ontwerptool](../../Koppelvlakspecificaties/Applicatiecomponenten/curriculum-ontwerptool.md)
- ArchiMate model: geen wijziging
