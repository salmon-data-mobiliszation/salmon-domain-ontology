# Term dereference preflight — 2026-03-27

Run timestamp (UTC): `2026-03-27T18:06:33Z` live resolver check, plus local/browser verification during repo fix work

Purpose: confirm that the remaining gap is at the resolver layer, not in the generated WIDOCO site, and record the expected post-rollout contract for canonical shared-term IRIs.

## Findings

### 1) Current live resolver behavior is still Turtle-first for term paths

Observed with:

```bash
curl -I https://w3id.org/smn/Escapement
```

Observed header excerpt:

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl
```

Conclusion: the live W3ID resolver still needs one more update for human-friendly term dereferencing.

### 2) The GitHub Pages WIDOCO site already supports direct term landing

Verified in-browser against:

- `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`

Observed during browser evaluation:

- `location.hash === "#/Escapement"`
- `document.getElementById("/Escapement")` exists
- the target element was at the top of the viewport after load (`rectTop ≈ 0`)

Conclusion: no WIDOCO HTML patch is required for the anchor landing behavior.

### 3) Anchor contract is checkable in-repo

Verified with:

```bash
make verify-doc-term-anchors
```

Expected output:

```text
OK docs/index.html: 88 documented smn terms expose stable #/Term anchors
OK docs/index-en.html: 88 documented smn terms expose stable #/Term anchors
```

## Expected contract after the pending W3ID follow-up

For a representative canonical term IRI such as `https://w3id.org/smn/Escapement`:

```bash
curl -I https://w3id.org/smn/Escapement
curl -I -H 'Accept: text/turtle' https://w3id.org/smn/Escapement
curl -I -H 'Accept: application/rdf+xml' https://w3id.org/smn/Escapement
curl -I -H 'Accept: application/ld+json' https://w3id.org/smn/Escapement
```

Expected results:

- default → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/#/Escapement`
- Turtle → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.ttl`
- RDF/XML → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.owl`
- JSON-LD → `303` to `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.jsonld`
