# Retrieval-Ready Markdown Skills

Claude Code and Codex skills for creating Markdown that agents can find, inspect, verify, and cite with Direct Corpus Interaction (DCI), `grep`, `ripgrep`, local file reads, and semantic search.

## Why this exists

Developers increasingly ask agents to work from local notes, plans, runbooks, acceptance tests, research summaries, and project memory. Those files often contain the answer, but the answer is buried behind vague titles, missing keywords, unclear headings, or paragraphs that only make sense after reading the whole file.

These skills help Claude Code and Codex turn ordinary Markdown into retrieval-ready Markdown: content that can be discovered by broad search, narrowed with exact terms, and verified from nearby lines.

The skills are based on the DCI idea: instead of forcing every knowledge task through a vector index or top-k retriever, a capable agent can directly search the raw corpus with file discovery, exact matching, local reads, and iterative refinement.

## Jobs to be done

Use these skills when you want an agent to:

- create new Markdown files that will be easy to find later;
- rewrite vague notes into searchable, citable knowledge-base content;
- optimize implementation plans, acceptance tests, runbooks, ADRs, and research notes;
- add summaries, keywords, aliases, headings, status markers, and direct-answer lines;
- make important facts retrievable by both semantic meaning and exact lexical anchors;
- reduce agent mistakes caused by duplicate, stale, or ambiguous documents.

## What the skills improve

A retrieval-ready Markdown file should make every important fact findable three ways:

1. **Semantic meaning:** The surrounding text says what the fact means in normal developer language.
2. **Exact search:** The same paragraph includes useful anchors such as feature names, aliases, versions, paths, IDs, dates, and likely search phrases.
3. **Local verification:** Nearby lines explain the claim well enough that an agent can cite or edit the text without loading the whole repo into context.

## Included skills

```text
skills/
  claude-code/
    dci-markdown-retrieval-writer/
      SKILL.md
      templates/
      examples/
      reference/
  codex/
    dci-markdown-retrieval-writer/
      SKILL.md
      agents/openai.yaml
      assets/templates/
      examples/
      references/
      scripts/check_dci_markdown.py
```

## Quick start

Install both skills as user-level skills:

```bash
curl -fsSL https://raw.githubusercontent.com/tvmaly/retrieval-ready-markdown-skills/main/install.sh | bash
```

This installs:

```text
~/.claude/skills/dci-markdown-retrieval-writer/
~/.agents/skills/dci-markdown-retrieval-writer/
```

Install both skills into the current repository instead:

```bash
curl -fsSL https://raw.githubusercontent.com/tvmaly/retrieval-ready-markdown-skills/main/install.sh | bash -s -- --project .
```

This installs:

```text
.claude/skills/dci-markdown-retrieval-writer/
.agents/skills/dci-markdown-retrieval-writer/
```

Install only one agent target:

```bash
curl -fsSL https://raw.githubusercontent.com/tvmaly/retrieval-ready-markdown-skills/main/install.sh | bash -s -- --claude-only
curl -fsSL https://raw.githubusercontent.com/tvmaly/retrieval-ready-markdown-skills/main/install.sh | bash -s -- --codex-only
```

## Usage examples

Ask Claude Code:

```text
Use the dci-markdown-retrieval-writer skill to rewrite docs/auth-login-notes.md so future agents can find the current login failure runbook, cite exact steps, and distinguish it from archived notes.
```

Ask Codex:

```text
Use $dci-markdown-retrieval-writer to create a retrieval-ready acceptance test file for the DCI  skill-system prerequisite work.
```

Ask either agent:

```text
Create a Markdown implementation plan that is optimized for DCI-style local search. Include a summary, keywords, aliases, citable decisions, constraints, expected results, and status markers.
```

## Before and after

### Before

```md
# Login issue

Sometimes login fails after deploy. Check auth service. Restart it maybe. The token stuff can get weird.

Need to document this better later.
```

### After

```md
# Auth Service — Login Failure After Deployment

Summary: This runbook explains how to diagnose login failures that occur immediately after a deployment when the auth service has stale token validation state.

Status: current

Keywords: login failure; sign-in failure; authentication error; auth service; deployment; stale token; token validation; session cache; `/login`; 401; 403

## Problem: Login Fails After Deployment

Direct answer: If users cannot log in immediately after a deployment, check the auth service for stale token validation state and stale session cache entries.

Related terms: sign-in broken after release; authentication failure after deploy; users get 401 on login; users get 403 on login.

## Signals: Auth Service Token Validation Failure

Expected evidence: Requests to `/login` return `401` or `403`, and auth service logs mention stale signing keys, token validation failure, or session cache mismatch.

Constraint: Do not rotate production signing keys until the auth service logs confirm token validation errors or the on-call engineer approves the rotation.

## Procedure: Restore Login After Deployment

Procedure:
1. Restart the auth service workers.
2. Clear the stale session cache.
3. Retry `/login` with a test account.
4. Rotate signing keys only if token validation errors continue after cache clearing.

Owner: Platform/Auth team

Related files: `services/auth/`, `docs/runbooks/deploy.md`, `docs/runbooks/session-cache.md`
```

### What changed

The edited version is easier for an agent to retrieve because it adds:

- a specific title with the owning system and failure mode;
- a summary that states the question the file answers;
- exact keywords and aliases for likely search phrases;
- headings that separate problem, signals, constraints, and procedure;
- citable labels such as `Direct answer:`, `Expected evidence:`, `Constraint:`, and `Procedure:`;
- local verification context near the important claims.

## Optional Markdown checker

The Codex skill includes a lightweight heuristic checker:

```bash
python3 ~/.agents/skills/dci-markdown-retrieval-writer/scripts/check_dci_markdown.py docs/example.md
```

For project installs:

```bash
python3 .agents/skills/dci-markdown-retrieval-writer/scripts/check_dci_markdown.py docs/example.md
```

Treat checker warnings as review prompts, not hard failures.

## Repository maintenance

When changing either skill:

1. Keep the main `SKILL.md` concise.
2. Put long examples, templates, and checklists in supporting files.
3. Update both Claude Code and Codex versions when the retrieval rules change.
4. Keep the before/after example aligned with the skill instructions.
5. Run the checker on edited Markdown examples.

## References

- DCI paper: https://arxiv.org/pdf/2605.05242
- Claude Code skills docs: https://code.claude.com/docs/en/skills
- Codex skills docs: https://developers.openai.com/codex/skills
