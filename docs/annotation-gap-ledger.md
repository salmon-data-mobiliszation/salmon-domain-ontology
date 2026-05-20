# Annotation Gap Ledger

Purpose: track unresolved annotation-completeness gaps in the Salmon Domain Ontology without inventing new definitions, sources, or ownership assertions.

## Ground rules

- Do **not** invent definitions or provenance just to satisfy a checklist.
- For migrated/shared terms, reuse existing wording exactly when authoritative text already exists.
- For imported external terms, prefer source-owned annotations or explicit exclusion from local completeness checks rather than hand-authoring local wording.
- `rdfs:comment` is for editorial scope notes / mapping rationale, not the primary definition field.

## Scope of this ledger

Current counts below cover **local typed terms in `ontology/modules/*.ttl`** with `smn:` / `smn/profile/...` IRIs:
- OWL classes / properties / annotation properties
- SKOS concepts / concept schemes

Imported external IRIs are intentionally out of scope for these counts.

## Current status (2026-05-13)

- Missing `rdfs:isDefinedBy`: **0**
- Missing definitions: **43**
- Missing provenance (`iao:0000119` / `dcterms:source`): **50**

## 2026-05-13 backfill note

Source-backed provenance was backfilled only where the term could be tied to a prior GCDFO Salmon Ontology release, the RDA case-study source sheet, or the Hakai GraphML source already used by the profile bridge modules.

No new definition was added where the only available text was inferred, generalized beyond the source term, or not present in the checked GCDFO/RDA/Hakai sources.

## Definition gaps by module

### `ontology/modules/01-entity-systematics.ttl`
- `Entity`
- `GeographicFeature`
- `HabitatUnit`
- `SalmonGroup`
- `SalmonIndividual`
- `SalmonPopulationGroup`
- `SalmonStockUnit`

### `ontology/modules/02-observation-measurement.ttl`
- `AggregatedMeasurement`
- `BodyShape`
- `Characteristic`
- `FishForkLengthMeasurementMethod`
- `FishLength`
- `FishLengthMeasurementMethod`
- `FishLengthMeasurementType`
- `FishWeight`
- `ForkLengthMeasurement`
- `ForkLengthMeasurementFieldMethod`
- `ForkLengthMeasurementLabMethod`
- `ForkLengthMeasurementMethod`
- `IndividualMeasurement`
- `Life-HistoryCharacteristic`
- `ModelMeasurement`
- `MorphologicalCharacteristic`
- `NCBITaxon_8018`
- `Observation`
- `Run`
- `SalmonLifeStage`
- `StandardLengthMeasurement`
- `TotalLengthMeasurement`
- `alevin`
- `basedOn`
- `characteristicFor`
- `forkLength`
- `fusiform`
- `hasEventType`
- `hasMeasurement`
- `observedTaxonFamily`
- `observedTaxonSpecies`
- `orbitalLength`
- `standardLength`
- `totalLength`

### `ontology/modules/04-management-governance.ttl`
- `FishingType`
- `seiningEvent`

## Provenance gaps by module

### `ontology/modules/01-entity-systematics.ttl`
- `Entity`
- `GeographicFeature`
- `HabitatUnit`
- `SalmonGroup`
- `SalmonIndividual`
- `SalmonPopulationGroup`
- `SalmonStockUnit`
- `hasPopulation`
- `populationOf`

### `ontology/modules/02-observation-measurement.ttl`
- `AggregatedMeasurement`
- `BodyShape`
- `Characteristic`
- `FishForkLengthMeasurementMethod`
- `FishLength`
- `FishLengthMeasurementMethod`
- `FishLengthMeasurementType`
- `FishWeight`
- `ForkLengthMeasurement`
- `ForkLengthMeasurementFieldMethod`
- `ForkLengthMeasurementLabMethod`
- `ForkLengthMeasurementMethod`
- `IndividualMeasurement`
- `Life-HistoryCharacteristic`
- `Measurement`
- `ModelMeasurement`
- `MorphologicalCharacteristic`
- `NCBITaxon_8018`
- `Observation`
- `Run`
- `SalmonLifeStage`
- `SamplingEvent`
- `StandardLengthMeasurement`
- `TotalLengthMeasurement`
- `alevin`
- `basedOn`
- `characteristicFor`
- `forkLength`
- `fusiform`
- `hasEventType`
- `hasMeasurement`
- `observedTaxonFamily`
- `observedTaxonSpecies`
- `orbitalLength`
- `standardLength`
- `totalLength`

### `ontology/modules/04-management-governance.ttl`
- `EventType`
- `FishingType`
- `seiningEvent`

### `ontology/modules/05-provenance-quality.ttl`
- `DataQualityAssessment`
- `MethodDocumentation`
