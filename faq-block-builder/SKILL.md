---
name: faq-block-builder
description: |
  Build FAQ blocks that answer the real questions about an entity, product or topic — in wording engines can quote verbatim.
  TRIGGERS - Use when user needs help with FAQ content / frequently asked questions / FAQ for AI answers tasks.
category: Citable Content
version: 1.0
---
# FAQ Block Builder

## What this skill does

Creates FAQ sections from real questions (sales calls, search queries, community threads), each answered in 2-4 self-contained sentences using canonical facts. Designed to pair with faq-schema-generator for markup.

Category: **Citable Content** — Layer 2 of the strategy: pages built to be lifted — answer-first structure, standalone numbers, FAQ blocks, original data.

## Inputs

- Real question sources (support logs, sales calls, Search Console queries, community questions)
- Canonical facts for the answers

## Workflow

1. **Harvest real questions** — Mine actual phrasings; do not invent questions nobody asks. Rank by frequency and by which target prompts they match.
2. **Answer self-containedly** — Each answer restates the subject ('Northwind Legal is…') instead of pronouns, so a lifted answer still makes sense alone.
3. **Use canonical facts only** — Names, figures and descriptors come from the fact sheet/stat bank. Opinion questions get the entity's stated position, attributed as such.
4. **Keep answers liftable length** — 40-80 words per answer. Shorter starves the answer; longer buries the quotable sentence.
5. **Place and mark up** — FAQ goes on the hub/topic page it belongs to (not a single site-wide FAQ dump), then hand to faq-schema-generator.

## Output

An FAQ block (question/answer pairs) placed on its page, plus the list handed to schema markup.

## Measurement

FAQ questions appearing as (or inside) AI answers for related prompts; zero answers contradicting the fact sheet at quarterly review.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not write FAQ answers as ads. 'We are the leading…' answers are never lifted; factual answers are.

## Fictional example

Fictional: 'Who is Maya Chen?' — 'Maya Chen is a maritime AI expert in Singapore and founder of PortLogic. She wrote Smart Ports (2025) and runs a 2,000-member port-technology community.'
