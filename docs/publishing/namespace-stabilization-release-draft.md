# Namespace stabilization release draft

Status: proposed

## Recommended tag

`0.1.0`

## Suggested release title

`0.1.0 — smn namespace stabilization`

## Why this tag

- First SemVer tag in the repo.
- Matches the future plain-semver W3ID version-path pattern (`/0.1.0`).
- Cleanly marks the first post-W3ID-live stabilization point.

## Scope for this release slice

- Canonical shared namespace locked to `https://w3id.org/smn` (`smn:`).
- Ontology, module, research, and case-study build IRIs rewritten to the live namespace.
- Migration map and cutover docs aligned to the canonical `smn` story.
- Contributor issue templates added for low-friction term/model maintenance.
- Live W3ID redirect verification recorded for the conservative Turtle-first surface.

## Explicitly not included in this release

- Published HTML docs.
- Published RDF/XML serialization.
- Published JSON-LD serialization.
- Versioned release snapshot directories served from a stable public host.
- A separate DFO live-runtime smoke pass. There is currently no separate DFO downstream consumer runtime for this phase, so issue #3 closure depends on the provider-verification note + final go/no-go logging instead.

## Release notes draft

```markdown
## Summary

This release establishes `https://w3id.org/smn` as the canonical shared namespace for the Salmon Domain Ontology and records the first stable post-registration baseline.

## Included

- rewrites ontology/module/profile IRIs to the canonical `smn` base
- aligns migration artifacts and cutover docs to `smn:`
- documents the live W3ID redirect behavior for the current Turtle-first publication surface
- adds issue templates for new terms, missing superclasses, definition updates, and obsoletions

## Current publication posture

The W3ID path is live, but publication remains intentionally conservative for now:

- root, `/latest`, representative term/module/build/profile paths resolve to current Turtle artifacts
- HTML docs, RDF/XML, JSON-LD, and versioned release snapshots are not published yet

## Validation

- ontology Turtle parse check passed for all files under `ontology/`
- live W3ID redirect verification recorded in `docs/publishing/evidence/2026-03-13-w3id-live-redirect-check.md`

## Follow-up

- publish richer HTML/RDF/XML/JSON-LD targets
- add versioned release snapshot redirects
- record the DFO provider-verification note (no separate DFO consumer runtime for this phase) and the final go/no-go logging for issue #3
```
