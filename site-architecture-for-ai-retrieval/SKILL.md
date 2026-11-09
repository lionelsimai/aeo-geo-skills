---
name: site-architecture-for-ai-retrieval
description: |
  Shape site structure so engines find the hub-and-asset system: shallow paths, descriptive URLs, and hub pages that link the cluster.
  TRIGGERS - Use when user needs help with site architecture / URL structure / content hub structure tasks.
category: Structured Data & Technical
version: 1.0
---
# Site Architecture for AI Retrieval

## What this skill does

Applies retrieval-friendly architecture to an AEO programme: entity hub at a short stable URL, flagship asset on a permanent page, query articles under a readable section, and internal linking that teaches engines which page is the hub.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- Current URL inventory of entity/citable pages
- The tier map (which pages are hubs vs spokes)

## Workflow

1. **Give the hub a short URL** — /[expert-name] or /about/[entity] — short, stable, name-bearing. Hub URLs never change; if one must, redirect permanently and update schema/llms.txt the same day.
2. **Put flagship data on a page, not a file** — Reports live as HTML pages (PDF as the download). Engines cite pages; PDFs are weak sources.
3. **Use descriptive article paths** — Query articles under a readable section with the topic in the slug — clarity for engines and humans alike.
4. **Link hub-out, spoke-in** — Hub links to every spoke; every spoke links back to the hub and the flagship. Orphan citable pages are found late or never.
5. **Kill duplicates** — One canonical page per topic/entity. Retire or canonicalise duplicates that split signals (old bios, mirror posts).

## Output

An architecture map (hub, flagship, spokes, link rules) and a fix list for orphan/duplicate pages.

## Measurement

All citable assets within 2 clicks of the homepage and linked from the hub; zero duplicate entity pages at quarterly checks.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not restructure URLs casually mid-programme. Every move costs re-indexing; batch structural changes and redirect properly.

## Fictional example

Fictional: moving a flagship report from /wp-content/uploads/report-final-v3.pdf to a permanent /state-of-industry/ page is the single change behind its first citations.
