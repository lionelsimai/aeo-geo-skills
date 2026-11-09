---
name: faq-schema-generator
description: |
  Convert on-page FAQ blocks into valid FAQPage schema that matches the visible text exactly.
  TRIGGERS - Use when user needs help with FAQ schema / FAQPage JSON-LD / FAQ structured data tasks.
category: Structured Data & Technical
version: 1.0
---
# FAQ Schema Generator

## What this skill does

Generates FAQPage JSON-LD from an existing visible FAQ block (built with faq-block-builder): each Question/Answer pair copied exactly from the page, structured so engines can lift the pair with its attribution intact.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- The published FAQ block (exact final wording)
- The page URL it lives on

## Workflow

1. **Copy, never paraphrase** — Schema answers must match the visible answers character-for-character in substance. Any edit to the page triggers a schema regeneration.
2. **One FAQPage per page** — Mark up the questions on that page only; do not aggregate the whole site's FAQs onto every page.
3. **Keep answers self-contained** — Confirm each answer still names its subject (inherited from the block builder) before marking it up.
4. **Validate** — Run the structured-data validator; confirm the FAQPage item parses with all pairs present.
5. **Log the pairing** — Record page -> schema version -> date, so content editors know a text change means a schema change.

## Output

Validated FAQPage JSON-LD matching the page, plus a pairing log entry.

## Measurement

FAQ content surfacing in AI answers for its questions; zero schema/page mismatches at quarterly technical checks.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: FAQ schema for content users cannot see on the page is a classic violation. If it is not visible, it is not marked up.

## Fictional example

Fictional: an expert page's five 'Who/What/Where' questions marked up exactly as printed, lifting the identity answer within one cycle.
