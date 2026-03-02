# DFO smoke run — 2026-03-02

## Metadata

| Field | Value |
| --- | --- |
| Owner | Alan (OpenClaw subagent on behalf of @Br-Johnson) |
| Date/time (PT) | 2026-03-02 08:31 PST |
| Build target | `ontology/salmon-domain-ontology.ttl` (shared modules fixture execution) |
| Branch/commit | `feat/module-domain-decomposition` @ `330d8da52b7a33e69f4589fe0f156733a36fc95a` |
| Dataset/input snapshot | `docs/migrations/gcdfo-to-salmon-wave1.csv`; shared modules `01-07` + `alignment-main`; local DFO repo scan; local SPSR template dictionary proxy for deferred-profile survivability |
| Environment | Local workspace fixture run (no live DFO consumer runtime available) |

## Checklist

- [ ] **Prefix migration check**: consumer configs bind shared namespace to `http://w3id.org/salmon/`.
  - Status: **GAP**
  - Evidence: local scan of `code/dfo-salmon-ontology` found no `w3id.org/salmon/` references (see JSON artifact below).
- [x] **Migrated-term check**: at least 3 `status=migrated` terms from `gcdfo-to-salmon-wave1.csv` resolve in pipeline/query output.
  - Status: **PASS**
  - Evidence: `ReportingOrManagementStratum`, `Stock`, `Deme` resolve in shared module graph.
- [x] **Deferred-profile check**: at least 2 `status=deferred_profile` terms remain profile-resolved (not promoted to shared).
  - Status: **PASS**
  - Evidence: `ConservationUnit` + `StockManagementUnit` not present as shared `salmon:` terms.
- [x] **Bridge handling check**: profile bridge terms are accepted without forcing canonical promotion.
  - Status: **PASS (fixture proxy)**
  - Evidence: deferred-profile terms remain consumable in local template artifacts (`ConservationUnit` rows=125, `StockManagementUnit` rows=84).
- [ ] **Output parity check**: key output fields match expected structure from last known-good run.
  - Status: **GAP**
  - Evidence: no local DFO consumer runtime/output baseline present in workspace.

## Result block (issue #3 paste-ready)

#### DFO smoke run — 2026-03-02
- Owner: Alan (OpenClaw subagent)
- Build/commit: `feat/module-domain-decomposition` @ `330d8da52b7a33e69f4589fe0f156733a36fc95a`
- Dataset: fixture run from migration map + shared modules + local repo scans
- Result: **DEFERRED**
- Evidence:
  - `docs/migrations/evidence/2026-03-02-phase2-smoke-fixture-results.md`
  - `docs/migrations/evidence/2026-03-02-phase2-smoke-fixture-results.json`
- Notes: Live DFO consumer config/output artifacts are external to this workspace; fixture checks passed where executable, but prefix-binding + output-parity remain blocked pending DFO operational run.

## Deferred-run required fields

- Explicit blocker reason: no live DFO consumer runtime/config/output baseline available locally.
- Owner for unblock action: DFO consumer lead (TBD in issue #3 owner checklist).
- Next execution date: 2026-03-05 (or next available DFO runtime window).
