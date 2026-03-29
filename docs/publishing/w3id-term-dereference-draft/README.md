# /smn/ term-dereference follow-up draft

This folder captures the **next proposed W3ID update** for `https://w3id.org/smn/`.
It is **not live yet**.

## Why this draft exists

Today, canonical shared-term IRIs such as `https://w3id.org/smn/Escapement` still resolve to the raw Turtle artifact.
That is acceptable for machines, but annoying for humans who click a term IRI and expect to land on the term documentation.

The WIDOCO publication surface already exposes stable term anchors such as:

- `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Stock`

This draft upgrades only the **term-path dereferencing contract**:

- **default / browser request** for `/Term` → HTML docs at `/#/Term`
- `Accept: text/turtle` for `/Term` → latest Turtle serialization
- `Accept: application/rdf+xml` for `/Term` → latest RDF/XML serialization
- `Accept: application/ld+json` for `/Term` → latest JSON-LD serialization

Root `/`, SemVer release paths `/X.Y.Z`, and current Turtle-first module / profile / research / case-study surfaces keep their existing behavior.

## Local verification before resolver rollout

- Anchor-presence check: `make verify-doc-term-anchors`
- Browser check: open `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- Resolver contract reference: `.htaccess` in this folder

## Expected post-rollout behavior

```bash
curl -I https://w3id.org/smn/Escapement
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/Escapement
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn/Escapement
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn/Escapement
```

Expected:

- default → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- Turtle → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.ttl`
- RDF/XML → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.owl`
- JSON-LD → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.jsonld`

## External action required

Apply this `.htaccess` update to `perma-id/w3id.org/smn/.htaccess` and merge the corresponding W3ID PR.
