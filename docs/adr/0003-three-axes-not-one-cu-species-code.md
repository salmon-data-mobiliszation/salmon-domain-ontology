# ADR-0003: Three orthogonal shared schemes, not one Conservation Unit species code

## Status

Proposed

Date: 2026-08-17. This ADR and the terms it describes are a **proposal for
review**, not an accepted decision. The terms are written into module 07 so
the proposal is concrete and reviewable rather than prose about terms that do
not exist.

## Context

A review of the Salmon Population Summary Repository (SPSR) extract raised
three held ontology-term requests, tracked as `dfo-salmon-ontology` issues
[#68](https://github.com/dfo-pacific-science/dfo-salmon-ontology/issues/68),
[#74](https://github.com/dfo-pacific-science/dfo-salmon-ontology/issues/74),
and [#70](https://github.com/dfo-pacific-science/dfo-salmon-ontology/issues/70).
The evidence pass recorded on those issues established four facts.

1. SPSR's `LIFE_HISTORY_TYPE` column mixes **two conceptual axes**: Sockeye
   juvenile rearing type (`Lake Type`, 1367 rows; `River Type`, 108) and Pink
   brood cycle (`Odd Year`, 33).
2. The column is **perfectly redundant** with the `CU_ID` prefix. The
   crosstab of prefix against value is diagonal: `SEL` → Lake Type, `SER` →
   River Type, `PKO` → Odd Year, and `CK`/`CM`/`CO` → null.
3. The DFO Conservation Unit species-code list is `SEL` = Sockeye (Lake
   Type), `SER` = Sockeye (River Type), `PKE` = Pink-Even, `PKO` = Pink-Odd,
   `CK` = Chinook, `CM` = Chum, `CO` = Coho. **`PKE` exists in that list**
   even though the SPSR extract contains no even-year rows — its 33 odd-year
   rows are a single Fraser Pink CU.
4. Neither `smn:` nor `gcdfo:` contains a lake-type, river-type, cycle-line,
   or species concept today. `smn:Life-HistoryCharacteristic` is an
   `owl:Class` whose only subclass is `smn:Run`, and `gcdfo:Species` is a
   bare field handle whose scope note says its values are common-name
   strings.

A fifth fact was established on the consumer side. The PSC controlled
vocabulary (`psc-salmon-vocabularies`, `v0.1.0-alpha.3`: 4 schemes, 38
concepts) has **zero** concepts covering species, life-history type, run
timing, cycle line, or juvenile rearing. There is nothing to reconcile and no
supersession problem. Its only live `smn:` anchor is nine `skos:broadMatch`
rows onto `smn:EnumerationMethod`. Its governance file states that PSC "may
publish a one-way PSC assertion to an immutable `smn:` target, but it cannot
mint or approve `smn:` terms," and its candidate review files instruct that
gaps stay blank because "a broad or wrong-kind term is not a substitute."

The obvious economical option was a **single CU species-code vocabulary**
covering `CK`/`CM`/`CO`/`SEL`/`SER`/`PKE`/`PKO`, which would close all three
issues with one scheme. That option is rejected here.

## Decision

### 1. Three schemes, in `smn:`, along the three axes the DFO code composes

The DFO code list is a **composite** identifier. `SEL` is Sockeye × lake-type.
`SER` is Sockeye × river-type. `PKE` is Pink × even-year line. `PKO` is Pink ×
odd-year line. `CK`, `CM`, and `CO` name a species alone. Minting the code
list as one shared vocabulary would publish that conflation into the shared
layer and make every consumer inherit it — which is the same defect that put
`Odd Year` into a life-history column in the first place. Splitting the code
into the three axes it composes gives three vocabularies each usable on its
own.

This is the move [ADR-0002](0002-year-age-basis-dimensions-and-abundance.md)
already made for year and age: four orthogonal schemes (notation, basis,
dimension, value) rather than one compound age vocabulary.

| Scheme | Top concept | Narrower concepts |
|---|---|---|
| `smn:LifeHistoryTypeScheme` | `smn:LifeHistoryType` | `smn:LakeTypeLifeHistory`, `smn:RiverTypeLifeHistory` |
| `smn:CycleLineScheme` | `smn:CycleLine` | `smn:OddYearCycleLine`, `smn:EvenYearCycleLine` |
| `smn:SalmonSpeciesScheme` | `smn:SalmonSpecies` | `smn:ChinookSalmon`, `smn:ChumSalmon`, `smn:CohoSalmon`, `smn:PinkSalmon`, `smn:SockeyeSalmon` |

Three schemes, 3 top concepts and 9 narrower concepts, 12 concepts total.

### 2. Each scheme is named and defined for its axis, not for a species

`smn:LifeHistoryTypeScheme` is a life-history-type vocabulary that *contains*
lake-type and river-type; it is not a Sockeye vocabulary. `smn:CycleLineScheme`
is a cycle-line vocabulary that *contains* odd-year and even-year; it is not a
Pink vocabulary. The species is stated separately, by a concept from the third
scheme. A dataset row that today carries `SEL` states three things with three
concepts instead of one code.

Each scheme carries a `skos:scopeNote` naming the axis it is **not**, so the
next contributor with a value in hand has a written reason not to repeat the
mixing:

- `LifeHistoryTypeScheme` states that cycle line has its own vocabulary and
  cycle-line values must not be added there.
- `CycleLine` states that cyclic **dominance** — dominant, subdominant,
  off-cycle — is a status a line holds in a system and period, not the
  identity of the line, and is a separate axis not modelled here.
- `SalmonSpecies` states why no concept carries a `skos:notation`.

### 3. Cycle line, not "dominant cycle"

Issue #70 asked for a *dominant cycle* scheme. The value in the data,
`Odd Year` from `PKO`, names a **line**, not a dominance status. Two
populations can both have an odd-year line while only one of them has an
odd-year *dominant* line, and dominance can shift between periods while the
line does not. Naming the scheme for the line keeps a stable identity in the
vocabulary and leaves dominance to be modelled later as what it is: a
time-scoped assessment about a line.

The scheme is broad by construction. A cycle line is defined as the years
congruent to one another modulo the population's cycle period, relative to a
declared year basis from `smn:YearBasisScheme`. Pink's fixed two-year cycle
makes brood-year and return-year parity identical, so the two minted concepts
are unambiguous; a four-year Fraser Sockeye cycle is the same construct at a
different period and extends the same scheme without redefinition.

### 4. Mint from the source code list, not from observed values

`smn:EvenYearCycleLine` is minted even though the extract that motivated this
work contains no even-year rows, and the species scheme covers all five
species in the code list rather than the three whose prefixes appear.

**This is a policy choice and future contributors should not silently reverse
it.** The code list, not a snapshot of it, is the vocabulary. A vocabulary
minted from observed values matches one extract and must be extended the first
time an unremarkable, already-documented case appears — and each such
extension is a version bump, a re-pin, and a mapping review for every
downstream consumer. DFO maintains even-year Pink Conservation Units;
`PKE`'s absence from the extract is a property of the snapshot, not of the
code system.

This narrows ADR-0002's neutral consequence, which minted age-class values 1
through 7 "because those are evidenced by the motivating use case and DFO
source". The two are compatible: an **open, unbounded** value space (integer
ages) is minted as evidenced, while a **closed, enumerated** code list is
minted whole. Where the source enumerates its own values, take the
enumeration.

### 5. The class/concept boundary is explicit, and no `skos:*Match` crosses it

All twelve terms are `skos:Concept`, in `skos:ConceptScheme`s, in module 07.
None is an `owl:Class`, and none reuses the IRI of one.

`smn:Life-HistoryCharacteristic` stays an `owl:Class` — it is a characteristic
that can be observed, the parent of `smn:Run`, and a legitimate
`sosa:observedProperty` filler. It is **not** a vocabulary identifier for a
coded column, and this ADR adds an `rdfs:comment` saying so on the term
itself, because the SPSR inventory script currently uses it as one.

The species concepts are **code-list handles, not taxa**. The taxon is already
an OWL class in the NCBI Taxonomy, and module 02 already mirrors part of that
hierarchy (`obo:NCBITaxon_8018`) and ranges `smn:observedTaxonSpecies` on it.
Each species concept therefore points at its taxon with `rdfs:seeAlso` and
asserts **no** `skos:exactMatch`, `closeMatch`, or `broadMatch` onto it. A
SKOS mapping predicate between a `skos:Concept` and an `owl:Class` is the
type confusion `dfo-salmon-ontology`'s
`scripts/sparql/skos-match-on-owl-classes.rq` lints for, and the shared layer
should not add rows to that report while asking another repository to reduce
its own.

Verified NCBI Taxonomy identifiers (checked against the NCBI Taxonomy API on
2026-08-17): Chinook 74940, Chum 8018, Coho 8019, Pink 8017, Sockeye 8023.

### 6. The composite DFO code list stays out of the shared layer

`SEL`/`SER`/`PKE`/`PKO`/`CK`/`CM`/`CO` is a DFO Conservation Unit indexing
convention. Under CONVENTIONS section 2 it is Layer C — an agency code list —
and under section 8 it fails the "non-reliance on agency-specific policy
interpretation" criterion. It belongs in `gcdfo:`, where each code carries its
`skos:notation` and decomposes onto the three shared schemes.

No concept in `smn:SalmonSpeciesScheme` carries a `skos:notation`, and the
reason is recorded on `smn:SalmonSpecies`: **the DFO list has no code for a
species alone.** There is no plain Sockeye code and no plain Pink code. Giving
`smn:SockeyeSalmon` the notation `SEL` would be wrong, and that it is tempting
is the clearest single symptom of the conflation.

## Consequences

### Positive

- The three axes become independently statable, queryable, and mappable. A
  consumer that only needs species is not forced to adopt a life-history
  claim.
- The redundancy finding is resolvable at the source: once `CU_ID` decomposes
  onto three schemes, `LIFE_HISTORY_TYPE` carries no information the CU
  identifier does not already carry, and SPSR can drop it rather than mint a
  term for it.
- PSC can map to these without restructuring. Its pipeline requires SKOS
  targets — it recorded a rejection of `smn:ObservedRateOrAbundance` as
  `rejected_wrong_kind_and_too_broad` with `native_type: owl:Class` — and
  composes `skos:broadMatch` through documented `skos:broader*` chains, which
  every concept here has.
- Every concept has exactly one `skos:prefLabel`, one `skos:definition`, one
  `skos:inScheme`, and at most one `skos:broader`, which is what PSC's own
  SHACL contract requires of a concept it will hold a mapping against.
- Minting `PKE` now avoids a predictable future version bump and re-pin cycle
  across three repositories.

### Negative

- Twelve new shared terms is the largest single admission to the shared layer
  since the age and year schemes, and CONVENTIONS section 1 sets a
  conservative default of keeping terms in a profile first.
- Three schemes is more work for a consumer than one code list: a row that
  was one string becomes three IRIs plus a decomposition rule.
- `smn:LifeHistoryTypeScheme` currently holds only the juvenile-rearing axis,
  so it is broad in definition before it is broad in content.

### Neutral

- `smn:Life-HistoryCharacteristic` and `smn:Run` are unchanged apart from an
  editorial comment. No IRI is renamed, retired, or re-typed.
- Module 07 goes from 10 schemes / 49 concepts to 13 schemes / 61 concepts.
  `knowledge/data/owl-skos-conventions-state.md` records the pre-merge figure
  and is updated when and if this merges, not before.
- Sea-type Sockeye, stream-type and ocean-type Chinook, and multi-year cycle
  lines are named in scope notes as the extension path but are not minted:
  no source in scope names them.

## What would have to change downstream

**`gcdfo`** — mint the composite CU species-code vocabulary as a `gcdfo:`
scheme, each code carrying its `skos:notation` and a decomposition onto the
shared schemes. `gcdfo:Species` keeps its role as a WSP output *field* handle;
its scope note asking for taxonomic IRIs is satisfied by pointing at
`smn:SalmonSpeciesScheme`. Issues #68, #74, and #70 close by reference to this
ADR.

**SPSR** — stop using `smn:Life-HistoryCharacteristic` as a `vocabulary_iri`
for SKOS codes (`spsr-inventory.r:842`); it is an `owl:Class`. Point
life-history codes at `smn:LifeHistoryTypeScheme` and cycle codes at
`smn:CycleLineScheme`. Given the redundancy finding, the better change is to
derive both from `CU_ID` and retire `LIFE_HISTORY_TYPE`.

**PSC** — no change required, and nothing to retract. If PSC wants to map into
these schemes it appends the IRIs to `allowed_object_ids` in
`data/external-sources.json`, adds reviewed rows to
`data/external-mapping-review.csv`, and cuts a release.

## Open questions for review

1. **Five species concepts or seven?** "Cover the full `CK`/`CM`/`CO`/`SEL`/
   `SER`/`PKE`/`PKO` set" is read here as *the species axis of that set*,
   which is five species. Reading it as seven concepts would put the
   composite codes back into the species scheme and undo decision 1.
2. **"Cycle line" instead of "dominant cycle"** (decision 3) renames away from
   the wording in issue #70.
3. **Does `smn:LifeHistoryTypeScheme` need an intermediate concept** for the
   juvenile-rearing axis, so that a future run-timing or age-at-maturity axis
   sits beside it rather than flat under `smn:LifeHistoryType`? Kept flat here
   to match the house style of every other module-07 scheme.
4. **Layer.** These are proposed straight into shared `smn:`, not into a
   `smn/profile/<program>/` bridge. The justification is that two
   independently governed organizations (DFO and PSC) can use them, which is
   PSC's own promotion bar — but PSC has not asked for them, so the
   multi-agency reuse in CONVENTIONS section 8 criterion 1 is expected rather
   than demonstrated.

## More Information

- Evidence: `dfo-salmon-ontology` issues #68, #74, #70 (evidence pass
  2026-08-16).
- Source code list: SPSR data dictionary crosswalk, `demo_cu`/`CU_ID` notes
  column.
- Life-history and cycle-line typology: Holtby, L.B. and Ciruna, K.A. 2007.
  *Conservation Units for Pacific Salmon under the Wild Salmon Policy.* DFO
  Can. Sci. Advis. Sec. Res. Doc. 2007/070, which characterizes Pacific salmon
  diversity along ecology, life-history, and molecular-genetic axes and
  compartmentalizes it into Conservation Units.
- Even-year Pink Conservation Units exist as a published DFO CU category
  independent of the SPSR extract; the CU boundary datasets are catalogued
  separately for odd-year and even-year Pink.
- Species names and scientific names: Fisheries and Oceans Canada,
  *Information about Pacific salmon*,
  <https://www.pac.dfo-mpo.gc.ca/fm-gp/salmon-saumon/facts-infos-eng.html>.
- Taxon identifiers verified against the NCBI Taxonomy API, 2026-08-17.

## Related

- [ADR-0002](0002-year-age-basis-dimensions-and-abundance.md) — the
  orthogonal-schemes precedent, and the mint-from-evidence consequence that
  decision 4 narrows.
- `CONVENTIONS.md` sections 2, 3, 4, 8, 10, and 11.
