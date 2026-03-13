# Phase 2 cutover execution runbook (DFO provider + SPSR consumer)

This runbook defines the minimum execution contract to declare phase-2
migration cutover publish-ready.

## 1) Scope

- Applies to the current phase-2 downstream reality:
  - **DFO** acts as the ontology/provider layer
  - **SPSR** is the operative downstream consumer execution lane
- Covers pre-cutover checks, cutover execution timing, owner assignments, and
  rollback triggers.
- Works with:
  - `phase2-adoption-checklist.md`
  - `phase2-downstream-smoke-run-templates.md`
  - `phase2-dfo-live-smoke-runbook.md`
  - `phase2-tier3-mapping-triage.md`

## 2) Owner matrix

| Role | Default owner | Responsibility |
| --- | --- | --- |
| Cutover coordinator | Ontology maintainer (`@Br-Johnson`) | Go/no-go facilitation, checklist completion, final cutover note |
| DFO provider verification owner | Ontology maintainer (`@Br-Johnson`) | Record that no separate DFO consumer runtime exists for this phase and attach provider-side evidence |
| SPSR smoke-run owner | SPSR consumer lead (TBD by team) | Execute SPSR smoke-run template and attach evidence |
| Rollback decision owner | Cutover coordinator + SPSR smoke-run owner | Trigger rollback when blocker criteria are met |

> If the SPSR smoke-run owner is unavailable, cutover is deferred. No separate
> DFO consumer smoke-run owner is required when no separate runtime exists.

## 3) Timing plan (Pacific time)

- Preferred window: Tuesday-Thursday, 09:00-12:00.
- Expected duration: 45-60 minutes.
- Freeze period: no ontology/module edits after T-24h except blocker fixes.

### T-5 business days

- Confirm merged PR #2 follow-up scope is stable and blocker checklist is
  current.
- Confirm SPSR smoke-run owner and meeting time.
- Confirm the DFO provider-verification note reflects current reality (no
  separate DFO runtime).
- Confirm Tier-3 triage register has explicit dispositions.

### T-1 business day

- Dry-run SPSR smoke template with representative datasets (or controlled
  fixture data).
- Confirm DFO provider-verification note/evidence links are prepared for issue
  #3.
- Confirm rollback contacts are reachable.

### T-0 cutover day

1. Go/no-go checkpoint (15 minutes)
   - Owner: cutover coordinator
   - Inputs: provider verification note, SPSR smoke evidence, triage register,
     rollback readiness
2. Publish/update canonical artifacts and references
   - Owner: ontology maintainer
3. Record DFO provider verification and execute SPSR smoke run against cutover
   target
   - Owners: DFO provider verification owner + SPSR smoke-run owner
4. Record results in issue #3 and the merged PR #2 follow-up thread/log
   - Owner: cutover coordinator

### T+1 business day

- Verify no post-cutover integration regressions are reported.
- Close/retire blocker checklist items that are complete.

## 4) Cutover checklist (execution-time)

- [ ] Go/no-go call held; SPSR owner present or delegated.
- [ ] DFO provider-verification note recorded with evidence link.
- [ ] SPSR smoke-run executed with evidence link.
- [ ] Tier-3 mapping triage dispositions reviewed and accepted for production posture.
- [ ] Publish-ready decision logged in issue #3 with timestamp and approver.

## 5) Rollback triggers

Rollback is mandatory if any of the following occurs:

1. SPSR smoke run fails on critical query/output paths.
2. DFO provider verification reveals boundary/docs drift that changes cutover
   meaning materially.
3. Tier-3 mapping behavior would require unsafe auto-canonicalization.
4. Broken namespace/prefix resolution in downstream integration scripts.
5. Missing evidence for the DFO provider-verification note or the required SPSR
   smoke run.

## 6) Rollback procedure

1. Announce rollback in issue #3 and the merged PR #2 follow-up thread/log
   immediately.
2. Revert consumer pointers/config to last known-good release artifact.
3. Mark failed cutover as `deferred` and capture root cause.
4. Open follow-up blocker item with owner + due date before rescheduling.

Rollback completion criteria:

- Previous known-good outputs restored for the operative consumer lane(s).
- New blocker entry and next cutover attempt date recorded.

## 7) Evidence format (required)

Every cutover action must include:

- Owner
- Timestamp (Pacific)
- Build target/commit reference
- Evidence link (log, query output, or checklist result)
- Status (`pass`, `fail`, `deferred`)
