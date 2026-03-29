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

## Current status (2026-03-28)

- Missing `rdfs:isDefinedBy`: **0**
- Missing definitions: **43**
- Missing provenance (`iao:0000119` / `dcterms:source`): **105**

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
- `Deme`
- `Entity`
- `GeographicFeature`
- `HabitatUnit`
- `Population`
- `ReportingOrManagementStratum`
- `SalmonGroup`
- `SalmonIndividual`
- `SalmonPopulationGroup`
- `SalmonStockUnit`
- `demeOf`
- `hasDeme`
- `hasPopulation`
- `populationOf`

### `ontology/modules/02-observation-measurement.ttl`
- `AggregatedMeasurement`
- `BodyShape`
- `Characteristic`
- `EnumerationMethod`
- `EscapementMeasurement`
- `EscapementSurveyEvent`
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

### `ontology/modules/03-assessment-benchmarks.ttl`
- `ObservedRateOrAbundance`
- `TargetOrLimitRateOrAbundance`
- `TotalExploitationRate`

### `ontology/modules/04-management-governance.ttl`
- `EventType`
- `FishingType`
- `seiningEvent`

### `ontology/modules/05-provenance-quality.ttl`
- `DataQualityAssessment`
- `MethodDocumentation`

### `ontology/modules/07-controlled-vocabularies.ttl`
- `CatchContext`
- `InRiverPhase`
- `LifePhase`
- `LifePhaseScheme`
- `MainstemPhase`
- `MeasurementContext`
- `MeasurementContextScheme`
- `OceanPhase`
- `RunContext`
- `SalmonOrigin`
- `SalmonOriginScheme`
- `SpawnerStageContext`
- `SurvivalOrMortalityContext`
- `TerminalPhase`

### `ontology/modules/08-rda-case-study-profile-bridges.ttl`
- `Fork_Length_Field_Measurement`
- `Fork_Length_Lab_Measurement`
- `Fork_Length_Measurement_Method`
- `fork_length_measurement_field_method`
- `fork_length_measurement_lab_method`
- `HakaiJSPMeasurementTermScheme`

### `ontology/modules/09-rda-neville-decomposition-profile-bridges.ttl`
- `ADCWT`
- `Age`
- `Area`
- `AverageConditionFactor`
- `AverageLength_mm`
- `AverageWeight_g`
- `Length_mm`
- `NonStandardSurvey`
- `NonStandardSurveyArea`
- `NumberSampled`
- `SampleType`
- `SpatialAndTemporalExtent`
- `Species`
- `StandardDeviationLength_mm`
- `StandardDeviationWeight_g`
- `StandardSurvey`
- `SurveyArea`
- `Weight_g`
- `WoundsParasitesOther`
- `NevilleDecompositionTermScheme`

### `ontology/modules/alignment-research.ttl`
- `hasFeatureOfInterest`
- `hasObservationResult`
- `isSampleOfStratum`
- `usesObservationProcedure`

## DFO-derived unresolved provenance-only carryovers

These shared terms still lack provenance in SMN, and no authoritative `iao:0000119` / `dcterms:source` was found for them in the DFO repo history used during migration cleanup.

### Wave-1 / shared carryovers
- `ReportingOrManagementStratum`
- `Deme`
- `Population`
- `hasDeme`
- `demeOf`
- `hasPopulation`
- `populationOf`
- `EscapementSurveyEvent`
- `EscapementMeasurement`
- `ObservedRateOrAbundance`
- `TargetOrLimitRateOrAbundance`
- `TotalExploitationRate`

### Alignment-branch carryovers
- `hasFeatureOfInterest`
- `hasObservationResult`
- `usesObservationProcedure`
- `isSampleOfStratum`

## Priority order for future cleanup

1. Reuse already-written authoritative definitions/provenance where available.
2. Close shared-core OWL definition gaps before polishing profile-only terms.
3. For provenance-only gaps, prefer explicit unresolved tracking over guessed citations.
4. When a gap cannot be resolved from existing written material, leave it here until a human source decision is made.
