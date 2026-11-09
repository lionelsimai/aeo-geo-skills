---
name: content-freshness-refresh-audit
description: |
  Audit citable content for staleness: facts, stats, screenshots and claims that aged out, ranked by citation value at risk.
  TRIGGERS - Use when user needs help with content freshness / refresh audit / stale content audit tasks.
category: GEO Content Ops & Workflows
version: 1.0
---
# Content Freshness Refresh Audit

## What this skill does

Inventories the entity's citable pages and scores each for freshness risk: dated statistics past their period, superseded product/facts, old screenshots, dead links — prioritised by which pages currently earn citations, because a stale cited page is actively spreading old facts.

Category: **GEO Content Ops & Workflows** — Run AEO as an operation: freshness systems, briefs, calendars, QA gates and agency delivery — the workflows that keep citations compounding.

## Inputs

- Citable asset inventory + citation log (what earns citations now)
- The stat bank expiry list

## Workflow

1. **Rank by citations at risk** — Currently-cited pages first. A stale uncited page is a chore; a stale cited page is a liability.
2. **Check fact-by-fact on top pages** — Every dated claim verified against its source as of today. Mark: still true / needs new figure / no longer true.
3. **Decide per page** — Refresh (new data, honest new date), annotate (historical piece labelled as of its date), or retire (redirect to the current asset).
4. **Refresh with substance** — A refresh adds the new figure/fact and updates methodology notes — never just a new date on old content.
5. **Set the cycle** — Each citable page gets a review date by type (data pages quarterly, guides annually). The audit recurs by calendar, not by crisis.

## Output

A freshness register (page, risk, decision, new review date) with top pages refreshed.

## Measurement

Zero cited pages carrying expired stats; % of citable pages inside their review window (target 100%).

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Date-bumping without content change is detectable and dishonest. If nothing changed, the date does not change.

## Fictional example

Fictional: the freshness audit catches a cited 2024 market figure still presented as current in a 2026 answer; the refresh publishes the new figure with its source the same week.
