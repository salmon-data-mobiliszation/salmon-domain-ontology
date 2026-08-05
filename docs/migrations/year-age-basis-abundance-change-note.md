# 0.0.2 change note: year basis, salmon age, and abundance

This change resolves the shared-model gap tracked in [issue #18](https://github.com/salmon-data-mobilization/salmon-domain-ontology/issues/18) and is prepared for the repository's `0.0.2` release snapshot. Publication and tagging remain maintainer actions.

## Added

- `smn:Abundance`, a reusable OWL characteristic for organism quantity
- `smn:YearBasisScheme` with brood-year, return-year, and catch-year basis concepts
- `smn:broodYear`, `smn:returnYear`, and `smn:catchYear` datatype/Data Cube dimension properties with `xsd:gYear` coordinates
- shared SKOS schemes for salmon age notation, age basis, age dimension, and age-class values 1–7
- a non-normative Fraser stock-recruit Data Cube/SOSA example
- a focused semantic-contract validation target

## Changed

- `smn:RecruitAbundance` now points to the explicit abundance characteristic and year model instead of an unresolved “defined year basis.”
- Numeric age-value labels no longer use “year class,” avoiding confusion with a brood cohort.
- Current DFO year-basis SKOS concepts receive conservative Tier-3 mappings to distinct shared basis concepts; the DFO `0.0.2` OWL-class representation is historical.
- Darwin Core `individualCount` is retained as an `rdfs:seeAlso` cross-reference rather than a SKOS concept mapping.
- The Fraser example separates recruit-abundance estimation from scale-based age determination using distinct SOSA observations, results, and procedures.

## Migration guidance

Use `docs/migrations/gcdfo-to-salmon-year-age.csv` for old-to-new IRIs. Important role changes are:

| Previous DFO role | Shared SDO target | Coordinate property |
| --- | --- | --- |
| `gcdfo:BroodYear` SKOS concept | `smn:BroodYearBasis` SKOS concept | `smn:broodYear` with `xsd:gYear` |
| `gcdfo:ReturnYear` SKOS concept | `smn:ReturnYearBasis` SKOS concept | `smn:returnYear` with `xsd:gYear` |
| `gcdfo:CatchYear` SKOS concept | `smn:CatchYearBasis` SKOS concept | `smn:catchYear` with `xsd:gYear` |
| `gcdfo:AgeNYearClass` | `smn:AgeClassValueN` | use with a separately declared age dimension, basis, and notation |

The DFO type statements above reflect [`c7a54251`](https://github.com/dfo-pacific-science/dfo-salmon-ontology/blob/c7a54251eb8f673052fed61f9ca2624e557249c7/ontology/dfo-salmon.ttl) and release `0.0.8`. The `skos:closeMatch` links are advisory and must not drive automatic canonicalization without review. NCEAS/DataONE `SALMON_00000520` is also a conservative close match to `smn:BroodYearBasis`; it remains an OWL class in its source ontology.

## Modeling boundaries

- A year basis says what a year means; a dimension property carries the year; an `xsd:gYear` literal is the coordinate.
- Age notation, reference basis, represented component, and numeric value are independent.
- A row-varying coordinate belongs in a data dimension. A fixed basis may additionally qualify a standalone I-ADOPT variable.
- Age determination and abundance estimation are SOSA procedures. They are not basis or notation concepts.
- Dataset-specific compound variables remain profile/project SKOS concepts; this change does not mint PSC compounds as OWL classes.

The complete rationale is recorded in `docs/adr/0002-year-age-basis-dimensions-and-abundance.md`.
