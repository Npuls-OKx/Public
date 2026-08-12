# Referentiesystemen

Het koppelvlak van een component is de optelsom van alle koppelingen die het raken ([instap-README](../README.md), [ADR 0021](../../Referentiemateriaal/adr/0021-koppeling-versus-koppelvlak-terminologie.md)). Deze map maakt die optelsom concreet: één document per systeem, met de endpoints en events die het raken, elk met een verwijzing naar de bron-interactie en de datamodellen die erbij horen. Het is een index, geen eigen bron — bij twijfel is de koppelingspecificatie leidend, en een koppeling zonder uitgewerkt §7 levert hier nog geen rijen op.

| Systeem | Afkorting | Koppelingen | Status | Document |
|---|---|---|---|---|
| Onderwijscatalogus | OC | [P&R](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md), [SIS](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem/onderwijscatalogus-studentinformatiesysteem.md), [LMS](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem/onderwijscatalogus-leermanagementsysteem.md) | P&R op endpointniveau uitgewerkt; SIS en LMS staan met interacties vast (§3) maar nog niet met endpoints (§7) | [onderwijscatalogus.md](onderwijscatalogus.md) |
| Planningssysteem | P | [P&R](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md) | Volledig op endpointniveau uitgewerkt | [planningssysteem.md](planningssysteem.md) |
| Studentinformatiesysteem (KRS/SVS) | SIS | [SIS](../Koppelingspecificaties/onderwijscatalogus-studentinformatiesysteem/onderwijscatalogus-studentinformatiesysteem.md) | Interacties (S1-S5) vastgelegd, endpoints nog niet uitgewerkt | Nog toe te voegen |
| Leermanagementsysteem | LMS | [LMS](../Koppelingspecificaties/onderwijscatalogus-leermanagementsysteem/onderwijscatalogus-leermanagementsysteem.md) | Interacties (L1-L6) vastgelegd, endpoints nog niet uitgewerkt | Nog toe te voegen |
| Roostersysteem | R | Geen — komt alleen als contextdiagram voor ([P&R §5.5](../Koppelingspecificaties/onderwijscatalogus-planning-en-roostering/onderwijscatalogus-planning-en-roostering.md#55-context-doorwerking-naar-het-roostersysteem)) | Geen koppeling gespecificeerd in dit pakket | Nog niet van toepassing |
| Studentkeuzesysteem | SKS | Geen | Eigen koppeling, buiten scope van dit pakket | Nog niet van toepassing |
| Curriculum-ontwerptool | CO | Geen | Levert aan OC, maar die koppeling is geen onderdeel van dit pakket | Nog niet van toepassing |
