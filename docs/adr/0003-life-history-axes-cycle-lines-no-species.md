# ADR-0003: Life-history axes, cycle lines, and no species vocabulary

## Status

Proposed

Date: 2026-08-17. This ADR and the terms it describes are a **proposal for
review**, not an accepted decision. The terms are written into modules 01, 02,
and 07 so the proposal is concrete and reviewable rather than prose about terms
that do not exist.

This revision supersedes the first draft of this ADR, which proposed three
schemes — life-history type, cycle line, and **salmon species** — with two
life-history concepts and five species concepts. Deep research on taxonomic
authorities and on the life-history literature, plus three rulings from Brett
Johnson on 2026-08-17, changed what the proposal should be. The species scheme
is withdrawn entirely, life-history type is decomposed into axes, and the
cycle-line scheme is redefined as a year-series construct. The reasoning that
survived is kept, not rewritten.

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
issues with one scheme. That option is rejected: the code is composite, and
minting it whole would publish the conflation into the shared layer where
every consumer inherits it. That much is unchanged from the first draft, and
it is the reason this ADR exists.

What changed is what the decomposition should produce.

## Decision

### 1. No species vocabulary in this proposal (Brett Johnson, 2026-08-17)

`smn:SalmonSpeciesScheme` and its five species concepts are **withdrawn**.
Nothing replaces them in this change. A row that carries `SEL` states its
life-history type with a concept from `smn:LifeHistoryTypeScheme`; its species
is carried by whatever species mechanism the consumer already has, and this
proposal does not supply one.

The reasons, in the order that decided it:

**Steelhead is in scope** (Brett Johnson, 2026-08-17), and steelhead has **no
taxonomic identifier in ITIS, WoRMS, NCBI, GBIF, or Catalogue of Life**. It is
a vernacular for the anadromous form of *Oncorhynchus mykiss* in every one of
them, and is managed by NOAA as eleven Distinct Population Segments. A
vocabulary that must be able to carry steelhead is not a species vocabulary;
calling it one guarantees that the first term it cannot represent is one of
the ones it was built for.

**The source data holds administrative codes, not taxa.** `SEL` is sockeye
crossed with a life-history type and `PKO` is pink crossed with a cycle line.
Four of the seven CU codes correspond to no taxon at all, and neither does
steelhead or kokanee. Building a *species* vocabulary to serve a *code* list
misdescribes what the codes are, which is the same error as minting the
composite code whole, one level down.

**The authorities disagree, actively.** WoRMS, Catalogue of Life, and GBIF
have elevated Lahontan and Rio Grande cutthroat to species while ITIS and NCBI
still hold them as subspecies, and *Oncorhynchus lewisi* — the current
American Fisheries Society name for westslope cutthroat — appears in none of
the five. Minting an `smn:` species concept means picking a side in a live
nomenclatural dispute and then owning the divergence.

**The identifier the first draft pointed at is the wrong kind.** NCBI Taxonomy
declares itself non-authoritative for nomenclature, and its OBO PURL serves
`text/html` under every RDF `Accept` header — verified 2026-08-17 against
`http://purl.obolibrary.org/obo/NCBITaxon_8018` with `text/turtle`,
`application/rdf+xml`, and `application/ld+json`, each returning a 303 to an
HTML page. The five `rdfs:seeAlso` links in the first draft therefore resolved
to documentation, not data.

**Where species reference goes if it is needed later: `smn`, never `gcdfo`**
(Brett Johnson, 2026-08-17). `smn` is the shared all-agency layer, and a
species reference that lives in one agency's namespace is a species reference
every other agency has to mirror or ignore.

**The likely future shape, recorded as an expectation and not decided here:**
a DFO **code** vocabulary in `gcdfo` — the codes are DFO's, and CONVENTIONS
section 2 puts an agency code list in Layer C — whose concepts carry
`dwc:scientificName` as a literal plus a WoRMS `dwc:scientificNameID`, with
ITIS as a CC0 second reference. WoRMS because it is the marine authority with
stable LSIDs; ITIS because it is CC0 and therefore redistributable. That shape
needs no `smn:` species concept at all, which is part of why it is attractive
and part of why the tension with the previous paragraph should be resolved
explicitly by Brett before either is built. Not this PR.

The one place species survives in this change is as a **literal**:
`dwc:scientificName "Oncorhynchus nerka"` on each named life-history type,
which species-scopes the type in a machine-readable way without adopting an
identifier, an authority, or a vocabulary.

### 2. Life-history type is asserted at Conservation Unit, population, or stock level (Brett Johnson, 2026-08-17)

Not for individual fish. This collapses the level problem the first draft left
open — whether a life-history type is a property of a fish, a brood, or a
group — by ruling that the assertion is population-level, and the design
follows the ruling: `smn:hasLifeHistoryType` relates a CU, population, or
stock to a named type, and nothing in the scheme is shaped for an individual.

### 3. Life-history type is decomposed into axes; named types are species-scoped combinations

The first draft's two flat concepts, `smn:LakeTypeLifeHistory` and
`smn:RiverTypeLifeHistory`, are replaced. They were too thin in two ways that
compound.

**Sockeye's three terms encode two axes, not one.** Sea-type, lake-type, and
river-type resolve into a *duration* axis (sea-type is under a year in fresh
water; lake- and river-type are a year or more) and, only within the year-or-
more group, a *nursery habitat* axis (lake versus river). Chinook's
stream-type/ocean-type distinction is the duration axis **only**, plus an adult
behavioural syndrome that sockeye's terms do not carry. A flat list of named
types hides both facts and makes the cross-species arithmetic look easy.

**And the names are actively dangerous.** "Sea-type" is a homograph: it was
Gilbert's 1913 name for what is now called ocean-type chinook, and today it
denotes a sockeye type. Same string, two species-scoped meanings, senses
similar enough that a lexical matcher will merge them and be wrong. Sockeye
river-type is likewise **not** chinook stream-type despite near-identical
English. A flat cross-species enum of these strings produces silent errors,
which is the failure mode this decision exists to prevent.

So: two species-neutral **axis schemes** hold the primitives, and
`smn:LifeHistoryTypeScheme` holds **named types, each scoped to one species**
and each defined as a combination of axis values.

| Scheme | Top concept | Narrower concepts |
|---|---|---|
| `smn:JuvenileFreshwaterResidenceScheme` | `smn:JuvenileFreshwaterResidence` | `smn:SubyearlingFreshwaterResidence`, `smn:YearlingFreshwaterResidence` |
| `smn:JuvenileNurseryHabitatScheme` | `smn:JuvenileNurseryHabitat` | `smn:LakeNurseryHabitat`, `smn:RiverineNurseryHabitat` |
| `smn:LifeHistoryTypeScheme` | `smn:LifeHistoryType` | `smn:SockeyeLakeTypeLifeHistory`, `smn:SockeyeRiverTypeLifeHistory`, `smn:SockeyeSeaTypeLifeHistory` |
| `smn:CycleLineScheme` | `smn:CycleLine` | `smn:OddYearCycleLine`, `smn:EvenYearCycleLine` |

The decomposition is machine-readable, not prose: each named type carries
`smn:hasJuvenileFreshwaterResidence` and, where it has one,
`smn:hasJuvenileNurseryHabitat`. `smn:SockeyeSeaTypeLifeHistory` carries only
the first — a group that leaves in its first year has no freshwater nursery
worth naming — and that asymmetry is the evidence, inside the artifact, that
the axes are separable rather than one bundle.

**Chinook ocean-type and stream-type are deliberately not minted**, and the
reason is now evidential rather than procedural. Healey's own model is
two-level: a race-defining bundle plus *tactical* variation within it, with age
at maturity and precocity explicitly not race-defining. He states he cannot
classify the Sacramento winter run, which pairs stream-type adult behaviour
with ocean-type juvenile behaviour — primary evidence that the axes come
apart. And the bundle is not stable across the range: in the interior Columbia
the split is a deep genetic division (G_ST ≈ 0.15), while coastally run timing
explains about 10% of G_ST and within-basin run types differ by G_ST < 0.02
(Waples et al. 2004), with Moran et al. (2013) finding the two-race model does
not hold coast-wide. Minting `smn:ChinookOceanType` as a primitive would assert
a bundle whose extension changes with latitude. The axes let such a group be
described exactly, one axis at a time, with no named type forced on it.

**`adfluvial`/`fluvial`/`lacustrine` is not this vocabulary.** It is a
potamodromous classification (Rieman and McIntyre 1993), and it treats anadromy
as a *separate category alongside* those terms rather than as something they
qualify. Applying "adfluvial" to an anadromous sockeye population is a category
error; applying it to kokanee is defensible and would be a different scheme.
The surface similarity — lacustrine resembles lake, fluvial resembles river —
is exactly why the nursery-habitat scheme says so in a scope note.

### 4. Cycle line is a year-series construct; reproductive independence is an additional claim

The first draft was closer to right than it looked: it already scoped both
minted concepts to a "two-year-cycle population" and already excluded dominance
in a scope note. Two specific defects are corrected.

**The scheme definition said "largely independent *reproductive* lines."** That
states a fact about period-2 populations as though it were the definition of
the construct. It is not. A cycle line is the set of years congruent to one
another modulo the population's cycle period, under a declared year basis —
a partition of a year series. Whether the resulting class is also
reproductively independent is a further claim, true in some populations and
false in others, and it is now asserted where it holds rather than assumed
everywhere.

**The first draft's section 3 claimed that a four-year Fraser Sockeye cycle
"extends the same scheme without redefinition." It does not, and that claim is
withdrawn.** For pink, age at return is invariantly 2, so a year's residue
class is **closed under reproduction**: every fish spawned on the odd line
returns on the odd line, and the class is a lineage. For Fraser sockeye,
roughly 89–92% return at age 4 with real age-3 and age-5 components, so a fish
spawned on one line can return on another. The class is **not closed**, and
brood-year and return-year bases give **non-equivalent partitions of the same
fish**. Declaring a year basis does not reconcile those partitions; it selects
which assertion is being made.

DFO's own data individuates the two cases. Pink CUs are split by line —
19 `PKO` and 14 `PKE`, with `FRASER RIVER` appearing as both `PKO-01` and
`PKE-9005` — while **zero** sockeye CUs anywhere are split by cycle line. DFO
also records Fraser Pink as `Cyclic = FALSE`, which is a useful reminder that
the dominance fields cut across this scheme rather than along it.

**Two properties, because the subject and the semantics differ even though the
range is shared:**

- `smn:hasCycleLine` — subject is a CU, population, or stock; the line is
  **lineage-defining**. Valid only where age at return is invariant. This is
  also the only condition under which assigning a line to an individual **fish**
  is valid.
- `smn:stratifiedByCycleLine` — subject is a record or observation carrying a
  return year; the line is a **stratification of the year series only**, with
  no reproductive claim. This is the correct property for Fraser sockeye.

A single property with a scope note would have been acceptable and cheaper. Two
is chosen because the distinction is the whole content of the correction above,
and a scope note is the part of a term that consumers skip.

**The deferred dominance model now names its successor.** The first draft
excluded cyclic dominance without saying what would replace it, which is how a
deferral outlives its cause. The successor is DFO's three Conservation Unit
fields: `Cyclic` (a boolean of the CU), `Cyc_Dom`, and `Cyc_Dom_Year` (which
line, for that CU, in that period), with values dominant, subdominant, and
off-cycle. Modelling those three fields retires the deferral.

### 5. Mint from the source code list, not from observed values

Unchanged from the first draft. `smn:EvenYearCycleLine` is minted even though
the extract that motivated this work contains no even-year rows.

**This is a policy choice and future contributors should not silently reverse
it.** The code list, not a snapshot of it, is the vocabulary. A vocabulary
minted from observed values matches one extract and must be extended the first
time an unremarkable, already-documented case appears — and each such extension
is a version bump, a re-pin, and a mapping review for every downstream
consumer. DFO maintains even-year Pink Conservation Units; `PKE`'s absence from
the extract is a property of the snapshot, not of the code system.

This narrows ADR-0002's neutral consequence, which minted age-class values 1
through 7 "because those are evidenced by the motivating use case and DFO
source". The two are compatible: an **open, unbounded** value space (integer
ages) is minted as evidenced, while a **closed, enumerated** code list is
minted whole. Where the source enumerates its own values, take the enumeration.

`smn:SockeyeSeaTypeLifeHistory` is minted on the same logic one level up: it is
the third value of a two-value axis the other two types already use, and
leaving it out would leave the duration axis defined but only half populated —
with the most dangerous name in the vocabulary undocumented at the one place a
contributor would look for it.

### 6. The class/concept boundary is explicit, and no `skos:*Match` crosses it

All thirteen vocabulary terms are `skos:Concept`, in `skos:ConceptScheme`s, in
module 07. None is an `owl:Class`, and none reuses the IRI of one. The five new
object properties are `owl:ObjectProperty` in modules 01 and 02; none is a
concept.

`smn:Life-HistoryCharacteristic` stays an `owl:Class` — it is a characteristic
that can be observed, the parent of `smn:Run`, and a legitimate
`sosa:observedProperty` filler. It is **not** a vocabulary identifier for a
coded column, and this ADR adds an `rdfs:comment` saying so on the term itself,
because the SPSR inventory script currently uses it as one.

Withdrawing the species scheme removes the five `rdfs:seeAlso` links into NCBI
Taxonomy, and with them the question of whether a SKOS mapping predicate may
point at an `owl:Class`. None is asserted anywhere in this change, so the
smn closure adds no rows to the report `dfo-salmon-ontology`'s
`scripts/sparql/skos-match-on-owl-classes.rq` produces.

The three new properties that range on `skos:Concept` do so deliberately:
values come from a named scheme, pointed at with `rdfs:seeAlso`, in the same
way `smn:broodYear` points at `smn:BroodYearBasis`. `rdfs:domain` is omitted on
all five properties, with the omission and its retirement condition recorded in
the module comments — the legitimate subjects have no common superclass in this
build, and an OWL 2 EL-safe union domain is not expressible.

### 7. The composite DFO code list stays out of the shared layer

`SEL`/`SER`/`PKE`/`PKO`/`CK`/`CM`/`CO` is a DFO Conservation Unit indexing
convention. Under CONVENTIONS section 2 it is Layer C — an agency code list —
and under section 8 it fails the "non-reliance on agency-specific policy
interpretation" criterion. It belongs in `gcdfo:`, where each code carries its
`skos:notation` and decomposes onto the shared terms: life-history type for
`SEL`/`SER`, cycle line for `PKE`/`PKO`, and species by whatever mechanism
decision 1's future resolution settles on.

No concept minted here carries a `skos:notation`, because no code in the DFO
list denotes any of these concepts alone. `SEL` is not a code for lake-type;
it is a code for sockeye-and-lake-type. That the composite codes are tempting
to attach is the clearest single symptom of the conflation.

## Consequences

### Positive

- The axes become independently statable, queryable, and mappable. A consumer
  that needs only juvenile rearing duration is not forced to adopt a named
  race, a species claim, or a genetic-structure claim.
- The homograph and the false cognate are documented at term level, where a
  contributor or a matcher will encounter them, rather than in an ADR nobody
  reads at mapping time.
- The cycle-line terms now say something true for every population rather than
  something true for pink. The strong claim is still available, on its own
  property, for the populations that support it.
- The redundancy finding is resolvable at the source: once `CU_ID` decomposes,
  `LIFE_HISTORY_TYPE` carries no information the CU identifier does not, and
  SPSR can drop it rather than mint a term for it.
- No taxonomic-authority dispute is imported into `smn:`, and no
  `rdfs:seeAlso` resolves to an HTML page.
- PSC can map to these without restructuring. Its pipeline requires SKOS
  targets — it recorded a rejection of `smn:ObservedRateOrAbundance` as
  `rejected_wrong_kind_and_too_broad` with `native_type: owl:Class` — and
  composes `skos:broadMatch` through documented `skos:broader*` chains, which
  every concept here has. Every concept has exactly one `skos:prefLabel`, one
  `skos:definition`, one `skos:inScheme`, and at most one `skos:broader`,
  which is what PSC's SHACL requires of a mapping target.

### Negative

- Eighteen new shared terms — 4 schemes, 13 concepts, 5 properties — is the
  largest single admission to the shared layer since the age and year schemes,
  and CONVENTIONS section 1 sets a conservative default of keeping terms in a
  profile first. The count is larger than the first draft's 12 despite dropping
  five species concepts.
- Two levels are more work for a consumer than one flat list: a row that was
  one string becomes a named type plus, if the consumer wants the axes, a
  decomposition lookup.
- `smn:LifeHistoryTypeScheme` holds Sockeye types only, so it is broad in
  definition before it is broad in content — and deliberately stays that way
  until a species' bundle is shown to be stable enough to name.
- The species question is left open rather than answered. Anyone who needs a
  species IRI today still has none from `smn:`.

### Neutral

- `smn:Life-HistoryCharacteristic` and `smn:Run` are unchanged apart from an
  editorial comment. No released IRI is renamed, retired, or re-typed; the two
  concepts renamed in this revision (`smn:LakeTypeLifeHistory` →
  `smn:SockeyeLakeTypeLifeHistory`, and its river counterpart) exist only on
  this unmerged branch.
- Module 07 would go from 10 schemes / 49 concepts to 14 / 62.
  `knowledge/data/owl-skos-conventions-state.md` records the pre-merge figure
  and is updated when and if this merges, not before.
- Module 07 remains free of OWL declarations: the new properties are declared
  in modules 01 and 02 and only *used* on concepts in 07.
- Using `smn:` and `dwc:` in predicate position for the first time exposed a
  reproducibility defect in `scripts/build_flat_smn_ttl.py`: the merged graph
  carried no prefix bindings, so rdflib numbered predicate namespaces `ns1:`,
  `ns2:`, ... in hash-randomized order. One such namespace had been stable by
  luck; two were not, and eight runs of the generator on this branch produced
  four distinct files. Fixed in this change by binding the prefixes the modules
  declare, which also rewrites every `<https://w3id.org/smn/Term>` in the flat
  TTL and `docs/smn.ttl` as `smn:Term`. That is a large, semantically empty
  diff and it is unrelated to the terms proposed here; it is included because
  the proposal is what made the defect live. See
  `knowledge/data/builds-and-import-graph.md`.

## What would have to change downstream

**`gcdfo`** — mint the composite CU species-code vocabulary as a `gcdfo:`
scheme, each code carrying its `skos:notation` and a decomposition onto the
shared terms. `gcdfo:Species` keeps its role as a WSP output *field* handle.
Its scope note asking for taxonomic IRIs is **not** satisfied by this
proposal, and decision 1 explains why; the likely answer is
`dwc:scientificName` plus a WoRMS `dwc:scientificNameID` on the gcdfo codes.
Issues #68 and #70 close by reference to this ADR; #74 (species) stays open.

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

1. **Species, resolved how?** Decision 1 records two of Brett's statements that
   pull in different directions: a species reference, if minted, goes in `smn`
   and never `gcdfo`; and the likely future shape is a `gcdfo` **code**
   vocabulary carrying `dwc:scientificName` and a WoRMS
   `dwc:scientificNameID` directly. Those are compatible only if the gcdfo
   codes never need an `smn:` species concept to point at. Confirm which is
   intended before either is built.
2. **Is `dwc:scientificName` as a literal on a life-history concept
   acceptable?** It is the minimum that makes "species-scoped" machine-checkable
   rather than a naming convention, and it commits to no authority. It is also
   the only species assertion of any kind in this change.
3. **Two decomposition properties or one generic one?** As proposed, each axis
   gets its own property. A single `smn:hasLifeHistoryAxisValue` would let a
   future axis be added without a new property, at the cost of making "all
   types with a lake nursery" a two-hop query through `skos:inScheme`.
4. **Is `smn:SockeyeSeaTypeLifeHistory` wanted?** It is not in the source data.
   It is minted to complete the duration axis and to put the sea-type homograph
   warning on a term rather than in a document.
5. **"Cycle line" instead of "dominant cycle"** renames away from the wording in
   issue #70. Decision 4 is the argument.
6. **Layer.** These are proposed straight into shared `smn:`, not into a
   `smn/profile/<program>/` bridge. The justification is that two independently
   governed organizations (DFO and PSC) can use them, which is PSC's own
   promotion bar — but PSC has not asked for them, so the multi-agency reuse in
   CONVENTIONS section 8 criterion 1 is expected rather than demonstrated.

## More Information

- Evidence: `dfo-salmon-ontology` issues #68, #74, #70 (evidence pass
  2026-08-16); taxonomic-authority and life-history literature review
  2026-08-17.
- Rulings recorded in this ADR: steelhead is in scope; life-history type is
  asserted at CU / population / stock level and not for individual fish; a
  species reference, if needed later, belongs in `smn` and never in `gcdfo`.
  All three: Brett Johnson, 2026-08-17.
- Source code list: SPSR data dictionary crosswalk, `demo_cu`/`CU_ID` notes
  column. CU individuation counts (19 `PKO`, 14 `PKE`, `FRASER RIVER` as both
  `PKO-01` and `PKE-9005`, no sockeye CU split by line, Fraser Pink
  `Cyclic = FALSE`) from the DFO Conservation Unit tables.
- Life-history and cycle-line typology: Holtby, L.B. and Ciruna, K.A. 2007.
  *Conservation Units for Pacific Salmon under the Wild Salmon Policy.* DFO
  Can. Sci. Advis. Sec. Res. Doc. 2007/070.
- Sockeye types: Burgner, R.L. 1991. *Life history of sockeye salmon
  (Oncorhynchus nerka).* In Groot, C. and Margolis, L. (eds.), Pacific Salmon
  Life Histories. UBC Press.
- Chinook races, tactical versus race-defining variation, and the Sacramento
  winter run: Healey, M.C. 1991. *Life history of chinook salmon (Oncorhynchus
  tshawytscha).* In the same volume.
- The prior chinook sense of "sea-type": Gilbert, C.H. 1913. *Age at maturity
  of the Pacific coast salmon of the genus Oncorhynchus.* Bulletin of the
  United States Bureau of Fisheries.
- Instability of the chinook two-race bundle: Waples, R.S., Teel, D.J., Myers,
  J.M., and Marshall, A.R. 2004. *Life-history divergence in Chinook salmon:
  historic contingency and parallel evolution.* Evolution. Moran, P., Teel,
  D.J., Banks, M.A., et al. 2013. *Divergent life-history races do not
  represent Chinook salmon coast-wide: the importance of scale in Quaternary
  biogeography.* Canadian Journal of Fisheries and Aquatic Sciences.
- The potamodromous vocabulary and anadromy as a category alongside it:
  Rieman, B.E. and McIntyre, J.D. 1993. *Demographic and habitat requirements
  for conservation of bull trout.* USDA Forest Service General Technical
  Report INT-302.
- NCBI Taxonomy OBO PURL content negotiation verified 2026-08-17 by request,
  not by report.

## Related

- [ADR-0002](0002-year-age-basis-dimensions-and-abundance.md) — the
  orthogonal-schemes precedent, and the mint-from-evidence consequence that
  decision 5 narrows.
- `CONVENTIONS.md` sections 2, 3, 4, 8, 10, and 11.
