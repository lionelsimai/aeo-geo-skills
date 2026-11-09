---
name: local-business-ai-visibility
description: |
  Get a local business correctly named, described and recommended in 'near me' and '[service] in [place]' AI answers.
  TRIGGERS - Use when user needs help with local AI visibility / near me answers / local business AEO tasks.
category: Local & Vertical AEO
version: 1.0
---
# Local Business AI Visibility

## What this skill does

The local playbook end to end: Google Business Profile and maps data as the entity base, NAP consistency, local reviews, a location page that states services/areas/hours as citable facts, and local prompts tracked monthly.

Category: **Local & Vertical AEO** — The five layers applied per vertical: local businesses, B2B SaaS, ecommerce, professional services and more — same discipline, different surfaces.

## Inputs

- Canonical fact sheet (NAP + services + hours + service area)
- Google Business Profile access
- Review platform status

## Workflow

1. **Fix the entity base** — GBP category, name, address, hours and services match the fact sheet exactly; Apple/Bing places aligned after.
2. **Publish the location page** — One page per location: services in plain words, area served, hours, contact — answer-first, with LocalBusiness schema via the technical skills.
3. **Earn local proof** — Real customer reviews on Google and the vertical's platforms (review-platform-presence-builder rules: real customers only).
4. **Get locally corroborated** — Local press, community pages, chambers/associations and local roundups ('best [service] in [neighbourhood]') with the correct descriptor.
5. **Track local prompts** — '[service] in [place]', 'best [service] near [area]', 'Who offers [service] in [place]?' in the monthly set, per location.

## Output

A local visibility pack (base fixed, location page live, proof plan) + local prompts in the tracker.

## Measurement

Mention/recommendation rate on local prompts per location; GBP facts 100% canonical at checks.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never buy local reviews or stuff the business name with keywords ('Best Cheap Top Plumber SG'). Name-field spam is a suspension risk, not a tactic.

## Fictional example

Fictional: a two-outlet bakery is recommended for the wrong outlet's neighbourhood until service areas are stated per location page; answers separate within a cycle.
