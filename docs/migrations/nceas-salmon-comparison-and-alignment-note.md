# SMN and NCEAS/DataONE SALMON: working thoughts on overlap, differences, and direction

_Status: working note (2026-03-28)._  
_Scope: shared-core Salmon Domain Ontology (`smn:`) compared against the NCEAS/DataONE SALMON ontology (`SALMON`)._  
_This is meant to read as a discussion note for the working group, not as a finished crosswalk or formal decision memo._

## Why this note exists

At this point it feels worth stepping back and looking at the emerging **Salmon Domain Ontology (SMN)** alongside the **NCEAS/DataONE SALMON ontology** in a more deliberate way.

The broad problem is familiar enough:

- salmon data are spread across organizations, projects, and reporting contexts
- the same idea gets named in different ways
- sometimes the same label means slightly different things
- and a lot of important meaning still lives in local spreadsheets, methods docs, and people’s heads

Both ontologies are trying to help with that, but they do not seem to be built from quite the same instincts. There is definitely overlap, but there are also some pretty clear differences in how the problem is being carved up.

This note is really just an attempt to say: **what seems similar, what seems different, and what direction makes the most sense for us right now?**

## Short version

The short version is:

- **SALMON** currently looks stronger as a **broad salmon-domain annotation vocabulary**.
- **SMN** currently looks stronger as a **smaller, more disciplined shared interoperability layer**.

That feels like the key distinction.

SALMON gives us breadth.  
SMN gives us architectural discipline.

Those are both useful. The trick is probably not to make one ontology imitate the other too quickly.

## What it feels like we are trying to do with SMN

Speaking a bit plainly, it seems like the basic idea behind SMN so far is **not** to build one giant salmon ontology that contains every useful term anybody might ever want.

Instead, the direction seems to be more like this:

- keep a **shared layer** for terms that are genuinely reusable across groups
- keep a **local or agency layer** for terms that are tied to one organization’s policy or workflow
- use **bridge mappings** to connect the two when needed

That is a pretty sensible pattern.

For anyone coming at this more as a salmon biologist than an ontology specialist, the easiest way to think about it is:

- **shared ontology** = the common language we want multiple groups to be able to use
- **local ontology/profile** = the terms a specific group needs for its own program logic
- **bridge layer** = the translation sheet between them

That seems to be the heart of the current SMN conventions.

## The conventions SMN seems to be settling into

### 1) Shared `smn:` should stay relatively small and reusable

The terms that seem most at home in shared `smn:` are things like:

- broad biological entities
- reusable observation and measurement patterns
- policy-neutral stock-assessment concepts
- a small number of controlled vocabularies that multiple groups might genuinely share

So far, this looks less like “put all salmon semantics here” and more like “put the durable shared middle layer here.”

That feels right.

### 2) Not every useful term belongs in shared `smn:`

This may be the most important convention of the lot.

A term can be:

- useful
- well-defined
- operationally important
- heavily used by one team

…and still **not** belong in the shared ontology.

If a term is really tied to one agency’s policy language, program workflow, or local method scheme, it probably belongs in a local/profile ontology first.

That is not a demotion. It is just good boundary discipline.

### 3) SMN is trying to separate durable concepts from controlled vocabularies

Another convention that seems important is the distinction between:

- **OWL classes/properties** for durable conceptual structure
- **SKOS concepts/schemes** for controlled vocabularies, codelists, and categories

In less ontology-ish language:

- use **OWL** when we are saying “this is a kind of thing” or “this is a real relation in the model”
- use **SKOS** when we are saying “this is a value in a vocabulary or scheme”

That distinction is easy to blur when we are just trying to get useful terms into the system, but it does seem to matter if we want the model to stay clean.

### 4) Shared-term promotion is supposed to be conservative

The working rule seems to be something like:

> if we are not sure a term is really shared, keep it local first

That means promotion into shared `smn:` should depend on things like:

- expected reuse across organizations
- reasonably stable meaning
- not being too tangled up in one agency’s policy language
- clear integration value

Again: boring rule, good rule.

### 5) We are trying not to invent meaning during cleanup and migration

Another good convention is that when terms move into shared space, we should reuse existing definitions and provenance where we can, rather than making up new wording just to make the docs look neat.

That may not sound exciting, but it is probably how we keep ontology work honest.

## How SMN seems to relate to the DFO salmon ontology

This part feels especially important, because the SMN/DFO boundary is doing a lot of practical work.

The cleanest current reading seems to be:

- **SMN** is the shared salmon-domain layer
- **DFO salmon ontology (`gcdfo:`)** is where DFO-specific policy/program semantics should live

So this is not really a contest between the two ontologies. They are playing different roles.

### In practice, that seems to mean:

#### Better fits for shared `smn:`

- broad biological units
- reusable observation/measurement patterns
- general stock-assessment concepts
- terms that would still make sense outside DFO

#### Better fits for `gcdfo:` or another local/profile layer

- DFO-specific policy status schemes
- DFO-specific benchmark categories
- DFO-specific method schemes
- estimate type / downgrade criteria / governance interpretation layers
- other terms whose meaning is strongly tied to one agency context

That boundary matters because otherwise the shared ontology starts soaking up local semantics just because they happen to be useful to the first group doing the work.

And that is exactly how shared ontologies get messy.

## What SALMON seems to be doing differently

SALMON appears to come from a somewhat different place.

It reads more like a broad ontology for annotating salmon-related datasets in one large space, rather than a deliberately layered shared-core-plus-profile architecture.

That gives it some real strengths:

- broad topical coverage
- lots of concrete salmon terms already there
- practical annotation value
- good comparison value when we want to see how another group handled a topic

But it also means SALMON seems more willing to keep a wider mix of things in one ontology, including:

- biological concepts
- measurement types
- fishery and gear categories
- tags and identifiers
- habitat/place terms
- local or operationally specific concepts

That is not necessarily a flaw. It is just a different modeling choice.

## Where the two ontologies clearly line up

There is real common ground here.

Both ontologies are trying to support:

- semantic annotation of salmon datasets
- better discovery and comparison across datasets
- more consistent reuse of terms
- less ambiguity in how data are described

That means SALMON is useful to us even if we do not adopt its modeling posture wholesale.

It gives us:

- a comparison ontology
- evidence for recurring salmon concepts
- another example of how to organize the space

## Main differences in modeling posture

| Topic | SMN (current direction) | NCEAS/DataONE SALMON | Why it matters |
| --- | --- | --- | --- |
| Overall shape | modular shared core + local/profile bridges | one large salmon-domain ontology | same label may still play a different role in the model |
| Main framing | SOSA + I-ADOPT + Darwin Core bridge posture | OBOE-centered measurement/annotation posture plus other external links | some measurement terms may be neighbors rather than exact equivalents |
| Scope discipline | tries to keep shared core fairly tight | broader in-core topical coverage | SALMON breadth should not automatically be imported into `smn:` |
| Controlled vocabularies | small curated shared SKOS layer | more operational categories represented as OWL classes | some SALMON content may fit better as profile vocabularies in SMN |
| Naming style | readable semantic IRIs | opaque numeric IRIs | label comparison is easy, semantic comparison still takes work |
| Governance posture | strong shared/local boundary | broader annotation-first coverage | easy to over-map if we are not careful |

## Some obvious places where the overlap looks promising

A few terms jump out as relatively straightforward starting points for comparison because they are concrete and biologically intuitive.

| SMN term | SALMON term | First-pass read |
| --- | --- | --- |
| `smn:alevin` | `SALMON` Alevin | looks like a pretty natural comparison point |
| `smn:forkLength` | `SALMON` Fork length | looks promising once hierarchy is right |
| `smn:standardLength` | `SALMON` Standard length | likely a useful early comparison term |
| `smn:totalLength` | `SALMON` Total length | likely a useful early comparison term |
| `smn:ForkLengthMeasurementMethod` | `SALMON` Fork length measurement method | probably in the same neighborhood, though still worth checking carefully |
| `smn:FishLengthMeasurementMethod` | `SALMON` Fish length determination method | clearly related, but not obviously identical |

These seem like good early terms to talk about because they are specific enough that the modeling issues are visible.

## Where we need to be careful

This is probably the most important part of the note.

### 1) Fish length is not the same thing as fork length

A useful example here is the fish-length area.

If we collapse **fish length** and **fork length** into the same thing, we lose the distinction between:

- a general characteristic
- one specific subtype of that characteristic

That matters.

The cleaner pattern seems to be:

- `FishLength` = the general characteristic
- `forkLength`, `standardLength`, `totalLength`, `orbitalLength` = kinds of fish length
- measurement classes then point to the specific subtype they measure

That is one of those spots where ontology modeling suddenly stops being abstract and becomes very concrete. A salmon biologist immediately knows fork length is not the same thing as fish length in general.

We already caught one case where the hierarchy was too strong there, which is probably a good reminder that the biologically obvious structure should not get lost in the formalism.

### 2) Escapement may overlap in subject matter but not in modeling pattern

SALMON includes classes like:

- salmon escapement count
- annual escapement count
- daily escapement count

SMN seems to be leaning more toward a compositional pattern where escapement is understood through combinations of:

- measurement
- survey/event
- time or context

So even when both ontologies are clearly about escapement, they may not be expressing it in the same way.

### 3) Stock semantics are similar, but not cleanly identical

SMN `Stock` is currently treated as a **reporting or management stratum**.

SALMON’s `Fish stock type` reads more broadly and mixes together management-unit and breeding-population language.

That does not make SALMON wrong. It just means we should probably avoid acting like these are automatically one-to-one.

### 4) Origin semantics do not line up neatly

Terms like `Wild stock` and `Hatchery` in SALMON do not map neatly onto SMN terms like `NaturalOrigin` and `HatcheryOrigin`.

That seems to be partly because the ontologies are talking at different levels:

- stock/facility/category semantics on one side
- individual-origin controlled vocabulary semantics on the other

### 5) Habitat and place terms may be better anchored externally

For habitat/place terms, it may be a mistake to think first in terms of bilateral SMN ↔ SALMON mapping.

In a lot of those cases, the better common anchor may actually be:

- ENVO
- GeoSPARQL
- another external geography/environment vocabulary

## Some SALMON terms that are interesting, but still not automatic shared-core candidates

SALMON highlights a few concepts that may be worth talking about further if they keep recurring across datasets and organizations:

- brood year
- run size
- spawner abundance
- recruit abundance
- migratory pattern
- reproductive strategy

The key point is not whether these are useful. They clearly are.

The key point is whether they belong in shared `smn:` yet.

That still seems to depend on questions like:

- would multiple groups actually reuse them?
- is the meaning stable enough across contexts?
- are they policy-neutral enough?
- would promotion improve interoperability, or just move clutter into shared space?

If the answer is not clearly yes, local/profile space still seems like the safer home.

## What probably should not be pulled into shared `smn:` just because SALMON has it

Examples include:

- ADF&G-specific codes
- local stock-name or stock-code administration terms
- many local fishery/gear/tag categories
- operational helper vocabularies that are useful in one setting but not clearly shared across settings

Those may still be perfectly good ontology terms. They just do not obviously belong in the shared layer.

## So where does that leave us?

At the moment, the comparison seems to point in a fairly clear direction.

### What seems true right now

1. **SALMON is useful as a comparison ontology.**  
   It gives us breadth, examples, and a way to spot recurring salmon concepts.

2. **SMN should probably stay disciplined as a shared-core ontology.**  
   Its value partly comes from not trying to absorb every local or operational term.

3. **The DFO salmon ontology still has a very real job to do.**  
   It remains the right place for DFO-owned semantics that are important but not yet truly shared.

4. **The shared/local boundary is not just technical fussiness.**  
   It is what keeps the architecture understandable.

5. **Same label does not mean same concept.**  
   We still need to compare meaning, scope, and modeling role, not just names.

### What seems like the sensible group posture for now

For now, the most sensible posture seems to be:

- use SALMON as a source of comparison and learning
- keep SMN fairly tight as the shared layer
- keep DFO-specific semantics where they belong
- be conservative about strong equivalence claims
- keep talking in terms of boundaries and direction, not rush into pretending the alignment questions are already settled

## Bottom line

The current read is that **SALMON and SMN are complementary, not competing**.

SALMON helps show us breadth.  
SMN helps us keep the shared architecture clean.  
The DFO salmon ontology helps keep agency-specific meaning where it belongs.

If those roles stay clear, then there is probably a very good path here: learn from SALMON, keep the SMN conventions disciplined, and avoid stuffing the shared layer full of useful-but-local semantics just because they happen to be available.

That feels like the right direction at this stage.

## Reference points

- NCEAS/DataONE SALMON repo: <https://github.com/DataONEorg/sem-prov-ontologies/tree/main/salmon>
- BioPortal entry: <https://bioportal.bioontology.org/ontologies/SALMON>
- SMN repo: <https://github.com/salmon-data-mobilization/salmon-domain-ontology>
- SMN conventions: `CONVENTIONS.md`
- Biologist-facing overview of modules/bridges: `docs/guides/modules-and-bridges-for-biologists.md`
