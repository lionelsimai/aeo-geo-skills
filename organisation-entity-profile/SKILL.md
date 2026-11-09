---
name: organisation-entity-profile
description: |
  Build an organisation's entity profile: what it is, where, founded when, what it offers — stated identically everywhere.
  TRIGGERS - Use when user needs help with company entity / organisation profile / business entity facts tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# Organisation Entity Profile

## What this skill does

The organisation-side fact record: legal and trading names, one-sentence definition, sector, HQ place, founding date, founders, offers, and official profiles — verified and frozen so the website, directories, schema and press all describe the same company.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- Registration-level facts (legal name, founding date, HQ)
- Offers and sectors as actually sold
- Official profile URLs

## Workflow

1. **Write the one-sentence definition** — '[Org] is a [category] in [place] that [does what] for [whom].' If the team cannot agree this sentence, that disagreement is the finding.
2. **Freeze the fact table** — Names, founding, HQ, founders, sector codes, contact facts — one value each, with the source that proves it.
3. **Audit the About surfaces** — Website About, LinkedIn company page, Crunchbase/directories, community pages — diff against the fact table.
4. **Align the offers language** — Engines describe what you do from repeated phrasing. The top three offers get exact names used everywhere.
5. **Publish and maintain** — Fact table owned by one person; changes (new HQ, rename) trigger a same-week sweep of all surfaces.

## Output

An organisation fact table + an About-surface alignment list.

## Measurement

Top 10 organisation surfaces match the fact table on every field; checked after any company change and quarterly otherwise.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Marketing adjectives are not facts. 'Leading', 'premier' and 'innovative' in the definition sentence are cut — engines and editors ignore them anyway.

## Fictional example

Fictional: a training company's definition is frozen as 'an AI training and community company in Singapore' after three different About pages gave three different categories.
