---
name: directory-listing-quality-audit
description: |
  Audit directory and listing presence: keep the legitimate, accurate listings; reject the spam farms.
  TRIGGERS - Use when user needs help with directory listings / listing audit / business directories tasks.
category: Third-Party Corroboration
version: 1.0
---
# Directory Listing Quality Audit

## What this skill does

Reviews an entity's directory footprint by quality tier: authoritative industry directories and platforms (keep, complete, correct) vs mass-submission spam farms (avoid or remove). Completeness and fact accuracy are scored per kept listing.

Category: **Third-Party Corroboration** — Layer 3 of the strategy: independent sources describing the entity the same way — the layer that actually moves prize queries.

## Inputs

- Current listing inventory (search the entity name + category)
- Canonical fact sheet

## Workflow

1. **Inventory what exists** — Every directory/profile page naming the entity, including ones nobody created deliberately (scraped listings count).
2. **Tier by legitimacy** — Tier 1: industry bodies, major platforms, curated directories. Tier 2: general business directories with real traffic. Tier 3: submission farms — mark do-not-touch.
3. **Score Tier 1-2 accuracy** — Per listing: name, descriptor/category, facts, links, logo — diff against the fact sheet.
4. **Fix and complete** — Correct facts, complete empty fields with canonical copy, claim unclaimed profiles where the platform allows.
5. **Delist the harmful** — Where a spam listing carries wrong facts, request correction or removal; do not create more of them.

## Output

A tiered listing register with accuracy scores and completed fixes.

## Measurement

Tier 1 listings: 100% present and accurate. Tier 3: zero new submissions, tracked as a policy metric.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Volume is not the goal. 200 junk listings dilute and contradict; 15 accurate authoritative ones corroborate.

## Fictional example

Fictional: an audit finds 43 listings: 9 Tier 1 (3 with an old address), 12 Tier 2, 22 scraped spam copies — effort goes to the 9, corrections requested on the worst spam facts.
