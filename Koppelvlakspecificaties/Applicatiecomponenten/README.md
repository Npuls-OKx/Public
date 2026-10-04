# Applicatiecomponenten

Het koppelvlak van een component is de optelsom van alle koppelingen die het raken ([instap-README](../README.md), [ADR 0021](../../Referentiemateriaal/adr/0021-koppeling-versus-koppelvlak-terminologie.md)). Deze map maakt die optelsom concreet: één document per systeem, met de [applicatiediensten](../Applicatiediensten/) die het implementeert en de [koppelingen](../Koppelingspecificaties/) waarin het optreedt. Het contract van een dienst — verplichtingen, endpoints, payloads — staat bij die dienst. Elk systeem uit de keten heeft een eigen document, ook wanneer dit pakket er nog geen dienst bij belegt: dan beschrijft het document wat het systeem voorstelt en waar het in de keten staat.


## Ecosysteem

![Informatiestromen-hoofdplaat v1.7](../src/informatiestromen_hoofdplaat_v1_7.png)

De hoofdplaat toont het volledige ecosysteem: alle informatiestromen tussen de applicatiecomponenten in de keten. Versie 1.7 is leidend; de legenda draagt nog de aanduiding "concept", dus de plaat is richtinggevend.

