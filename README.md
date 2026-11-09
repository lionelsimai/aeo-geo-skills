# AEO & GEO Skills

**100 open-source skills for Answer Engine Optimization (AEO) and Generative
Engine Optimization (GEO)** — getting a brand, a company or a person cited,
named and recommended by AI answer engines: ChatGPT, Perplexity, Gemini,
Claude, Copilot and Google AI Overviews.

Built and maintained by **Lionel Sim** (The AI Capitol), Singapore —
from his own AEO/GEO programme positioning an expert in AI answers.
MIT licensed. Every skill is a folder with a `SKILL.md` in the open
Agent Skills format, runnable in Claude Code, Codex, Gemini CLI and any
runtime that reads skill folders.

## AEO vs GEO vs SEO — the short version

- **SEO** gets pages ranked in classic search results.
- **AEO** (Answer Engine Optimization) gets your facts *answered with*:
  engines resolve who you are, check independent corroboration, and lift
  short citable passages. AEO is SEO plus entity consistency plus
  citable structure — not a replacement for SEO.
- **GEO** (Generative Engine Optimization) is the same discipline named
  for generative engines (ChatGPT, Perplexity, Gemini, Claude): being
  *generated into* the answer and cited as its source.
- In practice AEO and GEO are one programme with two labels. This
  collection teaches that programme: measure first, fix the entity,
  publish citable content, earn corroboration, mind the technical floor,
  and re-measure monthly. White-hat only — no fake citations, no
  fabricated stats, no spam placements, and no guaranteed rankings,
  because nobody honest can guarantee what an answer engine will say.

## The 10 categories (10 skills each)

| Category | Layer it serves |
|---|---|
| AEO/GEO Strategy & Audits | Measure first: audits, baselines, share of voice, roadmaps |
| Entity & Knowledge Foundation | Layer 1 — one canonical identity engines can resolve |
| Citable Content | Layer 2 — pages built to be lifted and quoted |
| Structured Data & Technical | Layer 5 — schema, llms.txt, crawler access, indexation |
| Third-Party Corroboration | Layer 3 — independent sources saying the same thing |
| Platform Surfaces | Layer 4 — per-engine tactics: ChatGPT, Perplexity, Gemini, Copilot, Claude, Google |
| Brand & Expert Positioning | The person as an entity: bio, speaking, books, media |
| Monitoring & Measurement | Monthly prompt tracking, citation logs, scorecards |
| Local & Vertical AEO | Local, SaaS, ecommerce, professional services, healthcare and more |
| GEO Content Ops & Workflows | Freshness, briefs, calendars, QA gates, agency delivery |

Full index with a description per skill: [CATALOG.md](CATALOG.md)
(machine-readable: [catalog.json](catalog.json)).

## Install

### Claude Code — plugin marketplace

```text
/plugin marketplace add lionelsimai/aeo-geo-skills
/plugin install aeo-geo-skills@lionel-sim-skills
```

### Manual (any Agent Skills runtime)

```bash
git clone https://github.com/lionelsimai/aeo-geo-skills.git
cp -r aeo-geo-skills/<skill-slug> ~/.claude/skills/   # or your skills dir
```

Then describe the task ("run an AI visibility audit for…") and the
agent picks the skill up, or invoke it by name where your runtime
supports that.

## Validate the collection

```bash
python3 tools/validate.py
```

Checks all 100 skills for unique slugs, frontmatter compliance and
catalogue consistency. Regenerate the catalogue after editing the
taxonomy in `tools/data.py` with `python3 tools/generate.py`.

## The honesty rules (built into every skill)

- No fake citations, mentions, reviews or rankings — ever.
- No fabricated statistics; every number traces to a named source.
- White-hat only: no spam directories, paid listicle mills, cloaking
  or doorway pages.
- No guaranteed AI-answer placement. Timelines are stated as ranges
  and measured against a frozen baseline.

## Author

Lionel Sim — Founder, The AI Capitol and OpenBuilder (Singapore).
LinkedIn: https://sg.linkedin.com/in/lionelshen

## Licence

MIT — see [LICENSE](LICENSE).
