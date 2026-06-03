#!/usr/bin/env python3
"""Audit Markdown files for DCI-style retrieval readiness.

This script is intentionally heuristic. It flags issues for review; it does not prove a file is bad.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

VAGUE_HEADINGS = {
    "notes",
    "misc",
    "more",
    "stuff",
    "todo",
    "todos",
    "thoughts",
    "ideas",
    "other",
    "general",
    "details",
    "info",
    "information",
    "test",
    "tests",
}

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
PARAGRAPH_SPLIT_RE = re.compile(r"\n\s*\n")
WORD_RE = re.compile(r"[A-Za-z0-9_][A-Za-z0-9_\-]*")


def iter_markdown_paths(paths: Iterable[Path]) -> list[Path]:
    out: list[Path] = []
    for path in paths:
        if path.is_dir():
            out.extend(sorted(p for p in path.rglob("*.md") if p.is_file()))
        elif path.is_file() and path.suffix.lower() == ".md":
            out.append(path)
    return sorted(set(out))


def line_no_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, max(offset, 0)) + 1


def words(text: str) -> list[str]:
    return WORD_RE.findall(text)


def strip_fenced_code(text: str) -> str:
    """Replace fenced code blocks with blank lines while preserving line numbers."""
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def audit_file(path: Path) -> tuple[int, list[str]]:
    warnings: list[str] = []
    try:
        raw_text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raw_text = path.read_text(encoding="utf-8", errors="replace")

    text = strip_fenced_code(raw_text)
    lines = text.splitlines()
    first_25 = "\n".join(lines[:25]).lower()
    first_40 = "\n".join(lines[:40]).lower()

    if not any(line.startswith("# ") for line in lines[:10]):
        warnings.append("missing top-level '# Title' in first 10 lines")

    if "summary:" not in first_25:
        warnings.append("missing 'Summary:' near the top")

    if "keywords:" not in first_40:
        warnings.append("missing 'Keywords:' near the top")

    stale_words = ("archived", "superseded", "deprecated", "replaces", "supersedes")
    if "status:" not in first_40 and any(word in text.lower() for word in stale_words):
        warnings.append("stale/status language appears but no clear top-level 'Status:' marker was found")

    for i, line in enumerate(lines, start=1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        heading = match.group(2).strip().rstrip(":").lower()
        if heading in VAGUE_HEADINGS:
            warnings.append(f"line {i}: vague heading '{match.group(2)}'")
        if len(words(match.group(2))) < 2 and match.group(1) != "#":
            warnings.append(f"line {i}: short heading may be weak for retrieval: '{match.group(2)}'")

    heading_positions = [(m.start(), m.group(0)) for m in HEADING_RE.finditer(text)]
    for idx, (start, _heading_line) in enumerate(heading_positions):
        end = heading_positions[idx + 1][0] if idx + 1 < len(heading_positions) else len(text)
        section = text[start:end]
        count = len(words(section))
        if count > 650:
            warnings.append(
                f"line {line_no_for_offset(text, start)}: section over 650 words; split into more specific headings"
            )

    seen_offsets: set[int] = set()
    for para in PARAGRAPH_SPLIT_RE.split(text):
        stripped = para.strip()
        if not stripped:
            continue
        offset = text.find(para)
        if offset in seen_offsets:
            continue
        seen_offsets.add(offset)
        count = len(words(stripped))
        if count > 180:
            warnings.append(
                f"line {line_no_for_offset(text, offset)}: paragraph over 180 words; split for local verification"
            )
        if re.search(r"\b(this|that|it|they|these|those)\s+(must|should|will|is|are|was|were)\b", stripped, re.I):
            if not re.search(
                r"\b(Direct answer|Decision|Constraint|Expected|Evidence|Status|Definition|Dependency|Procedure|DCI|Direct Corpus Interaction)\b",
                stripped,
            ):
                warnings.append(
                    f"line {line_no_for_offset(text, offset)}: possible vague pronoun; make the entity explicit"
                )

    labels = (
        "direct answer:",
        "decision:",
        "constraint:",
        "expected:",
        "evidence:",
        "definition:",
        "dependency:",
        "procedure:",
        "exception:",
        "related terms:",
    )
    if not any(label in text.lower() for label in labels):
        warnings.append("no citable labels found; consider Direct answer/Decision/Constraint/Evidence/Expected labels")

    keyword_line = next((line for line in lines if line.lower().startswith("keywords:")), "")
    if keyword_line:
        kw_terms = [term.strip() for term in keyword_line.split(":", 1)[1].split(";") if term.strip()]
        if len(kw_terms) > 20:
            warnings.append("keyword list has more than 20 terms; trim to high-signal anchors")
        if len(kw_terms) < 3:
            warnings.append("keyword list has fewer than 3 terms; add aliases or likely search phrases")

    return len(warnings), warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Markdown files for DCI-style retrieval readiness.")
    parser.add_argument("paths", nargs="+", help="Markdown files or directories to audit")
    args = parser.parse_args()

    paths = iter_markdown_paths(Path(p) for p in args.paths)
    if not paths:
        print("No Markdown files found.", file=sys.stderr)
        return 2

    total_warnings = 0
    for path in paths:
        count, warnings = audit_file(path)
        total_warnings += count
        rel = path.as_posix()
        if count == 0:
            print(f"PASS {rel}")
        else:
            print(f"WARN {rel} ({count})")
            for warning in warnings:
                print(f"  - {warning}")

    return 1 if total_warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
