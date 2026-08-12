# Mapping veldnamen: Engels (UK) naar Nederlands

De veldnamen in de datamodelschema's ([`Datamodelschema's/`](Datamodelschema's/)) zijn vertaald van Nederlands naar Engels (UK). Dit document legt per model vast welke Engelse veldnaam bij welke oorspronkelijke Nederlandse naam hoort, zodat wie de modellen kent vanuit eerdere Nederlandstalige documentatie of werksessies de nieuwe velden kan terugvoeren op de bekende termen.

Elke tabel dekt de velden van één schema. Velden in geneste objecten — de items van een array-eigenschap — staan in een aparte tabel direct daaronder, met een verwijzing naar de eigenschap waar ze bij horen. Vertaald zijn alleen de veldnamen: de sleutels onder `properties` en `required`. Enumeratiewaarden (zoals status- en typewaarden), `$id`, bestandsnamen en de `title`- en `$comment`-velden van de schema's blijven ongewijzigd Nederlands.

## Abonnement — Subscription

[`subscription.json`](Datamodelschema's/subscription.json)

| English (UK) | Nederlands |
|---|---|
| id | id |
| callbackUrl | callbackUrl |
| events | events |

## Adres — Address

[`address.json`](Datamodelschema's/address.json)

| English (UK) | Nederlands |
|---|---|
| street | straat |
| houseNumber | huisnummer |
| postcode | postcode |
| city | plaats |
| country | land |

## Bron — Source

[`source.json`](Datamodelschema's/source.json)

| English (UK) | Nederlands |
|---|---|
| standard | standaard |
| type | type |
| code | code |

## Code — Code

[`code.json`](Datamodelschema's/code.json)

| English (UK) | Nederlands |
|---|---|
| codeType | codeType |
| code | code |

## Geolocatie — Geolocation

[`geolocation.json`](Datamodelschema's/geolocation.json)

| English (UK) | Nederlands |
|---|---|
| latitude | breedtegraad |
| longitude | lengtegraad |

## Groep — Group

[`group.json`](Datamodelschema's/group.json)

| English (UK) | Nederlands |
|---|---|
| id | id |
| name | naam |
| capacity | capaciteit |

## Knelpunt — Bottleneck

[`bottleneck.json`](Datamodelschema's/bottleneck.json)

| English (UK) | Nederlands |
|---|---|
| code | code |
| description | omschrijving |
| involvedSpecificationIds | betrokkenSpecificatieIds |

## Leeruitkomst-aanduiding — Learning outcome designation

[`learning-outcome-designation.json`](Datamodelschema's/learning-outcome-designation.json)

| English (UK) | Nederlands |
|---|---|
| type | type |
| code | code |

## Leeruitkomst — Learning outcome

[`learning-outcome.json`](Datamodelschema's/learning-outcome.json)

| English (UK) | Nederlands |
|---|---|
| id | id |
| version | versie |
| name | naam |
| source | bron |
| parentLearningOutcomeId | bovenliggendLeeruitkomstId |
| indicativeVolume | indicatieveOmvang |
| nlqfLevel | nlqfNiveau |
| credentialDocument | waardedocument |
| description | omschrijving |
| result | resultaat |
| behaviour | gedrag |

## Locatie — Location

[`location.json`](Datamodelschema's/location.json)

| English (UK) | Nederlands |
|---|---|
| id | id |
| locationType | locatieType |
| name | naam |
| partOfLocationId | valtBinnenLocatieId |
| address | adres |
| geolocation | geolocatie |
| floor | verdieping |
| wing | vleugel |
| url | url |
| codes | codes |

## Manifest-item — Manifest item

[`manifest-item.json`](Datamodelschema's/manifest-item.json)

| English (UK) | Nederlands |
|---|---|
| specificationId | specificatieId |
| version | versie |
| relation | relatie |

## Omvang — Volume

[`volume.json`](Datamodelschema's/volume.json)

| English (UK) | Nederlands |
|---|---|
| value | waarde |
| unit | eenheid |

## Onderwijsaanbod — Education offering

[`education-offering.json`](Datamodelschema's/education-offering.json)

| English (UK) | Nederlands |
|---|---|
| offeringInstances | aanbodInstanties |
| locations | locaties |
| organisationUnits | organisatieEenheden |

Velden per item in `offeringInstances`:

| English (UK) | Nederlands |
|---|---|
| id | id |
| offeringType | aanbodType |
| version | versie |
| parentOfferingId | bovenliggendAanbodId |
| specificationReference | specificatieVerwijzing |
| name | naam |
| status | status |
| bottlenecks | knelpunten |
| cohort | cohort |
| period | periode |
| minStudentCount | minAantalStudenten |
| maxStudentCount | maxAantalStudenten |
| locationId | locatieId |
| executingTeamId | uitvoerendTeamId |
| groups | groepen |

## Onderwijsspecificatie-delta — Education specification delta

[`education-specification-delta.json`](Datamodelschema's/education-specification-delta.json)

| English (UK) | Nederlands |
|---|---|
| op | op |
| path | path |
| from | from |
| value | value |

## Onderwijsspecificatie — Education specification

[`education-specification.json`](Datamodelschema's/education-specification.json)

| English (UK) | Nederlands |
|---|---|
| learningOutcomes | leeruitkomsten |
| educationSpecifications | onderwijsspecificaties |
| ruleSets | regelsets |

Velden per item in `educationSpecifications`:

| English (UK) | Nederlands |
|---|---|
| id | id |
| specificationType | specificatieType |
| version | versie |
| parentSpecificationId | bovenliggendSpecificatieId |
| learningOutcomeId | leeruitkomstId |
| name | naam |
| description | omschrijving |
| status | status |
| studyLoad | studielast |
| curriculumType | curriculumtype |
| programmeType | programmatype |
| programmeLayer | programmaLaag |
| learningPathway | leerweg |
| targetGroup | doelgroep |
| electiveUnitClass | keuzedeelKlasse |
| organisation | organisatie |
| cohort | cohort |
| startDate | startdatum |
| validFrom | geldigVanaf |
| validUntil | geldigTot |
| timeDistribution | tijdsverdeling |
| explanation | toelichting |
| ruleSetReferences | regelsetVerwijzingen |
| manifest | manifest |

## OrganisatieEenheid — Organisation unit

[`organisation-unit.json`](Datamodelschema's/organisation-unit.json)

| English (UK) | Nederlands |
|---|---|
| id | id |
| unitType | eenheidType |
| name | naam |
| parentUnitId | bovenliggendeEenheidId |
| professionalIds | professionalIds |

## Periode — Period

[`period.json`](Datamodelschema's/period.json)

| English (UK) | Nederlands |
|---|---|
| start | start |
| end | eind |

## Regelset — Rule set

[`rule-set.json`](Datamodelschema's/rule-set.json)

| English (UK) | Nederlands |
|---|---|
| id | id |
| version | versie |
| name | naam |
| description | omschrijving |
| appliesTo | vanToepassingOp |
| rules | regels |

## Resultaatmodel — Result model

[`result-model.json`](Datamodelschema's/result-model.json)

| English (UK) | Nederlands |
|---|---|
| scale | schaal |
| passMark | cesuur |
| decimalPlaces | decimalen |

## Resultaatstructuur en examenplan — Result structure and exam plan

[`result-structure.json`](Datamodelschema's/result-structure.json)

| English (UK) | Nederlands |
|---|---|
| educationSpecifications | onderwijsspecificaties |
| ruleSets | regelsets |

Velden per item in `educationSpecifications`:

| English (UK) | Nederlands |
|---|---|
| id | id |
| specificationType | specificatieType |
| version | versie |
| parentSpecificationId | bovenliggendSpecificatieId |
| name | naam |
| description | omschrijving |
| status | status |
| validFrom | geldigVanaf |
| validUntil | geldigTot |
| appliesTo | geldtVoor |
| assesses | beoordeelt |
| learningOutcomeId | leeruitkomstId |
| learningOutcome | leeruitkomst |
| nature | aard |
| assessmentForm | toetsvorm |
| aggregation | aggregatie |
| weighting | weging |
| mandatory | verplicht |
| resultModel | resultaatmodel |
| ruleSetReferences | regelsetVerwijzingen |
| manifest | manifest |

## Specificatie-gewijzigd — Specification changed

[`specification-changed.json`](Datamodelschema's/specification-changed.json)

| English (UK) | Nederlands |
|---|---|
| objectId | objectId |
| oldVersion | oudeVersie |
| newVersion | nieuweVersie |
| changeClass | wijzigingsklasse |

## Specificatie-referentie — Specification reference

[`specification-reference.json`](Datamodelschema's/specification-reference.json)

| English (UK) | Nederlands |
|---|---|
| specificationId | specificatieId |
| version | versie |

## Specificatie-status-gewijzigd — Specification status changed

[`specification-status-changed.json`](Datamodelschema's/specification-status-changed.json)

| English (UK) | Nederlands |
|---|---|
| objectId | objectId |
| oldStatus | oudeStatus |
| newStatus | nieuweStatus |

## Verwerkingsstatus — Processing status

[`processing-status.json`](Datamodelschema's/processing-status.json)

| English (UK) | Nederlands |
|---|---|
| status | status |
| programmeOfferingId | opleidingsaanbodId |
| specificationReference | specificatieVerwijzing |
