---
name: entity-resolution-diagnostic
description: |
  Diagnose why AI engines misdescribe, confuse or hedge on an entity — and which conflicting signals cause it.
  TRIGGERS - Use when user needs help with entity confusion / wrong facts in AI answers / entity resolution tasks.
category: AEO/GEO Strategy & Audits
version: 1.0
---
# Entity Resolution Diagnostic

## What this skill does

Traces wrong or hedged AI descriptions back to their sources: conflicting bios, stale coverage, name collisions, and outdated high-authority pages. Produces a conflict list with the fix for each source.

Category: **AEO/GEO Strategy & Audits** — Know where the brand stands in AI answers before spending anything: audits, baselines, share of voice and roadmaps.

## Inputs

- The wrong/hedged answers captured in an audit
- The entity's canonical facts (name, role, org, place, works)
- The entity's top 15 public surfaces

## Workflow

1. **Collect the wrong claims** — From saved answers, extract every factual claim about the entity and mark correct / stale / wrong.
2. **Trace each wrong claim** — Search the claim's phrasing; find the page it came from (old employer coverage, an outdated bio, a namesake). Record the source URL per claim.
3. **Check for collisions** — Same-name people or companies in adjacent fields get their own line: what the engine merges, and what disambiguator (place, org, descriptor) separates them.
4. **Rank by authority** — A wrong fact on a high-authority page outranks five correct small pages. Fix order follows source authority.
5. **Assign the fix per source** — Update it, correct it via the publisher, or out-publish it with the canonical fact repeated on stronger surfaces.

## Output

A conflict table (claim, verdict, source, authority, fix) ordered by fix priority.

## Measurement

Re-run the identity prompt monthly. Success = the 'Who is X?' answer leads with canonical facts and stale claims disappear from answers.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Do not argue with the engine. Engines repeat sources; fix or out-publish the source, and the answer follows.

## Fictional example

Fictional: 'Who is Daniel Teo?' returns a 2021 employer because that coverage dominates. The diagnostic traces 4 of 5 wrong claims to two stale pages.
