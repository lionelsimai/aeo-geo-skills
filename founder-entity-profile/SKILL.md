---
name: founder-entity-profile
description: |
  Build a founder's person-entity profile: the facts, works and affiliations engines need to resolve them as a distinct expert.
  TRIGGERS - Use when user needs help with founder profile / personal entity / expert entity building tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# Founder Entity Profile

## What this skill does

The person-side counterpart to an organisation profile: a structured fact record for a founder/expert — descriptor, organisation founded, works, domain, place, credentials — assembled from verifiable sources and formatted for reuse in bios, schema and pitches.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- Verified CV facts (roles with dates, works, credentials)
- Canonical bio pack (or build it first)
- The sameAs map

## Workflow

1. **Separate person from company** — List which facts belong to the person (works, credentials, expertise) and which to the organisation (customers, revenue). Engines merge them when pages do.
2. **Pick the expertise claim** — One primary domain phrase. A founder who is 'expert in everything' resolves as expert in nothing.
3. **Attach works as evidence** — Books, flagship reports, tools, talks — each with a public URL. Works are the strongest person-entity evidence.
4. **Record affiliations precisely** — Founder-of, author-of, member-of, with start dates where public. Vague 'associated with' language is dropped.
5. **Publish the profile record** — One internal fact sheet + the public author page spec. Every pitch, bio and schema draws from this record only.

## Output

A founder entity fact sheet and the public-profile content spec derived from it.

## Measurement

Identity answers about the person state the primary domain and organisation correctly; profile record is the cited source for all new bios.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not pad with honorary or unverifiable titles. One exposed inflation poisons every true claim beside it.

## Fictional example

Fictional: a founder's record leads with 'founder of a 8,000-member builder community' only because the membership figure is publicly evidenced on the community page.
