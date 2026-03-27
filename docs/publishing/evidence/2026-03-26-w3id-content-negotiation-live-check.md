# W3ID live content-negotiation check — 2026-03-26

Run timestamp (UTC): `2026-03-27T03:43:59Z`

Purpose: verify the live `https://w3id.org/smn` surface after `perma-id/w3id.org` PR #5873 merged.

## Summary

| Surface | Request | Observed redirect behavior | Final target |
| --- | --- | --- | --- |
| Root | `https://w3id.org/smn` | `301` to trailing slash, then `303` | `https://salmon-data-mobilization.github.io/salmon-domain-ontology/` |
| Root + Turtle | `Accept: text/turtle` on `https://w3id.org/smn` | `301` to trailing slash, then `303` | `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.ttl` |
| Root + RDF/XML | `Accept: application/rdf+xml` on `https://w3id.org/smn` | `301` to trailing slash, then `303` | `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.owl` |
| Root + JSON-LD | `Accept: application/ld+json` on `https://w3id.org/smn` | `301` to trailing slash, then `303` | `https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.jsonld` |
| Version `0.0.0` | `https://w3id.org/smn/0.0.0` | `303` | `https://salmon-data-mobilization.github.io/salmon-domain-ontology/releases/0.0.0/` |
| Version `0.0.0` + Turtle | `Accept: text/turtle` on `https://w3id.org/smn/0.0.0` | `303` | `https://salmon-data-mobilization.github.io/salmon-domain-ontology/releases/0.0.0/smn.ttl` |
| Representative term | `https://w3id.org/smn/Stock` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl` |
| Representative module | `https://w3id.org/smn/modules/01-entity-systematics` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/modules/01-entity-systematics.ttl` |
| Research build | `https://w3id.org/smn/research` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology-research.ttl` |
| Case-study build | `https://w3id.org/smn/rda-case-study` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology-rda-case-study.ttl` |

## Header evidence (`curl -I` / `curl -L -I`)

### Root (default)

```text
HTTP/1.1 301 Moved Permanently
Location: https://w3id.org/smn/

HTTP/1.1 303 See Other
Location: https://salmon-data-mobilization.github.io/salmon-domain-ontology/

HTTP/2 200
```

### Root (`Accept: text/turtle`)

```text
HTTP/1.1 301 Moved Permanently
Location: https://w3id.org/smn/

HTTP/1.1 303 See Other
Location: https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.ttl

HTTP/2 200
content-type: text/turtle; charset=utf-8
```

### Root (`Accept: application/rdf+xml`)

```text
HTTP/1.1 301 Moved Permanently
Location: https://w3id.org/smn/

HTTP/1.1 303 See Other
Location: https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.owl

HTTP/2 200
content-type: application/rdf+xml
```

### Root (`Accept: application/ld+json`)

```text
HTTP/1.1 301 Moved Permanently
Location: https://w3id.org/smn/

HTTP/1.1 303 See Other
Location: https://salmon-data-mobilization.github.io/salmon-domain-ontology/smn.jsonld

HTTP/2 200
content-type: application/ld+json; charset=utf-8
```

### Version `0.0.0` (default)

```text
HTTP/1.1 303 See Other
Location: https://salmon-data-mobilization.github.io/salmon-domain-ontology/releases/0.0.0/

HTTP/2 200
content-type: text/html; charset=utf-8
```

### Version `0.0.0` (`Accept: text/turtle`)

```text
HTTP/1.1 303 See Other
Location: https://salmon-data-mobilization.github.io/salmon-domain-ontology/releases/0.0.0/smn.ttl

HTTP/2 200
content-type: text/turtle; charset=utf-8
```

### Representative module (`/modules/01-entity-systematics`)

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/modules/01-entity-systematics.ttl

HTTP/2 200
content-type: text/plain; charset=utf-8
```

### Representative term (`/Stock`)

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl

HTTP/2 200
content-type: text/plain; charset=utf-8
```

## Conclusion

The live `smn` W3ID contract now behaves as intended:

- root + SemVer paths use DFO-style content negotiation against the GitHub Pages publication surface;
- secondary surfaces remain Turtle-first;
- the initial conservative registration contract recorded on 2026-03-13 is now superseded for the shared ontology root and version paths.
