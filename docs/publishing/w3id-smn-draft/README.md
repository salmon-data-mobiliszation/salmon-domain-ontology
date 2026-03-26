# /smn/

Salmon Domain Ontology shared namespace (`smn:`).

## Canonical IRIs

- Latest ontology IRI: `https://w3id.org/smn`
- Version IRIs: `https://w3id.org/smn/X.Y.Z`
- Term namespace: `https://w3id.org/smn/`
- Module namespace: `https://w3id.org/smn/modules/<module-name>`
- Research build: `https://w3id.org/smn/research`
- Case-study build: `https://w3id.org/smn/rda-case-study`
- Profile roots:
  - `https://w3id.org/smn/profile/hakai/`
  - `https://w3id.org/smn/profile/neville/`
  - `https://w3id.org/smn/profile/rda-case-study/`

## Maintainer repository

- <https://github.com/salmon-data-mobilization/salmon-domain-ontology>

## Maintainer contact

- Brett Johnson — GitHub: `Br-Johnson`

## Local reference status

This folder now records the **follow-up W3ID update** for `smn`, not just the original conservative registration.

Current publication posture:

1. GitHub Pages targets are live at `https://salmon-data-mobilization.github.io/salmon-domain-ontology/`.
2. Latest HTML / Turtle / RDF/XML / JSON-LD assets are published there.
3. An immutable `releases/0.0.0/` snapshot is published there.
4. The live W3ID rules have **not** been updated yet, so `https://w3id.org/smn` still serves the older Turtle-first behavior.

The draft `.htaccess` in this folder intentionally mirrors the live DFO Salmon Ontology routing pattern for root + SemVer IRIs:

- HTML by default
- Turtle / RDF/XML / JSON-LD via `Accept`
- versioned release redirects for `/X.Y.Z`
- no `/latest` alias in the updated contract

Secondary surfaces (`/research`, `/rda-case-study`, `/modules/*`, `/profile/*`, and term paths) remain Turtle-first for now.

## Verification commands

### Current live behavior

```bash
curl -I https://w3id.org/smn
curl -I https://w3id.org/smn/Stock
curl -I https://w3id.org/smn/modules/01-entity-systematics
curl -I https://w3id.org/smn/research
curl -I https://w3id.org/smn/rda-case-study
curl -I https://w3id.org/smn/profile/hakai
curl -I -H 'Accept: text/turtle' https://w3id.org/smn
```

Expected: root returns `301` to the trailing-slash form, then `303` redirects resolve to the matching raw GitHub Turtle artifact.

### Expected behavior after the follow-up W3ID PR

```bash
curl -I https://w3id.org/smn
curl -I -H 'Accept: text/turtle' https://w3id.org/smn
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn
curl -I https://w3id.org/smn/0.0.0
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/0.0.0
```

Expected: `303` redirects to the GitHub Pages HTML/Turtle/RDFXML/JSON-LD latest surface and to the corresponding `releases/X.Y.Z/` assets.
