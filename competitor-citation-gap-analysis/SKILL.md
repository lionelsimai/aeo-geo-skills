---
name: competitor-citation-gap-analysis
description: |
  Find the exact pages and sources engines cite for competitors but not for you, and turn them into a target list.
  TRIGGERS - Use when user needs help with citation gap / competitor source analysis / why are competitors cited tasks.
category: AEO/GEO Strategy & Audits
version: 1.0
---
# Competitor Citation Gap Analysis

## What this skill does

Compares the citation footprint of the entity against each competitor across the prompt set: sources cited for them, not for you, classified as earnable (pitch, publish, list) or structural (their owned flagship assets).

Category: **AEO/GEO Strategy & Audits** — Know where the brand stands in AI answers before spending anything: audits, baselines, share of voice and roadmaps.

## Inputs

- Audit answers with sources for the entity and 3-5 competitors
- Each competitor's main website

## Workflow

1. **Build the citation inventory** — Every unique cited source across all answers, tagged by which entity it supported.
2. **Classify each source** — Roundup/listicle, trade press, directory, review platform, owned flagship content, video/transcript, reference (Wikipedia/Wikidata).
3. **Mark earnable vs structural** — Earnable = a third party you can legitimately pitch or join. Structural = their own asset you must match with your own, not copy.
4. **Check quality first** — Drop spam roundups and paid-placement mills from the target list even if engines cite them today; they dilute the entity.
5. **Sequence the targets** — Order by frequency cited x quality x effort. The top five become this quarter's corroboration plan.

## Output

A gap table (source, type, cited-for, earnable/structural, quality verdict) and a sequenced top-five target list.

## Measurement

Re-run quarterly. Success = earnable targets converted (listed/quoted/published) and first citations appearing from two or more of them.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Engines citing a spam listicle does not make it a good target. Lionel's rule: the Troniex/WhaTech class of list is skipped even when competitors are on it.

## Fictional example

Fictional: a training provider finds competitors cited from 14 sources it lacks: 6 legit roundups, 3 podcast pages, 2 directories, 3 spam lists (dropped). Nine targets remain.
