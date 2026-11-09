---
name: entity-consistency-sweep
description: |
  Audit every public surface describing an entity and flag every descriptor, role or fact that contradicts the canonical bio.
  TRIGGERS - Use when user needs help with bio consistency / profile audit / consistent entity tasks.
category: Entity & Knowledge Foundation
version: 1.0
---
# Entity Consistency Sweep

## What this skill does

Walks the entity's full surface list — own site, LinkedIn, Substack/newsletter, Amazon/Goodreads, YouTube, speaker and event pages, directories — and diffs each bio against the canonical version, producing a fix list ordered by surface authority.

Category: **Entity & Knowledge Foundation** — Layer 1 of the strategy: one canonical identity, repeated verbatim, that engines can resolve without hedging.

## Inputs

- The frozen canonical bio pack
- The surface list (build it by searching the entity name + descriptor variants)

## Workflow

1. **Build the surface list** — Search the name in quotes plus each old descriptor; capture every profile, author page and event bio in the top results.
2. **Diff each surface** — Per surface: descriptor used, role/org stated, place stated, proof listed. Mark match / partial / contradicts.
3. **Rank by authority** — The entity's own homepage and highest-traffic profiles first — engines weight them most.
4. **Write the fix list** — Per surface: exact replacement text (pasted from the canonical pack, not rewritten) and who can edit it.
5. **Re-sweep after fixes** — Verify each edited surface live, then log the date. Stale third-party pages get a correction request with the canonical text attached.

## Output

A sweep table (surface, verdict, replacement text, owner, status) covering every found profile.

## Measurement

Consistency = % of top 15 surfaces matching the canonical descriptor. Re-sweep quarterly; new event/speaker pages are the usual relapse.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Speaker and event pages are written by organisers from old bios. Send the canonical bio with every confirmation instead of fixing pages one by one forever.

## Fictional example

Fictional: a sweep finds 14 surfaces; 5 still say 'marketing consultant' two years after the pivot to AI training. The homepage contradiction is fixed first.
