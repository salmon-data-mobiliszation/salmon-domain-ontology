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

## Domain knowledge goes to the commons

`knowledge/` here records facts about **this repo** — the import graph, where
practice diverges from `CONVENTIONS.md`, the alignment state. Facts about
**salmon** go to
[`salmon-knowledge-commons`](https://github.com/salmon-data-mobilization/salmon-knowledge-commons):
biology, ecology, management, what a term actually means, why a modelling
choice went the way it did.

Write them there rather than into a PR description, a commit message or a chat
transcript. Those evaporate, and the next agent re-derives the finding — which
in an ontology means minting a second term for a distinction someone already
worked out and did not write down. The reasoning behind a class is usually
worth more than the class, and `rdfs:comment` is too small to hold it.

If you can push there, open a PR. If you cannot, put the finding **in your
report with its sources** so a maintainer can. Source-backed claims only — the
commons rejects a claim with no citation — and **never assert your own
verification**: `generated` says who wrote a card, `verified` says who
independently checked it.

**This repo is the far end of the commons' gap register.** A commons card that
finds no term for a concept records a gap with a `mint_target`, and for shared
all-agency biology that target is `smn` — here. Those gaps are drafted term
requests, and they arrive with the sources already attached. Reading them is a
reasonable way to decide what to mint next; **no agent mints from them
unilaterally**, and the commons says so on its own side too.

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
