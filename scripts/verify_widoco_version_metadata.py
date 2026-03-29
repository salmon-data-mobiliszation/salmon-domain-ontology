#!/usr/bin/env python3
"""Verify WIDOCO HTML exposes the ontology version metadata."""

from __future__ import annotations

from pathlib import Path

from rdflib import Graph
from rdflib.namespace import DCTERMS, OWL, RDF


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ontology" / "salmon-domain-ontology.ttl"
PAGES = ("docs/index.html", "docs/index-en.html")


def load_expected_values() -> list[tuple[str, str]]:
    graph = Graph()
    graph.parse(SOURCE, format="turtle")
    ontology = next(graph.subjects(RDF.type, OWL.Ontology), None)
    if ontology is None:
        raise SystemExit(f"No owl:Ontology declaration found in {SOURCE}")

    expected = []
    version_info = graph.value(ontology, OWL.versionInfo)
    version_iri = graph.value(ontology, OWL.versionIRI)
    prior_version = graph.value(ontology, OWL.priorVersion)
    modified = graph.value(ontology, DCTERMS.modified)

    if version_info is not None:
        expected.append(("versionInfo", str(version_info)))
    if version_iri is not None:
        expected.append(("versionIRI", str(version_iri)))
    if prior_version is not None:
        expected.append(("priorVersion", str(prior_version)))
    if modified is not None:
        expected.append(("modified", str(modified)))

    if not expected:
        raise SystemExit(f"No version metadata found in {SOURCE}")
    return expected


def main() -> int:
    expected = load_expected_values()
    failures = []

    for rel in PAGES:
        html = (ROOT / rel).read_text(encoding="utf-8")
        missing = [label for label, value in expected if value not in html]
        if missing:
            failures.append((rel, missing))
        else:
            labels = ", ".join(label for label, _ in expected)
            print(f"OK {rel}: exposes {labels}")

    if failures:
        for rel, missing in failures:
            print(f"FAIL {rel}: missing {', '.join(missing)}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
