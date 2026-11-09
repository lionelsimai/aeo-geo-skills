---
name: copilot-bing-citation-tactics
description: |
  Earn Copilot citations through the Bing index: IndexNow, Bing Webmaster data and Bing-visible corroboration.
  TRIGGERS - Use when user needs help with Copilot citations / Bing visibility / Microsoft Copilot answers tasks.
category: Platform Surfaces
version: 1.0
---
# Copilot & Bing Citation Tactics

## What this skill does

Copilot retrieves from Bing. This skill works that chain deliberately: Bing indexation verified per page, IndexNow keeping it current, Bing Places/webmaster data correct, and corroboration on sources Bing actually surfaces.

Category: **Platform Surfaces** — Layer 4 of the strategy: each engine retrieves and cites differently — per-engine tactics grounded in observed citation behaviour.

## Inputs

- Bing Webmaster Tools access and indexation status
- IndexNow status (from indexation-and-crawl-floor)

## Workflow

1. **Verify Bing indexation per URL** — Each citable asset checked in Bing Webmaster / site: queries. Google-indexed does not imply Bing-indexed.
2. **Turn on and test IndexNow** — Publish a test update; confirm the ping fires and Bing picks the change up. Un-tested IndexNow is usually broken IndexNow.
3. **Fix Bing-specific data** — Bing Places listing (for organisations with a location) and webmaster settings match the canonical fact sheet.
4. **Watch Bing's cited sources** — Copilot shows sources; log which domains it lifts for your prompts — Bing's mix differs from Google's, so targets may differ.
5. **Track the Copilot slice** — Monthly prompts on Copilot with citations logged, reported separately like every engine.

## Output

A Copilot/Bing checklist (indexation per asset, IndexNow verified, Places correct) + its slice of the citation log.

## Measurement

100% of citable assets Bing-indexed; Copilot mention/citation rates on the monthly slice.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Skipping Bing because 'nobody searches Bing' misses the point: Copilot's answers are the audience, Bing is just the plumbing.

## Fictional example

Fictional: a site's flagship page is Google-indexed for months but absent from Bing due to a robots path rule; one fix later, Copilot cites it.
