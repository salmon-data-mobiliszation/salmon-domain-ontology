#!/usr/bin/env python3
"""Verify WIDOCO HTML exposes stable #/Term anchors for documented smn: terms."""

from __future__ import annotations

import re
from pathlib import Path

TERM_REF_PATTERN = re.compile(r'title="https://w3id\.org/smn/([A-Za-z0-9._-]+)"')
PAGES = ("docs/index.html", "docs/index-en.html")


def verify_page(path: Path) -> tuple[int, list[str]]:
    html = path.read_text(encoding="utf-8")
    terms = sorted(set(TERM_REF_PATTERN.findall(html)))
    missing = [term for term in terms if f'id="/{term}"' not in html]
    return len(terms), missing



def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = []

    for rel in PAGES:
        path = root / rel
        count, missing = verify_page(path)
        if missing:
            failures.append((rel, count, missing))
        else:
            print(f"OK {rel}: {count} documented smn terms expose stable #/Term anchors")

    if failures:
        for rel, count, missing in failures:
            sample = ", ".join(missing[:10])
            print(
                f"FAIL {rel}: {len(missing)} of {count} documented smn terms are missing HTML anchors: {sample}"
            )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
