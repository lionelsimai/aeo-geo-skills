---
name: search-console-ai-query-mining
description: |
  Mine Search Console and Bing data for the real queries behind AI visibility: new prompt candidates and content gaps.
  TRIGGERS - Use when user needs help with search console mining / query research / prompt discovery tasks.
category: Monitoring & Measurement
version: 1.0
---
# Search Console AI Query Mining

## What this skill does

Uses classic search data as the discovery layer for AEO: queries the site already impressions for (especially question-form and category+place phrases), AI-referral traffic where visible, and Bing's AI citation reports — feeding new Tier 2 candidates and article topics.

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- Google Search Console access (queries/pages, 6+ months)
- Bing Webmaster Tools incl. AI performance/citation reports where available

## Workflow

1. **Pull question-form queries** — Filter for who/what/how/which/best/top phrasings in the entity's topics. These are tomorrow's prompts, in users' real words.
2. **Find near-miss pages** — Queries with impressions but weak positions where an answer-first rewrite or a focused page could win both search and citation.
3. **Read the AI reports** — In Bing's AI citation data: which pages get cited, for what themes. Confirm the flagship assets are the ones being used.
4. **Nominate prompt candidates** — Up to 5 new candidate prompts per quarter for the tier map — nominated by data, added only at a version change of the prompt set.
5. **Log the mining** — Record what was found and what was actioned; next quarter's mining starts from this log, not from scratch.

## Output

A mining report (question queries, near-miss pages, AI-citation observations, prompt candidates).

## Measurement

Candidates actioned per quarter; near-miss pages improved and re-measured in the following run.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not add every mined query to the frozen prompt set mid-cycle. Discovery is continuous; the measurement set changes only on version boundaries.

## Fictional example

Fictional: Console shows growing impressions for 'AI agents for finance teams Singapore' — it becomes a Tier 2 prompt and an article at the next set version.
