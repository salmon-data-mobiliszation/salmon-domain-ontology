# salmon-domain-ontology — agent guidance

The shared Salmon Domain Ontology (`smn:`, `https://w3id.org/smn`). Deliverables
are Turtle artifacts plus publication and migration docs — no app code.

## Knowledge bundle (read first)

`knowledge/` is this repo's Open Knowledge Format bundle: durable,
source-backed knowledge for agents and maintainers — the verified import
graph, where modelling practice diverges from `CONVENTIONS.md`, and the
cross-vocabulary alignment state with gcdfo and the PSC CV. Start at
`knowledge/index.md` before substantial ontology or conventions work, and
**update the relevant card when work changes or invalidates a recorded
fact** — cards cite the commit they were verified against. The bundle is
git-tracked and must contain no absolute filesystem paths. Validate from the
repo root, with a sibling `psc-data-systems` checkout:

```sh
uv run --project ../psc-data-systems psc-okf check knowledge --tier capture
```

## Coordination

Sequencing for cross-vocabulary work lives in the **metasalmon hub**
(`metasalmon/knowledge/roadmap.md`, stream S9); the execplan is
`metasalmon/knowledge/plans/2026-08-12-ontology-alignment-pass.md`. Do not
maintain a competing roadmap here.

## Before changing docs / ontology / builds

- `knowledge/index.md` — verified repo knowledge (OKF bundle)
- `README.md` — repo overview and build/release commands
- `CONVENTIONS.md` — modeling and mapping-strength rules (canonical)
- `ontology/modules/README.md` — module/build wiring
- `docs/entrypoints.md` — what is actually used, and what to read before editing

## Build / test

```sh
make verify-ontology-parse   # all TTLs parse
make test                    # fast validation bundle
make ci                      # full local CI bundle
```

Caution (verified, see the builds card): `make verify-flat-ttl` — and thus
`make test`/`make ci` — currently **rewrites generated modules 08/09 in the
working tree**; run on a clean tree. The root `salmon-domain-ontology.ttl` is
generated; the hand-authored source is `ontology/salmon-domain-ontology.ttl`.
