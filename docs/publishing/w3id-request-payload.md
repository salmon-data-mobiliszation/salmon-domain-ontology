# W3ID registration record for `smn`

Status: registration merged in `perma-id/w3id.org` PR #5829; follow-up routing update merged in PR #5873; path live
Target registry: <https://github.com/perma-id/w3id.org>
Requested path: `smn`

## Current status

The W3ID registration is now live.

Current live behavior:

- `https://w3id.org/smn` resolves as the canonical ontology IRI.
- Root routing now follows the live DFO Salmon Ontology pattern: HTML by default, with Turtle / RDF/XML / JSON-LD served via `Accept`-based `303` redirects.
- SemVer version paths such as `https://w3id.org/smn/0.0.0` now resolve to immutable release HTML by default, with versioned Turtle / RDF/XML / JSON-LD served via `Accept`-based `303` redirects.
- Secondary surfaces remain intentionally Turtle-first for now: representative term paths, module paths, research/case-study builds, and profile roots still resolve via `303` to raw GitHub Turtle artifacts.
- The routed publication targets live at `https://salmon-data-mobilization.github.io/salmon-domain-ontology/`, including `smn.ttl`, `smn.owl`, `smn.jsonld`, and immutable `releases/X.Y.Z/` snapshots.

This file keeps the merged registration payload in-repo and records the initial registration plus the later routing upgrade.

## Follow-up update status

The follow-up W3ID routing update is now merged and live:

- PR: <https://github.com/perma-id/w3id.org/pull/5873>
- Title: `smn: align W3ID root/version redirects with DFO content negotiation`
- Merged: `2026-03-26T23:54:33Z`
- Live verification: `docs/publishing/evidence/2026-03-26-w3id-content-negotiation-live-check.md`

## Merged PR contents in `perma-id/w3id.org`

Folder:

- `smn/`

Files:

- `smn/.htaccess`
- `smn/README.md`

Local reference sources:

- `.htaccess` reference: `docs/publishing/w3id-smn-draft/.htaccess`
- `README.md` reference: `docs/publishing/w3id-smn-draft/README.md`

## Registration PR title

`Add w3id redirects for smn`

## Registration PR body (historical reference)

```markdown
This PR registers persistent identifiers for the Salmon Domain Ontology shared layer.

Requested base:
- https://w3id.org/smn

Maintainer repository:
- https://github.com/salmon-data-mobilization/salmon-domain-ontology

Why:
- `w3id.org/salmon` is controlled by an unrelated project.
- The Salmon Domain Ontology shared layer now uses `smn:` as its canonical namespace/prefix.
- We need a maintainer-controlled persistent base for shared terms, module IRIs, and profile bridge namespaces.

Current registration behavior:
- This registration uses safe latest Turtle redirects for currently published repo assets.
- DFO-style HTML/RDF/XML/JSON-LD and SemVer version-path redirects are planned, but the corresponding public publication targets are not live yet.

Redirect behavior in the current registration:
- `/` and `/latest` resolve to the latest main Turtle build.
- `/research` and `/rda-case-study` resolve to current build artifacts.
- `/modules/<name>` resolves to module Turtle artifacts.
- `/profile/*` paths resolve to current bridge artifacts.
- term paths like `/Stock` resolve to the shared main Turtle graph.

Follow-up after publication-target work:
- switch latest-path redirects to stable public HTML/Turtle/RDFXML/JSON-LD assets
- add SemVer version-path redirects matching the live DFO pattern
```

Since that registration landed, the repo gained generated in-repo assets under `docs/` plus `docs/releases/0.0.0/`, and the later follow-up W3ID routing update has now switched the root + SemVer public contract to the verified GitHub Pages publication surface.

## Verification commands for the live registration

### Current live checks

```bash
curl -I https://w3id.org/smn
curl -I -H 'Accept: text/turtle' https://w3id.org/smn
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn
curl -I https://w3id.org/smn/0.0.0
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/0.0.0
curl -I https://w3id.org/smn/Stock
curl -I https://w3id.org/smn/modules/01-entity-systematics
curl -I https://w3id.org/smn/research
curl -I https://w3id.org/smn/rda-case-study
```

Expected for the current live contract:

- root returns `301` to the trailing-slash form, then `303` redirects to latest HTML / Turtle / RDFXML / JSON-LD targets depending on `Accept`
- SemVer version paths return `303` redirects to immutable `releases/X.Y.Z/` HTML or versioned serializations depending on `Accept`
- representative term/module/build/profile secondary surfaces continue resolving to Turtle artifacts

See:

- `docs/publishing/evidence/2026-03-26-w3id-content-negotiation-live-check.md` for the current live contract
- `docs/publishing/evidence/2026-03-13-w3id-live-redirect-check.md` for the initial conservative registration state (historical)

## Follow-up W3ID step

Completed.

The follow-up `perma-id/w3id.org` PR merged and the live `smn` contract now uses DFO-style root + SemVer content negotiation for the shared ontology root while keeping secondary surfaces Turtle-first.
