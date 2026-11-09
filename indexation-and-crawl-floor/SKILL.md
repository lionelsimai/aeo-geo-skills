---
name: indexation-and-crawl-floor
description: |
  Set the technical floor: Search Console + Bing Webmaster verified, sitemap submitted, IndexNow on, key pages confirmed indexed.
  TRIGGERS - Use when user needs help with indexation / search console setup / Bing webmaster / IndexNow tasks.
category: Structured Data & Technical
version: 1.0
---
# Indexation & Crawl Floor

## What this skill does

The week-1 technical checklist from the strategy's Layer 5: both webmaster consoles verified, sitemap live and submitted, IndexNow enabled so Bing (Copilot's index) picks up new pages fast, and every citable asset confirmed indexed in both indexes.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- Site admin access (or the developer who has it)
- The list of citable asset URLs that must be indexed

## Workflow

1. **Verify both consoles** — Google Search Console and Bing Webmaster Tools verified for the correct property (domain-level where possible).
2. **Submit a clean sitemap** — Sitemap contains only canonical, indexable URLs — no redirects, no duplicates, no staging leftovers.
3. **Enable IndexNow** — Key generated, endpoint live, CMS pings on publish/update. This is the fast lane into Bing and therefore Copilot answers.
4. **Confirm the key pages** — URL-inspect each hub/flagship/article URL in both consoles. 'Indexed' is verified per page, not assumed from the sitemap.
5. **Set the publish checklist** — New citable asset = console check + IndexNow ping + llms.txt update, as one routine step.

## Output

A completed floor checklist with per-page indexation status for every citable asset.

## Measurement

100% of citable assets indexed in Google and Bing, re-verified monthly for new assets.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: A submitted sitemap is not indexation. Pages sit unindexed for months while dashboards look green; inspect the actual URLs.

## Fictional example

Fictional: a flagship page is in the sitemap for 6 weeks but never indexed in Bing due to a stale noindex from staging; Copilot cannot cite what Bing has not indexed.
