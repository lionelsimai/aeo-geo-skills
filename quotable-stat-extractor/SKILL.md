---
name: quotable-stat-extractor
description: |
  Turn reports, datasets and operating numbers into standalone citable statistics with sources, dates and definitions.
  TRIGGERS - Use when user needs help with citable statistics / quotable stats / data extraction for citations tasks.
category: Citable Content
version: 1.0
---
# Quotable Stat Extractor

## What this skill does

Engines cite numbers, not PDFs. This skill mines a source document for its strongest figures and rewrites each as a self-contained stat unit: value, unit, population, date, method note, source link — ready to place on pages engines can lift.

Category: **Citable Content** — Layer 2 of the strategy: pages built to be lifted — answer-first structure, standalone numbers, FAQ blocks, original data.

## Inputs

- The source data (report, dashboard export, survey results)
- Permission to publish each figure
- Definitions behind each number (who counted, over what period)

## Workflow

1. **Inventory candidate figures** — List every number in the source; drop any whose definition you cannot state in one sentence.
2. **Rank by citability** — Prefer unique, current, specific figures (market size, adoption %, audience counts) over round or generic ones.
3. **Write stat units** — One sentence each: '[Figure] of [population] did X in [period] (source: [name], [date]).' No figure ships without its source clause.
4. **Build the stat bank** — Store units in a table with source and date. Mark each with a review/expiry date — stale stats get refreshed or retired.
5. **Place them** — Top stats go on the flagship landing page and the entity hub, worded identically in both places.

## Output

A stat bank table (stat unit, source, date, expiry) and the top-5 placement list.

## Measurement

Citations referencing the entity's own figures in AI answers; stat bank has zero expired units at each monthly check.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never round, merge or 'improve' a figure while extracting it. A stat that differs from its source is a fabrication once published.

## Fictional example

Fictional: from a community report — '9,834 people registered for 68 AI builder events in Singapore in 2026; 46% were decision-makers (source: organiser registration data, Oct 2026).'
