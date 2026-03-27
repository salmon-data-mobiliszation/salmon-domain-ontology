# W3ID live redirect check — 2026-03-13

> Historical note: this records the **initial conservative registration state** after PR #5829 merged.
> It is superseded as the current live-contract check by
> `docs/publishing/evidence/2026-03-26-w3id-content-negotiation-live-check.md`.

Run timestamp (UTC): `2026-03-13T12:46:54Z`

Purpose: verify the live conservative Turtle-first `https://w3id.org/smn` surface after W3ID PR #5829 merged.

## Summary

| Surface | Request | Observed redirect behavior | Final target |
| --- | --- | --- | --- |
| Root | `https://w3id.org/smn` | `301` to trailing slash, then resolves to main Turtle artifact | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl` |
| Latest | `https://w3id.org/smn/latest` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl` |
| Representative term | `https://w3id.org/smn/Stock` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl` |
| Representative module | `https://w3id.org/smn/modules/01-entity-systematics` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/modules/01-entity-systematics.ttl` |
| Research build | `https://w3id.org/smn/research` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology-research.ttl` |
| Case-study build | `https://w3id.org/smn/rda-case-study` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology-rda-case-study.ttl` |
| Representative profile root | `https://w3id.org/smn/profile/hakai` | `303` | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/modules/08-rda-case-study-profile-bridges.ttl` |
| Root with `Accept: text/turtle` | `https://w3id.org/smn` | same root `301` to trailing slash, then resolves to main Turtle artifact | `https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl` |

## Header evidence (`curl -I` / `curl -D - -o /dev/null`)

### Root

```text
HTTP/1.1 301 Moved Permanently
Location: https://w3id.org/smn/
```

### Latest

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl
```

### Representative term (`/Stock`)

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology.ttl
```

### Representative module (`/modules/01-entity-systematics`)

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/modules/01-entity-systematics.ttl
```

### Research build

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology-research.ttl
```

### Case-study build

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/salmon-domain-ontology-rda-case-study.ttl
```

### Representative profile root (`/profile/hakai`)

```text
HTTP/1.1 303 See Other
Location: https://raw.githubusercontent.com/salmon-data-mobilization/salmon-domain-ontology/main/ontology/modules/08-rda-case-study-profile-bridges.ttl
```

## Followed redirects (`curl -L`)

All checked endpoints resolved to `HTTP 200` from `raw.githubusercontent.com` with `CONTENT_TYPE=text/plain; charset=utf-8`.

## Conclusion

The live `smn` W3ID surface is working for the conservative Turtle-first publication contract: root/latest plus representative term/module/build/profile paths all resolve to the expected current Turtle artifacts.
