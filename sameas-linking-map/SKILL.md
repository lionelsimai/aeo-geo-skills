---
name: sameas-linking-map
description: |
  Build the definitive sameAs map: every official profile URL that represents the same entity, ready for schema and bios.
  TRIGGERS - Use when user needs help with sameAs / profile linking / entity link map tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# sameAs Linking Map

## What this skill does

Produces the verified list of URLs that are the same entity — official site, LinkedIn, YouTube, author pages, Substack, organisation pages — checked one by one, so Person/Organisation schema and every bio link to the same identity graph.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- The entity's known profiles (collect candidates first, verify after)
- Canonical website URL

## Workflow

1. **Collect candidates** — Every profile the entity or team can name, plus anything ranking for the entity's name in search.
2. **Verify ownership** — Each URL must be controlled by the entity or officially represent it. Fan pages, parody, and namesake profiles are excluded and noted.
3. **Check the reverse links** — Profiles should link back to the canonical site where the platform allows it. List the ones that do not.
4. **Publish the map** — One table: platform, URL, verified date, links-back yes/no. This table is the single source schema builders must use.
5. **Maintain on change** — New platform joined or handle changed → update the map first, then schema and bios. Stale sameAs links actively confuse engines.

## Output

A sameAs map table + the fix list for profiles not linking back to the canonical site.

## Measurement

100% of schema sameAs URLs resolve live and are entity-controlled, checked quarterly.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never add a profile 'that looks official'. An unverified sameAs link tells engines a namesake is you.

## Fictional example

Fictional: a founder's map holds 9 verified profiles; a lookalike account with a similar handle is documented as NOT the entity and excluded.
