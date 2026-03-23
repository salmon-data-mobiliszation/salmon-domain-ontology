# RDA juvenile-condition integrated walkthrough (discussion prep)

Purpose: prepare the Hakai + Neville case study for a focused architecture discussion on **salmon-domain decomposition style + salmon metamodel fit**, without asking reviewers to adjudicate strong semantic equivalence yet.

## Artifacts prepared

1. Integrated TTL walkthrough:
   - `ontology/case-studies/rda-juvenile-condition/10-rda-integrated-metamodel-walkthrough.ttl`
2. Case-study folder map updated:
   - `ontology/case-studies/rda-juvenile-condition/README.md`

This walkthrough is profile-scoped and review-oriented. It is not a shared-core promotion artifact.

## What the integrated TTL now shows

- One integrated Hakai + Neville variable decomposition surface
- Explicit metamodel-slot connections via `smnv:` predicates:
  - `smnv:variableRepresentsEntity`
  - `smnv:variableRepresentsProperty`
  - `smnv:variableUsesConstraint`
  - `smnv:variableUsesStatisticalModifier`
- Observation/sampling pattern concepts connected to metamodel observation/procedure/result slots
- A provisional candidate scheme for terms that may need shared `smn:` representations later

## Integrated decomposition snapshot

| Integrated variable concept | Entity slot | Property slot | Constraint slot(s) | Statistical slot | Source bridge terms |
| --- | --- | --- | --- | --- | --- |
| `rda:JuvenileForkLengthVariable` | `smn:SalmonIndividual` | `smn:forkLength` | `neville:Age`, `neville:Area`, `neville:SampleType`, `neville:StandardSurvey` | — | `neville:Length_mm`, `hakai:Fork_Length_Field_Measurement`, `hakai:Fork_Length_Lab_Measurement` |
| `rda:JuvenileWeightVariable` | `smn:SalmonIndividual` | `smn:FishWeight` | `neville:Age`, `neville:Area`, `neville:SampleType`, `neville:StandardSurvey` | — | `neville:Weight_g` |
| `rda:AverageJuvenileWeightVariable` | `smn:SalmonGroup` | `smn:FishWeight` | `neville:SpatialAndTemporalExtent`, `neville:Area` | `rdac:AverageStatisticalModifier` | `neville:AverageWeight_g` |
| `rda:AverageJuvenileConditionFactorVariable` | `smn:SalmonGroup` | `rdac:ConditionFactor` (candidate) | `neville:SpatialAndTemporalExtent`, `neville:Area`, `neville:Age` | `rdac:AverageStatisticalModifier` | `neville:AverageConditionFactor` |
| `rda:JuvenileSampleCountVariable` | `smn:SalmonGroup` | `rdac:SampleCount` (candidate) | `neville:SpatialAndTemporalExtent`, `neville:Area`, `neville:SampleType`, `neville:StandardSurvey` | — | `neville:NumberSampled` |

## Provisional candidate shared terms (not yet in canonical `smn:`)

Defined in scheme `rdac:SharedTermCandidateScheme`:

- `rdac:ConditionFactor`
- `rdac:SampleCount`
- `rdac:AverageStatisticalModifier`
- `rdac:SurveyDesignContext`
- `rdac:SpatialTemporalExtentConstraint`
- `rdac:OceanAgeClass`
- `rdac:MeasurementSettingContext`

Validation note: these local names currently have no collisions with canonical shared `smn:` term local names.

## What this discussion should and should not do

### In scope

- Does the integrated decomposition make sense for real Hakai + Neville dataset usage?
- Does the salmon metamodel framing feel clear and practical?
- Are the candidate-gap abstractions the right kind of shared-term candidates?

### Out of scope (for now)

- `owl:equivalent*` / `skos:exactMatch` upgrades
- promotion decisions into shared `smn:`
- final semantic-strength adjudication

## Copy/paste discussion-thread draft

> We’ve prepared an integrated Hakai + Neville case-study walkthrough to show salmon-domain decomposition style and salmon metamodel fit in one place.
>
> Main artifact:
> - `ontology/case-studies/rda-juvenile-condition/10-rda-integrated-metamodel-walkthrough.ttl`
>
> The goal of this pass is **not** to decide exact-match strength or promotion yet. The goal is to check whether the integrated decomposition is clear and practical for dataset-driven modeling, and whether the case-study is surfacing the right candidate shared-term gaps.
>
> Specifically, could you review:
> 1. Integrated variable decomposition (entity/property/constraint/statistical/method/result framing)
> 2. Whether the metamodel-slot usage is understandable and useful
> 3. Whether candidate abstractions (condition factor, sample count, survey-design context, etc.) look like the right gap signals
>
> Tagging for review: @Shirley @Graham @Mel
>
> We can handle semantic-strength/promotion decisions after this fit-and-clarity review.
