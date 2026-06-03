# DCI Markdown Retrieval Writer Examples

Summary: These examples show weak Markdown patterns and DCI-friendly rewrites that improve discovery, narrowing, and local verification.

Keywords: DCI examples; Markdown retrieval examples; before and after;  DCI; citable labels; local verification

## Example 1: Prerequisite Clarity

Weak:

```md
## Notes

This has to happen first. Then the new mode can be added later.
```

Better:

```md
## Prerequisite: Skill System Must Exist Before DCI

Dependency: The  skill system must be implemented before the DCI phase because the DCI research workflow is delivered as a reusable skill over local workspace files.

Related terms: Direct Corpus Interaction; DCI;  skill system; DCI research mode; local workspace search.
```

## Example 2: Bounded Search Constraint

Weak:

```md
Search should be safe and not too broad.
```

Better:

```md
## Constraint: DCI Search Roots Are Bounded

Constraint: DCI search roots are limited to configured corpus directories such as `~/./workspace` and project curriculum folders. Whole-home-directory search is not allowed by default.

Rationale: Bounded search reduces false positives, cost, latency, and accidental exposure of unrelated files.
```

## Example 3: Acceptance-Test Retrieval Anchors

Weak:

```md
The search tool should return good results.
```

Better:

```md
## Acceptance Test: Search Results Include File and Line References

Scenario: A user searches the configured DCI corpus for `skill system prerequisite`.

Expected: `dci_search` returns each match with a relative file path, line number, matching line, and bounded surrounding context.
```

## Example 4: Disambiguation

Weak:

```md
Use the Lite project as the basis.
```

Better:

```md
## Disambiguation: DCI-Agent-Lite Versus  DCI

Disambiguation: DCI-Agent-Lite is the minimal reference scaffold from the DCI paper. The  DCI phase is inspired by that scaffold, but it should use 's existing Go tool-source and skill-system architecture rather than copying the Python harness directly.
```

## Example 5: Stale Content Marker

Weak:

```md
The DCI command should search everything under the user's home directory.
```

Better:

```md
## Status: Superseded Broad Search Proposal

Status: superseded

Superseded decision: The earlier proposal to search the whole home directory is not current.

Current constraint: DCI search roots must be bounded to configured corpus paths such as `~/./workspace` and project curriculum directories.
```
