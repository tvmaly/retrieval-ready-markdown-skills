# DCI Markdown Retrieval Writer — Codex Skill

This is a Codex-compatible skill for creating or modifying Markdown files so they are easier to retrieve with Direct Corpus Interaction (DCI), `grep`, `ripgrep`, local file search, and semantic/agentic retrieval.

The skill helps Codex add useful retrieval affordances to Markdown corpus files:

- direct titles and summaries;
- high-signal keywords and aliases;
- specific headings;
- citable labels such as `Decision:`, `Constraint:`, `Expected:`, and `Procedure:`;
- local verification context around important facts;
- status, disambiguation, and conflict markers.

## Skill contents

```text
dci-markdown-retrieval-writer-codex/
  SKILL.md
  README.md
  agents/openai.yaml
  assets/templates/dci-optimized-document.md
  assets/templates/dci-section-template.md
  examples/before-after.md
  references/dci-markdown-checklist.md
  references/dci-retrieval-principles.md
  scripts/check_dci_markdown.py
```

## Install as a repo skill

From the directory containing this folder:

```bash
mkdir -p .agents/skills
cp -R dci-markdown-retrieval-writer-codex .agents/skills/dci-markdown-retrieval-writer
```

Run Codex from the repository root or a subdirectory where repo skills are discovered.

## Install as a personal skill

```bash
mkdir -p "$HOME/.agents/skills"
cp -R dci-markdown-retrieval-writer-codex "$HOME/.agents/skills/dci-markdown-retrieval-writer"
```

Restart Codex if the skill does not appear immediately.

## Example prompts

```text
Use $dci-markdown-retrieval-writer to create a DCI-optimized implementation plan for this feature.
```

```text
Use $dci-markdown-retrieval-writer to rewrite docs/notes.md so a DCI agent can find and cite the important decisions.
```

```text
Use $dci-markdown-retrieval-writer to add summaries, keywords, headings, and citable expected results to this acceptance-test file.
```

## Optional checker

After installing the skill, Codex can run:

```bash
python3 .agents/skills/dci-markdown-retrieval-writer/scripts/check_dci_markdown.py docs/file.md
```

The checker is heuristic. Treat warnings as review prompts, not hard failures.
