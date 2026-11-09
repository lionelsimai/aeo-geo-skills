---
name: platform-priority-planner
description: |
  Decide where AEO effort goes per platform: rank engines and surfaces by audience, effort and observed citation behaviour.
  TRIGGERS - Use when user needs help with platform priorities / where to focus AEO / engine effort split tasks.
category: Platform Surfaces
version: 1.0
---
# Platform Priority Planner

## What this skill does

Turns the landscape scan and per-engine evidence into an effort plan: which engines get active tactics, which get monitoring only, and which owned/third-party surfaces feed them — with the reasoning written down so the split survives team changes.

Category: **Platform Surfaces** — Layer 4 of the strategy: each engine retrieves and cites differently — per-engine tactics grounded in observed citation behaviour.

## Inputs

- Answer-engine landscape scan
- Per-engine slices of the latest audit
- Programme capacity (hours/people per month)

## Workflow

1. **Rank by audience x evidence** — Score each engine: does the audience use it, and does the audit show winnable citation behaviour for this category?
2. **Assign tiers of effort** — Tier A engines: active tactics + monthly tracking. Tier B: tracking only. Tier C: ignore for now, revisit at the next scan.
3. **Map surfaces to engines** — Each Tier A engine gets its feeding surfaces named (e.g. Bing index + IndexNow for Copilot; roundups for ChatGPT) so work items are concrete.
4. **Cap the plan at capacity** — An effort split the team cannot execute is fiction. Cut Tier B tactics before diluting Tier A.
5. **Review quarterly** — Engine behaviour and audience habits move; the planner re-runs with fresh audit slices each quarter.

## Output

A platform priority plan (engine tiers, feeding surfaces, effort split) with quarterly review dates.

## Measurement

Programme hours actually spent match the plan's split; Tier A engines show tracked movement before Tier B gets investment.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not let the loudest new engine launch rewrite the plan mid-quarter. Evidence from your own audit outranks launch hype.

## Fictional example

Fictional: a firm sets Google surfaces + ChatGPT as Tier A (audience), Perplexity Tier B, and parks a new entrant at Tier C pending its next scan.
