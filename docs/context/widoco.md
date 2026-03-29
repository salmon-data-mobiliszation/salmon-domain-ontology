# WIDOCO in this repo

This file is the repo-specific guide for generating the Salmon Domain Ontology publication surface.

## Purpose

WIDOCO generates the HTML documentation site for the shared ontology.

This repo uses WIDOCO as part of a broader publication contract that also includes downloadable serializations and immutable release snapshots.

## Canonical source

- Main ontology input for WIDOCO: `salmon-domain-ontology.ttl` (generated flattened master from `ontology/salmon-domain-ontology.ttl`)

## Canonical outputs

Latest publication surface under `docs/`:
- `docs/index.html` — latest HTML documentation
- `docs/smn.ttl` — latest Turtle serialization
- `docs/smn.owl` — latest RDF/XML serialization
- `docs/smn.jsonld` — latest JSON-LD serialization

Immutable version snapshots:
- `docs/releases/<version>/index.html`
- `docs/releases/<version>/smn.ttl`
- `docs/releases/<version>/smn.owl`
- `docs/releases/<version>/smn.jsonld`

## Commands

- Download WIDOCO: `make install-widoco`
- Download ROBOT: `make install-robot`
- Generate HTML only: `make docs-widoco`
- Generate serializations only: `make docs-serializations`
- Run full publication refresh: `make docs-refresh`
- Verify stable WIDOCO `#/Term` anchors: `make verify-doc-term-anchors`
- Write immutable snapshot: `make release-snapshot VERSION=X.Y.Z`

## Current limitations

- Java is required for both WIDOCO and ROBOT.
- W3ID now points the shared ontology root and SemVer release paths at the generated GitHub Pages publication surface using content negotiation.
- The WIDOCO HTML already exposes stable term anchors such as `#/Escapement`; that makes human-friendly canonical-term dereferencing possible once the pending resolver update in `docs/publishing/w3id-term-dereference-draft/` is deployed.
- Module / research / case-study / profile secondary surfaces remain Turtle-first.
- Ontology header metadata is still thin, so WIDOCO output quality will improve once version / attribution / namespace metadata are expanded.

## Guardrails

- Treat `docs/index.html` as generated output after WIDOCO is adopted.
- Keep project-specific HTML tweaks in `scripts/postprocess_widoco_html.py` rather than hand-editing generated HTML.
- Keep the `#/Term` fragment contract stable; run `make verify-doc-term-anchors` after WIDOCO refreshes or ontology doc-structure changes.
- Prefer updating ontology metadata in `ontology/salmon-domain-ontology.ttl` rather than patching generated docs by hand.
