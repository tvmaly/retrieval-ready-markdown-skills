# DCI Markdown Retrieval Checklist

Summary: Use this checklist before finishing Markdown files that should be easy to find, inspect, verify, and cite with DCI-style local search.

Keywords: DCI checklist; Markdown retrieval checklist; local corpus search; semantic retrieval; grep; ripgrep; citable facts; line references

## Discovery

- [ ] Filename names the entity, topic, and date or version when practical.
- [ ] Top-level title states the topic directly.
- [ ] `Summary:` appears near the top and says what question the document answers.
- [ ] `Status:` appears near the top when draft/current/accepted/superseded state matters.
- [ ] `Keywords:` includes official names, aliases, abbreviations, paths, and likely search phrases.

## Iterative Narrowing

- [ ] Important constraints use exact words such as `requires`, `depends on`, `blocked by`, `must`, `not allowed`, `deprecated`, `accepted`, or `current`.
- [ ] Project-specific terms appear near the claims they support.
- [ ] Similar entities, phases, files, or versions are disambiguated.
- [ ] Archived or superseded content is clearly labeled.
- [ ] Section headings are specific enough to be useful in `rg '^## '` output.

## Local Verification

- [ ] Each important fact is understandable within nearby lines.
- [ ] Vague pronouns have been replaced with explicit nouns where needed.
- [ ] Decisions, constraints, procedures, exceptions, and expected results are labeled.
- [ ] Related terms are near the fact they clarify.
- [ ] Facts that future agents may cite are not buried in long paragraphs.

## Chunk Quality

- [ ] Sections are focused and roughly 200-500 words when practical.
- [ ] Paragraphs contain one main idea.
- [ ] Unrelated topics are split into separate sections or files.
- [ ] Boilerplate does not appear before the useful content.
- [ ] Tables and lists include enough surrounding text to explain what they mean.

## Fidelity

- [ ] No facts, dates, owners, metrics, citations, or statuses were invented.
- [ ] Missing facts are marked as `TBD:` or `Needs evidence:`.
- [ ] Code blocks and citations were preserved unless the user asked to change them.
- [ ] Conflicts between files are marked instead of silently resolved.
