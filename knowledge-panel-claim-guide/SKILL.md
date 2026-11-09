---
name: knowledge-panel-claim-guide
description: |
  Claim and correct a Google Knowledge Panel: verify identity, submit sourced corrections, and keep the panel accurate.
  TRIGGERS - Use when user needs help with knowledge panel / claim knowledge panel / Google entity panel tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# Knowledge Panel Claim Guide

## What this skill does

Walks the Knowledge Panel process end to end: checking eligibility, claiming via Google's verification, and submitting corrections where every claimed fact is backed by an authoritative source Google can check.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- The entity's canonical facts
- Official identity/ownership proof for the entity's main profiles
- Authoritative sources per fact (official site, publisher pages, press)

## Workflow

1. **Confirm a panel exists** — Search the exact name. No panel means the job is entity-building first (consistency + Wikidata), not claiming.
2. **Claim it** — Use Google's 'Claim this knowledge panel' flow and verify with an official profile or site the entity controls.
3. **Audit the panel fields** — Name, descriptor/subtitle, image, facts, linked profiles — diff each against the canonical bio.
4. **Submit sourced corrections** — One suggestion per wrong field, each with the authoritative URL that proves it. Unsourced suggestions are ignored.
5. **Re-check monthly** — Panels update from the wider web; a correction that reverts means the underlying source still contradicts you — fix the source.

## Output

Claim status plus a correction log (field, current value, canonical value, proof URL, status).

## Measurement

Panel descriptor matches the canonical phrase and no stale facts remain, checked monthly against the log.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never submit a correction you cannot source. Google weighs the submitter's reliability; junk suggestions burn it.

## Fictional example

Fictional: a speaker's panel lists a company he left in 2022. The correction cites his current organisation's official team page and is accepted.
