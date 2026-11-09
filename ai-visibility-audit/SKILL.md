---
name: ai-visibility-audit
description: |
  Audit how a brand or person actually appears across ChatGPT, Perplexity, Gemini, Claude, Copilot and Google AI Overviews.
  TRIGGERS - Use when user needs help with AI visibility audit / AEO audit / GEO audit tasks.
category: AEO/GEO Strategy & Audits
version: 1.0
---
# AI Visibility Audit

## What this skill does

Runs a structured audit of an entity's presence in AI answers: which prompts mention it, which sources get cited instead, and which facts engines get wrong. Produces a scored audit, not a vibe.

Category: **AEO/GEO Strategy & Audits** — Know where the brand stands in AI answers before spending anything: audits, baselines, share of voice and roadmaps.

## Inputs

- Entity name, canonical descriptor and website
- 10-20 target prompts (or build them with query-tier-mapping)
- 3-5 named competitors

## Workflow

1. **Fix the prompt set** — Use the same prompts, in the same wording, on every engine; record date, engine and whether answers are logged-in or fresh sessions.
2. **Run every engine** — Ask each prompt on ChatGPT, Perplexity, Gemini, Claude, Copilot and Google AI Overviews; save the full answer text, not a summary.
3. **Score each answer** — Mentioned yes/no, position in the answer, descriptor used, facts stated, and sources cited — five fields per answer.
4. **Inspect the cited sources** — List which domains engines actually lift from for these prompts; that list is the corroboration target list.
5. **Write the audit** — Lead with the score table, then the three biggest gaps: entity, corroboration, citable content.

## Output

An audit document: per-engine score table, cited-source list, factual errors found, and gaps ranked by layer (entity, corroboration, content, technical).

## Measurement

Baseline = % of prompts where the entity is mentioned, and % where it appears in the first three names/sources. Re-audit monthly on the identical prompt set; only the delta is meaningful.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never present a single chat session as 'the ranking'. Answers vary by session and account; report the sample size and method.

## Fictional example

Fictional: Northwind Legal, a Singapore law firm, is mentioned in 2 of 60 answers and misdescribed as a conveyancing-only firm in 4. The audit ranks an entity-consistency fix first.
