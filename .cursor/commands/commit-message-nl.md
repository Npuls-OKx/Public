Schrijf een commit message die ik kan copy-pasten.

- Samenvatting in 50 tekens of minder, gebiedende wijs, geen punt aan het eind.
- Daarna een lege regel.
- Daarna een toelichting, afgebroken op ongeveer 72 tekens per regel.
- Leg uit **welk probleem dit oplost en waarom** deze wijziging nodig is. Wat er is veranderd staat al in de diff; waarom niet.
- Alinea's gescheiden door lege regels. Bullets mogen (`- `).

Noem expliciet wat je bij het maken van de wijziging bent tegengekomen dat de reviewer moet weten: een fout die al in de bron zat, een aanname die je hebt gemaakt, iets dat je bewust hebt laten liggen.

Sluit af met de gekoppelde issues, als die er zijn:

```
Fixes #...
See also #...
```

Issueverwijzingen horen **wel** in een commit message en pull request, en **niet** in de documenten zelf: die worden gereleased en gelezen door mensen zonder toegang tot dit werkproces.

Kun je geen issue afleiden, vraag de gebruiker dan of er een is in plaats van er een te verzinnen.

Output alleen de commit message, geen extra uitleg. Pas geen bestanden aan tijdens deze stap.
