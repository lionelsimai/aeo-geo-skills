---
name: canonical-and-duplicate-content-fix
description: |
  Find duplicate or competing pages about the same entity/topic and consolidate them so signals stop splitting.
  TRIGGERS - Use when user needs help with duplicate content / canonical tags / competing pages tasks.
category: Structured Data & Technical
version: 1.0
---
# Canonical & Duplicate Content Fix

## What this skill does

Hunts the duplicates that dilute entity resolution: reposted articles on multiple domains, old bio pages, syndicated copies without canonicals, and near-identical topic pages — then consolidates each cluster to one canonical URL with correct redirects/canonical tags.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- The entity's domains and subdomains
- Search results for the entity's key phrases (duplicates surface there first)

## Workflow

1. **Find the clusters** — Search exact titles and key sentences from key pages; list every live copy with its domain and traffic/index status.
2. **Pick the canonical** — The copy on the main domain, on the hub-linked URL, wins. Syndicated copies point their canonical tag to it or are removed.
3. **Redirect or canonicalise** — Owned duplicates: 301 to the canonical. Partner/syndication copies: request a canonical tag or a link + attribution line to the original.
4. **Fix internal mirrors** — Newsletter posts republished on the owned site are originals; the walled-platform version links to them, not the reverse.
5. **Verify consolidation** — Re-search the cluster phrases after propagation; one dominant result should remain, and it should be the canonical.

## Output

A cluster list (copies, chosen canonical, action per copy) and post-fix verification notes.

## Measurement

One canonical result per key phrase in search; zero owned duplicates at quarterly checks.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not delete an old page that third parties link to without a redirect. Deletion throws away the corroboration the programme is trying to build.

## Fictional example

Fictional: the same talk summary lives on a blog, a newsletter platform and an event site; engines cite the event site's weaker copy until canonicals consolidate the signal.
