# Conventions

This document defines how we model shared salmon semantics versus agency/profile-specific vocabularies.

## 1) Goal

Build a **shared interoperability layer** that supports precise cross-agency integration while still allowing each organization to maintain local policy/program vocabularies.

Conservative default: **if unsure, keep terms in a profile ontology first**. Promote to shared only when reuse is clear.

## 2) Layered model (authoritative)

### Layer A — Shared OWL semantic core (`smn:`)

Use for cross-agency concepts with stable semantics and reusable logical structure.

Examples:
- biological entities (`Population`, `Deme`)
- reusable monitoring/measurement semantics (`SurveyEvent`, `EscapementMeasurement`)
- reusable quantitative semantics (`ExploitationRate`)

### Layer B — Shared SKOS interoperability layer (`smn:`)

A **small curated SKOS layer** for truly cross-agency controlled vocabularies.

Use for:
- shared codelists that are expected to be reused by multiple organizations
- concept labels/definitions that support operational data harmonization

### Layer C — Agency/profile ontologies (organization namespaces)

Use for policy/program-specific vocabularies that should remain local, including one-off project terms, local method taxonomies, and governance interpretation layers.

Examples:
- named policy schemes and statuses that are not broadly governed across agencies
- organization-specific method taxonomies and quality bins

A profile can start in a local namespace (recommended default), and only later be promoted to a shared collaboration namespace such as `https://w3id.org/smn/profile/<program>/` if needed for cross-organization reuse.

## 2b) Profile publishing progression (practical)

Use this decision path to reduce namespace burden while still allowing formal semantics:

1. **Private/local draft (fastest):** define terms in your project repo or package as a simple TTL file.
   - No public namespace commitment required.
   - Link terms to shared anchors with provisional mappings for testing/integration.
2. **Project bridge (shared in collaboration):** if multiple teams need shared access, publish a profile artifact under `https://w3id.org/smn/profile/<program>/` only for bridge terms that are actively co-owned.
   - This is a *collaboration artifact*, not a guarantee of long-term canonical shared meaning.
   - Keep detailed provenance + mapping rationale in the profile module.
3. **Shared namespace promotion:** only move terms into `smn:` when reuse is stable across multiple agencies and semantics are policy-neutral.

### Layer D — Mapping/bridge artifacts

Machine-readable mappings that connect profile terms to shared domain terms.

Use these to support ingestion, search, and migration without collapsing distinct semantics.

## 3) OWL vs SKOS modeling rules

### Use OWL classes/properties when:
1. You need formal logical structure (subclass/property reasoning, restrictions, constraints).
2. The term represents a durable domain concept rather than a codelist entry.
3. Integration pipelines need deterministic canonicalization.

### Use SKOS concepts/schemes when:
1. You are modeling code values, method bins, status categories, or policy vocabulary.
2. Label hierarchy and human interpretation are primary.
3. Local governance of terms is expected to evolve quickly.

### Dual representation rule

A concept may exist as both OWL and SKOS **only with separate IRIs** and explicit mapping.

## 4) IRI strategy

1. Shared terms use `smn:` IRIs.
2. Default for local/project ontologies: use organization-owned namespaces first.
3. Optional collaboration publishing: `https://w3id.org/smn/profile/<program>/` only for curated bridge artifacts.
4. Do not overload a single IRI with incompatible roles.
5. OWL class IRIs and SKOS concept IRIs must remain distinct where both are needed.

### Profile artifact rule for publication

- **If terms are only for one team/project:** keep them in a local namespace.
- **If terms are needed across a specific collaborating group:** use the `smn/profile/<program>/` pattern as an agreed-on bridge container.
- **If terms are intended for broad cross-organization reuse:** propose promotion to shared `smn:` after evidence review.

## 5) Mapping strength policy

Treat mapping predicates as different evidence strengths:

### Tier 1 (strict / automation-safe)
- `owl:equivalentClass`
- `owl:equivalentProperty`
- `owl:sameAs`
- `rdfs:subClassOf`
- `rdfs:subPropertyOf`

### Tier 2 (strong lexical/conceptual)
- `skos:exactMatch`

### Tier 3 (advisory / candidate only)
- `skos:closeMatch`
- `skos:broadMatch`
- `skos:narrowMatch`
- `skos:relatedMatch`

Operational rule: Tier 3 links should not auto-canonicalize data into the production graph without review/promotion.

## 6) Profile-to-domain bridge pattern

When a profile concept corresponds to shared domain semantics:

1. Keep the profile concept in profile namespace.
2. Link it to shared domain semantics using mapping predicates.
3. Prefer `skos:exactMatch` only when semantics are truly equivalent.
4. Use `skos:closeMatch`/`broadMatch` as provisional links.
5. Attach provenance and reviewer metadata for each bridge.

Example (conceptual):
- `profile:SomeMethodConcept skos:closeMatch smn:EscapementMeasurement .`
- `profile:SomeMethodConcept prov:wasDerivedFrom <source-doc> .`

## 7) LLM-assisted integration policy

LLMs may propose mappings, but production integration must follow approval gates.

### Required output from mapping assistants
1. proposed shared target
2. mapping predicate suggestion
3. confidence score
4. rationale text
5. recommended action (`accept`, `review`, `defer`, `new-term-request`)

### Ingestion gate

Only approved mappings (Tier 1/2 or explicitly promoted Tier 3) materialize into canonical graph integration transforms.

## 8) Shared-term admission policy

Expert judgment is allowed, but conservative.

Promotion to shared should include:
1. expected multi-agency reuse
2. semantic stability across contexts
3. non-reliance on agency-specific policy interpretation
4. practical integration benefit

If any criterion is weak, keep term in profile and map to shared anchors.

## 9) Versioning and transition

Current posture:
1. migration mode can use direct replacement for alpha transitions when risk is low
2. publish machine-readable old→new mapping for each migration wave
3. maintain explicit migration notes per release
4. endpoint cutover timing may be deferred until profile/shared boundary stabilizes

## 10) Term annotation completeness and rendering

This section is canonical for the annotation fields that make shared terms complete and render well in generated docs.

### Shared OWL terms (classes + properties)

Required:
- `rdfs:label "Human Name"@en`
- `iao:0000115 "1–2 sentence definition."@en`
- `rdfs:isDefinedBy <https://w3id.org/smn>`

Recommended when authoritative wording already exists:
- `iao:0000119 "Citation text here."@en`
- `dcterms:source <https://example.org/source>`

Use `rdfs:comment` only for editorial notes, migration notes, scope notes, or maintainer guidance. Do **not** use `rdfs:comment` as the primary definition field for OWL terms.

### Shared SKOS concepts and schemes

Required:
- `skos:prefLabel "Human Name"@en`
- `rdfs:isDefinedBy <https://w3id.org/smn>`

Additional expectations:
- Concepts should include `skos:inScheme :SchemeName`
- Concepts and schemes should include `skos:definition "1–2 sentence definition."@en` whenever authoritative wording is available
- Provenance should be attached with `iao:0000119` and/or `dcterms:source` when that information already exists

### Backfilling migrated terms

When shared `smn:` terms were migrated from another ontology or profile:
1. reuse the existing definition/provenance text exactly where possible
2. do **not** invent new IRIs, sources, or definitions during migration cleanup
3. if a required/recommended field cannot be filled from existing written material, leave the term unresolved and track it in the gap ledger for follow-up

### Rendering rule of thumb

If you care how WIDOCO/docs render, put the definition on the term itself using `iao:0000115` (OWL) or `skos:definition` (SKOS), keep `rdfs:isDefinedBy` present, and attach provenance directly to that same term.

## 11) Current boundary decisions (working set)

### Keep in shared domain (current)
1. `Stock`
2. `IndicatorRiver`
3. core biological and measurement semantics that are policy-neutral

### Keep in profile layer (current)
1. WSP-specific status and confidence schemes/concepts
2. Enumeration method scheme (organization/program-specific)
3. Estimate method scheme (organization/program-specific)
4. Benchmark level scheme (organization/program-specific)
5. Policy framework scheme terms that are organization-specific
6. Estimate type and downgrade-criteria schemes/concepts

These decisions are revisited only with explicit governance review and evidence.
