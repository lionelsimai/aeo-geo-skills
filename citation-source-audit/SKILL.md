---
name: citation-source-audit
description: |
  Audit which sources AI engines cite for a category's prompts, and what makes those sources liftable.
  TRIGGERS - Use when user needs help with citation sources / what do AI engines cite / source audit tasks.
category: AEO/GEO Strategy & Audits
version: 1.0
---
# Citation Source Audit

## What this skill does

Studies the cited sources themselves across a prompt set: source types, page structures, and the properties (answer-first openings, standalone stats, FAQ blocks, freshness) that make engines lift them.

Category: **AEO/GEO Strategy & Audits** — Know where the brand stands in AI answers before spending anything: audits, baselines, share of voice and roadmaps.

## Inputs

- Saved audit answers with citations for 10-20 prompts
- Access to open the cited pages

## Workflow

1. **Inventory the sources** — Every cited URL, deduplicated, with engine and prompt counts.
2. **Classify by type** — Owned brand pages, roundups, trade press, directories, reference, community/forum, video transcripts, government/edu.
3. **Open the top sources** — For the 10 most-cited pages, record structure: answer in first 100 words? standalone numbers? FAQ? named author? publish/update date?
4. **Extract the pattern** — Write the shared properties as a checklist — this becomes the house style for citable content.
5. **Gap the owned site** — Compare the entity's pages against the pattern and list the structural gaps to close.

## Output

A source inventory + a citable-structure checklist derived from evidence, plus the owned site's structural gaps.

## Measurement

Repeat each quarter — cited-source sets drift. The checklist is only valid while it matches what engines currently lift.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Frequency is not endorsement. A source can be cited because it ranks in classic search; the audit separates 'cited' from 'worth imitating'.

## Fictional example

Fictional: across 18 prompts, engines cite 41 sources; the top 8 all open with a direct answer and a dated stats table. The client's essay-style pages cite zero times.
