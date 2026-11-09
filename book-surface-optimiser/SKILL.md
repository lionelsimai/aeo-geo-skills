---
name: book-surface-optimiser
description: |
  Optimise the surfaces books create — Amazon author page, Goodreads, publisher pages — as entity evidence with one canonical bio.
  TRIGGERS - Use when user needs help with book pages / Amazon author page / Goodreads / author surfaces tasks.
category: Third-Party Corroboration
version: 1.0
---
# Book Surface Optimiser

## What this skill does

For authors, books are among the strongest entity evidence engines have: ISBNs, publisher records, retailer author pages. This skill aligns every book surface — author page bio, per-book descriptions, Goodreads, publisher catalogue — to the canonical bio and descriptor.

Category: **Third-Party Corroboration** — Layer 3 of the strategy: independent sources describing the entity the same way — the layer that actually moves prize queries.

## Inputs

- Book list with ISBNs, publishers and retailer links
- Canonical bio pack
- Author Central / Goodreads author account access

## Workflow

1. **Claim the author pages** — Amazon Author Central and Goodreads author profile claimed and verified; unclaimed pages cannot be corrected.
2. **Paste the canonical bio** — Author pages carry the 150-word canonical bio verbatim, descriptor included. Retailer bios written years ago are the usual stale source.
3. **Align book descriptions** — Each book's description names the author with the descriptor and links the series/order correctly; facts (edition, date, ISBN) match the publisher record.
4. **Connect the graph** — Author page links the official site; the site's author page and Person schema link back with the books as works.
5. **Maintain per release** — New book launch checklist includes every surface on day one — surfaces created late carry stale bios by default.

## Output

A book-surface register (surface, bio version, facts verified) with all corrections applied.

## Measurement

100% of book surfaces on the current canonical bio; books appearing correctly attributed in identity answers.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not stuff book descriptions with keywords or claims ('#1 bestseller') that the sales record cannot support on that retailer.

## Fictional example

Fictional: an author's Amazon page still leads with a corporate role from 2021; replacing it with the canonical expert bio changes how 'Who is…?' answers open within two cycles.
