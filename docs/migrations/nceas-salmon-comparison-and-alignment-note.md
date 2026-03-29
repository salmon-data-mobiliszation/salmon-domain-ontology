# SMN and NCEAS/DataONE SALMON: working comparison note for group discussion

_Status: working assessment note (2026-03-28)._  
_Scope: shared-core Salmon Domain Ontology (`smn:`) compared against the NCEAS/DataONE Salmon Ontology (`SALMON`)._  
_This note is meant to support discussion among working-group co-chairs and collaborators. It is deliberately written as an assessment, not as a finished crosswalk or implementation plan._

## Why this note exists

We are now at the point where it is useful to compare the emerging **Salmon Domain Ontology (SMN)** with the **NCEAS/DataONE SALMON ontology** in a more deliberate way.

At a high level, both ontologies are trying to help with similar problems:

- making salmon datasets easier to describe and search
- making terms more consistent across projects
- making it easier to compare or combine datasets from different places
- reducing the amount of meaning that stays trapped in local spreadsheets, codebooks, or team memory

That said, they do **not** appear to be solving the problem in quite the same way. The overlap is real, but the modeling posture is different enough that we should be careful about assuming that same label = same meaning = same modeling move.

## Short take

Our current reading is this:

- **SALMON** is stronger today as a **broad salmon-domain annotation vocabulary**.
- **SMN** is stronger today as a **smaller, cleaner shared interoperability layer**.

In other words, SALMON currently looks more like a wide salmon-domain lexicon, while SMN is being shaped more like a shared coordination layer that can sit between multiple local or agency-specific ontologies.

That difference matters. It suggests that our job is probably **not** to make SMN look exactly like SALMON, and also **not** to ignore SALMON just because it grew out of a different context.

## The conventions we seem to be building in SMN so far

This section is written in plain language on purpose.

The best way to describe the emerging SMN conventions is that we are trying to separate the salmon ontology stack into a few different layers instead of putting everything into one giant ontology.

### 1) We are treating SMN as the shared layer

The current vision seems to be that `smn:` should hold terms that are:

- reusable across organizations
- reasonably stable in meaning
- not tightly tied to one agency’s policy wording or program workflow

Examples include things like:

- broad biological entities (`Population`, `Deme`)
- reusable observation and measurement patterns
- policy-neutral stock-assessment concepts
- a small number of shared controlled vocabularies

This makes SMN feel less like “one organization’s full ontology” and more like a **shared middle layer** that others can build around.

### 2) We are trying to keep DFO-specific semantics in the DFO ontology

The current boundary with the **DFO salmon ontology** seems to be:

- **SMN** = shared salmon-domain concepts that could reasonably be reused beyond DFO
- **DFO salmon ontology (`gcdfo:`)** = DFO-specific policy, program, status, method, and governance semantics

This is an important convention because it gives us a way to say:

> not every useful term belongs in the shared ontology

That is a healthy rule.

A term can be important, well-defined, and operationally necessary **without** belonging in shared `smn:`.

### 3) We are using a layered modeling pattern rather than one undifferentiated term pool

The emerging stack looks something like this:

1. **Shared OWL core** for durable shared concepts
2. **Small shared SKOS layer** for shared controlled vocabularies
3. **Local or agency/profile ontologies** for organization-specific semantics
4. **Bridge mappings** that connect local terms to shared terms

For a salmon biologist, the easiest way to think about this is:

- the **shared layer** is our common scientific/operational language
- the **local layer** is each program’s own wording and practical categories
- the **bridge layer** is the translation sheet between them

That seems to be one of the most important design choices in SMN.

### 4) We are being conservative about promotion into shared `smn:`

The working rule seems to be:

- if we are unsure, keep the term local first
- only promote it into shared `smn:` if reuse is clear and the meaning is stable

That is a useful safeguard because it prevents the shared ontology from becoming an uncurated pile of one-off project language.

### 5) We are distinguishing between durable concepts and controlled vocabularies

Another important convention is the difference between:

- **OWL classes/properties** for durable conceptual structure
- **SKOS concepts/schemes** for controlled vocabularies, status bins, method categories, and similar codelist-like material

A plain-language version of that distinction is:

- use **OWL** when we mean “this is a real kind of thing or relation in the model”
- use **SKOS** when we mean “this is a value in a controlled vocabulary”

That distinction is subtle at first, but it becomes very important once we start comparing ontologies built by different teams.

### 6) We are trying not to invent meaning during migration cleanup

Another emerging convention is that when terms move into shared space, we should:

- reuse existing definitions when authoritative wording already exists
- reuse provenance where we have it
- avoid inventing new definitions or sources just to make the docs look complete

That is less glamorous than minting new terms, but it is the sort of discipline that keeps an ontology from drifting away from the source material it claims to represent.

## How SMN currently seems to relate to the DFO salmon ontology

This relationship matters just as much as the comparison to SALMON.

At the moment, the cleanest way to explain the relationship is:

- **DFO salmon ontology** is still the right home for DFO-owned policy and operational semantics
- **SMN** is the place where we put the terms that look shared enough to be useful beyond DFO

That means the relationship is **complementary**, not competitive.

We do not need one ontology to “win.” We need the layers to stay understandable.

### What this means in practice

Our current conventions seem to imply the following:

#### Better candidates for shared `smn:`

- broad biological units
- reusable measurement patterns
- generic stock-assessment concepts
- terms that are understandable and useful across agencies or projects

#### Better candidates to remain in `gcdfo:` or another local/profile layer

- DFO policy status schemes
- DFO-specific benchmark categories
- DFO-specific method schemes
- estimate-type schemes and downgrade criteria
- other terms whose meaning depends strongly on one program’s governance context

This is consistent with recent boundary decisions where some terms that looked useful at first were judged to be **DFO-specific rather than truly shared**.

The practical lesson is simple:

> “useful to DFO” is not the same thing as “belongs in SMN.”

## What SALMON seems to be doing differently

The NCEAS/DataONE SALMON ontology appears to come from a different starting point.

Its strongest pattern is not “small shared core plus profile layers.” Instead, it looks more like a broad ontology for annotating salmon-related datasets in one large domain space.

That brings some strengths:

- wide topical coverage
- lots of concrete salmon terms already present
- useful annotation vocabulary for datasets and portals
- practical value as a source ontology when we want to see how someone else handled a problem

But it also means SALMON seems more willing to keep the following in one place:

- biological concepts
- measurement types
- fishery and gear categories
- tags and identifiers
- place/habitat terms
- some fairly local or operational concepts

That is not “wrong.” It is simply a different design choice.

## Main synergies between SMN and SALMON

There is real common ground.

Both ontologies are trying to support:

- semantic annotation of salmon datasets
- interoperability across data holdings
- reuse of existing standards where possible
- better search, discovery, and interpretation

We should not overstate the overlap, but we also should not miss it.

SALMON is useful to us because it gives us:

- a broad comparison source
- evidence that certain salmon concepts really do recur
- examples of how another group chose to partition the space

## Main differences in modeling posture

| Topic | SMN (current direction) | NCEAS/DataONE SALMON | Why it matters |
| --- | --- | --- | --- |
| Overall shape | modular shared core + local/profile bridges | one large salmon-domain ontology | similar labels may still play different roles |
| Main upper-level framing | SOSA + I-ADOPT + Darwin Core bridge posture | OBOE-centered measurement/annotation posture plus external links | measurement terms may look similar but still model different things |
| Scope discipline | conservative shared-core admission | broader in-core topical coverage | SALMON terms are not automatically candidates for shared `smn:` |
| Controlled vocabularies | small curated shared SKOS layer | many operational categories represented as OWL classes | some SALMON areas may align better to SMN profile vocabularies than to shared core |
| Naming/IRI style | readable semantic IRIs | opaque numeric IRIs | label comparisons are easier than structural comparisons |
| Governance posture | explicit boundary between shared and local | broader annotation-first posture | we should resist collapsing distinct local meanings into shared terms too early |

## Obvious areas of overlap worth reviewing first

A few terms stand out as relatively obvious early review candidates because they are concrete and easier to reason about than policy-heavy concepts.

| SMN term | SALMON term | First-pass assessment |
| --- | --- | --- |
| `smn:alevin` | `SALMON` Alevin | looks like a strong candidate for close review |
| `smn:forkLength` | `SALMON` Fork length | looks promising once hierarchy is correct |
| `smn:standardLength` | `SALMON` Standard length | likely a good early comparison candidate |
| `smn:totalLength` | `SALMON` Total length | likely a good early comparison candidate |
| `smn:ForkLengthMeasurementMethod` | `SALMON` Fork length measurement method | likely in the same neighborhood, but still needs modeling review |
| `smn:FishLengthMeasurementMethod` | `SALMON` Fish length determination method | clearly related, but probably not safe to treat as automatically identical |

These are useful starting points because they are biologically intuitive and narrow enough that the modeling questions are visible.

## Areas where similarity in label may hide a real modeling difference

This is where we need to be careful.

### 1) Fish length vs fork length

This is the clearest example.

If we say **fish length** and **fork length** are the same thing, we flatten a general characteristic into one particular subtype.

That is not just a wording problem. It changes the logic of the ontology.

A safer pattern is:

- `FishLength` = the general characteristic
- `forkLength`, `standardLength`, `totalLength`, `orbitalLength` = different kinds of fish length
- measurement classes then point to the specific subtype they measure

We have already seen how easy it is for this distinction to blur when ontology work starts to feel abstract. In practice, this is exactly the kind of modeling detail that matters.

### 2) Escapement

SALMON includes classes such as:

- salmon escapement count
- annual escapement count
- daily escapement count

SMN seems to be moving toward a more compositional pattern where we treat escapement through combinations of:

- measurement
- survey/event
- time or context

So even when the subject matter overlaps, the modeling move may not.

### 3) Stock semantics

SMN `Stock` is currently being treated as a **reporting or management stratum**.

SALMON’s `Fish stock type` reads more broadly and mixes together management-unit and breeding-population language.

That does not make it useless. It just means we should not rush into exact-match claims.

### 4) Origin semantics

SALMON terms such as `Wild stock` and `Hatchery` do not line up neatly with SMN terms such as `NaturalOrigin` and `HatcheryOrigin`.

Here the problem is not that one ontology is right and the other is wrong. The problem is that they are talking about meaning at different levels.

### 5) Habitat and place terms

In this area, bilateral SMN ↔ SALMON mapping may not even be the best first move.

If both ontologies are drawing on broader geographic or environmental standards, then the better anchor may often be:

- ENVO
- GeoSPARQL
- another external geography/environment vocabulary

## Candidate terms that SALMON highlights, but that we should still treat cautiously

SALMON suggests some concepts that may become good candidates for future shared-core discussion **if** we start seeing repeated use across datasets and organizations:

- brood year
- run size
- spawner abundance
- recruit abundance
- migratory pattern
- reproductive strategy

At this stage, the important point is not whether these are “good” terms. The important point is whether they meet the shared-core test.

That test still seems to be:

- would multiple groups reuse them?
- is the meaning stable enough?
- are they policy-neutral enough?
- would promoting them into shared `smn:` actually improve interoperability?

If the answer is not clearly yes, the safer move is still to keep them local or profile-scoped for now.

## What probably should **not** be pulled into shared SMN just because SALMON has it

Examples include:

- ADF&G-specific codes
- local stock-name or stock-code administration terms
- many local fishery/gear/tag categories
- other operational helper vocabularies that are useful in one program but not clearly shared across programs

These may be perfectly legitimate ontology terms. They just do not obviously belong in the shared salmon-domain layer.

## Where this leaves us

At the moment, the comparison suggests a fairly clear working position.

### What seems true

1. **SALMON is worth taking seriously as a comparison ontology.**  
   It covers a lot of useful salmon-domain ground.

2. **SMN should probably stay disciplined as a shared-core ontology.**  
   Its value comes partly from not trying to absorb every useful local concept.

3. **The DFO salmon ontology still has an important role.**  
   It remains the right place for DFO-owned policy/program semantics that are not yet truly shared.

4. **The shared/local boundary is doing real work.**  
   It is not just technical fussiness. It is how we avoid turning shared ontology work into a dumping ground.

5. **A label-level overlap is not enough.**  
   We need to compare meaning, scope, and modeling role, not just names.

### What we should take away as a group

If we accept the current SMN conventions, then the right direction seems to be:

- use SALMON as a source of comparison, ideas, and possible gap signals
- keep SMN small enough to remain genuinely shared
- keep DFO-specific semantics where they belong
- be cautious about strong equivalence claims
- treat this stage as assessment and boundary-setting, not as a race to make one giant alignment artifact

## Bottom line

Our current read is that **SALMON and SMN are complementary, not competing ontologies**.

SALMON helps us see breadth.
SMN helps us enforce discipline.
The DFO salmon ontology helps us keep agency-specific meaning in the right place.

If we keep those roles clear, we should be able to learn from SALMON without losing the architectural logic we have been trying to build in SMN.

## Reference points

- NCEAS/DataONE SALMON repo: <https://github.com/DataONEorg/sem-prov-ontologies/tree/main/salmon>
- BioPortal entry: <https://bioportal.bioontology.org/ontologies/SALMON>
- SMN repo: <https://github.com/salmon-data-mobilization/salmon-domain-ontology>
- SMN conventions: `CONVENTIONS.md`
- Biologist-facing overview of modules/bridges: `docs/guides/modules-and-bridges-for-biologists.md`
