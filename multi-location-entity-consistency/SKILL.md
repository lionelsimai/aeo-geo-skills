---
name: multi-location-entity-consistency
description: |
  Keep many locations consistent without making them identical: brand facts frozen centrally, local facts owned locally.
  TRIGGERS - Use when user needs help with multi-location consistency / franchise entity / branch listings consistency tasks.
category: Local & Vertical AEO
version: 1.0
---
# Multi-Location Entity Consistency

## What this skill does

For chains, franchises and multi-branch firms: a two-tier fact system — brand-level facts (name, descriptor, offers) frozen centrally and identical everywhere; location-level facts (address, hours, team, areas) owned and verified per branch — plus a sweep routine that scales past five locations.

Category: **Local & Vertical AEO** — The five layers applied per vertical: local businesses, B2B SaaS, ecommerce, professional services and more — same discipline, different surfaces.

## Inputs

- Brand fact sheet + per-location fact sheets
- The full location/listing inventory (owned, franchisee-run, scraped)

## Workflow

1. **Split the fact tiers in writing** — Tier B (brand): changes only centrally. Tier L (local): branch-owned fields listed explicitly. Most multi-location mess is tier confusion.
2. **Build the master register** — Every location x every surface in one register, with an owner per branch who answers for its rows.
3. **Sweep by sampling + automation** — All Tier B fields checked everywhere; Tier L fields sampled deeply per branch on rotation, fully once a year.
4. **Fix through the owners** — Corrections issued to branch owners with exact replacement text and a deadline; central team verifies, because issued ≠ done.
5. **Onboard new locations into the system** — A new branch launches with its register rows, canonical copy pack and first sweep date — never as a free-form local effort.

## Output

A multi-location register (tiers, owners, sweep status) + the copy pack per tier.

## Measurement

Tier B consistency 100% across locations; Tier L factual-variant count per sweep trending down; new locations registered on launch day.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not force identical local pages. Branches with genuinely different services/hours must differ in Tier L facts — false uniformity is its own inconsistency.

## Fictional example

Fictional: a 12-branch tuition chain finds 4 branches using an old brand descriptor and 2 with wrong hours; the tier system fixes the brand centrally and hours locally in one sweep.
