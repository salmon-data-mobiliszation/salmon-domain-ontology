#!/usr/bin/env python3
"""Enforce CONVENTIONS section 5b mapping placement and coherence rules.

Three checks, all CI-fatal:

1. Foreign-subject statements outside alignment modules: a subject smn does
   not own may carry only documentation annotations (label/comment/seeAlso/
   isDefinedBy) and bare declaration stubs. Everything else — Tier-1 axioms
   AND instance-level property assertions — is confined to the alignment
   modules; the annotated NCBITaxon MIREOT mirror in module 02 is the one
   explicit exception.
2. One strongest mapping per subject-object pair, checked two ways: within
   every single module/view file (covers 08/09, alignment-research, views —
   the promotion-staging exception is cross-module by definition and can
   never apply within one file), and across the default build spine (which
   excludes alignment-research, the documented staging exception).
3. Reasoner-clean typing invariant: no IRI in the flattened build may be
   typed both owl:Class and skos:Concept (the dual-representation rule).
"""

from collections import defaultdict
from pathlib import Path

from rdflib import Graph, RDF, RDFS, OWL, URIRef
from rdflib.namespace import SKOS

ROOT = Path(__file__).resolve().parents[1]
SMN = "https://w3id.org/smn"
ALIGNMENT_MODULES = {
    "alignment-main.ttl",
    "alignment-upper.ttl",
    "alignment-research.ttl",
}
SPINE = [
    "01-entity-systematics.ttl",
    "02-observation-measurement.ttl",
    "03-assessment-benchmarks.ttl",
    "04-management-governance.ttl",
    "05-provenance-quality.ttl",
    "06-data-interoperability.ttl",
    "07-controlled-vocabularies.ttl",
    "alignment-main.ttl",
    "alignment-upper.ttl",
]
TIER1 = {
    RDFS.subClassOf,
    RDFS.subPropertyOf,
    OWL.equivalentClass,
    OWL.equivalentProperty,
    OWL.sameAs,
}
TIER2 = {SKOS.exactMatch}
TIER3 = {SKOS.closeMatch, SKOS.broadMatch, SKOS.narrowMatch, SKOS.relatedMatch}


# Predicates a foreign-namespace subject may carry outside alignment
# modules: declaration stubs and documentation annotations only.
# Everything else — Tier-1 axioms AND instance-level property assertions
# (the old `sosa:FeatureOfInterest sosa:hasSample sosa:Sample` class of
# mistake) — must live in an alignment module (CONVENTIONS 5b rule 2).
FOREIGN_ALLOWED_PREDICATES = {
    RDFS.comment,
    RDFS.label,
    RDFS.seeAlso,
    RDFS.isDefinedBy,
}
FOREIGN_ALLOWED_TYPE_OBJECTS = {
    OWL.Class,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.NamedIndividual,
    OWL.Ontology,
}


def check_foreign_subjects() -> list:
    failures = []
    paths = sorted((ROOT / "ontology" / "modules").glob("*.ttl")) + sorted(
        (ROOT / "ontology" / "views").glob("*.ttl")
    )
    for path in paths:
        if path.name in ALIGNMENT_MODULES:
            continue
        graph = Graph()
        graph.parse(path, format="turtle")
        for subject, predicate, obj in graph:
            if not isinstance(subject, URIRef) or str(subject).startswith(SMN):
                continue
            if predicate in FOREIGN_ALLOWED_PREDICATES:
                continue
            if predicate == RDF.type and obj in FOREIGN_ALLOWED_TYPE_OBJECTS:
                continue  # bare declaration stub
            if path.name == "02-observation-measurement.ttl" and "NCBITaxon" in str(subject):
                continue  # annotated MIREOT mirror of the upstream taxon hierarchy
            failures.append(
                f"{path.relative_to(ROOT)}: foreign-subject statement "
                f"{subject.n3(graph.namespace_manager)} "
                f"{predicate.n3(graph.namespace_manager)} "
                f"{obj.n3(graph.namespace_manager)}"
            )
    return failures


def _pair_tiers(graph: Graph) -> dict:
    tiers_by_pair = defaultdict(set)
    for subject, predicate, obj in graph:
        if not (isinstance(subject, URIRef) and isinstance(obj, URIRef)):
            continue
        if predicate in TIER1:
            tiers_by_pair[(subject, obj)].add("1")
        elif predicate in TIER2:
            tiers_by_pair[(subject, obj)].add("2")
        elif predicate in TIER3:
            tiers_by_pair[(subject, obj)].add("3")
    return tiers_by_pair


def check_tier_mixing() -> list:
    failures = []
    # (a) No pair mixes tiers WITHIN any single module or view file — this
    # covers 08/09, alignment-research, and the views, where the
    # promotion-staging exception (a cross-module pattern by definition)
    # can never apply.
    all_paths = sorted((ROOT / "ontology" / "modules").glob("*.ttl")) + sorted(
        (ROOT / "ontology" / "views").glob("*.ttl")
    )
    for path in all_paths:
        graph = Graph()
        graph.parse(path, format="turtle")
        for (subject, obj), tiers in sorted(_pair_tiers(graph).items()):
            if len(tiers) > 1:
                failures.append(
                    f"{path.relative_to(ROOT)}: tier-mixed pair within one "
                    f"module (tiers {'/'.join(sorted(tiers))}): {subject} -> {obj}"
                )
    # (b) No pair mixes tiers across the default build spine (which excludes
    # alignment-research — the documented promotion-staging exception).
    graph = Graph()
    for name in SPINE:
        graph.parse(ROOT / "ontology" / "modules" / name, format="turtle")
    for (subject, obj), tiers in sorted(_pair_tiers(graph).items()):
        if len(tiers) > 1:
            failures.append(
                f"tier-mixed pair across the default spine "
                f"(tiers {'/'.join(sorted(tiers))}): {subject} -> {obj}"
            )
    return failures


def check_dual_typing() -> list:
    graph = Graph()
    graph.parse(ROOT / "salmon-domain-ontology.ttl", format="turtle")
    classes = set(graph.subjects(RDF.type, OWL.Class))
    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    return [
        f"IRI typed both owl:Class and skos:Concept: {iri}"
        for iri in sorted(str(x) for x in classes & concepts if isinstance(x, URIRef))
    ]


def main() -> None:
    failures = check_foreign_subjects() + check_tier_mixing() + check_dual_typing()
    if failures:
        for failure in failures:
            print(failure)
        raise SystemExit(1)
    print("Mapping policy verified: no foreign-subject axioms outside alignment "
          "modules, no tier-mixed pairs in the default spine, no dual-typed IRIs.")


if __name__ == "__main__":
    main()
