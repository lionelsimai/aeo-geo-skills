---
name: wikidata-entry-builder
description: |
  Prepare a well-sourced Wikidata item for a person or organisation — only when notability evidence genuinely supports it.
  TRIGGERS - Use when user needs help with Wikidata entry / knowledge graph entity / structured entity record tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# Wikidata Entry Builder

## What this skill does

Assesses whether an entity clears Wikidata's notability bar, then prepares the item properly: statements sourced to independent references (books with ISBNs, press coverage, official records), correct properties, and no promotional language.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- Evidence of notability: independent press, published books (ISBN), awards from notable bodies, official roles
- Canonical facts with sources per fact
- Existing identifiers (ISNI, VIAF, ORCID, company registration) if any

## Workflow

1. **Gate on notability first** — Wikidata requires serious independent coverage or a structural need. If the evidence is thin, stop and say so — a deleted item is worse than none.
2. **Check for an existing item** — Search name variants and identifiers. Edit the existing item rather than creating a duplicate.
3. **Draft statements offline** — Instance of, occupation, employer/founder-of, country, works (with ISBN), official website — each with its reference URL listed beside it.
4. **Create with references** — Every statement carries its reference at creation time, not 'to be added'. Unsourced statements are removed by editors.
5. **Maintain it** — Re-check after major facts change (new book, new role). Never use the item as a billboard; keep it factual and current.

## Output

A readiness verdict plus, if warranted, a created/updated Wikidata item with fully referenced statements.

## Measurement

Item survives 90 days without deletion or unsourced-content tags, and engines begin resolving the entity with correct facts.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not force this early. Lionel's strategy rule: Wikidata comes at month 2-3, after the entity is consistent everywhere else.

## Fictional example

Fictional: an author with three ISBN books and national-press coverage clears the bar; a consultant with only self-published content does not, and is told to wait.
