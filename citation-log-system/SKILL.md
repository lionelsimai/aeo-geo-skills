---
name: citation-log-system
description: |
  Log every citation an entity earns in AI answers: source, prompt, engine, date and position — the asset register of AEO.
  TRIGGERS - Use when user needs help with citation log / citation tracking / AI citation register tasks.
category: Monitoring & Measurement
version: 1.0
---
# Citation Log System

## What this skill does

Builds the running register of citations: each time an owned or corroborating source is cited in a tracked answer, it is logged with context. Over quarters this log answers 'what actually earns citations here?' with data instead of folklore.

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- Monthly tracker runs (the raw material)
- The owned/corroborating source inventory

## Workflow

1. **Define a citation record** — Date, engine, prompt, cited URL, source owner (owned/partner/third-party), position in source list, answer excerpt.
2. **Harvest from every run** — After each monthly run, extract citations into the log before scores are summarised; do not rely on memory or highlights.
3. **Tag by asset type** — Flagship data, article, author page, roundup, review platform, video — the tags that later reveal which asset class performs.
4. **Review the log quarterly** — Which assets earn repeat citations? Which earned one and vanished? Feed both answers into the content plan.
5. **Keep it append-only** — Citations are never deleted when they stop appearing; disappearance is data (see citation-regression-alerts).

## Output

An append-only citation log + a quarterly asset-performance summary.

## Measurement

Log completeness = citations in raw answers vs citations logged (spot-check target 100%); quarterly summary delivered on schedule.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not log only the wins you noticed. A partial log manufactures confidence; completeness is the entire point.

## Fictional example

Fictional: after 3 months, the log shows the data landing page earns 60% of owned citations while 20 articles share the rest — the next quarter doubles down on data editions.
