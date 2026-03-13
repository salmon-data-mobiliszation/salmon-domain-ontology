# Phase 2 release-readiness notes (DFO provider + SPSR downstream consumer)

These notes track the minimum evidence required before publish-ready
migration/cutover.

## Readiness dimensions

### 1) Shared/profile boundary stability

- Boundary rules documented and aligned with `CONVENTIONS.md`.
- Deferred profile terms remain out of shared core.
- Bridge modules are used for profile concept interoperability without semantic
  collapse.

### 2) Migration artifact completeness

- Machine map exists: `gcdfo-to-salmon-wave1.csv`.
- Human-readable inventory exists: `wave1-term-inventory.md`.
- Case-study bridge coverage exists: `rda-graph-concept-coverage.md`.
- Phase 2 operations docs exist:
  - `phase2-boundary-rules.md`
  - `phase2-adoption-checklist.md`
  - `phase2-cutover-execution-runbook.md`
  - `phase2-downstream-smoke-run-templates.md`
  - `phase2-dfo-live-smoke-runbook.md`
  - `phase2-tier3-mapping-triage.md`

### 3) DFO provider readiness

Required evidence:

- DFO/provider-side docs and route-coverage artifacts align to the locked
  `smn:` shared / `gcdfo:` profile boundary.
- Existing fixture/prereq evidence is retained as non-live supporting evidence.
- The absence of a separate DFO downstream consumer runtime is recorded
  explicitly, rather than hidden behind a fictional live-smoke gate.

### 4) SPSR downstream readiness

Required evidence:

- SPSR query/report layer resolves shared terms and bridge mappings.
- Reports depending on profile vocabularies retain expected references.
- At least one end-to-end smoke run passes against selected build target.

## Blocker register (issue #3)

| Blocker | Owner | Evidence | Status |
| --- | --- | --- | --- |
| DFO provider verification recorded (no separate DFO consumer runtime exists) | Ontology maintainer (`@Br-Johnson`) | `docs/migrations/evidence/2026-03-02-dfo-live-smoke-prereq-package.md` + `phase2-dfo-live-smoke-runbook.md` + issue #3 provider-verification comment | Pending issue #3 provider-verification note |
| SPSR consumer smoke-run evidence recorded | Alan (OpenClaw subagent) | Issue #3 SPSR evidence comment + `docs/migrations/evidence/2026-03-02-spsr-smoke-run.md` | **Cleared** |
| Cutover execution runbook finalized (timing, owner, rollback) | Ontology maintainer (`@Br-Johnson`) | `phase2-cutover-execution-runbook.md` | Cleared |
| Tier-3 mapping queue explicitly triaged for production policy | Ontology maintainer (`@Br-Johnson`) | `phase2-tier3-mapping-triage.md` | Cleared |

## Publish-ready decision gate

Publish-ready cutover requires:

1. SPSR consumer smoke evidence is closed and DFO provider verification is
   recorded in issue #3.
2. No unresolved critical regressions from the SPSR smoke run or provider-side
   verification.
3. Cutover coordinator records final go/no-go decision in issue #3.
