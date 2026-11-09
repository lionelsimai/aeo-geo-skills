# Contributing

Issues and pull requests welcome. The bar for contributions:

1. **White-hat only.** No skill may teach fake citations, fabricated
   statistics, spam placements, review manipulation, cloaking or
   guaranteed rankings. PRs adding them are closed.
2. **Keep the format.** Each skill is a folder `<slug>/SKILL.md` with
   frontmatter: `name` (== folder), `description` including a
   `TRIGGERS -` line, `category` (one of the 10 in CATALOG.md),
   `version`.
3. **Stay substantive.** A skill needs concrete steps, inputs/outputs,
   a measurement method and guardrails — no stub or template-only skills.
4. **Examples are fictional.** Never contribute a real client's or
   person's private audit data as an example.
5. **Validate before submitting.** Run `python3 tools/validate.py`
   and keep it green; if you change the taxonomy in `tools/data.py`,
   re-run `python3 tools/generate.py` so CATALOG.md and catalog.json
   stay in sync.
