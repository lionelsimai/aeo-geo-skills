---
name: citation-driven-content-gap-planner
description: |
  Plan new content from citation evidence: the prompts where engines cite others, the sub-questions with no asset, the formats that win.
  TRIGGERS - Use when user needs help with content gap planning / citation gaps to content / what content to create tasks.
category: GEO Content Ops & Workflows
version: 1.0
---
# Citation-Driven Content Gap Planner

## What this skill does

The planning counterpart to the editorial calendar: merges the citation-source audit, fan-out maps and competitor gaps into a prioritised list of content to create — each item justified by observed citation behaviour, not by topic enthusiasm.

Category: **GEO Content Ops & Workflows** — Run AEO as an operation: freshness systems, briefs, calendars, QA gates and agency delivery — the workflows that keep citations compounding.

## Inputs

- Citation source audit + competitor citation gap analysis
- AI Mode fan-out maps
- Current asset inventory

## Workflow

1. **Merge the gap sources** — One list: prompts citing competitors only, fan-out sub-queries with no asset, formats missing for owned topics. Dedupe ruthlessly.
2. **Score by winnability** — Per gap: prompt value (tier), evidence a page can win it (format pattern exists?), effort. High value x winnable first.
3. **Check fact readiness** — Can we actually evidence this piece (data, expertise, access)? Gaps we cannot evidence honestly are parked, not assigned.
4. **Write the plan as briefs** — Top gaps become aeo-content-brief-builder briefs directly — planning that stops at a list tends to stay a list.
5. **Re-plan from the log quarterly** — After each citation-log review, re-score: did created pieces win? Are new gaps visible? The planner is a loop, not an event.

## Output

A prioritised gap plan with the top items converted into content briefs.

## Measurement

Gap-plan conversion: briefs shipped per quarter; citations earned by gap-planned pieces vs unplanned pieces (the log decides).

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not plan content for prompts the entity has no business winning. Ambition filtered by evidence is the entire discipline.

## Fictional example

Fictional: planning surfaces that engines cite comparison pages for 5 prompts where the entity has none — comparisons become the quarter's top briefs.
