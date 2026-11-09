---
name: prompt-set-tracker-design
description: |
  Design the tracking sheet/system for a prompt set: fields, engine slices, and a run protocol anyone can repeat identically.
  TRIGGERS - Use when user needs help with prompt tracking / visibility tracker / AEO tracking setup tasks.
category: Monitoring & Measurement
version: 1.0
---
# Prompt Set Tracker Design

## What this skill does

Specifies the tracker behind monthly measurement: one row per prompt x engine, fields for mention, position, descriptor accuracy, citations and answer links, plus the run protocol (fresh sessions, same wording, full answers saved) that makes months comparable.

Category: **Monitoring & Measurement** — Prove it monthly: frozen prompt sets, citation logs, scorecards and regression alerts — the discipline that separates AEO from superstition.

## Inputs

- The frozen prompt set (from ai-baseline-measurement)
- Engines in scope
- Who runs it and when

## Workflow

1. **Define the row structure** — Prompt, tier, engine, date, session type, mentioned, position, descriptor verdict, cited sources, owned-site cited, notes. No free-text-only logs.
2. **Write the run protocol** — Fresh/logged-out where feasible, prompts pasted verbatim, full answers saved to the evidence folder before scoring.
3. **Separate evidence from scores** — Raw answers live in dated files; the tracker holds scores + links to evidence. Scores without evidence are opinions.
4. **Add the summary views** — Per-tier and per-engine rollups computed from rows, never hand-typed — hand-typed summaries drift from data.
5. **Version the set** — Any prompt change increments the set version and restarts comparability; the tracker records which version each run used.

## Output

A tracker (sheet or table) with the run protocol document and summary views.

## Measurement

Runs completed on schedule with 100% evidence files present; zero summary figures that cannot be traced to rows.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not let the person who did the work also be the only person who can run the tracker. A bus-factor of one kills measurement within a quarter.

## Fictional example

Fictional: a 12-prompt x 6-engine tracker where every score links to a saved answer file; a disputed month is settled by opening the evidence, not by memory.
