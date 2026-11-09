---
name: llms-txt-builder
description: |
  Create and maintain an llms.txt file: a clean map of the site's key entity pages and citable assets for AI systems.
  TRIGGERS - Use when user needs help with llms.txt / llms full text / AI site map file tasks.
category: Structured Data & Technical
version: 1.0
---
# llms.txt Builder

## What this skill does

Builds /llms.txt (and llms-full.txt where warranted): a markdown index of the pages that matter — entity hub, flagship data page, key articles, about — with one-line descriptions in canonical wording, kept current as assets publish.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- The site's key URLs (entity hub, flagship asset, top articles, about)
- Canonical one-line descriptions per page

## Workflow

1. **List only what matters** — 10-30 URLs: entity pages and citable assets. llms.txt is a curated map, not a sitemap dump.
2. **Describe in canonical wording** — Each entry: title + link + one line using the frozen descriptors — the file itself is an entity-consistency surface.
3. **Order by importance** — Entity hub first, flagship data second, then articles by tier. Order signals priority.
4. **Publish at the root** — /llms.txt, plain markdown, no login, no blocking. Verify it returns 200 and renders as text.
5. **Maintain on publish** — Every new citable asset is added the week it ships; dead links are removed at the monthly check.

## Output

A published /llms.txt (+ optional llms-full.txt) and a maintenance rule in the publishing checklist.

## Measurement

File live and current (checked monthly); included pages match the tier map's live assets exactly.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not stuff llms.txt with every URL or with claims the pages do not support. It is an index, not an ad.

## Fictional example

Fictional: an llms.txt leading with the expert page, the state-of-industry data page, and 12 query articles — each line in canonical wording.
