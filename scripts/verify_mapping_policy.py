#!/usr/bin/env python3
"""Enforce CONVENTIONS section 5b mapping placement and coherence rules.

Three checks, all CI-fatal:

1. Foreign-subject logical axioms (subClassOf / subPropertyOf /
   equivalentClass / equivalentProperty / sameAs) are permitted only in the
   alignment modules. Core modules (01-07) and views must never state them.
   Bare declaration stubs (``ex:Term a owl:Class .``) and documentation
   annotations are allowed anywhere; the annotated NCBITaxon MIREOT mirror
   in module 02 is an explicit exception.
2. One strongest mapping per subject-object pair across the default build
   spine: a pair may carry predicates from exactly one tier
   (Tier 1 = subClassOf/subPropertyOf/equivalent*/sameAs,
   Tier 2 = exactMatch, Tier 3 = closeMatch/broadMatch/narrowMatch/
   relatedMatch). The alignment-main/alignment-research promotion-staging
   exception is cross-module by construction and therefore not visible to
   this spine-level check.
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
            if predicate in TIER1:
                if path.name == "02-observation-measurement.ttl" and "NCBITaxon" in str(subject):
                    continue  # annotated MIREOT mirror of the upstream taxon hierarchy
                failures.append(
                    f"{path.relative_to(ROOT)}: foreign-subject axiom "
                    f"{subject.n3(graph.namespace_manager)} "
                    f"{predicate.n3(graph.namespace_manager)} "
                    f"{obj.n3(graph.namespace_manager)}"
                )
    return failures


def check_tier_mixing() -> list:
    graph = Graph()
    for name in SPINE:
        graph.parse(ROOT / "ontology" / "modules" / name, format="turtle")
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
    return [
        f"tier-mixed pair (tiers {'/'.join(sorted(tiers))}): {s} -> {o}"
        for (s, o), tiers in sorted(tiers_by_pair.items())
        if len(tiers) > 1
    ]


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
