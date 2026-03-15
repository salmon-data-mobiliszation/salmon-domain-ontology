# Tech Debt Log

This file tracks technical debt with rationale, impact, and remediation notes. Keep it current as debt is identified, addressed, or becomes obsolete.

## Active Technical Debt

### 2026-03-15 — ROBOT/WIDOCO serialization warning on external SOSA/DWC axiom

**Description**: `make docs-refresh` logs a non-blocking ROBOT conversion warning for
`<http://www.w3.org/ns/sosa/ObservingProcedure> owl:equivalentClass <http://rs.tdwg.org/dwc/terms/Protocol>` while generating `docs/smn.owl`.

**Rationale**: External modeling shape appears to violate strict serializable assumptions in one conversion path, but this has not broken local parsing or ontology semantics.

**Impact**:
- **Severity**: Low
- **Affected Areas**: serialisation QA and release artifact generation
- **User Impact**: low direct user impact today
- **Maintenance Cost**: recurring noise during docs refresh and future artifact review

**Remediation**:
- **Effort Estimate**: Medium
- **Approach**: either upstream-compatible remap in source ontology or explicit tolerance note in publication runbook so this warning is treated as expected
- **Prerequisites**: access to source of the SOSA/DWC axiom and agreement on compatibility risk
- **Risk**: low semantic risk if tolerated, medium risk if we patch semantics without broader review

**Status**: Active

**Related Issues/PRs**:
- `Makefile`
- `docs/migrations/README.md`
- `docs/context/widoco.md`

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

### 2026-03-15 — Migration scaffolding for build/verify docs path is in place

**Resolved Date**: 2026-03-15
**Resolution**: build flow now has scripted split-module composition + flat TTL generation for deterministic source updates before docs refresh.
**Lessons Learned**: explicit composition scripts lower the risk of manual drift when the case-study modules are touched.
