---
name: article-schema-builder
description: |
  Add Article/BlogPosting schema with a real author entity, dates and headline discipline to every citable article.
  TRIGGERS - Use when user needs help with Article schema / BlogPosting JSON-LD / author markup tasks.
category: Structured Data & Technical
version: 1.0
---
# Article Schema Builder

## What this skill does

Ensures each query-targeted article carries Article schema whose author is the Person entity (@id reference, not a bare name string), with honest publish/modified dates and the page's real headline — the signals engines use to attribute and date content.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- The article's final headline, publish date and update dates
- The author's Person item @id / author page URL

## Workflow

1. **Reference the author entity** — author points to the Person @id from the author page, so articles accumulate onto the person entity instead of floating as byline text.
2. **Use true dates** — datePublished is the real first-publish date; dateModified changes only on substantive updates, never as a freshness trick.
3. **Match the headline** — headline equals the page's H1/title. A different, punchier schema headline is a mismatch — cut it.
4. **Add the publisher graph** — publisher references the Organization item; image is the page's actual share image.
5. **Template it** — Bake the pattern into the CMS/template so every new article ships with it — hand-adding schema per post always lapses.

## Output

An Article schema pattern/template plus a check of existing articles for missing or string-only authors.

## Measurement

% of citable articles with entity-referenced author schema (target 100%); modified dates that match real edit history.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never bump dateModified without changing content. Engines compare; fake freshness is detected and discounted.

## Fictional example

Fictional: 24 articles retrofitted so their author resolves to one Person entity; identity answers start attributing the topic to that author.
