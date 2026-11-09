---
name: ai-share-of-voice
description: |
  Measure a brand's share of mentions and citations against competitors across a fixed set of AI-answer prompts.
  TRIGGERS - Use when user needs help with AI share of voice / competitor visibility share / SOV in AI answers tasks.
category: AEO/GEO Strategy & Audits
version: 1.0
---
# AI Share of Voice

## What this skill does

Turns raw audit answers into a share-of-voice table: for each prompt, which entities are named and cited, and what share of total mentions each competitor holds per engine and overall.

Category: **AEO/GEO Strategy & Audits** — Know where the brand stands in AI answers before spending anything: audits, baselines, share of voice and roadmaps.

## Inputs

- A completed audit run (raw answers saved)
- The competitor set (3-6 entities)
- The prompt set used

## Workflow

1. **Extract mentions** — From each saved answer, list every entity named, in order, and every source cited.
2. **Normalise names** — Merge variants of the same entity (abbreviations, old names) under one canonical name before counting.
3. **Compute shares** — Share = entity mentions / total entity mentions, per engine and overall. Compute citation share separately from mention share.
4. **Split by tier** — Report Tier 1 and Tier 2 shares separately; a blended number hides where the fight actually is.
5. **Name the gap owners** — For prompts where a competitor dominates, record which of their sources engines cite — those sources are the pitch targets.

## Output

A share-of-voice table (entity x engine, mentions and citations) plus the top competitor sources to target.

## Measurement

Track share monthly on the frozen prompt set. A rising mention share with flat citation share means engines name you from others' pages — a corroboration problem, not a content problem.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Small prompt sets make shares jump wildly. Report the prompt count next to every percentage.

## Fictional example

Fictional: three accounting firms share 40 tracked mentions 55/30/15 across engines. The 15% firm's gap traces to two roundup articles it is absent from.
