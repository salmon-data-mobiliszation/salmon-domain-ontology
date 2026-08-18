# Bundle log

- 2026-08-12 — Bundle seeded from step-0 recon of the ontology alignment pass
  (metasalmon roadmap S9). Five cards: domain, context, and three
  InformationObject cards carrying the verified builds/imports facts, the
  F1–F8 conventions findings, and the cross-vocabulary alignment state.
  All cards `status: draft`; sources cited inline as file:line against the
  commits named in each card. Validation: `psc-okf check --tier capture`.
- 2026-08-13 — Codex review fixes: corrected the module-02 card (class-level
  property assertions are legal OWL 2 DL punning, not OWL Full; remedy is a
  targeted SPARQL report plus axiom rewrite, not the DL gate) and registered
  the bundle in docs/entrypoints.md.
- 2026-08-13 — Portability pass: removed all absolute filesystem paths (new
  hub rule); validation command is now relative to a sibling psc-data-systems
  checkout. Cross-repo references updated for metasalmon's notes/ -> knowledge/
  migration.
- 2026-08-13 — S9 step 1 (alignment semantics): F1-F7 fixed, F8 property-side
  fixed; conventions cards updated to reflect the landed state.
- 2026-08-13 — S9 steps 2+5: methods-as-SKOS migration (smn:MethodScheme) and
  smn:StatisticalModifierScheme landed; cross-repo pun resolved; cards updated.
- 2026-08-13 — PR 22 review: added ontology/shapes/method-shapes.ttl (the
  enumeration-method value constraint, SKOS-native via skos:broader*,
  behaviourally tested with pyshacl) and refreshed the conventions card's
  module-07 inventory (10 schemes / 49 concepts).
- 2026-08-13 — S9 step 1b (tooling): verify targets are read-only, generated
  modules 08/09 gain a drift gate, CONVENTIONS 5b checks + method-shapes
  behavioural check wired into make test and CI, new ELK reasoner-gate CI job
  (passes: consistent, zero unsatisfiable classes), views documented as
  non-dereferenceable identifiers.
- 2026-08-13 — S9 step 3 (smn side): the two alignment rows referencing the
  never-declared smn:FisheriesReferencePointLower retarget the re-namespaced
  gcdfo:FisheriesReferencePointLower (gcdfo PR 78 carries the rename and the
  new gcdfo-to-smn SSSOM mapping set, 28 rows, pinned both sides).
- 2026-08-17 — SPSR-derived term proposal (branch
  `feat/spsr-shared-life-history-schemes`, ADR-0003, **not merged**): the DFO
  Conservation Unit species code is decomposed rather than minted whole. Four
  SKOS schemes for module 07 — two species-neutral life-history axes
  (juvenile freshwater residence, juvenile nursery habitat), one scheme of
  species-scoped named types defined as combinations of them, and cycle line
  — plus five object properties in modules 01/02. Cross-vocabulary card gains
  the verified psc→smn anchoring state (one released target, hard allow-list,
  wrong-kind and too-broad rejections, four recorded gaps). The conventions
  card's module-07 inventory is deliberately **left at 10 schemes / 49
  concepts**: it records what is released, and the proposal would make it
  14/62 only on merge. If ADR-0003 is accepted, bump that count in the same
  PR that merges it; if it is rejected or reshaped, nothing needs undoing.
- 2026-08-17 — Reproducibility defect found and fixed while proposing those
  terms: the generated root flat TTL was **hash-order dependent**. The merged
  graph carried no prefix bindings, so rdflib invented `ns1:`/`ns2:`/... for
  predicate namespaces in store-iteration order; one such namespace was stable
  by luck, two were not. Eight generator runs on `main` gave one hash; eight on
  the branch gave four. `make verify-flat-ttl` would have flaked in CI with no
  source change behind it. Fixed by binding the prefixes the modules declare;
  see the builds card. The artifact now reads `smn:Term` instead of
  `<https://w3id.org/smn/Term>`, which is a large one-time diff in
  `salmon-domain-ontology.ttl` and `docs/smn.ttl` with no semantic content.
- 2026-08-17 — Three rulings recorded in ADR-0003 (Brett Johnson, 2026-08-17),
  which reshaped that proposal after a taxonomic-authority and life-history
  literature review. (1) **Steelhead is in scope**, and steelhead has no
  taxonomic identifier in ITIS, WoRMS, NCBI, GBIF, or Catalogue of Life — it
  is a vernacular of *O. mykiss* everywhere and is managed by NOAA as 11 DPSs.
  With four of the seven CU codes, kokanee, and steelhead absent from every
  taxonomic authority, and those authorities actively diverging (Lahontan and
  Rio Grande cutthroat elevated by WoRMS/COL/GBIF but not ITIS/NCBI;
  *Oncorhynchus lewisi* in none of the five), the proposed
  `smn:SalmonSpeciesScheme` and its five species concepts were **withdrawn**.
  (2) **Life-history type is asserted at CU / population / stock level, never
  for an individual fish.** (3) **If a species reference is needed later it
  goes in `smn`, never `gcdfo`** — `smn` is the shared all-agency layer. Also
  verified by request, not report: the NCBI Taxonomy OBO PURL serves
  `text/html` under `text/turtle`, `application/rdf+xml`, and
  `application/ld+json` alike, so the withdrawn scheme's five `rdfs:seeAlso`
  links resolved to documentation rather than data.
- 2026-08-17 — Correction to a fact recorded on the open branch
  `fix/label-ambiguity-at-source` (PR 26), not yet on main: that branch's F9
  section calls the `make verify-generated-artifacts` changelog failure
  "environment- (likely network-) dependent". It is not. GitHub Actions
  produces the same populated `<div id="changelog">` block, byte-for-byte,
  that a local run produces — the local and CI diffs on PR 27 carry identical
  blob hashes (a4268f7..df5d5f4). The committed `null` on main is simply
  **stale**: it entered at `5279971`, the 0.0.3 re-cut, when WIDOCO could not
  download the `owl:priorVersion` `https://w3id.org/smn/0.0.3` because that
  snapshot had not yet reached Pages. Every branch that regenerates docs
  inherits the failure until it commits the real block; PR 27 commits it.
  **Resolved 2026-08-17:** PR 26 now carries the amended F9 paragraph and its
  own regenerated block, so the card and this entry agree. The one residual
  sensitivity, recorded there: an offline `make ci` still writes `null`, and
  that is the broken direction.
- 2026-08-14 — Release 0.0.3 cut: first release carrying the alignment-pass
  state (imported W3C SOSA-PROV alignment, CONVENTIONS 5b + CI gates,
  methods-as-SKOS in smn:MethodScheme, smn:StatisticalModifierScheme,
  EscapementEstimate rename, step-3 boundary updates). PSC anchoring (S9
  step 4) pins against this release.
