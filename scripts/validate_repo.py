#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_readme_version(readme: str) -> str | None:
    m = re.search(r"Latest doctrinal release:\s*(v\d+\.\d+\.\d+)", readme)
    return m.group(1) if m else None


def extract_changelog_version(changelog: str) -> str | None:
    m = re.search(r"^##\s+(v\d+\.\d+\.\d+)\s*$", changelog, flags=re.MULTILINE)
    return m.group(1) if m else None


def extract_citation_version(cff: str) -> str | None:
    # Prefer top-level version, fall back to preferred-citation if needed.
    m = re.search(r"^version:\s*\"?(v\d+\.\d+\.\d+)\"?\s*$", cff, flags=re.MULTILINE)
    if m:
        return m.group(1)
    m2 = re.search(r"^\s+version:\s*\"?(v\d+\.\d+\.\d+)\"?\s*$", cff, flags=re.MULTILINE)
    return m2.group(1) if m2 else None


def extract_citation_type(cff: str) -> str | None:
    m = re.search(r"^type:\s*\"?([a-zA-Z_-]+)\"?\s*$", cff, flags=re.MULTILINE)
    return m.group(1) if m else None


def json_load(path: Path) -> object:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def find_repo_version_from_jsonld(obj: dict) -> str | None:
    graph = obj.get("@graph", [])
    for node in graph:
        if isinstance(node, dict) and node.get("@id", "").endswith("#repository"):
            v = node.get("version")
            if isinstance(v, str) and v.strip():
                # JSON-LD stores it without a leading 'v'
                return "v" + v.strip().lstrip("v")
    return None


def markdown_fences_balanced(md_text: str) -> bool:
    in_fence = False
    for line in md_text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
    return not in_fence


def iter_markdown_files(root: Path):
    for p in root.rglob("*.md"):
        # Keep validation strict: include all .md files.
        yield p


def iter_json_like_files(root: Path):
    # Strict on JSON/JSON-LD artifacts.
    yield root / "ssa-e-a2-dual-web-doctrine.jsonld"
    yield root / "links.json"
    for p in (root / "schema-templates").glob("*.jsonld"):
        yield p


def check_internal_links(md_path: Path, md_text: str, errors: list[str]) -> None:
    # Very small, conservative checker for local links only.
    # We skip anything that is external, an anchor-only link, or mailto.
    pattern = re.compile(r"\]\(([^)]+)\)")
    for raw_target in pattern.findall(md_text):
        target = raw_target.strip()
        if not target:
            continue
        # Strip surrounding angle brackets
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()

        if target.startswith("#"):
            continue
        if target.startswith("mailto:"):
            continue
        if "://" in target:
            continue

        # Remove querystring and anchor
        target = target.split("#", 1)[0].split("?", 1)[0].strip()
        if not target:
            continue

        # Ignore non-file pseudo links
        if target.startswith("javascript:"):
            continue

        # Root-relative -> interpret as repo-root relative
        if target.startswith("/"):
            candidate = (ROOT / target.lstrip("/")).resolve()
        else:
            candidate = (md_path.parent / target).resolve()

        if not candidate.exists():
            errors.append(f"[link] {md_path.relative_to(ROOT)} -> missing target: {raw_target}")


def main() -> int:
    errors: list[str] = []

    # 1) JSON / JSON-LD syntax
    for p in iter_json_like_files(ROOT):
        if not p.exists():
            errors.append(f"[json] missing file: {p.relative_to(ROOT)}")
            continue
        try:
            json_load(p)
        except Exception as e:
            errors.append(f"[json] invalid JSON: {p.relative_to(ROOT)} ({e})")

    # 2) Version consistency
    readme_path = ROOT / "README.md"
    citation_path = ROOT / "CITATION.cff"
    changelog_path = ROOT / "CHANGELOG.md"
    links_path = ROOT / "links.json"
    jsonld_path = ROOT / "ssa-e-a2-dual-web-doctrine.jsonld"

    readme_v = extract_readme_version(read_text(readme_path)) if readme_path.exists() else None
    cff_text = read_text(citation_path) if citation_path.exists() else ""
    citation_v = extract_citation_version(cff_text) if cff_text else None
    citation_type = extract_citation_type(cff_text) if cff_text else None
    changelog_v = extract_changelog_version(read_text(changelog_path)) if changelog_path.exists() else None

    links_v = None
    if links_path.exists():
        try:
            links = json_load(links_path)
            if isinstance(links, dict):
                rel = links.get("releases", {})
                if isinstance(rel, dict):
                    lt = rel.get("latest_tag")
                    if isinstance(lt, str) and lt.strip():
                        links_v = lt.strip()
        except Exception as e:
            errors.append(f"[json] cannot read links.json for version: {e}")

    jsonld_v = None
    if jsonld_path.exists():
        try:
            obj = json_load(jsonld_path)
            if isinstance(obj, dict):
                jsonld_v = find_repo_version_from_jsonld(obj)
        except Exception as e:
            errors.append(f"[json] cannot read doctrine jsonld for version: {e}")

    versions = {
        "README": readme_v,
        "CITATION": citation_v,
        "CHANGELOG": changelog_v,
        "links.json": links_v,
        "doctrine JSON-LD": jsonld_v,
    }

    missing = [k for k, v in versions.items() if not v]
    if missing:
        errors.append("[version] missing version in: " + ", ".join(missing))

    # If all present, ensure they match
    present = [v for v in versions.values() if v]
    if present and len(set(present)) != 1:
        errors.append("[version] mismatch: " + ", ".join(f"{k}={v}" for k, v in versions.items()))

    # Enforce doctrinal citation posture
    if citation_type and citation_type.strip() != "dataset":
        errors.append(f"[citation] expected type: dataset (got: {citation_type})")

    # 3) Markdown fence balance + internal links
    for md_path in iter_markdown_files(ROOT):
        txt = read_text(md_path)

        if not markdown_fences_balanced(txt):
            errors.append(f"[md] unbalanced code fences: {md_path.relative_to(ROOT)}")

        check_internal_links(md_path, txt, errors)

    # 4) Specific guard: no duplicate traceability section in Q-Layer
    q_layer_path = ROOT / "layers" / "q-layer.md"
    if q_layer_path.exists():
        q_txt = read_text(q_layer_path)
        count = q_txt.count("## Traceability of non-actions")
        if count != 1:
            errors.append(f"[q-layer] expected 1 'Traceability of non-actions' section, found {count}")

    if errors:
        print("Validation failed:")
        for e in errors:
            print(" - " + e)
        return 1

    print("Validation OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
