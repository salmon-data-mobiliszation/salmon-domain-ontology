# Salmon data metamodel views

This folder holds an **optional, non-normative mental model** for the shared salmon ontology.

It is meant to answer one simple question:

> *When salmon people talk about the thing, the property, the variable, the method, the observation, and the result — how do those pieces fit together?*

## Use this view when you want

- a simple orientation layer for biologists and data stewards,
- a lightweight architecture review surface,
- a plain-language bridge into the shared ontology.

Use the shared core (`ontology/modules/01-07...`) when you want the canonical reusable terms.

## What this view is not

- It is **not** imported by `ontology/salmon-domain-ontology.ttl`.
- It is **not** the normative source of term definitions.
- It is **not** the place for partner-specific profile mappings or publication wiring details.

## Read it in this order

1. **Entity** — what the data is about
2. **Property** — what aspect you care about
3. **Variable** — the data question you are really publishing
4. **Context / constraint** — what narrows the variable
5. **Method** — how it was measured or estimated
6. **Observation / event** — when and where the work happened
7. **Result** — the value or sample that came out
8. **Provenance** — who made it and from what inputs

## Files

- `salmon-data-metamodel.ttl` — composition root for the optional view set
- `salmon-data-metamodel-entity.ttl` — what the data is about
- `salmon-data-metamodel-property.ttl` — what aspect is being described
- `salmon-data-metamodel-variable.ttl` — variable + context/constraint framing
- `salmon-data-metamodel-method-protocol.ttl` — how the work was done
- `salmon-data-metamodel-event-observation.ttl` — observation/sampling context
- `salmon-data-metamodel-result-datum.ttl` — the result or sample
- `salmon-data-metamodel-provenance.ttl` — lineage and provenance links

## Architectural note

These views were moved here from the DFO repo so the shared salmon mental model lives with the shared ontology, while DFO keeps a cleaner **core ontology + optional overlays** posture.

Detailed publication mappings stay in the shared interoperability module and profile/case-study layers, not in this simple view.
