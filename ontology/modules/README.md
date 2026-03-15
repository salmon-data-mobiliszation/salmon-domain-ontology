# Salmon Domain Ontology Modules

This directory contains the modular build-out for the salmon-domain ontology.

If you are new to ontologies, read this first:
- `../../docs/guides/modules-and-bridges-for-biologists.md`

That guide explains (in plain language) how modules, local program ontologies, and bridge profiles work together when mapping real datasets.

## Shared-core modules (01–07)

These files are the shared Salmon-layer baseline by default:

1. `01-entity-systematics.ttl` — core entities, strata classes, and biological unit composition relations.
2. `02-observation-measurement.ttl` — SOSA-aligned observations, measurements, survey events, and escapement measurement semantics.
3. `03-assessment-benchmarks.ttl` — stock-assessment abstractions, reference points, benchmark classes, and exploitation-rate terms.
4. `04-management-governance.ttl` — conservative shared event taxonomy (policy schemes remain profile-scoped).
5. `05-provenance-quality.ttl` — shared provenance/quality artifact classes (program confidence vocabularies profile-scoped).
6. `06-data-interoperability.ttl` — I-ADOPT/SOSA/Darwin Core interoperability bridge axioms.
7. `07-controlled-vocabularies.ttl` — small curated shared SKOS schemes/concepts for context, life phase, and origin only.

## Profile/case-study modules (08, 09)

These are not part of the permanent shared baseline by default. They are the **RDA juvenile-condition working case study** used to test the practical mapping process:

- `08-rda-case-study-profile-bridges.ttl` — Hakai profile-layer bridge terms.
  - Focus today: **method semantics and measurement-context terms**.
  - Implemented as an assembled module from split case-study fragments in `../case-studies/rda-juvenile-condition/`:
    - `08-rda-hakai-method-scheme.ttl` (scheme/context)
    - `08-rda-hakai-measurement-methods.ttl` (measurement term mappings)
  - Built via `make compose-case-study-modules`.

- `09-rda-neville-decomposition-profile-bridges.ttl` — Neville decomposition profile-layer bridge terms.
  - Focus today: **entity semantics, observation/measurement concepts, and constraint/statistical modifier terms**.
  - Implemented as an assembled module from split case-study fragments in `../case-studies/rda-juvenile-condition/`:
    - `09-rda-neville-entities.ttl` (entities/strata)
    - `09-rda-neville-observations.ttl` (variables + measurements)
    - `09-rda-neville-constraints.ttl` (constraints/statistical modifiers)
  - Built via `make compose-case-study-modules`.

Importantly, both modules stay in profile-space and map to `smn:` with conservative SKOS predicates unless there is explicit promotion criteria.

## Alignment modules (phase 2 migration)

- `alignment-main.ttl` — conservative merge-safe upper-level alignment bridges.
- `alignment-research.ttl` — exploratory alignment candidates with stronger axioms.

## Import behavior

- `../salmon-domain-ontology.ttl` imports modules 01–07 + `alignment-main.ttl`.
- `../salmon-domain-ontology-research.ttl` imports the conservative build and then adds `alignment-research.ttl`.
- `../salmon-domain-ontology-rda-case-study.ttl` imports the conservative build and then adds `08-rda-case-study-profile-bridges.ttl` and `09-rda-neville-decomposition-profile-bridges.ttl`.

## Suggested editing posture for future refactors

- If your goal is a simpler onboarding draft, keep the build surface to `smn`, `02`, `07` initially and layer in other shared modules by need.
- If review pressure spikes, merge additional semantics from modules 08/09 into shared core only after cross-dataset reuse is demonstrated.
- Prefer adding explicit `rdfs:comment` + provenance fields to profile terms to preserve mapping rationale before any promotion decision.

## Guardrails

- Use `smn:` for domain terms intended for reuse across organizations.
- Preserve source-provenance notes when migrating terms from DFO Salmon Ontology.
- Do **not** remove terms from DFO source ontology as part of this phase.
