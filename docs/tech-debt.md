# Tech Debt Log

This file tracks technical debt with rationale, impact, and remediation notes. Keep it current as debt is identified, addressed, or becomes obsolete.

## Active Technical Debt

### 2026-03-15 — WIDOCO changelog rendering errors on complex restrictions

**Description**: `docs-widoco` can emit `OntologyDifferencesRenderer` errors for several `SubClassOf` restrictions whose fillers are property restrictions rather than OWL classes in import chain assertions.

**Rationale**: This currently does not fail generation, but it degrades changelog readability and creates recurring false signals in CI logs.

**Impact**:
- **Severity**: Low
- **Affected Areas**: changelog artifact and release-note quality
- **User Impact**: no functional breakage; reduced trust in automatically generated release diffs
- **Maintenance Cost**: ongoing log triage

**Remediation**:
- **Effort Estimate**: Medium
- **Approach**: keep changelog generation off by default or post-filter known-safe warnings once WIDOCO behavior is updated
- **Prerequisites**: decision whether changelog is required for this ontology's release rhythm
- **Risk**: low to medium

**Status**: Active

**Related Issues/PRs**:
- `Makefile`
- `docs/context/widoco.md`

## Resolved Technical Debt

### 2026-03-15 — External SOSA/DWC protocol bridge no longer emits docs-refresh serialization noise

**Resolved Date**: 2026-03-15
**Resolution**: replaced the `sosa:ObservingProcedure owl:equivalentClass dwc:Protocol` axiom in `ontology/modules/06-data-interoperability.ttl` with a documentation-level bridge (`rdfs:comment` + `rdfs:seeAlso` to `dwc:protocol` and `dwcdp:Protocol`). `make docs-refresh` now completes without the previous ROBOT conversion warning.
**Lessons Learned**: publication-oriented interoperability hints belong in documentation-level or annotation-level bridges unless both sides are clean OWL classes with compatible semantics.

### 2026-03-15 — Migration scaffolding for build/verify docs path is in place

**Resolved Date**: 2026-03-15
**Resolution**: build flow now has scripted split-module composition + flat TTL generation for deterministic source updates before docs refresh.
**Lessons Learned**: explicit composition scripts lower the risk of manual drift when the case-study modules are touched.
