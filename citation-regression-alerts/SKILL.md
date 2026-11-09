---
name: citation-regression-alerts
description: |
  Detect and diagnose lost citations: when a previously-cited source drops out of answers, find out why before it compounds.
  TRIGGERS - Use when user needs help with lost citations / visibility drop / citation regression tasks.
category: Monitoring & Measurement
version: 1.0
---
# Citation Regression Alerts

## What this skill does

Compares each monthly run against the citation log to flag regressions: assets that were cited and no longer are, entities whose mentions dropped, descriptors that reverted. Each flag gets a cause hypothesis tested against evidence (page changed? competitor asset launched? engine update?).

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- Current run vs citation log history
- Site change log (redesigns, migrations, edits)
- Engine product-change notes where known

## Workflow

1. **Diff the runs** — Per prompt x engine: citation gained / held / lost vs last month. Losses listed first — they are the agenda.
2. **Check your own changes first** — Was the page edited, moved, de-indexed or schema-stripped since the last run? Own-goals outnumber competitor attacks ten to one.
3. **Check the competitive change** — Did a competitor publish a stronger asset for that prompt, or a roundup update its list? Record the new cited source.
4. **Check engine change** — Note known engine updates in the window; a cross-prompt simultaneous drop usually means the engine changed, not your site.
5. **Assign the response** — Per regression: fix (own change), counter (stronger asset), or watch (engine noise, one month). No panic rebuilds on one month's data.

## Output

A regression list with cause classification and an assigned response per item.

## Measurement

Regressions acknowledged within the monthly cycle; repeat regressions on the same asset trigger a structural fix, not another watch.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not treat normal answer variance as regression. Single-prompt, single-engine flickers are noise; patterns across prompts are signal.

## Fictional example

Fictional: a flagship page loses citations on 4 prompts the month after a redesign — extraction shows its schema and FAQ block were dropped in the new template.
