---
name: nap-consistency-checker
description: |
  Check name, address, phone and core bio fields for one entity across directories, maps and profiles — and fix the variants.
  TRIGGERS - Use when user needs help with NAP consistency / directory data accuracy / listing consistency tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# NAP & Bio-Field Consistency Checker

## What this skill does

For businesses and professionals, engines resolve entities from repeated structured facts. This skill audits name/address/phone plus role, founding year and service area across maps, directories and profiles, and produces a correction list per variant.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- The canonical fact sheet (legal name, trading name, address, phone, website, founding year, service area)
- The listing/profile set to check

## Workflow

1. **Freeze the fact sheet** — One canonical value per field, decided once. Trading-name vs legal-name usage is a written rule, not per-listing taste.
2. **Harvest the listings** — Google Business Profile, Apple Maps, Bing Places, industry directories, social profiles — record the live value of every field.
3. **Diff and classify** — Match / formatting variant (harmless) / factual variant (different phone, old address, wrong year — harmful). Only factual variants go on the fix list.
4. **Fix at the source** — Correct owned listings directly; for aggregator-fed directories, fix the aggregator record so the fix propagates.
5. **Verify and log** — Re-pull each corrected listing after the propagation window and log the date verified.

## Output

A consistency table (surface, field, live value, canonical value, verdict) and a completed-fix log.

## Measurement

Factual-variant count trends to zero across the top 20 listings; re-check quarterly or after any move/rebrand.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not 'fix' formatting variants (St. vs Street) while a wrong phone number sits live. Severity order: contact facts, identity facts, formatting.

## Fictional example

Fictional: a dental clinic has three phone numbers live across listings, one from a previous tenancy. Engines hedge on the entity until the aggregator record is fixed.
