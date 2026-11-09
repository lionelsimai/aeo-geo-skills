---
name: corroboration-gap-mapper
description: |
  Map which corroboration types an entity is missing — roundups, press, podcasts, reviews, directories — against what its category's answers reward.
  TRIGGERS - Use when user needs help with corroboration gaps / third-party proof gaps / off-site audit tasks.
category: Third-Party Corroboration
version: 1.0
---
# Corroboration Gap Mapper

## What this skill does

Builds the corroboration balance sheet: for each type (editorial roundups, trade press quotes, podcast pages, speaker pages, review platforms, quality directories, book/author surfaces), does the entity have current, descriptor-correct presence — and which missing type is costing the most citations?

Category: **Third-Party Corroboration** — Layer 3 of the strategy: independent sources describing the entity the same way — the layer that actually moves prize queries.

## Inputs

- Citation-source audit + competitor citation gap analysis
- The entity's current off-site presence (assemble honestly)

## Workflow

1. **Score presence per type** — Present-and-current / present-but-stale / absent, per type, with the best example URL as evidence for each.
2. **Weight by category behaviour** — From the source audit: which types do engines actually cite for this category's prompts? Weight the map by that, not by generic SEO habit.
3. **Cost the gaps** — For each absent type: effort to earn, time to effect, and which tier of queries it unlocks.
4. **Pick the quarter's two types** — Corroboration compounds slowly; two types worked properly beat seven touched lightly.
5. **Re-map quarterly** — Presence decays (bios go stale, listings lapse). The map is a living register, re-scored each quarter.

## Output

A corroboration map (type x status x evidence) and the quarter's two priority types with owners.

## Measurement

Priority types move from absent/stale to present-and-current per quarter; citation share from third-party sources rises in the monthly tracker.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Presence with the WRONG descriptor counts as stale, not present. A podcast page with a 2021 bio is a liability wearing an asset's clothes.

## Fictional example

Fictional: a consultant's map shows strong speaker pages, zero review presence and stale roundups; the quarter's work is reviews + roundup refresh, not more speaking.
