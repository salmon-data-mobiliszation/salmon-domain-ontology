# Ontology source layout

This folder is the canonical ontology source for the Salmon Domain Ontology. Everything under `docs/` is generated output; this folder contains the local TTL sources and import graph used to build releases.

## What is in this folder

### Main build files

- `salmon-domain-ontology.ttl`
  - Primary canonical local entrypoint for the shared ontology.
  - Imports all core modules `01`–`07` plus `alignment-main`.
  - This is the default artifact for shared-term reuse and day-to-day consumption.

- `salmon-domain-ontology-research.ttl`
  - Experimental/second pass build.
  - Imports the canonical ontology (`https://w3id.org/smn`) and adds `alignment-research`.
  - Intended for review/debate on stronger semantics before they move into `alignment-main`.

- `salmon-domain-ontology-rda-case-study.ttl`
  - Case-study bridge build for the RDA juvenile-condition pilot.
  - Imports the canonical ontology and adds profile bridge modules `08` and `09`.
  - The case-study layer is intentional and **not yet permanent**; it is here to make the mapping workflow explicit and reviewable.

- `../salmon-domain-ontology.ttl`
  - Generated flattened, import-free artifact intended for one-file consumers and downstream tooling.
  - Regenerated with `make compose-flat-ttl` and treated as read-only.

## Core modules (`01`–`07`)

1. **`modules/01-entity-systematics.ttl`**
  - Shared entities and biological organization: population, stock, deme, management units, geographic units.
  - Use case: anchoring `entity_iri` and high-level relationships.

2. **`modules/02-observation-measurement.ttl`**
  - Observations and measurements, SOSA-aligned patterns, measurement-event primitives.
  - Use case: anchoring `property_iri`, `unit`-adjacent modeling, and base measurement semantics.

3. **`modules/03-assessment-benchmarks.ttl`**
  - Assessment and benchmark classes: reference points, benchmark framing, exploitation semantics.
  - Use case: shared stock-assessment terms once teams move from pure observation toward status products.

4. **`modules/04-management-governance.ttl`**
  - Conservative event/procedure taxonomy for fisheries governance context.
  - Use case: shared governance/event vocabulary where explicit policy-neutral terms are needed.

5. **`modules/05-provenance-quality.ttl`**
  - Shared provenance and quality artifacts: data-quality descriptors, method-doc types.
  - Use case: provenance pipelines and quality reporting.

6. **`modules/06-data-interoperability.ttl`**
  - Crosswalk axioms for SOSA/I-ADOPT/Darwin Core interoperability.
  - Use case: interoperability-focused profiles and mappings, not required for bare-minimum domain mapping.

7. **`modules/07-controlled-vocabularies.ttl`**
  - Shared SKOS control layers for context/facet concepts (life phase, origin, measurement context, etc.).
  - Use case: statistical modifiers and constrained categorical terms.

### Bridge/profile modules

- **`modules/08-rda-case-study-profile-bridges.ttl`**
  - Hakai case-study source terms mapped conservatively to shared anchors.
  - Focus: **measurement method/context** terms from the RDA juvenile-condition pilot.
  - Assembled from split case-study fragments under `case-studies/rda-juvenile-condition/`.

- **`modules/09-rda-neville-decomposition-profile-bridges.ttl`**
  - Neville decomposition profile bridges for case-study interoperability.
  - Focus: **entity + observation + aggregate/statistical modifier** terms from the RDA juvenile-condition pilot.
  - Assembled from split case-study fragments under `case-studies/rda-juvenile-condition/`.

### Alignment modules

- **`modules/alignment-main.ttl`**
  - Conservative bridges already considered stable enough for baseline inclusion.

- **`modules/alignment-research.ttl`**
  - Exploratory, stronger-style alignments held out from baseline.

### How case-study modules map to the onboarding workflow

The case-study modules were intentionally arranged to mirror the same onboarding sequence used by Salmon Data GPT:

1. **Entities observed** → shared `01` terms and local profile entities in `09` (Neville terms like `Species`, `Area`, `SampleType`, `StandardSurvey`).
2. **Variables/properties measured** → shared `02` properties plus `09` local mapped measure terms (`Length_mm`, `Weight_g`, `AverageLength_mm`, etc.).
3. **Method + statistical context** → `08` method concepts (`...ForkLengthMeasurement*`) and modifier-heavy terms in `09` (`StandardDeviation*`, `NumberSampled`, constraint context terms).

That keeps the case study as a practical “manual bridge first, automation second” artifact.

## Recommended “what to touch” rule

For changes to shared semantics:

- Put genuinely cross-organization terms in `01`–`07` (and only there).
- Keep local program/partner vocabulary in profile files, then bridge there.
- Keep uncertain or higher-friction upper-level modeling in `alignment-research` or profile modules until reviewed.

## How this lines up with the biologist onboarding workflow

For early-stage data standardization (the way smn-data-gpt proposes output), we want frictionless semantic mapping:

1. **Observed entities** (`entity_iri`)
2. **Measured property/variable** (`term_iri`, `property_iri`)
3. **Method/context + statistical modifiers** (`method_iri`, `constraint_iri`, scheme concepts)

In that flow, the practical first pass is usually driven by:

- `01-entity-systematics`
- `02-observation-measurement`
- `07-controlled-vocabularies`
- optionally `06-data-interoperability` when teams explicitly need interoperability scaffolds.

The current pattern does **not** require BFO/IAO-first modeling for first-pass output; those richer semantics are available as the ontology matures and become useful for reasoning-heavy consumers.

## Is the current module count too much?

Short answer: maybe for external onboarding, yes; for maintainability, no.

- Current structure is healthy for internal ontology development because it keeps concerns separated and review boundaries clear.
- For initial MVP biologist rollout, too many modules can look noisy, so the practical compromise is:
  - keep this source layout,
  - expose only the minimal build surface and docs to users,
  - defer collapsing/merging module files until stable usage confirms a cleaner shape.

A later simplification pass could collapse:

- **`03` + `05`** if benchmark/provenance growth remains small,
- **`04` + `05`** if governance and quality stay low-volume operational terms,
- while keeping **`06`** as a clearly optional interoperability overlay.

For now, this split is defensible and gives us a safe runway to trim on evidence, not assumptions.