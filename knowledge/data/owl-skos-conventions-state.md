---
type: InformationObject
title: OWL/SKOS conventions — stated vs practiced
description: Where the repository's modelling practice diverges from CONVENTIONS.md, with the eight adversarially verified metamodel findings (F1–F8) from the 2026-08-12 recon and the upstream-spec facts they rest on.
status: draft
tags: [owl, skos, conventions, metamodel, iadopt, sosa]
psc:
  id: smn:data:owl-skos-conventions-state
  contexts: [smn:context:ontology-alignment-pass-2026]
---

Verified 2026-08-12 (main at `3995a17`). Fix plan: step 1 of
`metasalmon/knowledge/plans/2026-08-12-ontology-alignment-pass.md`.

## What holds

- File-level OWL/SKOS separation is clean: modules 01–05 pure OWL (63
  classes, 13 properties), module 07 pure SKOS (8 schemes, 36 concepts),
  bridges 08/09 pure profile-namespace SKOS.
- The dual-representation rule (`CONVENTIONS.md:72`) holds at the
  explicit-typing level: **no IRI in `ontology/modules/` is declared both
  `owl:Class` and `skos:Concept`** (scripted scan).
- The §12 basis-vs-dimension split is honored (e.g. `smn:BroodYearBasis`
  concept at `07:181` vs `smn:broodYear` datatype property at `02:303`), and
  `ontology/examples/fraser-stock-recruit-year-age.ttl` follows it —
  including using **native** `iadopt:hasProperty/hasObjectOfInterest/hasConstraint`.
- Annotation completeness is bimodal by design history: modules 03/05/07
  ~100% complete against §10; modules 01/02/04 carry exactly the 43 missing
  definitions already tracked in `docs/annotation-gap-ledger.md`.

## Verified divergences (adversarial verdicts, 2026-08-12)

- **F1 (nuanced)** — the views assert OWL axioms on foreign subjects
  (`iadopt:Variable rdfs:subClassOf iao:0000030, sosa:Property`
  `views/salmon-data-metamodel-variable.ttl:14-15`; `sosa:Observation ⊑
  prov:Activity` `event-observation:15`; three `sosa:* ⊑ prov:*` property
  axioms `provenance:14-16`). Not an exposure incident (views unreachable —
  see the builds card) but a policy gap: CONVENTIONS never says whether
  foreign-subject Tier-1 axioms are permitted anywhere.
- **F2 (confirmed)** — Tier-mixed pairs: `iadopt:Variable` gets Tier-1
  `subClassOf` **and** Tier-3 `closeMatch` to `sosa:Property`
  (`variable.ttl:14,69`); worse, the **default build** carries module 06's
  `owl:equivalentClass sosa:Observation ≡ dwc:Occurrence` (`06:22`) alongside
  alignment-main's `closeMatch` on the same pair (`alignment-main:81`).
- **F3 (confirmed)** — `smnv:variableRepresentsProperty/…Entity/…UsesConstraint/…UsesStatisticalModifier`
  duplicate I-ADOPT's native `iop:hasProperty/hasObjectOfInterest/hasConstraint/hasStatisticalModifier`
  with no `subPropertyOf` bridges — while `smnv:constraintConstrains` *is*
  bridged (`variable.ttl:65`) and the fraser example uses `iop:` directly.
  Case-study walkthrough instance data is therefore invisible to
  I-ADOPT-aware consumers.
- **F4 (confirmed)** — relative `owl:imports` in the composite view; no
  catalog; no w3id `views/` route (see the builds card).
- **F5 (nuanced)** — `iadopt:Property ⊑ iao:0000030` is wrong by I-ADOPT's own
  definition (Property = "a type of a characteristic", not a description) and
  collides with module 06's `iadopt:Property owl:equivalentClass
  sosa:Property`; ICE typing of `Variable`/`Constraint` is defensible by
  I-ADOPT's wording.
- **F6 (confirmed)** — `smn:EscapementMeasurement` (a **datum**,
  ⊑ `iao:0000109`, `02:253`) is the lone `*Measurement` class that is not a
  subclass of the **activity** `smn:Measurement` (`02:147`). The name
  (inherited from gcdfo) is the defect; the view mappings are correct.
- **F7 (nuanced)** — TDWG **redefined `dwc:Occurrence` on 2026-05-26** ("A
  dwc:Event that establishes the state of a dwc:Organism…"), which makes
  `sosa:Observation closeMatch dwc:Occurrence` defensible, but module 06's
  `equivalentClass` versions (`06:22-23`) are indefensible under any DwC
  vintage; `sosa:Sampling closeMatch dwc:Event` should weaken to
  `broadMatch` (Event is strictly broader).
- **F8 (nuanced)** — `smnv:variableUsesStatisticalModifier rdfs:range
  owl:Thing` is an unnecessary placeholder: **I-ADOPT 1.1.0 has
  `StatisticalModifier` + `iop:hasStatisticalModifier`**. No smn statistical
  scheme exists among module 07's eight schemes.

## Upstream facts these rest on (fetched 2026-08-12)

- I-ADOPT current release **1.1.0** (2025-05-28): 9 classes (incl.
  `StatisticalModifier`, `VariableSet`), 17 object properties;
  ObjectOfInterest/ContextObject/Matrix are **roles, not classes**; no
  unit/method component; **no published SOSA alignment**.
- SOSA/SSN 2017 REC: all five published alignments (incl. PROV-O) are
  **non-normative**; a 2023 Edition exists only as a First Public Working
  Draft (2025-09-16) — do not pin conventions to it.
- **Unresolved:** one verifier claimed the views' PROV axioms diverge from
  W3C's `sosa-prov-mapping.ttl` (`hasFeatureOfInterest ⊑ prov:used`); the
  upstream surveyor read that file and found they match. Read the mapping
  file directly before writing any alignment-core module.
- No authoritative DwC↔SOSA mapping exists anywhere; any assertion is a
  local editorial commitment and belongs in a clearly-labeled alignment
  module (SSN practice), never in a core module.

## Module 02 latent modeling errors

`02:213-214` applies object properties **between classes**
(`sosa:FeatureOfInterest sosa:hasSample sosa:Sample`;
`sosa:Sample sosa:isResultOf sosa:Sampling`). This is *legal* OWL 2 DL —
using a class IRI in individual position is punning, and the two meanings are
kept semantically separate — so a DL-profile gate will **not** flag it. That
separation is exactly the problem: the triples relate the class-individuals
and say **nothing about any instance**, while the author almost certainly
intended instance-level semantics (e.g.
`sosa:FeatureOfInterest ⊑ hasSample some sosa:Sample` restrictions) or a
mere schema-level pointer (`rdfs:seeAlso`). Remedy (step 1): rewrite the
axioms to say what is meant, and add a **targeted** CI report (a SPARQL query
flagging object-property assertions whose subject or object is also an
`owl:Class`) — the generic reasoner gate alone cannot catch this class of
mistake.
