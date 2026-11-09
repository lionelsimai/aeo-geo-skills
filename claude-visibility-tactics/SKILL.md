---
name: claude-visibility-tactics
description: |
  Understand how Claude answers entity and category questions, and which sources shape those answers.
  TRIGGERS - Use when user needs help with Claude visibility / Claude citations / Anthropic answers tasks.
category: Platform Surfaces
version: 1.0
---
# Claude Visibility Tactics

## What this skill does

Claude's answers draw on its web search and its strong weighting of authoritative, well-structured sources. This skill observes Claude's behaviour on the prompt set, notes where its entity facts come from, and aligns the entity's most authoritative pages accordingly.

Category: **Platform Surfaces** — Layer 4 of the strategy: each engine retrieves and cites differently — per-engine tactics grounded in observed citation behaviour.

## Inputs

- Claude slice of the audit run (answers, sources where shown)
- The entity's most authoritative pages (author page, flagship data)

## Workflow

1. **Probe entity resolution** — Claude is conservative: it hedges when sources conflict. Identity prompts reveal exactly which facts it trusts and which it doubts.
2. **Trace its trusted sources** — Where Claude states a fact, find the page behind it. Its preference for primary and reference sources tells you where to publish corrections.
3. **Strengthen primary pages** — The author page and flagship asset get the clearest structure and the most explicit sourcing — Claude rewards pages that show their evidence.
4. **Correct at the source** — For wrong facts, fix the authoritative page Claude relies on rather than publishing five new minor ones.
5. **Log behaviour changes** — Claude's search and citation features evolve; note product changes in the tracker so score shifts are interpretable.

## Output

A Claude behaviour note + the primary-page strengthening actions taken.

## Measurement

Hedge rate (answers that qualify or disclaim the entity) falling; canonical facts appearing in Claude identity answers.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not mistake a fluent Claude answer for a correct one. Verify every fact it states about the entity against the record — fluency hides stale sources.

## Fictional example

Fictional: Claude describes a founder via a 2022 conference bio; strengthening the author page and correcting that conference page resolves it next cycle.
