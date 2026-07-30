# Wat verandert er

<!-- In een paar zinnen: welk probleem lost dit op, en waarom nu. Wat er precies is
     gewijzigd staat in de diff; het waarom niet. -->

## Aanleiding

<!-- Koppel het issue: Fixes #... of See also #...
     Issueverwijzingen horen hier en in de commit message, en NIET in de documenten
     zelf: die worden gereleased en gelezen door mensen zonder toegang tot dit
     werkproces. -->

## Type wijziging

- [ ] **Patch** — correctie zonder semantische wijziging (typefix, verduidelijking, gerepareerde link of voorbeeld)
- [ ] **Minor** — nieuwe, niet-breaking mogelijkheid (nieuw optioneel veld, nieuw scenario, nieuwe koppeling)
- [ ] **Major** — breaking: bestaande implementaties of interpretaties worden ongeldig

Bij twijfel tussen minor en major is het major. De zwaarste wijziging bepaalt de bump.

## Controles

Gedraaid vanuit de repo-root:

- [ ] `python3 scripts/check-links.py` — schoon
- [ ] `python3 scripts/check-conventies.py` — schoon
- [ ] `python3 scripts/json-tree.py --check <document>.md` — schoon, voor elk gewijzigd payload-document

## Conventies

- [ ] Geen issueverwijzingen in de documenten
- [ ] De inleiding benoemt aanleiding, context, doel en scope, en de scope sluit af
- [ ] Geen metadatakop, geen statusaanduiding in titel of doel, geen datumprefix in bestandsnamen
- [ ] Verwijzingen naar de meta-repository zijn gepind op een commit, niet op een branch
- [ ] De README van de bovenliggende map noemt nieuwe documenten

## Wat de reviewer moet weten

<!-- Aannames die je hebt gemaakt, fouten die al in de bron zaten, dingen die je
     bewust hebt laten liggen. Liever hier dan dat een reviewer het zelf ontdekt. -->
