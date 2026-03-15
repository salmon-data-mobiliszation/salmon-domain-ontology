# Salmon data metamodel views

This folder holds **non-normative view files** for the shared salmon ontology.

These views are intentionally **outside** the shared-core `01`–`07` import spine. They are meant to help maintainers, mappers, and salmon biologists answer a practical question:

> *How do the "thing we care about", the property, the variable, the constraint/context, the method, the observation event, the result, and the provenance fit together?*

## What these files are for

Use these files when you want:

- a salmon-biologist-friendly mental model of the ontology,
- a lightweight review surface for upper-level alignment work,
- a place to discuss SOSA / I-ADOPT / PROV / Darwin Core / BFO-IAO framing **without** turning that framing into default shared-core imports.

Use the shared core (`ontology/modules/01-07...`) when you want the canonical reusable terms.

## What these files are **not**

- They are **not** imported by `ontology/salmon-domain-ontology.ttl`.
- They are **not** the normative source of shared term definitions.
- They are **not** the place to add partner-specific profile mappings.

## Files

- `salmon-data-metamodel.ttl` — composition root for the optional view set
- `salmon-data-metamodel-entity.ttl` — what the data is about
- `salmon-data-metamodel-property.ttl` — what aspect/characteristic is being described
- `salmon-data-metamodel-variable.ttl` — the decomposed variable pattern (entity + property + constraints/modifiers)
- `salmon-data-metamodel-method-protocol.ttl` — how the observation/sampling was carried out or documented
- `salmon-data-metamodel-event-observation.ttl` — survey/observation context (when/where/by whom)
- `salmon-data-metamodel-result-datum.ttl` — the result/sample/value carrier side
- `salmon-data-metamodel-provenance.ttl` — lineage and provenance links

## Plain-language reading guide

A practical salmon-data variable usually reads like this:

1. **Entity** — what the data is about
   - fish, population, stock, river, habitat unit, reporting stratum
2. **Property** — what aspect you care about
   - length, weight, escapement, abundance, life stage
3. **Variable** — the data question you actually publish
   - often entity + property + qualifiers together
4. **Constraint / context / modifier** — what narrows or shapes the variable
   - brood year, location, method context, average vs count, confidence band
5. **Method / protocol** — how it was measured, estimated, or documented
6. **Observation / event** — when and where the work happened
7. **Result / datum** — the sample or value that came out
8. **Provenance** — who produced it, from what inputs, using which workflow

## Architectural note

These views were moved here from the DFO repo so that the shared salmon mental model lives with the shared ontology, while DFO keeps a cleaner posture of **core ontology + optional overlays** rather than owning the broader upper-level/metamodel story.
