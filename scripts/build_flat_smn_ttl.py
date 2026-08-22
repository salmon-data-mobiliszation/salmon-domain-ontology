#!/usr/bin/env python3
"""Compose a flattened, import-expanded Salmon Domain Ontology TTL artifact.

This script resolves local `owl:imports` recursively from the canonical source
TTL and writes a single merged TTL file suitable for low-friction consumption.
The generated output intentionally strips `owl:imports` triples so it behaves like a
stable "master" read-only artifact.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict

from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, split_uri

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_ROOT = ROOT / "ontology"
SOURCE_DEFAULT = Path("ontology") / "salmon-domain-ontology.ttl"
FLAT_DEFAULT = Path("salmon-domain-ontology.ttl")


def discover_local_ontology_index() -> Dict[str, Path]:
    """Build mapping of ontology IRI -> local file path for local module imports.

    ontology/imports/ is deliberately excluded: it holds vendored snapshots of
    upstream ontologies (the W3C SOSA-PROV alignment and its transitive
    prov-o/sosa imports) that exist for offline catalog resolution only. The
    flattened one-file artifact stays smn-authored content: inlining upstream
    ontologies would triple its size and change its licensing story.
    """
    index: Dict[str, Path] = {}
    for path in sorted(ONTOLOGY_ROOT.rglob("*.ttl")):
        if "imports" in path.parts:
            continue
        graph = Graph()
        graph.parse(path, format="turtle")
        ontology_iri = graph.value(predicate=RDF.type, object=OWL.Ontology)
        if isinstance(ontology_iri, URIRef):
            index[str(ontology_iri)] = path
    return index


def collect_import_closure(
    source_path: Path, index: Dict[str, Path]
) -> tuple[Graph, Dict[str, str]]:
    graph = Graph()
    visited_paths = set()
    # namespace IRI -> the prefix the module sources declare for it. Visit
    # order is deterministic (sorted imports) and first declaration wins, so
    # two modules disagreeing about a prefix cannot make the output depend on
    # which was parsed first.
    source_prefixes: Dict[str, str] = {}

    def visit(path: Path) -> None:
        if path in visited_paths:
            return
        if not path.exists():
            raise FileNotFoundError(f"Local ontology file not found: {path}")

        local_graph = Graph()
        local_graph.parse(path, format="turtle")
        for triple in local_graph:
            graph.add(triple)
        for prefix, namespace in local_graph.namespaces():
            source_prefixes.setdefault(str(namespace), prefix)
        visited_paths.add(path)

        # Recurse deterministically through local imports.
        import_uris = sorted(
            (obj for obj in local_graph.objects(None, OWL.imports) if isinstance(obj, URIRef)),
            key=str,
        )
        for import_uri in import_uris:
            imported_path = index.get(str(import_uri))
            if imported_path is None:
                # Non-local imports are intentionally left as-is; consumers can resolve
                # those via standard ontology resolution if needed.
                continue
            if imported_path == path:
                continue
            visit(imported_path)

    visit(source_path)

    # Flattened file should be import-free and single-file consumable.
    for s, _, o in list(graph.triples((None, OWL.imports, None))):
        graph.remove((s, OWL.imports, o))

    # The flattened artifact must carry exactly ONE ontology identity: the
    # root <https://w3id.org/smn>. Merging the modules used to leave every
    # module's owl:Ontology header in the graph, and downstream ROBOT
    # serialization then attached the release metadata to whichever ontology
    # IRI sorted first (module 01) — the defect visible in the 0.0.0-0.0.2
    # release snapshots, found in the 0.0.3 release review. Non-root ontology
    # headers are dropped entirely; module identity remains recoverable from
    # each term's rdfs:isDefinedBy and the modular source tree.
    root = URIRef("https://w3id.org/smn")
    for ontology in list(graph.subjects(RDF.type, OWL.Ontology)):
        if ontology != root:
            for s, p, o in list(graph.triples((ontology, None, None))):
                graph.remove((s, p, o))

    return graph, source_prefixes


def apply_stable_prefixes(graph: Graph, source_prefixes: Dict[str, str]) -> None:
    """Give every predicate namespace a stable, meaningful prefix.

    The merged graph is built by copying triples only, so it inherits none of
    the modules' prefix bindings. rdflib's Turtle serializer then invents a
    prefix for each namespace it meets in *predicate* position — and only
    there, which is why subjects and objects were previously written in full —
    numbering them ns1, ns2, ... in store-iteration order. That order is
    hash-randomized per process, so with two or more such namespaces the same
    commit serialized to different bytes on different runs and
    `make verify-flat-ttl` reported the difference as drift. One namespace was
    stable by luck, which is why this stayed dormant until module 07 gained an
    `smn:` and a `dwc:` predicate on the same day.

    Binding the prefix the sources already declare removes the generated
    numbering altogether, which is both deterministic and readable: the
    artifact says `smn:hasCycleLine`, not `ns3:hasCycleLine`. Namespaces
    rdflib has already bound are left alone, and a prefix the sources declare
    for two different namespaces is used for the first only; anything left
    unnamed falls back to rdflib's numbering, applied here in sorted order so
    that the fallback is deterministic too. Retire this function only if the
    merge itself starts carrying the source bindings.
    """
    bound_namespaces = {str(ns) for _, ns in graph.namespace_manager.namespaces()}
    bound_prefixes = {prefix for prefix, _ in graph.namespace_manager.namespaces()}

    for predicate in sorted({p for _, p, _ in graph}, key=str):
        try:
            namespace, _local = split_uri(str(predicate))
        except Exception:
            # A predicate IRI rdflib cannot split needs no prefix; the
            # serializer writes it in full.
            continue
        if namespace in bound_namespaces:
            continue
        prefix = source_prefixes.get(namespace)
        if prefix and prefix not in bound_prefixes:
            graph.namespace_manager.bind(prefix, URIRef(namespace))
            bound_prefixes.add(prefix)
        else:
            graph.namespace_manager.compute_qname(str(predicate), generate=True)
        bound_namespaces.add(namespace)


def build_flat_ttl(*, source_path: Path, output_path: Path) -> None:
    if not source_path.exists():
        raise FileNotFoundError(f"Source ontology not found: {source_path}")

    index = discover_local_ontology_index()
    flat_graph, source_prefixes = collect_import_closure(
        source_path=source_path, index=index
    )
    apply_stable_prefixes(flat_graph, source_prefixes)

    serialized = flat_graph.serialize(format="turtle", sort_keys=True)
    if isinstance(serialized, bytes):
        serialized = serialized.decode("utf-8")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "# Auto-generated flattened TTL (read-only source artifact)\n"
        "# Generated by: scripts/build_flat_smn_ttl.py\n"
        f"# Source: {source_path.as_posix()}\n"
        "# DO NOT edit manually. Rebuild with `make compose-flat-ttl`.\n"
        "\n"
        + str(serialized),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a flattened local master TTL file.")
    parser.add_argument(
        "--source",
        type=Path,
        default=SOURCE_DEFAULT,
        help="Source ontology entrypoint (default: ontology/salmon-domain-ontology.ttl)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=FLAT_DEFAULT,
        help="Output flattened TTL file (default: salmon-domain-ontology.ttl)",
    )

    args = parser.parse_args()
    try:
        build_flat_ttl(source_path=args.source, output_path=args.output)
    except Exception as exc:  # broad by design: CLI user gets one clear error path.
        print(f"❌ failed to build flat TTL: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
