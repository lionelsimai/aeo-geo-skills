---
name: monthly-ai-visibility-scorecard
description: |
  Produce the one-page monthly scorecard: tier scores vs baseline, per-engine movement, descriptor accuracy and the month's actions.
  TRIGGERS - Use when user needs help with monthly scorecard / visibility report / AEO reporting tasks.
category: Monitoring & Measurement
version: 1.0
---
# Monthly AI Visibility Scorecard

## What this skill does

The reporting ritual from the strategy: one page per month comparing the frozen prompt set against baseline — mentions and positions by tier, per-engine slices, whether engines used the right descriptor, and what shipped that month. No vanity metrics, no blended averages hiding a dead tier.

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- The month's tracker run + evidence
- The baseline document
- The month's shipped actions (published, pitched, fixed)

## Workflow

1. **Lead with tier deltas** — Tier 3, 2, 1 movement vs baseline, in that order — the order the strategy says results arrive.
2. **Show engine slices** — Each engine's mention/citation rate separately. A blended 'AI visibility up 10%' line is banned.
3. **Report descriptor accuracy** — % of mentions using the canonical descriptor, with one wrong example quoted if any exist.
4. **Tie actions to movement** — List what shipped; state plainly where movement did NOT follow effort. Honest negatives keep the programme credible.
5. **Set next month's two priorities** — Derived from the data (weakest tier/engine), not from habit. Close the page with them.

## Output

A one-page monthly scorecard (deltas, slices, descriptor accuracy, actions, priorities).

## Measurement

Scorecard ships monthly without exception; every figure traceable to tracker rows; priorities visibly derived from the weakest data.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Never cherry-pick the best engine or tier for the headline. Stakeholders forgive slow months; they do not forgive discovering the cherry-pick.

## Fictional example

Fictional: a month-2 scorecard shows Tier 3 fixed, Tier 2 citations up on Perplexity only, Tier 1 flat — priorities: ChatGPT-weighted roundups, not more articles.
