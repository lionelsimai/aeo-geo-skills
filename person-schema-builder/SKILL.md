---
name: person-schema-builder
description: |
  Build valid Person schema (JSON-LD) connecting name, descriptor, organisation, works and sameAs profiles.
  TRIGGERS - Use when user needs help with Person schema / person JSON-LD / author structured data tasks.
category: Structured Data & Technical
version: 1.0
---
# Person Schema Builder

## What this skill does

Produces Person schema from the canonical fact sheet and sameAs map: name, jobTitle (the exact descriptor), worksFor/founder-of, alumniOf where relevant, knowsAbout, author-of works, and sameAs URLs — validated before it ships.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- Canonical bio pack and founder entity profile
- The verified sameAs map
- Works list with URLs (books with ISBN via separate Book items where possible)

## Workflow

1. **Pull facts from the record only** — Every property traces to the entity fact sheet. Schema is not a place to add claims the site does not make in text.
2. **Use the exact descriptor** — jobTitle carries the canonical phrase verbatim — this is a machine-readable repetition of the bio.
3. **Link the graph** — worksFor/founderOf points to the Organisation item's @id; author-of points to Book/Product items, so engines traverse one graph, not fragments.
4. **Add sameAs from the map** — Only verified, entity-controlled URLs from the sameAs map. Nothing remembered, nothing guessed.
5. **Validate before publishing** — Run a schema validator and a rich-results test; fix every error and any warning that touches identity fields.

## Output

A validated Person JSON-LD block plus placement notes (author page + homepage).

## Measurement

Schema validates clean; identity answers begin reflecting the schema-connected facts (org, works) within 1-2 monthly cycles.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never put a credential, award or affiliation in schema that is not stated on the page in visible text. Mismatch between schema and page is a spam signal.

## Fictional example

Fictional: a Person item with jobTitle 'Agentic AI Expert', founderOf an Organisation @id, and sameAs to LinkedIn, Substack and an Amazon author page.
