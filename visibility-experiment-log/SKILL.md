---
name: visibility-experiment-log
description: |
  Run AEO as experiments: hypothesis, change, window, result — so the programme learns what actually moves answers.
  TRIGGERS - Use when user needs help with AEO experiments / visibility testing / experiment log tasks.
category: Monitoring & Measurement
version: 1.0
---
# Visibility Experiment Log

## What this skill does

Imposes experiment discipline on a field full of folklore: every intervention (schema added, article shipped, roundup won) is logged before results are known, with the prompts expected to move and the window allowed — then judged against the tracker data.

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- The tracker + citation log (the measurement base)
- The change being made (with its ship date)

## Workflow

1. **Write the hypothesis first** — 'Adding FAQ schema to the author page will move Tier 3 descriptor accuracy within 2 runs.' Written before the change ships, in the log.
2. **Isolate where possible** — Change one major variable per window per prompt cluster, or admit in the log that attribution will be fuzzy.
3. **Wait the full window** — Engines re-crawl and re-answer on their own schedule. Judging at 3 days manufactures false negatives.
4. **Judge on the pre-set metric** — Moved / no effect / hurt — recorded against the metric named in the hypothesis, not a friendlier one found afterwards.
5. **Publish learnings internally** — Quarterly, the log's confirmed effects become the team's playbook; its nulls kill superstitions.

## Output

An experiment log (hypothesis, change, window, verdict) + a quarterly learnings summary.

## Measurement

100% of major interventions logged with pre-written hypotheses; quarterly learnings cite verdicts, not anecdotes.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: The classic sin: shipping five changes, seeing movement, and crediting your favourite. The log exists to prevent exactly that story.

## Fictional example

Fictional: an experiment shows llms.txt alone moved nothing in 2 runs, while the same window's roundup inclusion moved Tier 1 mentions — budget follows the evidence.
