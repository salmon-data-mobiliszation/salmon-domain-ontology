# Phase 2 release-readiness notes (DFO + SPSR downstream consumers)

These notes track the minimum evidence required before publish-ready migration/cutover.

## Readiness dimensions

### 1) Shared/profile boundary stability

- Boundary rules documented and aligned with `CONVENTIONS.md`
- Deferred profile terms remain out of shared core
- Bridge modules are used for profile concept interoperability without semantic collapse

### 2) Migration artifact completeness

- Machine map exists: `gcdfo-to-salmon-wave1.csv`
- Human-readable inventory exists: `wave1-term-inventory.md`
- Case-study bridge coverage exists: `rda-graph-concept-coverage.md`
- Phase 2 operational docs exist:
  - `phase2-boundary-rules.md`
  - `phase2-adoption-checklist.md`

### 3) DFO downstream readiness

Required evidence:

- DFO pipelines can consume shared `salmon:` terms for migrated rows.
- Deferred DFO terms remain profile-resolved without loss.
- No production dependency on auto-canonicalizing Tier 3 mappings.

### 4) SPSR downstream readiness

Required evidence:

- SPSR query/report layer resolves shared terms and bridge mappings.
- Reports depending on policy-specific vocabularies keep profile references.
- At least one end-to-end smoke run passes against selected build target.

## Remaining blockers before publish-ready cutover

1. **Consumer sign-off evidence is not yet recorded in-repo** for DFO and SPSR smoke runs.
2. **Cutover execution runbook is not yet finalized** (timing, owner, rollback trigger).
3. **Tier 3 mapping promotion queue is not yet explicitly triaged** for production auto-canonicalization eligibility.

Track and close these blockers via GitHub issues before marking migration as publish-ready.
