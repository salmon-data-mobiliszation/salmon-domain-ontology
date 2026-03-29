#!/usr/bin/env python3
"""Update version metadata in ontology/salmon-domain-ontology.ttl."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "ontology" / "salmon-domain-ontology.ttl"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
VERSION_INFO = re.compile(r'owl:versionInfo "([^"]+)"')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", required=True, help="New ontology version, e.g. 0.0.1")
    parser.add_argument(
        "--prior-version",
        help="Previous ontology version. Defaults to current versionInfo or latest docs/releases snapshot.",
    )
    parser.add_argument(
        "--modified",
        default=dt.date.today().isoformat(),
        help="Modification date in YYYY-MM-DD format (default: today).",
    )
    return parser.parse_args()


def require_semver(value: str, label: str) -> str:
    if not SEMVER.match(value):
        raise SystemExit(f"{label} must be SemVer-like X.Y.Z, got: {value}")
    return value


def infer_prior_version(text: str) -> str | None:
    current = VERSION_INFO.search(text)
    if current:
        return current.group(1)

    release_root = ROOT / "docs" / "releases"
    if not release_root.exists():
        return None

    versions = sorted(
        path.name for path in release_root.iterdir() if path.is_dir() and SEMVER.match(path.name)
    )
    return versions[-1] if versions else None


def update_prefix_block(lines: list[str]) -> list[str]:
    prefix_end = 0
    while prefix_end < len(lines) and lines[prefix_end].startswith("@prefix "):
        prefix_end += 1

    body_start = prefix_end
    while body_start < len(lines) and lines[body_start] == "":
        body_start += 1

    existing = {}
    extra_prefixes = []
    for line in lines[:prefix_end]:
        parts = line.split()
        if len(parts) < 3:
            extra_prefixes.append(line)
            continue
        prefix = parts[1].rstrip(":")
        existing[prefix] = line
        if prefix not in {"dcterms", "owl", "rdfs", "xsd"}:
            extra_prefixes.append(line)

    ordered = [
        existing.get("dcterms", "@prefix dcterms: <http://purl.org/dc/terms/> ."),
        existing.get("owl", "@prefix owl: <http://www.w3.org/2002/07/owl#> ."),
        existing.get("rdfs", "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> ."),
        existing.get("xsd", "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> ."),
    ]

    return ordered + extra_prefixes + [""] + lines[body_start:]


def update_ontology_block(lines: list[str], version: str, prior_version: str, modified: str) -> list[str]:
    start = next(
        (index for index, line in enumerate(lines) if line.startswith("<https://w3id.org/smn> a owl:Ontology ;")),
        None,
    )
    if start is None:
        raise SystemExit(f"Could not locate ontology declaration in {SOURCE}")

    end = start
    while end < len(lines) and not lines[end].rstrip().endswith("."):
        end += 1
    if end >= len(lines):
        raise SystemExit(f"Could not locate the end of the ontology declaration in {SOURCE}")

    block = lines[start : end + 1]
    filtered = [
        line
        for line in block
        if not line.strip().startswith("dcterms:modified ")
        and not line.strip().startswith("owl:versionIRI ")
        and not line.strip().startswith("owl:priorVersion ")
        and not line.strip().startswith("owl:versionInfo ")
    ]

    insert_at = next(
        (
            index + 1
            for index, line in enumerate(filtered)
            if line.strip().startswith("rdfs:comment ")
        ),
        1,
    )
    filtered[insert_at:insert_at] = [
        f'  dcterms:modified "{modified}"^^xsd:date ;',
        f"  owl:versionIRI <https://w3id.org/smn/{version}> ;",
        f"  owl:priorVersion <https://w3id.org/smn/{prior_version}> ;",
        f'  owl:versionInfo "{version}" ;',
    ]

    return lines[:start] + filtered + lines[end + 1 :]


def main() -> int:
    args = parse_args()
    version = require_semver(args.version, "version")
    prior_version = require_semver(args.prior_version, "prior-version") if args.prior_version else None

    text = SOURCE.read_text(encoding="utf-8")
    inferred_prior = infer_prior_version(text)
    if prior_version is None:
        if inferred_prior is None:
            raise SystemExit("Could not infer prior version; pass --prior-version explicitly.")
        prior_version = require_semver(inferred_prior, "prior-version")

    if not re.match(r"^\d{4}-\d{2}-\d{2}$", args.modified):
        raise SystemExit(f"modified must be YYYY-MM-DD, got: {args.modified}")

    lines = text.splitlines()
    lines = update_prefix_block(lines)
    lines = update_ontology_block(lines, version=version, prior_version=prior_version, modified=args.modified)
    SOURCE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(
        f"Updated root ontology metadata: version={version}, prior_version={prior_version}, modified={args.modified}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
