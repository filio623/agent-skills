---
name: to-issues
description: Convert a plan, PRD, design, or discussion into clear GitHub issues. Use when the user asks to break work into issues, create tickets, define implementation tasks, or prepare scoped work items for a project.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/to-issues
---

# To Issues

Turn a plan into actionable issues that are independently understandable and reviewable.

## Workflow

1. Read the source material: PRD, plan, design doc, conversation, or code context.
2. Identify the workstreams and dependencies.
3. Split the work into issues that can be implemented and reviewed independently.
4. For each issue, define scope, acceptance criteria, implementation notes, and verification.
5. If GitHub CLI is configured and the user wants issues created, use `gh issue create`; otherwise produce markdown issue drafts.

## Issue Template

```markdown
## Summary

One concise paragraph describing the work.

## Scope

- What is included.
- What is explicitly out of scope.

## Acceptance Criteria

- Observable completion criteria.

## Implementation Notes

- Relevant files, modules, APIs, or constraints.

## Verification

- Tests, commands, or manual checks.
```

## Splitting Heuristics

- Keep each issue independently valuable when possible.
- Separate exploration from implementation.
- Separate backend, frontend, migration, and QA work when they can move independently.
- Do not create tiny issues for changes that must be reviewed together.
