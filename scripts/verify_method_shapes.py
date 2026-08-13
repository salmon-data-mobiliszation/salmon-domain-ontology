#!/usr/bin/env python3
"""Behavioural check for ontology/shapes/method-shapes.ttl.

The shapes carry the value constraint the 2026-08-13 methods-as-SKOS
migration moved out of OWL: smn:basedOn values must be method concepts at
or below smn:EnumerationMethod in smn:MethodScheme. Because the ontology
itself contains no smn:AggregatedMeasurement instances, this check runs
the shapes against a built-in fixture: a conforming instance (based on an
enumeration method) must pass, and a violating instance (based on a
fork-length method) must be flagged. Requires pyshacl.
"""

from pathlib import Path

from pyshacl import validate
from rdflib import Graph

ROOT = Path(__file__).resolve().parents[1]

FIXTURE = """
@prefix smn: <https://w3id.org/smn/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ex: <http://example.org/> .

smn:EnumerationMethod skos:inScheme smn:MethodScheme .
smn:ForkLengthMeasurementLabMethod skos:inScheme smn:MethodScheme ;
  skos:broader smn:ForkLengthMeasurementMethod .
smn:ForkLengthMeasurementMethod skos:inScheme smn:MethodScheme ;
  skos:broader smn:FishForkLengthMeasurementMethod .
smn:FishForkLengthMeasurementMethod skos:inScheme smn:MethodScheme ;
  skos:broader smn:FishLengthMeasurementMethod .
smn:FishLengthMeasurementMethod skos:inScheme smn:MethodScheme .

ex:conforming a smn:AggregatedMeasurement ; smn:basedOn smn:EnumerationMethod .
ex:violating a smn:AggregatedMeasurement ; smn:basedOn smn:ForkLengthMeasurementLabMethod .
"""


def main() -> None:
    data = Graph()
    data.parse(data=FIXTURE, format="turtle")
    shapes = Graph()
    shapes.parse(ROOT / "ontology" / "shapes" / "method-shapes.ttl", format="turtle")
    conforms, _, report_text = validate(data, shacl_graph=shapes, advanced=True)

    failures = []
    if conforms:
        failures.append("expected the violating fixture instance to be flagged, "
                        "but the report conforms")
    # pyshacl may render focus nodes prefixed (ex:violating) or as full IRIs
    if not any(m in report_text for m in ("ex:violating", "http://example.org/violating")):
        failures.append("the violating instance is not named in the report")
    if any(m in report_text for m in ("ex:conforming", "http://example.org/conforming")):
        failures.append("the conforming instance was incorrectly flagged")

    if failures:
        for failure in failures:
            print(failure)
        print(report_text)
        raise SystemExit(1)
    print("Method shapes verified: violating fixture flagged, conforming fixture passes.")


if __name__ == "__main__":
    main()
