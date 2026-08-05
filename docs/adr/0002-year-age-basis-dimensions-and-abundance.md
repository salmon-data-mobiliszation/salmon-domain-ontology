# ADR-0002: Separate year and age bases, dimensions, values, and procedures

## Status

Accepted

## Context

Stock-recruit datasets use year and age fields in several distinct semantic roles. In the Fraser Sockeye detailed product, spawner and juvenile estimates vary at stock × brood year, while recruit estimates additionally vary by return year and age. The previous shared ontology referred to a “defined year basis” without defining a basis vocabulary. The historical [DFO `0.0.2` snapshot](https://github.com/dfo-pacific-science/dfo-salmon-ontology/blob/c7a54251eb8f673052fed61f9ca2624e557249c7/docs/releases/0.0.2/gcdfo.ttl) represented `YearBasis`, `BroodYear`, and `CatchYear` as OWL classes. In [DFO commit `c7a54251`](https://github.com/dfo-pacific-science/dfo-salmon-ontology/blob/c7a54251eb8f673052fed61f9ca2624e557249c7/ontology/dfo-salmon.ttl), also published as release `0.0.8`, `YearBasis`, `BroodYear`, `ReturnYear`, and `CatchYear` are SKOS concepts. The shared model still needs distinct basis-concept and coordinate-property IRIs even though the current source type is already SKOS.

Treating a basis, a table dimension, and a coordinate value as the same thing prevents reliable mixed-grain bindings. It also risks conflating age notation with age basis, age component, age value, or the procedure used to determine age.

## Decision

1. Represent reusable year-reference roles in `smn:YearBasisScheme` as SKOS concepts: `BroodYearBasis`, `ReturnYearBasis`, and `CatchYearBasis`. Calendar representation is not a biological basis, so no `CalendarYearBasis` is created.
2. Represent row-varying year coordinates with separate OWL datatype properties: `smn:broodYear`, `smn:returnYear`, and `smn:catchYear`. Their values are `xsd:gYear`. In the interoperability module, they are also `qb:DimensionProperty` resources whose `qb:concept` identifies the corresponding basis.
3. Use OWL-Time only as a conservative `rdfs:seeAlso` bridge to `time:inXSDgYear`. Consumers that require temporal entities, intervals, or reference-system reasoning may build that richer representation without forcing it on tabular exchange.
4. Promote the reusable DFO age model as four orthogonal shared SKOS schemes: notation, basis, age component/dimension, and age-class value. Rename numeric values to `AgeClassValue1` through `AgeClassValue7` and avoid “year class,” which commonly means a cohort.
5. Add `smn:Abundance` as the reusable OWL characteristic. Keep “absolute,” “relative,” “estimated,” “expanded,” and method-specific distinctions in units, statistical modifiers, contexts, and procedures unless a future cross-dataset competency question demonstrates that a narrower characteristic is necessary. QUDT `Population` is therefore a `skos:closeMatch` and QUDT `Count` a `skos:broadMatch`; neither is an equivalence. Darwin Core `individualCount` is an RDF property rather than a concept, so it is retained only as an `rdfs:seeAlso` cross-reference, not a SKOS mapping.
6. Keep compound dataset variables in profile or project SKOS, optionally typed as I-ADOPT variables. Do not mint PSC compound column variables as OWL classes in the shared ontology.
7. Model age determination, abundance estimation, imputation, and expansion as `sosa:Procedure` resources used by observations. A procedure is not an age/year basis or notation.
8. Treat canonical measure-to-dimension bindings as a data-shape concern. The non-normative Fraser example uses separate RDF Data Cube structures for its two measurement grains. A fixed basis may also qualify a standalone I-ADOPT variable description, but it does not replace a row-varying dimension binding.

## Consequences

### Positive

- Queries can distinguish parental spawning, adult return, and fishery catch without treating a basis concept as a literal year.
- Mixed-grain tables can state which dimensions apply to each measure instead of inheriting every row key indiscriminately.
- Gilbert–Rich values can be decomposed into explicit age components only when the notation is declared.
- The shared `Abundance` characteristic is reusable without adopting QUDT's `Population` label or duplicating compound OWL classes.
- Method provenance remains expressible with SOSA and can evolve independently from controlled vocabularies.

### Negative

- Downstream consumers must migrate DFO year-class IRIs and cannot use a single field interchangeably as basis, dimension property, and value.
- Data Cube consumers with mixed measurement grain need separate structures or an equally explicit measure-dimension binding model.

### Neutral

- Existing DFO ontology IRIs are not changed by this decision. The migration map and Tier-3 mappings describe the new shared targets.
- Only age-class values 1 through 7 are minted because those are evidenced by the motivating use case and DFO source. The value scheme remains open.

## More Information

- The worked example is `ontology/examples/fraser-stock-recruit-year-age.ttl`.
- The machine-readable migration record is `docs/migrations/gcdfo-to-salmon-year-age.csv`.
- `scripts/verify_year_age_semantic_contract.py` checks annotations, scheme membership, mappings, coordinate types, and the mixed-grain example.

## Related

- [Issue #18](https://github.com/salmon-data-mobilization/salmon-domain-ontology/issues/18) - motivating use case and competency questions
- [W3C RDF Data Cube Vocabulary](https://www.w3.org/TR/vocab-data-cube/)
- [I-ADOPT ontology](https://i-adopt.github.io/ontology/)
- [SOSA/SSN](https://www.w3.org/TR/vocab-ssn/)
- [OWL-Time](https://www.w3.org/TR/owl-time/)
