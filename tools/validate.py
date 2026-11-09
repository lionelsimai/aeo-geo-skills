#!/usr/bin/env python3
"""Validate the AEO & GEO Skills collection. Stdlib only.

    python3 tools/validate.py

Checks: exactly 100 skill folders, unique slugs, folder name == frontmatter
name, 100% frontmatter compliance (name, description with TRIGGERS line,
category in the 10-category set, version), and catalog.json / CATALOG.md
matching the folders on disk. Exit 1 on any failure.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_CATS = {
    "AEO/GEO Strategy & Audits", "Entity & Knowledge Foundation",
    "Citable Content", "Structured Data & Technical",
    "Third-Party Corroboration", "Platform Surfaces",
    "Brand & Expert Positioning", "Monitoring & Measurement",
    "Local & Vertical AEO", "GEO Content Ops & Workflows",
}

def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
        elif fm.get("_last") == "description":
            fm["description"] = fm.get("description", "") + " " + line.strip()
        if m:
            fm["_last"] = m.group(1)
    return fm

def main():
    errors, slugs, cats_seen = [], [], {}
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name, "SKILL.md")
        if not os.path.isfile(path):
            continue
        slugs.append(name)
        text = open(path, errors="ignore").read()
        fm = parse_frontmatter(text)
        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name {fm.get('name')!r} != folder")
        if "TRIGGERS" not in fm.get("description", ""):
            errors.append(f"{name}: description missing TRIGGERS line")
        if fm.get("category") not in EXPECTED_CATS:
            errors.append(f"{name}: bad category {fm.get('category')!r}")
        else:
            cats_seen[fm["category"]] = cats_seen.get(fm["category"], 0) + 1
        if not fm.get("version"):
            errors.append(f"{name}: missing version")
        for section in ("## Workflow", "## Measurement", "## Guardrails"):
            if section not in text:
                errors.append(f"{name}: missing section {section}")
    if len(slugs) != 100:
        errors.append(f"expected 100 skills, found {len(slugs)}")
    if len(set(slugs)) != len(slugs):
        errors.append("duplicate slugs")
    for c in EXPECTED_CATS:
        if cats_seen.get(c) != 10:
            errors.append(f"category {c!r} has {cats_seen.get(c, 0)} skills, expected 10")
    cat = json.load(open(os.path.join(ROOT, "catalog.json")))
    if cat.get("count") != len(slugs):
        errors.append(f"catalog count {cat.get('count')} != {len(slugs)}")
    cat_slugs = sorted(s["slug"] for c in cat["categories"] for s in c["skills"])
    if cat_slugs != sorted(slugs):
        errors.append("catalog slugs do not match folders")
    if not os.path.isfile(os.path.join(ROOT, "CATALOG.md")):
        errors.append("CATALOG.md missing")
    compliant = len(slugs) - len({e.split(':')[0] for e in errors if '/' not in e.split(':')[0]})
    print(f"skills: {len(slugs)} | categories: {len(cats_seen)} x10 | catalog count: {cat.get('count')}")
    if errors:
        print("FAILURES:")
        for e in errors:
            print(" -", e)
        return 1
    print("ALL CHECKS PASSED — 100 unique slugs, 100% frontmatter compliance, catalog matches")
    return 0

if __name__ == "__main__":
    sys.exit(main())
