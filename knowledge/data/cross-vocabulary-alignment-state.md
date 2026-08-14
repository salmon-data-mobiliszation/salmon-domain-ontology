---
type: InformationObject
title: Cross-vocabulary alignment state
description: The verified relationship between smn, gcdfo 0.0.8, and the PSC controlled vocabulary as of 2026-08-12 — the live pun, the minted term, the unbridged duplication, and why PSC maps to gcdfo but refuses smn.
status: draft
tags: [gcdfo, psc, sssom, alignment, methods]
psc:
  id: smn:data:cross-vocabulary-alignment-state
  contexts: [smn:context:ontology-alignment-pass-2026]
---

Verified 2026-08-12: smn main `3995a17`, gcdfo main `c7a5425` (release
0.0.8), psc-salmon-vocabularies branch `feature/fair-mapping-products-roadmap`
(`8e50d81`).

## The boundary is now structural, not prose

`dfo-salmon.ttl:200` `owl:imports <https://w3id.org/smn>`; gcdfo subclasses
smn upper classes 26 times and re-declares 39 `smn:` subjects as MIREOT-style
mirrors (with `rdfs:isDefinedBy` pointed at smn per gcdfo's ownership rule).
Any earlier claim that the smn/gcdfo boundary is "prose-only" is stale.

## Defects in the merged closure

- ~~Live pun~~ **Resolved 2026-08-13 (step 2):** smn migrated its six method
  OWL classes to SKOS concepts in `smn:MethodScheme` (module 07), each
  instance-typed `sosa:Procedure`, IRIs unchanged — so `smn:EnumerationMethod`
  is now `skos:Concept` on both sides and the merged closure has zero
  dual-typed IRIs (verified against the flat build). PSC's wrong-kind
  objection (`sdo-alignment-gap.md`) no longer applies; updating their doc
  and drafting psc→smn SSSOM rows is step 4.
- **Minted foreign term:** `smn:FisheriesReferencePointLower` is declared
  only in `dfo-salmon.ttl` (~line 1920); smn never declares it.
- ~~Unbridged duplication~~ **Resolved 2026-08-13 (step 3, gcdfo PR #78):**
  `mappings/gcdfo-to-smn.sssom.tsv` publishes the boundary as data — 28
  reviewed rows covering the age/year family, the renamed age classes,
  CatchYear, and EscapementEstimate, with predicates graded by smn's own
  migration provenance (Migrated → exactMatch, Adapted → closeMatch) and
  both sides version-pinned. The 2026-08-13 recon found **zero**
  same-name-different-semantics collisions — the old "~55 collisions" figure
  counted MIREOT mirrors and migrated-identical pairs.
- ~~Zero-delta duplicates~~ **Resolved 2026-08-13 (step 3, gcdfo PR #78):**
  the four duplicate object properties are removed; consumers use the smn
  twins directly.

## Why PSC maps to gcdfo but refuses smn — the decisive field evidence

The PSC CV is SKOS-only, CSV-authoritative, with mappings living exclusively
in SSSOM TSVs gated by a review CSV and an allow-list of pinned sources.
Released: **18 `skos:exactMatch` + 2 `closeMatch` to gcdfo** (pinned to gcdfo
0.0.8, commit `c7a54251`) and 3 AGROVOC `closeMatch`. And
`docs/sdo-alignment-gap.md` **explicitly refuses any psc→smn mapping set
because smn's method anchor is an `owl:Class`, not a `skos:Concept`** — the
"wrong-kind" objection. gcdfo's ADR-001 ("Methods as SKOS Concepts") is
therefore winning in practice: the OWL-vs-SKOS methods decision is already
determining which cross-vocabulary mappings exist.

Consequences for the alignment pass (steps 2–4 of the execplan): migrating
smn methods to SKOS (with thin `sosa:Procedure` instance typing) resolves the
pun and dissolves PSC's objection in one move; the smn↔gcdfo boundary then
gets one SSSOM set covering the ~55 term-name collisions and the age/year
family.

## PSC pipeline constraints to budget for

- SHACL shapes are `sh:closed` — any SKOS enrichment (altLabels, in-graph
  mappings, new statuses) is a build-breaking change requiring coordinated
  shape + `build.py` + CSV edits.
- `build.py:672` hard-codes SSSOM `mapping_date`; `build.py:18-30` hard-codes
  scheme ids and the contiguous concept-id range.
- PSC's promotion gate requires reuse by "two independently governed
  organizations" — anchor via mappings, do not attempt term promotion.
- gcdfo `docs/ADR.md` numbering disagrees with `docs/adr/` files (ADR-005/006
  refer to different decisions in each place).
