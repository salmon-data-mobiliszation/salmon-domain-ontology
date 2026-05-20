# W3ID term dereference live check — 2026-05-13

Run timestamp (UTC): `2026-05-13T15:42:49Z`

Purpose: confirm that canonical shared-term IRIs now dereference to WIDOCO term anchors by default while retaining content-negotiated RDF serialization redirects.

Upstream W3ID PR:

- <https://github.com/perma-id/w3id.org/pull/5881>
- Title: `smn: dereference term IRIs to WIDOCO anchors`
- Merged: `2026-03-27T18:35:58Z`

## Checks

```bash
curl -sI https://w3id.org/smn/Escapement
curl -sI -H 'Accept: text/turtle' https://w3id.org/smn/Escapement
curl -sI -H 'Accept: application/rdf+xml' https://w3id.org/smn/Escapement
curl -sI -H 'Accept: application/ld+json' https://w3id.org/smn/Escapement
```

Observed redirects:

- default: `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- Turtle: `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.ttl`
- RDF/XML: `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.owl`
- JSON-LD: `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.jsonld`

Conclusion: the term-path resolver update is live. No WIDOCO HTML patch is required for anchor landing behavior.
