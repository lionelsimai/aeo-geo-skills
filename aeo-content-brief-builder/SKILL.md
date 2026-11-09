---
name: aeo-content-brief-builder
description: |
  Write content briefs that make any writer produce citable work: target prompt, answer-first structure, allowed facts and proof requirements.
  TRIGGERS - Use when user needs help with AEO brief / content brief for citations / writer brief tasks.
category: GEO Content Ops & Workflows
version: 1.0
---
# AEO Content Brief Builder

## What this skill does

The brief template that scales the citable-content layer beyond one author: target prompt and tier, the direct answer the piece must open with, the fact allow-list (stats/facts the writer may use, with sources), structure, FAQ requirements and the QA gate it must pass.

Category: **GEO Content Ops & Workflows** — Run AEO as an operation: freshness systems, briefs, calendars, QA gates and agency delivery — the workflows that keep citations compounding.

## Inputs

- Tier map entry for the piece
- Stat bank + fact sheet (the allow-list source)
- The house formats (answer-first article, guide, definition, comparison)

## Workflow

1. **State the target and the answer** — Brief line one: the prompt. Line two: the direct answer in one sentence (the writer expands it; they do not invent a different one).
2. **Attach the allow-list** — Every fact/stat the piece may use, with its source. Anything not on the list needs approval before drafting, not forgiveness after.
3. **Specify the structure** — Format type, H2 questions, FAQ count, stat-unit placements, internal links to hub/flagship.
4. **Set the proof bar** — Examples and claims the piece needs (a real case, a dated figure) and what to do if they cannot be sourced: flag, never fill.
5. **Name the QA gate** — The piece ships only after aeo-qa-review-checklist passes, including fact-vs-allow-list diffing.

## Output

A complete brief (prompt, answer, allow-list, structure, proof bar, QA gate) ready to hand to a writer or agent.

## Measurement

Briefed pieces passing QA first time (% rising over time); zero published facts outside allow-lists.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: A brief that says 'write engaging content about X' is not an AEO brief. If the answer and allow-list are missing, the brief is not done.

## Fictional example

Fictional: a brief for 'AI agent costs for SMEs' carries the answer, 6 allowed stats with sources, and a note that implementation pricing must be ranged, not invented.
