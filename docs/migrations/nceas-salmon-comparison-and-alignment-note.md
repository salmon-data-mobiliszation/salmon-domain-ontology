# SMN and NCEAS/DataONE SALMON: comparison and first-pass alignment note

_Status: initial comparison note (2026-03-28)._  
_Scope: shared-core Salmon Domain Ontology (`smn:`) compared against the NCEAS/DataONE Salmon Ontology (`SALMON`). This is a practical alignment note, not a full term-by-term crosswalk._

## Short take

The two ontologies are trying to help with many of the same problems — semantic annotation, dataset harmonization, and cross-dataset discovery — but they come from different modeling instincts.

- **SALMON** is currently a **broad salmon annotation lexicon** built for dataset annotation and portal/search use.
- **SMN** is currently a **smaller, more opinionated interoperability core** with explicit profile-space and conservative promotion rules.

That makes SALMON stronger today as a broad source/comparison ontology, and SMN stronger as the architectural target for a shared cross-organization core.

## What changed over time

### NCEAS/DataONE SALMON

SALMON grew out of SASAP/DataONE annotation work. Its current public form is a large monolithic ontology with broad salmon-domain coverage, including:

- fish and salmon measurement terms
- life-stage and stock-related terms
- fishery and gear categories
- codes and identifiers
- habitat/place terms
- a mix of biological, operational, and archive-annotation concepts

It imports or reuses external structures such as **OBOE**, **ENVO**, and **GeoSPARQL**, and it keeps many terms in a single broad ontology space.

### Salmon Domain Ontology (SMN)

SMN is being shaped as a modular shared core with a stricter boundary between:

- reusable shared-domain terms (`smn:`)
- small curated shared SKOS vocabularies
- program/agency/profile-specific bridge layers
- conservative alignment modules

Recent SMN direction has been to keep the shared layer smaller, cleaner, and more explicitly cross-organization, while pushing unstable or program-specific semantics into profile space first.

## Shared ground / synergies

There is real overlap in intent and content.

Both ontologies aim to support:

- semantic dataset annotation
- search and discovery across salmon datasets
- cross-dataset harmonization
- alignment to external standards rather than inventing everything from scratch

Both also already use bridge/alignment thinking rather than assuming a single ontology should own the whole problem.

## Main differences in modeling posture

| Area | SMN | NCEAS/DataONE SALMON | Alignment implication |
| --- | --- | --- | --- |
| Overall shape | Modular shared core + profile/bridge posture | Large monolithic ontology | SALMON is a rich source ontology; SMN should stay the cleaner shared-core target |
| Main framing | SOSA + I-ADOPT + Darwin Core bridge posture | OBOE-centered measurement/annotation posture with additional external links | Similar concepts often need `closeMatch`, not direct equivalence |
| Scope discipline | Tries to keep program/policy/local semantics out of shared core | More willing to keep operational and local annotation concepts in-core | Avoid importing SALMON breadth directly into `smn:` |
| Controlled vocabularies | Uses SKOS selectively for curated shared vocabularies | Mostly OWL classes, including many codelist-like operational categories | Some SALMON class hierarchies are better treated as profile vocabularies in SMN |
| IRI style | Readable semantic IRIs | Opaque numeric IRIs | Label-based review is easy, but semantic review still matters |
| Promotion policy | Conservative shared-term admission | Broad annotation-first coverage | Use SALMON as evidence for possible shared terms, not automatic promotion |

## Obvious early alignment opportunities

These are the terms where overlap is strong enough to justify early review.

| SMN term | SALMON term | First-pass view | Notes |
| --- | --- | --- | --- |
| `smn:alevin` | `SALMON_00000403` Alevin | likely strong match | Same label and same general life-stage meaning |
| `smn:forkLength` | `SALMON_00000128` Fork length | likely strong match after review | Good early candidate once SMN fork-length hierarchy is fixed |
| `smn:standardLength` | `SALMON_00000135` Standard length | likely strong match after review | Specific fish-length subtype |
| `smn:totalLength` | `SALMON_00000134` Total length | likely strong match after review | Specific fish-length subtype |
| `smn:ForkLengthMeasurementMethod` | `SALMON_00000631` Fork length measurement method | likely `skos:closeMatch` or stronger after review | Labels align well, but measurement/procedure modeling should still be checked |
| `smn:FishLengthMeasurementMethod` | `SALMON_00000630` Fish length determination method | likely `skos:closeMatch` | Same neighborhood, slightly different naming posture |

These are good places to start because they are concrete, visible, and less politically loaded than stock/benchmark/governance terms.

## Terms that look similar but should **not** be exact-matched yet

### 1) `Fish length` / measurement-type pattern

This is the clearest immediate modeling caution.

SMN currently separates:

- a general characteristic: `smn:FishLength`
- specific subtypes such as `smn:forkLength`, `smn:standardLength`, `smn:totalLength`
- measurement classes such as `smn:ForkLengthMeasurement`

SALMON uses a more OBOE-oriented measurement-type pattern.

That means label similarity alone is not enough for exact matching between SMN and SALMON measurement classes.

### 2) Escapement

SALMON has named classes such as:

- `Salmon escapement count`
- `Annual escapement count`
- `Daily escapement count`

SMN is better suited to modeling escapement more compositionally through measurement + event + time/context rather than proliferating one class per temporal grain.

So this is a likely `closeMatch` family, not an automatic exact-match family.

### 3) Stock semantics

SMN `Stock` is a **reporting or management stratum**.

SALMON `Fish stock type` includes a broader mix of management-unit and breeding-population language. That makes it useful comparison material, but not a clean exact match.

### 4) Origin semantics

SALMON terms such as `Wild stock` and `Hatchery` do not line up cleanly with SMN concepts such as `NaturalOrigin` and `HatcheryOrigin`.

The mismatch is partly because they are speaking about different things:

- stock/facility/category semantics in SALMON
- individual-origin controlled-vocabulary semantics in SMN

This should stay conservative.

### 5) Habitat/place terms

When both ontologies point toward external habitat/place standards, bilateral matching is often the wrong first move.

For many place/habitat cases, the better alignment anchor is:

- **ENVO**
- **GeoSPARQL**
- other established geographic/environmental vocabularies

## Immediate SMN modeling follow-up

The current SMN model had one clear logical error:

- `smn:forkLength owl:equivalentClass smn:FishLength`

That is too strong. Fork length is a kind of fish length, not the same thing as fish length in general.

This is now tracked in:

- **[#10](https://github.com/salmon-data-mobilization/salmon-domain-ontology/issues/10)** — _Fix fork length modeling: make forkLength a subtype of FishLength, not an equivalent class_

The safer pattern is:

- `smn:FishLength` = general characteristic
- `smn:forkLength`, `smn:standardLength`, `smn:totalLength`, `smn:orbitalLength` = specific subclasses
- measurement classes constrain `sosa:observedProperty` against the specific subtype they measure

## Candidate shared terms to evaluate for future SMN promotion

The NCEAS/DataONE SALMON ontology highlights a few concepts that may be worth evaluating for shared-core SMN admission **if** reuse shows up across multiple datasets and organizations:

- `BroodYear`
- `RunSize`
- `SpawnerAbundance`
- `RecruitAbundance`
- `MigratoryPattern`
- `ReproductiveStrategy`

These should not be promoted just because SALMON already has them. They should only move into shared `smn:` if they prove both reusable and policy-neutral.

## Terms that should probably stay out of shared SMN core unless reuse evidence becomes very strong

Examples:

- ADF&G-specific codes
- local stock-name/code administration terms
- program-specific fishery/gear/tag vocabularies
- local archive-annotation helper categories

Those are better handled in profile vocabularies and bridge artifacts unless there is clear cross-organization demand.

## Recommended alignment strategy

1. **Keep SMN as the shared-core target architecture.**  
   Do not expand SMN into a clone of SALMON.

2. **Treat SALMON as a rich comparison/source ontology.**  
   It is useful evidence for overlap, candidate mappings, and possible shared-term gaps.

3. **Create a dedicated bridge artifact for NCEAS SALMON mappings.**  
   A future file such as `ontology/modules/alignment-nceas-salmon.ttl` would keep those mappings explicit and reviewable.

4. **Use conservative mapping predicates first.**  
   Prefer `skos:closeMatch` until the semantics are genuinely safe for stricter axioms.

5. **Start with a small pilot set (10–15 terms).**  
   Begin with concrete overlap terms rather than jumping straight to stock, benchmark, and governance semantics.

6. **Prefer external anchors where appropriate.**  
   If the best common target is ENVO, GeoSPARQL, SOSA, Darwin Core, or I-ADOPT, use that rather than forcing a bilateral SMN ↔ SALMON equivalence.

7. **Promote new shared SMN terms only with evidence.**  
   Reuse across organizations, semantic stability, and policy-neutral meaning should remain the admission gate.

## Summary

SALMON and SMN are complementary, not redundant.

- **SALMON** is stronger today as a broad salmon-domain annotation vocabulary.
- **SMN** is stronger today as a disciplined shared interoperability architecture.

The right move is not to collapse them into each other. The right move is to align them carefully, use SALMON as a comparison source, fix obvious SMN modeling mistakes when they show up, and keep shared `smn:` promotion conservative.

## Reference points

- NCEAS/DataONE SALMON repo: <https://github.com/DataONEorg/sem-prov-ontologies/tree/main/salmon>
- BioPortal entry: <https://bioportal.bioontology.org/ontologies/SALMON>
- SMN repo: <https://github.com/salmon-data-mobilization/salmon-domain-ontology>
