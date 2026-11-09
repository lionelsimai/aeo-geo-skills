---
name: organisation-schema-builder
description: |
  Build valid Organization schema: legal/trading names, founding, HQ, founders, offers and official profiles.
  TRIGGERS - Use when user needs help with Organization schema / company JSON-LD / business structured data tasks.
category: Structured Data & Technical
version: 1.0
---
# Organisation Schema Builder

## What this skill does

Produces Organization JSON-LD from the organisation fact table: name + alternateName, foundingDate/Location, founder links to Person items, address, contactPoint, makesOffer/service names in the frozen offers language, and sameAs.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- Organisation entity profile (fact table)
- Founder Person items or their page URLs
- Verified organisation profiles for sameAs

## Workflow

1. **Start from the fact table** — Names, dates and places come from the frozen record — including the legal vs trading name distinction.
2. **Connect the founders** — founder references the Person items so the graph resolves people and company as one entity system.
3. **State offers in frozen language** — Use the exact offer names used on the site and profiles. New marketing phrases do not belong in schema first.
4. **Place it site-wide correctly** — Organisation schema belongs on the homepage/About; do not paste conflicting copies with different facts across pages.
5. **Validate and monitor** — Validate at launch; re-validate after any site redesign or fact change — redesigns silently drop schema.

## Output

A validated Organization JSON-LD block and placement/maintenance notes.

## Measurement

Zero validation errors; organisation facts (founding, HQ, category) stated correctly in AI answers.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: One organisation, one fact set. Two pages emitting different founding dates or addresses is worse than no schema.

## Fictional example

Fictional: an Organization item for a Singapore training company with founder linked to its Person item and three frozen offer names.
