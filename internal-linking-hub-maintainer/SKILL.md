---
name: internal-linking-hub-maintainer
description: |
  Maintain the internal link graph of the entity hub: every new asset linked in and out, hubs updated, dead ends eliminated.
  TRIGGERS - Use when user needs help with internal linking / hub maintenance / link graph upkeep tasks.
category: GEO Content Ops & Workflows
version: 1.0
---
# Internal Linking Hub Maintainer

## What this skill does

The unglamorous routine that keeps the architecture working: on every publish, the new asset is linked from its cluster/hub and links back; quarterly, the graph is crawled for orphans, dead links and hub pages missing their newest assets.

Category: **GEO Content Ops & Workflows** — Run AEO as an operation: freshness systems, briefs, calendars, QA gates and agency delivery — the workflows that keep citations compounding.

## Inputs

- The hub map (from personal-entity-content-hub)
- Publish checklist access

## Workflow

1. **Wire at publish time** — New asset checklist: link from cluster page, link from hub if flagship-tier, link out to hub + flagship, add to llms.txt and sitemap verification.
2. **Crawl quarterly** — List pages with zero internal inbound links (orphans) and hub/cluster pages; diff against the hub map.
3. **Fix orphans deliberately** — Each orphan: link it properly, merge it into a stronger page, or retire it with a redirect. No orphan is left 'for later' twice.
4. **Repair dead links** — Outbound and internal 404s fixed; where a cited external source moved, update to its new home so your citations stay credible.
5. **Log the graph state** — Record orphan count and fixes per quarter in the technical QA notes; the trend is a health metric for the whole programme.

## Output

A maintained link graph: publish-time wiring done + a quarterly orphan/dead-link fix list closed out.

## Measurement

Orphan citable assets = 0 at each quarterly crawl; new assets wired on publish day (spot-check).

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not over-link with keyword-stuffed anchors. Natural, descriptive anchors to the hub; the graph serves retrieval and readers, not anchor-text games.

## Fictional example

Fictional: a quarterly crawl finds a high-performing article orphaned by a template change; one cluster link restores its citations the following run.
