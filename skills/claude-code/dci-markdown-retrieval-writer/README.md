# DCI Markdown Retrieval Writer Claude Code Skill

This Claude Code skill creates or modifies Markdown files so they are easier for Direct Corpus Interaction (DCI), agentic search, grep/ripgrep, and semantic retrieval tools to find, inspect, verify, and cite.

## Install as a project skill

Copy the folder into a repository:

```bash
mkdir -p .claude/skills
cp -R dci-markdown-retrieval-writer .claude/skills/
```

## Install as a personal skill

Copy the folder into your user skills directory:

```bash
mkdir -p ~/.claude/skills
cp -R dci-markdown-retrieval-writer ~/.claude/skills/
```

## Example prompts

```text
Create a DCI-optimized markdown plan for this feature.
```

```text
Rewrite docs/notes.md so it is easier to retrieve with DCI-style local search.
```

```text
Add summaries, keywords, headings, and citable decision labels to this acceptance-test file.
```
