# W3ID registration record for `smn`

Status: merged in `perma-id/w3id.org` PR #5829; path live
Target registry: <https://github.com/perma-id/w3id.org>
Requested path: `smn`

## Current status

The W3ID registration is now live.

Current live behavior:

- `https://w3id.org/smn` resolves as the canonical ontology IRI.
- The live redirect surface is still the conservative Turtle-first registration.
- Root, representative term paths, module paths, build paths, and profile roots resolve via `303` to raw GitHub Turtle artifacts.
- The repo now also carries live GitHub Pages publication targets at `https://salmon-data-mobilization.github.io/salmon-domain-ontology/`, including `smn.ttl`, `smn.owl`, `smn.jsonld`, and an immutable `releases/0.0.0/` snapshot.
- `docs/publishing/w3id-smn-draft/.htaccess` now contains the exact follow-up routing draft to switch `https://w3id.org/smn` and `https://w3id.org/smn/X.Y.Z` to the GitHub Pages publication surface using the same root + SemVer content-negotiation pattern as the live DFO Salmon Ontology rules, while leaving research/module/profile/term paths Turtle-first.

This file keeps the merged registration payload in-repo and records the follow-up publication work.

## Follow-up update status

A follow-up W3ID PR has now been opened to switch `smn` root + SemVer routing to the GitHub Pages publication surface using the same content-negotiation pattern as the live DFO Salmon Ontology rules:

- PR: <https://github.com/perma-id/w3id.org/pull/5873>
- Title: `smn: align W3ID root/version redirects with DFO content negotiation`

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

## Registration PR body (reference)

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

Since that registration landed, the repo has gained generated in-repo assets under `docs/` plus `docs/releases/0.0.0/`, but the live W3ID rules still intentionally serve the conservative Turtle-first surface until stable public targets are chosen and verified.

## Verification commands for the live registration

### Conservative Turtle-first checks

```bash
curl -I https://w3id.org/smn
curl -I https://w3id.org/smn/Stock
curl -I https://w3id.org/smn/modules/01-entity-systematics
curl -I https://w3id.org/smn/research
curl -I https://w3id.org/smn/rda-case-study
curl -I https://w3id.org/smn/profile/hakai
curl -I -H 'Accept: text/turtle' https://w3id.org/smn
```

Expected for the current registration: root returns `301` to the trailing-slash form, then `303` redirects resolve to the corresponding raw GitHub Turtle artifacts. See `docs/publishing/evidence/2026-03-13-w3id-live-redirect-check.md` for recorded evidence.

### Follow-up content-negotiation checks (for the next W3ID PR)

```bash
curl -I https://w3id.org/smn
curl -I -H 'Accept: text/turtle' https://w3id.org/smn
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn
curl -I https://w3id.org/smn/0.0.0
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/0.0.0
```

Expected after the follow-up routing change: content-negotiated `303` redirects for latest HTML/Turtle/RDFXML/JSON-LD plus SemVer version-path redirects to the GitHub Pages publication surface, matching the live DFO Salmon Ontology root + version pattern.

## Follow-up W3ID step

The publication targets now exist and have been verified on GitHub Pages:

- latest HTML docs,
- latest Turtle,
- latest RDF/XML,
- latest JSON-LD,
- versioned release snapshots.

That follow-up `perma-id/w3id.org` PR has now been opened and replaces the conservative root + generic catch-all behavior with DFO-style root + SemVer content negotiation using the exact GitHub Pages routing captured in `docs/publishing/w3id-smn-draft/.htaccess`.
