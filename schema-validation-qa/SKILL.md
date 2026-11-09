---
name: schema-validation-qa
description: |
  Validate all structured data on the key pages: parse errors, fact mismatches against the fact sheet, and dropped schema after redesigns.
  TRIGGERS - Use when user needs help with schema validation / structured data QA / schema errors tasks.
category: Structured Data & Technical
version: 1.0
---
# Schema Validation & QA

## What this skill does

A QA pass over the entity's schema system — Person, Organization, FAQPage, Article — checking three things: it parses, it matches the visible page and fact sheet, and it is still there after the latest site changes.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- Key page URLs (hub, homepage, flagship, sample articles)
- The entity fact sheet and canonical bio

## Workflow

1. **Extract what's live** — Pull the JSON-LD actually served on each page (view-source or a testing tool), not what the CMS claims to inject.
2. **Validate syntax** — Run validators; zero errors required on identity pages. Warnings triaged: identity-field warnings are fixed, cosmetic ones logged.
3. **Diff facts against the record** — Every name, date, descriptor and sameAs in schema vs the fact sheet. Any mismatch is a defect, whichever side is wrong.
4. **Check schema vs page text** — Schema claims must appear in visible content. Anything schema-only gets added to the page honestly or removed from schema.
5. **Log and schedule** — Record results per page with dates; re-run after every redesign, migration or CMS change — the top three schema killers.

## Output

A QA report per page (parse status, mismatches, fixes) and a re-check schedule tied to site changes.

## Measurement

Zero parse errors and zero fact mismatches on key pages at each scheduled check.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Valid syntax is not valid schema. JSON that parses but states a wrong founding date passes the tool and fails the entity.

## Fictional example

Fictional: QA finds a redesign dropped FAQPage schema from the expert page and left an old jobTitle in the Person item — both invisible until extracted and diffed.
