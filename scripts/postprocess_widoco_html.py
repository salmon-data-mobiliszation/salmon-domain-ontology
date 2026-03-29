#!/usr/bin/env python3
"""Post-process WIDOCO HTML output for project-specific UX defaults.

Current policy for this repo:
- normalize the displayed ontology title to "Salmon Domain Ontology"
- remove "Draft" wording from the default WIDOCO subtitle
- stabilize WIDOCO changelog list ordering across regenerations
- restore stable `#/Term` anchors for `smn:` terms
- inject the version IRI into the rendered metadata block
"""

from __future__ import annotations

import re
from pathlib import Path

from rdflib import Graph
from rdflib.namespace import OWL, RDF


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ontology" / "salmon-domain-ontology.ttl"
SMN_ENTITY_PATTERN = re.compile(
    r'(?P<indent>\s*)<div class="entity" id="https://w3id\.org/smn/(?P<term>[A-Za-z0-9._-]+)">'
)
SMN_LINK_PATTERN = re.compile(r'href="#https://w3id\.org/smn/([A-Za-z0-9._-]+)"')


def _load_version_iri() -> str | None:
    graph = Graph()
    graph.parse(SOURCE, format="turtle")
    ontology = next(graph.subjects(RDF.type, OWL.Ontology), None)
    if ontology is None:
        return None
    version_iri = graph.value(ontology, OWL.versionIRI)
    return str(version_iri) if version_iri is not None else None


def _canonicalize_change_lists(content: str) -> str:
    ul_pattern = re.compile(r"<ul>\s*(?:<li>.*?</li>\s*)+</ul>", flags=re.S)

    def _normalize_ul(match: re.Match[str]) -> str:
        block = match.group(0)
        items = re.findall(r"<li>.*?</li>", block, flags=re.S)
        if not items:
            return block

        normalized = [re.sub(r"\s+", " ", item).strip() for item in items]
        if not all(
            item.startswith("<li>Added:") or item.startswith("<li>Deleted:")
            for item in normalized
        ):
            return block

        ordered = [raw for _, raw in sorted(zip(normalized, items), key=lambda t: t[0])]
        indent_match = re.search(r"\n(\s*)<li>", block)
        indent = indent_match.group(1) if indent_match else ""
        return "<ul>\n" + "\n".join(f"{indent}{item.strip()}" for item in ordered) + "\n</ul>"

    return ul_pattern.sub(_normalize_ul, content)


def _restore_smn_term_anchors(content: str) -> str:
    content = SMN_LINK_PATTERN.sub(lambda match: f'href="#/{match.group(1)}"', content)

    def _inject_anchor(match: re.Match[str]) -> str:
        indent = match.group("indent")
        term = match.group("term")
        return f'{indent}<a id="/{term}"></a>\n{indent}<div class="entity" id="https://w3id.org/smn/{term}">'

    return SMN_ENTITY_PATTERN.sub(_inject_anchor, content)


def _inject_version_iri(content: str, version_iri: str | None) -> str:
    if not version_iri or version_iri in content or "<dt>Previous version:</dt>" not in content:
        return content

    injection = (
        f'<dt>Version IRI:</dt>\n<dd><a href="{version_iri}">{version_iri}</a></dd>\n<dt>Previous version:</dt>'
    )
    return content.replace("<dt>Previous version:</dt>", injection, 1)


def patch_html(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    original = content
    version_iri = _load_version_iri()

    content = content.replace("Salmon Domain Ontology (modular build)", "Salmon Domain Ontology")
    content = content.replace("Ontology Specification Draft", "Ontology Specification")
    content = _canonicalize_change_lists(content)
    content = _restore_smn_term_anchors(content)
    content = _inject_version_iri(content, version_iri)

    if content != original:
        path.write_text(content, encoding="utf-8")
        print(f"Patched {path}")
    else:
        print(f"No changes for {path}")


def main() -> None:
    for rel in ["docs/index.html", "docs/index-en.html"]:
        path = ROOT / rel
        if path.exists():
            patch_html(path)


if __name__ == "__main__":
    main()
