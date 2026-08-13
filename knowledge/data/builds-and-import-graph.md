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
- **No catalog file exists** (`catalog-v001.xml` or equivalent). The only
  IRI→file resolution is `discover_local_ontology_index()` inside
  `build_flat_smn_ttl.py`, keyed on *declared ontology IRIs* — so the views'
  relative imports are invisible to it.

## Generated vs hand-authored mixing

- Bridge modules `08`/`09` under `ontology/modules/` are **generated**
  (concatenated from `ontology/case-studies/` fragments) but sit beside
  hand-authored modules; CI's drift gate (`make verify-generated-artifacts`,
  Makefile:126) covers only `docs/` and the root flat TTL — a hand-edit to
  08/09 passes CI and is silently clobbered by the next `make test`.
- `make verify-flat-ttl` (and hence `make test` / `make ci`) **mutates the
  working tree** (rewrites modules 08/09) — a verify target with write
  side-effects (Makefile:102).
- Every `REQUIRED ANNOTATION BACKFILL (auto-generated; do not hand-edit)`
  block has **no generator**: `git log -S` shows they entered in authored
  commit `2549f74` and no script writes or refreshes them.

## w3id dereference gaps (live-checked 2026-08-12)

- No rewrite rule matches `views/...` paths or the `smnv:` fragment
  namespace — view IRIs 404 (`docs/publishing/w3id-htaccess.example:66-84`
  mirrors the live rules).
- Module IRIs dereference to **mutable** `raw.githubusercontent.com`
  main-branch files, unlike the root/SemVer paths which hit the immutable
  Pages release surface.
- Profile **term** IRIs (e.g. `.../profile/hakai/...`) asserted in modules
  08/09 have no dereference route either.
