# Entrypoints (What Is Actually Used?)

Purpose: keep one short, reliable map of what starts the ontology builds, what is wired in, and where to edit things.

## Run (human-facing)

- Start command(s): none; this repo ships ontology artifacts and docs, not a running app/service.
- Local URL(s): none.
- Required environment variables (names only, no secrets): none for normal doc/ontology work.

## Build

- Canonical release path: `make release VERSION=X.Y.Z`
- Canonical publication refresh: `make docs-refresh`
- Compose split case-study fragments: `make compose-case-study-modules`
- Rebuild flattened master TTL: `make compose-flat-ttl`
- Build the root-ontology-only WIDOCO input: `make docs-widoco-input`
- Verify flat TTL is up-to-date: `make verify-flat-ttl`
- Verify ontology Turtle parses cleanly: `make verify-ontology-parse`
- Verify WIDOCO term anchors stay stable: `make verify-doc-term-anchors`
- Verify WIDOCO version metadata renders from source: `make verify-doc-version-metadata`
- Run the fast validation bundle: `make test`
- Run the full local CI bundle: `make ci`
- CI drift gate for generated artifacts: `make verify-generated-artifacts`
- WIDOCO only: `make docs-widoco`
- Serializations only: `make docs-serializations`
- Immutable release snapshot from current docs: `make snapshot-release VERSION=X.Y.Z`
- Immutable release snapshot with refresh: `make release-snapshot VERSION=X.Y.Z`
- Main deliverables:
  - `ontology/salmon-domain-ontology.ttl` - primary modular build
  - `ontology/salmon-domain-ontology-research.ttl` - research overlay build
  - `ontology/salmon-domain-ontology-rda-case-study.ttl` - case-study/profile-bridge build (working integration pilot, profile-scoped by default)
  - `salmon-domain-ontology.ttl` - generated flattened, import-free master TTL artifact for one-file consumers
  - `docs/index.html` - latest generated HTML docs
  - `docs/smn.ttl` / `docs/smn.owl` / `docs/smn.jsonld` - latest downloadable serializations
  - `docs/releases/<version>/` - immutable release snapshot surface
  - `ontology/views/salmon-data-metamodel.ttl` - optional non-normative metamodel view (not part of default imports)

## Test

- Test command(s):
  - Parse all ontology Turtle files:
    ```bash
    make verify-ontology-parse
    ```
  - Rebuild and verify the flat master artifact does not drift:
    ```bash
    make verify-flat-ttl
    ```
  - Verify documented `smn:` terms still expose stable WIDOCO `#/Term` anchors:
    ```bash
    make verify-doc-term-anchors
    ```
  - Verify the generated WIDOCO HTML still exposes ontology release metadata:
    ```bash
    make verify-doc-version-metadata
    ```
  - Run the full fast validation bundle:
    ```bash
    make test
    ```
  - Regenerate fixture smoke evidence when the migration/evidence helper changes:
    ```bash
    python3 docs/migrations/evidence/run_phase2_smoke_fixture_checks.py
    ```
- Fastest smoke test: `make test` after any ontology/doc refresh.

## App Entry Points / Wiring

- Main entry file(s):
  - `ontology/salmon-domain-ontology.ttl`
  - `ontology/salmon-domain-ontology-research.ttl`
  - `ontology/salmon-domain-ontology-rda-case-study.ttl`
  - `salmon-domain-ontology.ttl` (generated, flattened one-file artifact)
- Routes / handlers / commands:
  - No app routes.
  - Publication-routing source of truth lives in:
    - `docs/publishing/namespace-decision.md`
    - `docs/publishing/w3id-request-payload.md`
    - `docs/publishing/w3id-smn-draft/.htaccess` (current live root + SemVer contract mirror)
    - `docs/publishing/w3id-term-dereference-draft/.htaccess` (pending term-path human-dereferencing follow-up)
- Background jobs (if any): none.

## UI Styling

- Canonical styling system (repo-majority): not applicable.
- Style entry files / patterns: not applicable.
- Design tokens / CSS variables live in: not applicable.
- Inline styles policy: not applicable.

## Canonical Implementations (Per Feature)

- Shared ontology core -> `ontology/salmon-domain-ontology.ttl` importing modules `01`-`07` plus `ontology/modules/alignment-main.ttl`
- Flattened one-file build artifact -> `salmon-domain-ontology.ttl` (auto-generated from the canonical core source)
- WIDOCO docs input -> `release/tmp/widoco-input.ttl` (auto-generated from the flattened artifact with only the root ontology declaration retained)
- Research alignment overlay -> `ontology/salmon-domain-ontology-research.ttl` + `ontology/modules/alignment-research.ttl`
- Case-study/profile bridges -> `ontology/salmon-domain-ontology-rda-case-study.ttl` + modules `08` and `09` (RDA juvenile-condition pilot, explicit manual-to-automation mapping reference)
  - `08` and `09` are assembled from split files under `ontology/case-studies/rda-juvenile-condition/`.

- Optional metamodel view surface -> `ontology/views/salmon-data-metamodel.ttl` + supporting files under `ontology/views/` (kept out of the shared-core import spine by default)

- `https://w3id.org/smn` root + release routes are live via W3ID publication config; canonical term-path human dereferencing is defined in the pending W3ID follow-up draft under `docs/publishing/w3id-term-dereference-draft/`
- Modeling rules and boundary decisions -> `CONVENTIONS.md` + `docs/migrations/phase2-boundary-rules.md`
- Migration/cutover status and evidence -> `docs/migrations/README.md` + `docs/migrations/phase2-*.md` + `docs/migrations/evidence/`
- Namespace/publication posture -> `docs/publishing/namespace-decision.md` + `docs/publishing/w3id-request-payload.md`

## What to read before editing

- Changing ontology terms/modules/build imports:
  - `CONVENTIONS.md`
  - `ontology/modules/README.md`
  - `ontology/views/README.md` (if you are touching the optional metamodel view layer)
  - the relevant module(s) under `ontology/modules/`
- Changing migration/cutover docs:
  - `docs/migrations/README.md`
  - `docs/migrations/phase2-adoption-checklist.md`
  - `docs/migrations/phase2-cutover-execution-runbook.md`
  - `docs/migrations/phase2-tier3-mapping-triage.md`
- Changing namespace/publication docs:
  - `docs/context/widoco.md`
  - `docs/publishing/namespace-decision.md`
  - `docs/publishing/w3id-request-payload.md`
  - `docs/publishing/evidence/2026-03-13-w3id-live-redirect-check.md`
