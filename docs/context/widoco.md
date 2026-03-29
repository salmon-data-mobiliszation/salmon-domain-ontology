# WIDOCO in this repo

This file is the repo-specific guide for generating the Salmon Domain Ontology publication surface.

## Purpose

WIDOCO generates the HTML documentation site for the shared ontology.

This repo uses WIDOCO as part of a broader publication contract that also includes downloadable serializations and immutable release snapshots.

## Canonical source

- Main ontology source for release metadata and imports: `ontology/salmon-domain-ontology.ttl`
- Flattened source artifact: `salmon-domain-ontology.ttl`
- Direct WIDOCO input: `release/tmp/widoco-input.ttl` generated from the flattened artifact with only the root ontology declaration retained

## Canonical outputs

Latest publication surface under `docs/`:
- `docs/index.html` - latest HTML documentation
- `docs/index-en.html` - latest English HTML documentation
- `docs/smn.ttl` - latest Turtle serialization
- `docs/smn.owl` - latest RDF/XML serialization
- `docs/smn.jsonld` - latest JSON-LD serialization

Immutable version snapshots:
- `docs/releases/<version>/index.html`
- `docs/releases/<version>/smn.ttl`
- `docs/releases/<version>/smn.owl`
- `docs/releases/<version>/smn.jsonld`

## Commands

- Download WIDOCO: `make install-widoco`
- Download ROBOT: `make install-robot`
- Generate HTML only: `make docs-widoco`
- Build the root-ontology-only WIDOCO input: `make docs-widoco-input`
- Generate serializations only: `make docs-serializations`
- Run full publication refresh: `make docs-refresh`
- Run the fast validation bundle: `make test`
- Run the local CI bundle: `make ci`
- Verify generated artifacts are committed: `make verify-generated-artifacts`
- Verify stable WIDOCO `#/Term` anchors: `make verify-doc-term-anchors`
- Verify WIDOCO version metadata rendering: `make verify-doc-version-metadata`
- Write immutable snapshot from current docs: `make snapshot-release VERSION=X.Y.Z`
- Refresh docs and then write immutable snapshot: `make release-snapshot VERSION=X.Y.Z`
- Full release path: `make release VERSION=X.Y.Z`

## Current behavior

- Java 17+ is required for both WIDOCO and ROBOT.
- W3ID now points the shared ontology root and SemVer release paths at the generated GitHub Pages publication surface using content negotiation.
- The WIDOCO HTML already exposes stable term anchors such as `#/Escapement`; that makes human-friendly canonical-term dereferencing possible once the pending resolver update in `docs/publishing/w3id-term-dereference-draft/` is deployed.
- Module / research / case-study / profile secondary surfaces remain Turtle-first.
- Ontology header metadata now carries `owl:versionInfo`, `owl:versionIRI`, `owl:priorVersion`, and `dcterms:modified` so WIDOCO can render release metadata directly from the canonical source ontology.

## Guardrails

- Treat `docs/index.html` and `docs/index-en.html` as generated output after WIDOCO is adopted.
- Keep project-specific HTML tweaks in `scripts/postprocess_widoco_html.py` rather than hand-editing generated HTML.
- Keep the `#/Term` fragment contract stable; run `make verify-doc-term-anchors` after WIDOCO refreshes or ontology doc-structure changes.
- Keep ontology release metadata in `ontology/salmon-domain-ontology.ttl`; update it through `make release VERSION=X.Y.Z` or `scripts/update_root_release_metadata.py` rather than patching generated docs by hand.
