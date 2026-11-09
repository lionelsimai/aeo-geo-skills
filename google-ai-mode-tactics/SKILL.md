---
name: google-ai-mode-tactics
description: |
  Prepare for conversational AI Mode search: multi-turn queries, follow-up context and fan-out sub-queries.
  TRIGGERS - Use when user needs help with Google AI Mode / conversational search / AI Mode visibility tasks.
category: Platform Surfaces
version: 1.0
---
# Google AI Mode Tactics

## What this skill does

AI Mode answers with query fan-out: one question becomes many sub-queries, and sources are gathered across all of them. This skill maps the fan-out for target topics and ensures the entity has a citable page for the sub-questions, not just the headline query.

Category: **Platform Surfaces** — Layer 4 of the strategy: each engine retrieves and cites differently — per-engine tactics grounded in observed citation behaviour.

## Inputs

- Target topics from the tier map
- The sub-questions each topic generates (gathered by testing AI Mode follow-ups)

## Workflow

1. **Map the fan-out** — For each target topic, record the follow-up questions AI Mode asks itself (visible via answer structure and related questions): definitions, costs, comparisons, local variants.
2. **Audit coverage per sub-query** — For each sub-question: does a citable owned or corroborating page exist? Mark the gaps — the headline article rarely covers them.
3. **Fill gaps with focused assets** — Short, specific pages/sections per gap sub-query (definition, comparison, local), each answer-first.
4. **Support multi-turn context** — Pages should state their subject fully (names, place, category) since follow-up answers lift fragments out of context.
5. **Track AI Mode separately** — Add AI Mode observations to the monthly run as its own surface; its source mix differs from both classic and Overviews.

## Output

A fan-out map per topic (sub-queries x coverage) + the gap assets created.

## Measurement

Coverage = sub-queries with a citable asset; citations observed in AI Mode answers for target topics.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not write one mega-page claiming to answer every sub-query. Focused pages get lifted; mega-pages get skimmed.

## Fictional example

Fictional: 'AI training Singapore' fans out into cost, duration, beginner, and finance-specific sub-queries; three focused pages fill the gaps the main article missed.
