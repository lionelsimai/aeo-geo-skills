#!/usr/bin/env python3
"""Generate the AEO & GEO Skills collection from the taxonomy in data.py.
Each skill folder gets a substantive SKILL.md in the collection frontmatter
standard (name / description with TRIGGERS / category / version)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import CATS, GLOBAL_GUARDRAILS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def render(cat, s):
    steps = "\n".join(f"{i+1}. **{t}** — {d}" for i, (t, d) in enumerate(s["steps"]))
    return f"""---
name: {s['slug']}
description: |
  {s['desc']}
  TRIGGERS - Use when user needs help with {s['trigger']} tasks.
category: {cat['name']}
version: 1.0
---
# {s['title']}

## What this skill does

{s['focus']}

Category: **{cat['name']}** — {cat['blurb']}

## Inputs

{s['inputs']}

## Workflow

{steps}

## Output

{s['output']}

## Measurement

{s['metric']}

## Guardrails

{GLOBAL_GUARDRAILS}
- Skill-specific: {s['pitfall']}

## Fictional example

{s['example']}
"""

def main():
    total = 0
    catalog = {"name": "aeo-geo-skills", "version": "1.0.0",
               "author": "Lionel Sim", "license": "MIT", "count": 0,
               "categories": []}
    for cat in CATS:
        entry = {"category": cat["name"], "skills": []}
        for s in cat["skills"]:
            d = os.path.join(ROOT, s["slug"])
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "SKILL.md"), "w") as fh:
                fh.write(render(cat, s))
            entry["skills"].append({"slug": s["slug"], "title": s["title"],
                                    "tool_kind": "skill",
                                    "description": s["desc"]})
            total += 1
        catalog["categories"].append(entry)
    catalog["count"] = total
    with open(os.path.join(ROOT, "catalog.json"), "w") as fh:
        json.dump(catalog, fh, indent=2)
    lines = ["# Catalogue — AEO & GEO Skills", "",
             f"{total} skills across {len(CATS)} categories. "
             "Every skill is a folder with a SKILL.md in the open Agent Skills format.", ""]
    for cat in CATS:
        lines += [f"## {cat['name']}", "", f"{cat['blurb']}", "",
                  "| Skill | What it does |", "|---|---|"]
        for s in cat["skills"]:
            lines.append(f"| [{s['slug']}]({s['slug']}/SKILL.md) | {s['desc']} |")
        lines.append("")
    with open(os.path.join(ROOT, "CATALOG.md"), "w") as fh:
        fh.write("\n".join(lines))
    print(f"generated {total} skills in {len(CATS)} categories")

if __name__ == "__main__":
    main()
