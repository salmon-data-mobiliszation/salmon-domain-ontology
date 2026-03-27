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

This folder records the **merged routing update** for `smn`, not just the original conservative registration.

Current publication posture:

1. GitHub Pages targets are live at `https://salmon-data-mobilization.github.io/salmon-domain-ontology/`.
2. Latest HTML / Turtle / RDF/XML / JSON-LD assets are published there.
3. An immutable `releases/0.0.0/` snapshot is published there.
4. The live W3ID rules now serve DFO-style root + SemVer content negotiation for `https://w3id.org/smn` and `https://w3id.org/smn/X.Y.Z`.

The `.htaccess` in this folder mirrors the live DFO Salmon Ontology routing pattern for root + SemVer IRIs:

- HTML by default
- Turtle / RDF/XML / JSON-LD via `Accept`
- versioned release redirects for `/X.Y.Z`
- no `/latest` alias in the updated contract

Secondary surfaces (`/research`, `/rda-case-study`, `/modules/*`, `/profile/*`, and term paths) remain Turtle-first for now.

## Verification commands

### Current live behavior

```bash
curl -I https://w3id.org/smn
curl -I -H 'Accept: text/turtle' https://w3id.org/smn
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn
curl -I https://w3id.org/smn/0.0.0
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/0.0.0
curl -I https://w3id.org/smn/Stock
curl -I https://w3id.org/smn/modules/01-entity-systematics
curl -I https://w3id.org/smn/research
curl -I https://w3id.org/smn/rda-case-study
```

Expected:

- root returns `301` to the trailing-slash form, then `303` redirects to latest HTML / Turtle / RDFXML / JSON-LD targets depending on `Accept`
- SemVer version paths return `303` redirects to immutable `releases/X.Y.Z/` HTML or versioned serializations depending on `Accept`
- secondary surfaces still resolve to Turtle artifacts
