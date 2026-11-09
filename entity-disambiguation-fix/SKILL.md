---
name: entity-disambiguation-fix
description: |
  Separate an entity from its namesakes in AI answers: choose disambiguators and apply them consistently until engines split the entities.
  TRIGGERS - Use when user needs help with name collision / namesake confusion / wrong person in AI answers tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# Entity Disambiguation Fix

## What this skill does

For entities sharing a name with another person, company or product: identify how engines merge them, choose the disambiguating facts (place, organisation, domain, middle/brand name), and apply those qualifiers on every owned and pitched surface until answers separate.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- Answers showing the merge (saved audit evidence)
- The namesake's distinguishing facts (theirs and yours)
- Canonical bio pack

## Workflow

1. **Document the merge** — Which prompts return which entity, and which facts get crossed (their role with your name, your work under their bio).
2. **Choose the qualifier set** — 2-3 facts that always separate you: geography, organisation, domain. E.g. always '[Name] ([Place])' or the organisation on first mention.
3. **Apply it everywhere owned** — Titles, bios, bylines and page headings carry the qualifier set. Your own site must never present the bare ambiguous name.
4. **Brief third parties** — Event pages, podcasts and press get the qualified descriptor in the credit line — corroboration must use the disambiguated form.
5. **Track the split** — Monthly identity prompts: measure how often answers resolve to the right entity with the right facts.

## Output

A disambiguation plan (qualifier set + surface fix list) and a monthly split-rate tracker.

## Measurement

Split rate = % of identity/category answers resolving to the correct entity. Target steady improvement over 2-3 monthly cycles.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not try to suppress the namesake. You cannot remove them; you can only make your own signal unambiguous.

## Fictional example

Fictional: a Singapore community called OpenBuilder collides with a US startup of the same name; the fix is '(Singapore)' on first mention everywhere until engines separate them.
