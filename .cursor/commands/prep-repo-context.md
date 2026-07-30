Doorloop dit repository om te begrijpen hoe het werkt. $ARGUMENTS

Denk grondig. Bereid je voor om het in detail te bespreken. Maak geen nieuwe documenten aan en pas geen bestaande aan.

## Leesvolgorde

1. [`README.md`](../../README.md) — wat dit repository is en welke containers er zijn
2. De rules in [`.cursor/rules/`](../rules/) — governance, structuur, documentconventies, verwijzingen, stijl
3. [`Koppelvlakspecificaties/README.md`](../../Koppelvlakspecificaties/README.md) — de instap op het releasepakket: keten, afkortingen, leesvolgorde
4. [`Koppelvlakspecificaties/uitgangspunten.md`](../../Koppelvlakspecificaties/uitgangspunten.md) — U1 tot en met U10
5. [`Referentiemateriaal/README.md`](../../Referentiemateriaal/README.md) — de onderbouwing en hoe die zich tot het pakket verhoudt

Doe eerst een high-level scan en gebruik daarna, als het nuttig is, subagents om delen dieper te verkennen.

## Let in het bijzonder op

**Het onderscheid koppeling versus koppelvlak.** Een koppeling is de informatiestroom tussen twee referentiecomponenten; het koppelvlak van een component is de verzameling koppelingen die dat component raken. De mapstructuur draagt dat onderscheid.

**De ankertabel.** Zes families over de niveaus van het kwalificatiekader heen: kader, beoogde leeruitkomst, specificatie, aanbod, verbintenis, resultaat. De leeruitkomst is de sleutel die de kolommen doorkruist. Alle payload-specificaties spreken deze taal.

**De verhouding tot de meta-repository.** Materiaal rijpt daar en komt hierheen zodra het releasebaar is. Verwijzingen naar meta zijn gepind op een commit.

## Vraag voordat je verder gaat

Vraag of je de bijbehorende architectuurmodellen in de meta-repository moet begrijpen. Die staan niet in dit repository; ze zijn groot maar richtinggevend. Zo ja, zet een subagent in om dat efficiënt te doen. Zo nee, sla die stap over en gebruik alleen wat hier staat.
