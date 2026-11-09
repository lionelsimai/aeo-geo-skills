---
name: ai-crawler-access-audit
description: |
  Audit robots.txt, CDN and firewall rules for AI crawler access — and make the allow/block decision per crawler, deliberately.
  TRIGGERS - Use when user needs help with robots.txt AI crawlers / GPTBot access / AI crawler blocking tasks.
category: Structured Data & Technical
version: 1.0
---
# AI Crawler Access Audit

## What this skill does

Reviews how the site treats AI crawlers (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot and search crawlers): what is allowed, what is blocked, and whether the current state matches the entity's actual goal — being cited requires being readable.

Category: **Structured Data & Technical** — Layer 5, the technical floor: schema, llms.txt, crawler access and indexation — how engines connect and retrieve the facts.

## Inputs

- The live robots.txt and any CDN/WAF bot rules
- The entity's policy choice (maximise citation access vs restrict training use — these are different decisions)

## Workflow

1. **Fetch the live rules** — Pull robots.txt and check CDN bot settings; the intended policy and the live config often differ after migrations.
2. **Separate search from training** — List crawlers by function: answer/search retrieval vs training-data collection. Decide per group, not with one blanket rule.
3. **Check the key pages** — Verify the entity hub and flagship pages are not blocked by path rules, login walls or JS-only rendering for the allowed crawlers.
4. **Write the policy down** — One table: crawler, allow/block, reason, date decided. Future edits follow the table, not whoever is on call.
5. **Re-audit quarterly** — Crawler names and engine behaviours change; a 2025 blocklist silently blocking a 2026 answer engine is a common own-goal.

## Output

A crawler access table (current state vs intended policy) and the robots/CDN fixes to apply.

## Measurement

Zero unintended blocks on citation-critical pages; policy table reviewed quarterly.

## Guardrails

- **No fake citations.** Only cite sources that exist and say what you claim they say. Never invent a mention, a quote, a ranking or a review.
- **No fabricated stats.** Every number comes from the user's own data or a named public source. If a figure cannot be verified, mark it `[verify]` and leave it out of published copy.
- **White-hat only.** No spam directories, no paid listicle placements on SEO-spam roundups, no cloaking, no hidden text, no fake reviews, no doorway pages.
- **No guarantees.** AI answer placement cannot be guaranteed. State realistic ranges and timelines; engines change without notice.
- **Entity facts stay consistent.** Use the canonical bio and descriptor verbatim wherever the entity is described; flag any surface that contradicts it.
- Skill-specific: Blocking all AI crawlers while running an AEO programme is self-defeating for retrieval-based engines. If the choice is to block training crawlers, say so explicitly and accept the trade-off in writing.

## Fictional example

Fictional: a site migration accidentally disallows PerplexityBot on /insights/ — the exact folder holding its citable articles. Found in one audit pass.
