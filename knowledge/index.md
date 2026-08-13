---
okf_version: "0.2"
---

# Salmon Domain Ontology — knowledge bundle

Durable, source-backed knowledge about this repository for future agents and
maintainers, in Open Knowledge Format (OKF) using the canonical PSC profile
(v0.4) and its `psc-okf` validator from the canonical `psc-data-systems`
repository (assumed checked out as a sibling of this repo).

Seeded 2026-08-12 from the step-0 recon of the ontology conventions and
alignment pass (execplan:
`metasalmon/knowledge/plans/2026-08-12-ontology-alignment-pass.md`).

## Cards

- [Salmon semantics domain](domains/salmon-semantics.md)
- [Ontology alignment pass 2026 (context)](contexts/ontology-alignment-pass-2026.md)
- [Builds and import graph](data/builds-and-import-graph.md)
- [OWL/SKOS conventions — stated vs practiced](data/owl-skos-conventions-state.md)
- [Cross-vocabulary alignment state](data/cross-vocabulary-alignment-state.md)

## Validation

From this repo's root, with a sibling `psc-data-systems` checkout:

```sh
uv run --project ../psc-data-systems psc-okf check knowledge --tier capture
```
