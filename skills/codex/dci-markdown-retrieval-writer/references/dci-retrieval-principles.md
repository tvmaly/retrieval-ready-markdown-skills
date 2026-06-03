# DCI Retrieval Principles for Markdown Corpora

Summary: This reference explains how to write Markdown that supports Direct Corpus Interaction (DCI), local search, iterative narrowing, and local evidence verification.

Keywords: Direct Corpus Interaction; DCI; grep; ripgrep; rg; local corpus search; semantic retrieval; lexical anchors; local verification; Markdown retrieval; agentic search

## Definition: Direct Corpus Interaction for Markdown

Definition: Direct Corpus Interaction means an agent searches raw files directly with file discovery, exact matching, bounded reads, shell tools, or lightweight scripts rather than relying only on a fixed top-k retriever.

Rationale: DCI benefits when corpus text has stable names, exact anchors, nearby context, and line-level claims that can be searched and verified locally.

## Principle: Retrieval Needs Both Meaning and Exact Anchors

Decision: Important text should be semantically clear and include the exact words that future users are likely to search.

Examples of exact anchors: official names, abbreviations, aliases, versions, dates, paths, issue IDs, file names, commands, phase names, status words, and domain-specific terms.

Related terms: lexical search; semantic search; keyword search; sparse clues; query reformulation.

## Principle: Local Verification Beats Global Reading

Decision: A future DCI agent should be able to verify an important fact by reading nearby lines around a match.

Procedure: Put constraints, exceptions, rationale, and expected outcomes close to the claim they support.

Weak pattern: `This must happen first.`

Strong pattern: `Dependency: The  skill system must be implemented before the DCI phase because DCI is exposed as a reusable research skill.`

## Principle: Status Markers Prevent Stale Retrieval

Decision: Files or sections that may conflict with newer content should include explicit status markers.

Useful markers: `Status: draft`, `Status: current`, `Status: accepted`, `Status: superseded`, `Status: archived`, `Deprecated:`, `Supersedes:`, `Replaces:`.

## Principle: Sections Should Be Focused

Procedure: Keep sections focused on one decision, procedure, test area, or concept. Long mixed sections make it harder for a DCI agent to isolate the right evidence.

Expected: A search hit inside a section should indicate what topic, decision, or expectation the surrounding text supports.

## Principle: Avoid Retrieval Traps

Retrieval traps:

- generic filenames such as `notes.md` or `plan.md`;
- generic headings such as `Notes`, `Misc`, `Stuff`, or `More`;
- important claims expressed only with pronouns;
- duplicated drafts with no status marker;
- buried constraints inside long paragraphs;
- image-only or PDF-only evidence without a text equivalent;
- keyword stuffing that creates noisy false positives.
