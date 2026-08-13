---
type: InformationObject
title: Builds and import graph
description: What each build variant buys, the exact import graph including its cycle and the views' relative imports, where generated output mixes with source, and the w3id dereference gaps.
status: draft
tags: [builds, imports, w3id, tooling]
psc:
  id: smn:data:builds-and-import-graph
  contexts: [smn:context:ontology-alignment-pass-2026]
---

Verified 2026-08-12 against the working tree at commit `3995a17` (main).

## The four build artifacts

| Artifact | Nature | Imports |
|---|---|---|
| `ontology/salmon-domain-ontology.ttl` | hand-authored MAIN composition root (21 lines) | modules 01–07 + `alignment-main`, by **absolute w3id IRIs** |
| `ontology/salmon-domain-ontology-research.ttl` | research root (9 lines) | `<https://w3id.org/smn>` + `alignment-research` |
| `ontology/salmon-domain-ontology-rda-case-study.ttl` | case-study root (10 lines) | `<https://w3id.org/smn>` + generated bridge modules 08/09 |
| `salmon-domain-ontology.ttl` (repo root) | **generated** import-stripped flattening of MAIN (`scripts/build_flat_smn_ttl.py`), drift-guarded by `make verify-flat-ttl` + CI | none |

The root flat artifact shares a basename with the modular source — only a
header comment distinguishes them, which invites wrong-file edits.

## Import-graph facts that surprise people

- **Cycle:** `<https://w3id.org/smn>` imports `alignment-main`
  (`ontology/salmon-domain-ontology.ttl:21`) and `alignment-main.ttl:14`
  imports `<https://w3id.org/smn>` back. Legal OWL, but the module cannot be
  loaded standalone without pulling the whole ontology.
- **Views are unreachable from every build**, the flat artifact, and both
  sibling repos; `views/README.md` states this is deliberate. The composite
  view `ontology/views/salmon-data-metamodel.ttl:7-14` is the **only** file
  using relative (filename) `owl:imports` — resolvable solely from a local
  checkout with siblings intact.
- ~~No catalog file exists~~ **Fixed 2026-08-13:** `ontology/catalog-v001.xml`
  and `ontology/views/catalog-v001.xml` now map every module, view, and the
  vendored W3C SOSA–PROV snapshot (`ontology/imports/sosa-prov.ttl`) to local
  files; the composite view imports by ontology IRI. The main build now also
  imports `modules/alignment-upper` (which imports the W3C alignment — the
  first remote import in the graph; offline loading resolves it via the
  catalog).

## Generated vs hand-authored mixing

- Bridge modules `08`/`09` under `ontology/modules/` are **generated**
  (concatenated from `ontology/case-studies/` fragments) beside
  hand-authored modules. ~~Drift-gate gap and verify-mutates-source~~
  **Fixed 2026-08-13 (step 1b):** `make test` runs
  `build_rda_case_study_modules.py --check` (compose in memory, diff, fail
  on drift) — verification is read-only and hand-edits to 08/09 now fail CI.
- ~~Phantom "auto-generated" markers~~ **Fixed 2026-08-13:** the markers
  (which never had a generator — authored in `2549f74`) are replaced with
  honest hand-authored markers in the fragments.
- **CI gates since step 1b:** `verify_mapping_policy.py` (CONVENTIONS §5b:
  foreign-subject statements, tier-mixing per-file and across the spine,
  dual typing), `verify_method_shapes.py` (pyshacl behavioural fixture),
  and an ELK reasoner-gate job over the catalog-resolved closure.

## w3id dereference gaps (live-checked 2026-08-12)

- No rewrite rule matches `views/...` paths or the `smnv:` fragment
  namespace — view IRIs 404 (`docs/publishing/w3id-htaccess.example:66-84`
  mirrors the live rules).
- Module IRIs dereference to **mutable** `raw.githubusercontent.com`
  main-branch files, unlike the root/SemVer paths which hit the immutable
  Pages release surface.
- Profile **term** IRIs (e.g. `.../profile/hakai/...`) asserted in modules
  08/09 have no dereference route either.
