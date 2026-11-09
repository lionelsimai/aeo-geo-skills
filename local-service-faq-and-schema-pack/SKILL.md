---
name: local-service-faq-and-schema-pack
description: |
  Equip local service pages with the FAQ answers and LocalBusiness schema that make services, areas and prices liftable.
  TRIGGERS - Use when user needs help with local schema / LocalBusiness schema / local FAQ tasks.
category: Local & Vertical AEO
version: 1.0
---
# Local Service FAQ & Schema Pack

## What this skill does

Builds the local content+markup pair: FAQs answering the real local questions (areas covered, response times, price basis, booking) and LocalBusiness/ProfessionalService schema whose facts match the page and the fact sheet exactly.

Category: **Local & Vertical AEO** — The five layers applied per vertical: local businesses, B2B SaaS, ecommerce, professional services and more — same discipline, different surfaces.

## Inputs

- Service list with honest price basis (ranges or 'from' prices that are real)
- Service areas, hours, contact facts
- The location page

## Workflow

1. **Harvest local questions** — From calls and messages: 'Do you cover [area]?', 'How fast?', 'How much for…?' — the questions local prompts are made of.
2. **Answer with operational truth** — Areas actually served, times actually met, prices actually charged. An answer the business cannot honour is a future bad review quoted by an engine.
3. **Mark up the business** — LocalBusiness subtype schema: name, address, geo, openingHours, areaServed, sameAs — all from the fact sheet, validated.
4. **Pair FAQ with schema** — FAQPage markup added for the on-page FAQ, copied exactly per faq-schema-generator rules.
5. **Maintain on change** — Hours/area/price changes update page, schema and GBP in the same task — the three must never disagree.

## Output

A location page with FAQ block + validated LocalBusiness and FAQPage schema.

## Measurement

Local prompt answers state the business's areas/hours correctly; zero page/schema/GBP fact conflicts at checks.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not list service areas the business does not serve to 'catch' prompts. Engines will recommend you for jobs you then refuse — publicly.

## Fictional example

Fictional: an aircon servicing firm's FAQ states its real 4-hour emergency window; AI answers begin quoting it for urgent-repair prompts in its districts.
