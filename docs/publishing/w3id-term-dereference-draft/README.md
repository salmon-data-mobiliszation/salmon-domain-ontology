# /smn/ term-dereference contract

This folder captures the live W3ID term-dereferencing update for `https://w3id.org/smn/`.
It was merged upstream in `perma-id/w3id.org` PR #5881 and verified live on 2026-05-13.

## Why this contract exists

Canonical shared-term IRIs such as `https://w3id.org/smn/Escapement` should land humans on the term documentation while still giving machines serialization-specific redirects through content negotiation.

The WIDOCO publication surface already exposes stable term anchors such as:

- `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Stock`

This contract covers only the **term-path dereferencing contract**:

- **default / browser request** for `/Term` → HTML docs at `/#/Term`
- `Accept: text/turtle` for `/Term` → latest Turtle serialization
- `Accept: application/rdf+xml` for `/Term` → latest RDF/XML serialization
- `Accept: application/ld+json` for `/Term` → latest JSON-LD serialization

Root `/`, SemVer release paths `/X.Y.Z`, and current Turtle-first module / profile / research / case-study surfaces keep their existing behavior.

## Local verification

- Anchor-presence check: `make verify-doc-term-anchors`
- Browser check: open `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- Resolver contract reference: `.htaccess` in this folder

## Live behavior

```bash
curl -I https://w3id.org/smn/Escapement
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/Escapement
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn/Escapement
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn/Escapement
```

Expected and observed:

- default → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- Turtle → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.ttl`
- RDF/XML → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.owl`
- JSON-LD → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.jsonld`

## Upstream status

The external W3ID update has been applied to `perma-id/w3id.org/smn/.htaccess` and merged in PR #5881.
