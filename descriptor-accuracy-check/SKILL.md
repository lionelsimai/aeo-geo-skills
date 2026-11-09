---
name: descriptor-accuracy-check
description: |
  Check the words engines use for an entity: is the canonical descriptor spreading, and which wrong phrases persist from which sources?
  TRIGGERS - Use when user needs help with descriptor check / how do AI engines describe / brand descriptor accuracy tasks.
category: Monitoring & Measurement
version: 1.0
---
# Descriptor Accuracy Check

## What this skill does

Extracts, from the monthly run's answers, every phrase engines use to describe the entity (job titles, category labels, organisational claims) and scores each against the canonical descriptor — producing a phrase ledger that shows adoption and the stubborn wrong phrases with their sources.

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- The month's saved answers
- The canonical descriptor
- The entity-resolution diagnostic (for source tracing)

## Workflow

1. **Extract describing phrases** — Pull the exact words used for the entity in each answer ('…is a Singapore-based marketing executive…') into a list.
2. **Classify each phrase** — Canonical / acceptable variant / stale / wrong. Acceptable variants defined in advance (e.g. shortened org name), not decided per instance.
3. **Compute adoption** — Canonical-descriptor rate = canonical phrases / all describing phrases, per engine.
4. **Trace the stubborn wrong ones** — Any stale/wrong phrase appearing 2+ runs running gets traced to its feeding page via the diagnostic method.
5. **Feed fixes back** — Traced sources join the consistency sweep / repair queue with the exact phrase they are spreading.

## Output

A phrase ledger (phrase, class, engine count, source if traced) + the adoption rate trend.

## Measurement

Canonical adoption rate trending up quarter on quarter; zero untraced recurring wrong phrases.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not demand 100% verbatim adoption — engines paraphrase. The metric is the canonical phrase becoming the dominant pattern, with wrong facts at zero.

## Fictional example

Fictional: adoption rises 20% -> 55% over a quarter while 'TikTok executive' persists from one stale profile, which the ledger finally pinpoints.
