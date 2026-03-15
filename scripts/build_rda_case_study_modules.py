#!/usr/bin/env python3
"""Compose the case-study profile modules from split fragments."""

from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "ontology" / "modules"
FRAGMENTS_DIR = ROOT / "ontology" / "case-studies" / "rda-juvenile-condition"

MODULE_SPECS = [
    {
        "output": MODULE_DIR / "09-rda-neville-decomposition-profile-bridges.ttl",
        "fragments": [
            FRAGMENTS_DIR / "09-rda-neville-entities.ttl",
            FRAGMENTS_DIR / "09-rda-neville-observations.ttl",
            FRAGMENTS_DIR / "09-rda-neville-constraints.ttl",
        ],
        "header": dedent(
            """
            @prefix smn: <https://w3id.org/smn/> .
            @prefix neville: <https://w3id.org/smn/profile/neville/> .
            @prefix rda: <https://w3id.org/smn/profile/rda-case-study/> .
            @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
            @prefix owl: <http://www.w3.org/2002/07/owl#> .
            @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
            @prefix prov: <http://www.w3.org/ns/prov#> .
            @prefix dcterms: <http://purl.org/dc/terms/> .
            @prefix obo: <http://purl.obolibrary.org/obo/> .
            @prefix iadopt: <https://w3id.org/iadopt/ont/> .
            @prefix time: <http://www.w3.org/2006/time#> .

            # Auto-generated. Do NOT edit directly.
            # Edit fragments under ontology/case-studies/rda-juvenile-condition/ and
            # regenerate with: python3 scripts/build_rda_case_study_modules.py

            <https://w3id.org/smn/modules/09-rda-neville-decomposition-profile-bridges> a owl:Ontology ;
              rdfs:label "Salmon Domain Ontology Module 09: RDA Neville decomposition profile bridges"@en ;
              rdfs:comment "Profile-layer bridge concepts from Neville juvenile salmon decomposition materials. This working pilot module captures entity/observation/statistical-concept vocabulary and maps it conservatively to shared salmon-domain anchors."@en ;
              dcterms:source <https://docs.google.com/document/d/1myb-EsbtiJS7-x5wyuzMT9anrQyFC6zELy-WwykChRE/edit> ;
              dcterms:source <https://drive.google.com/drive/folders/1lM-qrgRib_vob-YEYzpqYqGCG_xBwo1V> ;
              dcterms:source <https://docs.google.com/spreadsheets/d/10Bd7bhTJvOOr-V1wK6YyAj9A4PvxKKpumEvcyIobBlw/edit> .
            """
        ).lstrip(),
    },
    {
        "output": MODULE_DIR / "08-rda-case-study-profile-bridges.ttl",
        "fragments": [
            FRAGMENTS_DIR / "08-rda-hakai-method-scheme.ttl",
            FRAGMENTS_DIR / "08-rda-hakai-measurement-methods.ttl",
        ],
        "header": dedent(
            """
            @prefix smn: <https://w3id.org/smn/> .
            @prefix hakai: <https://w3id.org/smn/profile/hakai/> .
            @prefix rda: <https://w3id.org/smn/profile/rda-case-study/> .
            @prefix skos: <http://www.w3.org/2004/02/skos/core#> .
            @prefix owl: <http://www.w3.org/2002/07/owl#> .
            @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
            @prefix prov: <http://www.w3.org/ns/prov#> .
            @prefix dcterms: <http://purl.org/dc/terms/> .

            # Auto-generated. Do NOT edit directly.
            # Edit fragments under ontology/case-studies/rda-juvenile-condition/ and
            # regenerate with: python3 scripts/build_rda_case_study_modules.py

            <https://w3id.org/smn/modules/08-rda-case-study-profile-bridges> a owl:Ontology ;
              rdfs:label "Salmon Domain Ontology Module 08: RDA case-study profile bridges"@en ;
              rdfs:comment "Profile-layer bridge concepts from the RDA juvenile salmon condition case-study graph. This is a working pilot module: it captures source vocabulary terms and maps them to shared salmon-domain semantics without promoting profile terms into shared core unless adoption criteria are met."@en ;
              dcterms:source <https://drive.google.com/file/d/1-WPKX6XwDiyLGZGT-bcF36N4ankpNi1o/view> ;
              dcterms:source <https://docs.google.com/document/d/1myb-EsbtiJS7-x5wyuzMT9anrQyFC6zELy-WwykChRE/edit> .
            """
        ).lstrip(),
    },
]


def main() -> None:
    for spec in MODULE_SPECS:
        output_path = spec["output"]
        lines = [spec["header"].rstrip()]

        for fragment in spec["fragments"]:
            fragment_text = fragment.read_text().strip()
            if not fragment_text:
                continue
            lines.append(f"# --- begin {fragment.relative_to(ROOT)} ---")
            lines.append(fragment_text)
            lines.append(f"# --- end {fragment.relative_to(ROOT)} ---")
            lines.append("")

        output_path.write_text("\n".join(lines).strip() + "\n")


if __name__ == "__main__":
    main()
