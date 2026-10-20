# Gebruiksprofielen

Elke afnemer van de koppeling [Onderwijsspecificatie ophalen](../Koppelvlakspecificaties/Koppelingen/onderwijsspecificatie-ophalen.md) haalt dezelfde onderwijsspecificatie-payload op; per afnemer verschilt welke onderdelen hij gebruikt. Dat verschil staat hier, niet in het schema: het schema legt de vorm vast, het profiel wat een afnemer ervan gebruikt.

| Onderdeel | Planningssysteem | Studentinformatiesysteem (SVS) | Leermanagementsysteem |
|---|---|---|---|
| `onderwijsspecificaties` | Volledig, inclusief manifest | Volledig, inclusief manifest (nominaal template) | Volledig tot en met `leeronderdeelspecificatie` |
| `regelsets` | Volledig; `voorwaardeVooraf` bevat leeruitkomst-ids uitsluitend als **verbindende sleutels** voor volgordebepaling: planning gebruikt ze zonder de inhoud te kennen ([ADR 0026](../Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md)) | Volledig (kiesbaarheid keuzedeelruimte, voorwaarden in behaalde leeruitkomsten) | **Niet nodig.** Kiesbaarheid is het domein van SKS en SIS |
| `leeruitkomsten` | **Niet nodig.** Planning heeft de betekenis, aggregatie en inhoud van leeruitkomsten niet nodig ([ADR 0026](../Referentiemateriaal/adr/0026-leeruitkomst-als-verbindende-sleutel.md)) | **Volledig**, inclusief aggregatie (`bovenliggendLeeruitkomstId`), `waardedocument` en `indicatieveOmvang`: de sleutel tussen specificatie, resultaatstructuur en onderwijsresultaat ([ADR 0022](../Referentiemateriaal/adr/0022-resultaatbegrippen-conform-rosa-koi.md)) | **Met inhoudsvelden** (`omschrijving`, `resultaat`, `gedrag`): dat is precies wat het LMS uitwerkt en aan de student exposet |

Wat een afnemer niet nodig heeft, laat hij liggen. De koppeling verbiedt de aanbieder niet om het mee te leveren, want alle afnemers halen op hetzelfde endpoint op ([ontwerpregels](../Koppelvlakspecificaties/Koppelingen/README.md#ontwerpregels)). Een parameter waarmee een afnemer onderdelen uitsluit, is bij [onderwijsspecificatiestructuur-aanbieder](../Koppelvlakspecificaties/Koppelvlakdiensten/onderwijsspecificatiestructuur-aanbieder.md) nog niet vastgelegd.

De resultaatstructuur haalt het studentinformatiesysteem op in de koppeling [Resultaatstructuur ophalen](../Koppelvlakspecificaties/Koppelingen/resultaatstructuur-ophalen.md), met [result-structure.json](schemas/result-structure.json) als payload.

De payload van de leermiddelkoppeling in [Leeromgeving inrichten](../Koppelvlakspecificaties/Koppelingen/leeromgeving-inrichten.md) is nog niet uitgewerkt. Verwachte kern: `id`, `versie`, en per specificatie de leermiddelgroepen met een `specificatieVerwijzing` (id en versie).
