---
name: aeo-qa-review-checklist
description: |
  The pre-publish QA gate for citable content: facts vs allow-list, structure, schema pairing, links and dates — pass or it does not ship.
  TRIGGERS - Use when user needs help with AEO QA / pre-publish checklist / content review gate tasks.
category: GEO Content Ops & Workflows
version: 1.0
---
# AEO QA Review Checklist

## What this skill does

A hard gate, run by someone other than the author where possible: every fact traced to the allow-list/stat bank, answer-first structure confirmed, FAQ/schema pairing ready, hub links wired, dates and update notes correct. The checklist is short enough to actually be run, strict enough to matter.

Category: **GEO Content Ops & Workflows** — Run AEO as an operation: freshness systems, briefs, calendars, QA gates and agency delivery — the workflows that keep citations compounding.

## Inputs

- The draft + its content brief (with allow-list)
- The canonical fact sheet and stat bank

## Workflow

1. **Diff every fact** — Each number, name, date and claim in the draft ticked against the allow-list or its source. Untraced facts are cut or escalated — never waved through.
2. **Check the structure** — Answer in first 100 words? H2s as questions? Stat units standalone? FAQ present where the format requires it?
3. **Check the entity language** — Descriptors, org names and byline match canonical exactly; the piece links the author page with the right anchor.
4. **Check technical pairing** — Schema needed (Article/FAQ) prepared and matching the final text; internal links live; llms.txt addition queued.
5. **Sign and file** — Reviewer signs the checklist into the piece's record. A piece without a filed checklist is treated as unpublished for reporting purposes.

## Output

A signed QA checklist per piece + the corrections made at the gate.

## Measurement

QA pass rate and defects caught per category (facts vs structure vs entity) — the defect mix steers writer training.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: The author self-certifying under deadline is how fabrications ship. If no second person exists, the checklist runs after a night's gap, item by item, out loud.

## Fictional example

Fictional: QA catches a draft citing 'industry growth of 40%' with no source; the line is cut before publish — the kind of figure that, shipped, would be quoted back for years.
