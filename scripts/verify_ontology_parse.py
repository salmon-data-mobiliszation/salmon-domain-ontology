#!/usr/bin/env python3
"""Parse all ontology Turtle files and fail fast on syntax errors."""

from __future__ import annotations

from pathlib import Path

from rdflib import Graph


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for path in sorted((root / "ontology").rglob("*.ttl")):
        Graph().parse(path, format="turtle")
        print(f"OK {path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
