---
name: source-worthy-update-writer
description: |
  Write updates that give engines a reason to re-cite: new data, corrected facts and genuinely new sections — announced honestly.
  TRIGGERS - Use when user needs help with content updates / updating articles / refresh content writing tasks.
category: GEO Content Ops & Workflows
version: 1.0
---
# Source-Worthy Update Writer

## What this skill does

Produces the actual refresh content for existing citable pages: leading with what changed and why, integrating new verified figures, and keeping a visible update note — so readers and engines can see the page is maintained, and what the current version says.

Category: **GEO Content Ops & Workflows** — Run AEO as an operation: freshness systems, briefs, calendars, QA gates and agency delivery — the workflows that keep citations compounding.

## Inputs

- The page's freshness-audit findings
- The new verified data/facts (with sources)

## Workflow

1. **Lead the update with the delta** — Draft the changed sections first: new figure, new fact, new guidance. Cosmetic edits wait.
2. **Integrate, don't bolt on** — New data replaces the old in the body and the stat units; a 2024 number lingering below a 2026 headline is a contradiction, not an archive.
3. **Write the update note** — 'Updated [date]: [what changed and why].' on the page. Engines and readers both use it to judge currency.
4. **Update schema dates truthfully** — dateModified moves only because content genuinely changed in this pass — which it did, and the note proves it.
5. **Re-ping and re-track** — IndexNow/console ping per the floor routine; the page's prompts get watched in the next tracker run for citation change.

## Output

The refreshed page (integrated new facts, update note, correct schema dates) + re-indexing done.

## Measurement

Refreshed pages retain/regain citations at the next runs; zero pages with headline/body figure contradictions.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never delete the old figure's context silently where others have cited it; where a cited figure was wrong, correct it visibly in the update note.

## Fictional example

Fictional: a flagship guide's update note — 'Updated Mar 2026: adoption figure replaced with the 2026 survey (n=412), pricing section rewritten' — is itself quoted as a currency signal.
