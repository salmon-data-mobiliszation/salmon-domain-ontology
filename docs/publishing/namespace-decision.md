# Namespace decision for Salmon Domain Ontology (`smn`)

Status: **implemented; stabilized in `0.0.0` pre-alpha tag**
Owner: `@Br-Johnson`
Date: 2026-03-13

This file is the authoritative record of the canonical shared namespace decision.
The transition is no longer pending: the live `smn` W3ID path, canonical IRI rewrites,
migration-doc alignment, and the `0.0.0` pre-alpha stabilization tag closed the
phase-2 namespace cutover package.

## Why this decision mattered

The project needed a maintainer-controlled persistent namespace because:

- `https://w3id.org/salmon/` resolves to an unrelated external project (name collision).
- `https://w3id.org/smn` is live and gives the project a maintainer-controlled persistent base.
- Internal ontology files and migration artifacts previously used draft IRIs under `http://w3id.org/salmon/` and `http://w3id.org/salmon-domain-ontology`, which are not the canonical persistent identifiers.
- The live W3ID publication surface is intentionally conservative for now: root, `/latest`, representative term/module/build/profile paths currently resolve to Turtle artifacts only.

## Canonical namespace decision

Use one persistent shared-layer base:

- **Shared prefix:** `smn:`
- **Term namespace (`smn:`):** `https://w3id.org/smn/`
- **Ontology IRI (main build):** `https://w3id.org/smn`
- **Module IRIs:** `https://w3id.org/smn/modules/<module-name>`
- **Research build IRI:** `https://w3id.org/smn/research`
- **Case-study build IRI:** `https://w3id.org/smn/rda-case-study`
- **Profile namespaces:**
  - `https://w3id.org/smn/profile/hakai/`
  - `https://w3id.org/smn/profile/neville/`
  - `https://w3id.org/smn/profile/rda-case-study/`

## Boundary rule

- Shared reusable terms live in `smn:`.
- DFO-specific policy/program terms stay in `gcdfo:` (or other profile namespaces) and bridge to shared anchors where appropriate.

## Transition mapping (from prior draft IRIs)

| Current pattern | Canonical pattern |
| --- | --- |
| `http://w3id.org/salmon/<x>` | `https://w3id.org/smn/<x>` |
| `http://w3id.org/salmon-domain-ontology...` | `https://w3id.org/smn...` |
| `https://w3id.org/salmon-domain-ontology...` | `https://w3id.org/smn...` |
| `https://w3id.org/salmon/profile/<p>/...` | `https://w3id.org/smn/profile/<p>/...` |

## Closure gate used before broad downstream cutover

The namespace transition was treated as complete only after all were true:

1. The `smn` W3ID path was live and redirect behavior was recorded.
2. Ontology IRIs in this repo were rewritten to the canonical `https://w3id.org/smn` base.
3. Migration docs/maps used by downstream consumers were updated to the same canonical `smn` namespace story.
4. One stabilization release was tagged from the live namespace state.

## Closure checklist

- [x] W3ID path `smn` is merged and resolvable
- [x] Conservative Turtle-first redirect behavior is recorded (`docs/publishing/evidence/2026-03-13-w3id-live-redirect-check.md`)
- [x] Ontology files updated to canonical `smn` IRIs
- [x] Migration map (`docs/migrations/gcdfo-to-salmon-wave1.csv`) updated to canonical `new_iri` values
- [x] README + conventions + cutover docs updated to the same canonical namespace story
- [x] Stabilization release tagged from the live namespace state (`0.0.0`)


### Governance note for profile namespaces

`/profile/*` paths in the live `smn` namespace are intended for **project-curated bridge artifacts** (for example, the RDA pilot profiles), not by default for every organization’s canonical vocabulary.

Recommended default for any organization:
- publish local/program terms from an organization-owned namespace (their own domain, own w3id slug, etc.);
- keep canonical local terms there; for shared collaboration, publish bridge modules using one of these tracks:
  1) local draft only (no public IRI commitment yet)
  2) shared collaboration bridge at `https://w3id.org/smn/profile/<program>/` (for cross-team reuse), with explicit stewardship.

A shared profile under `/profile/<program>/` may stay there long-term, but only with a governance decision that records: owner(s), acceptance/review rhythm, version/deprecation policy, and whether SMN remains the steward of any exposed docs.

If a team wants a standalone WIDOCO/HTML site for profile terms, run WIDOCO in that team’s own ontology workspace and host docs there; SMN stays focused on shared-core and pilot profile bridge artifacts. If a team wants `smn/profile` itself to serve a profile WIDOCO site, that must be an explicit routing change in `w3id-smn-draft/.htaccess` plus an agreed publication contract.

Publishing under `https://w3id.org/smn/<org>/...` should be treated as a stewarded, cross-cutting decision, not the default.

## Publication caveat

The W3ID registration is live, and the repo now includes a generated publication surface:

- latest HTML docs at `docs/index.html`,
- latest Turtle at `docs/smn.ttl`,
- latest RDF/XML at `docs/smn.owl`,
- latest JSON-LD at `docs/smn.jsonld`,
- immutable snapshot assets at `docs/releases/0.0.0/`.

Those targets are also live on GitHub Pages at `https://salmon-data-mobilization.github.io/salmon-domain-ontology/`.

What has **not** changed yet is the live public routing contract: W3ID still serves the intentionally conservative Turtle-first/publication-v1 behavior, not the richer final content-negotiated/versioned surface. The repo now contains the exact follow-up routing draft for that switch in `docs/publishing/w3id-smn-draft/.htaccess`, aligned to the same root + SemVer content-negotiation pattern used by the live DFO Salmon Ontology W3ID rules. See also `w3id-request-payload.md` and `docs/publishing/evidence/2026-03-13-w3id-live-redirect-check.md`.

## Notes on repository entrypoint

`/salmon-domain-ontology.ttl` at repo root now exists as a generated, flattened, import-free master TTL for one-file consumers.
`ontology/salmon-domain-ontology.ttl` remains the canonical modular local source of truth.
Canonical public ontology IRI is still `https://w3id.org/smn`.
