---
name: triage-issue
description: Investigate and triage a GitHub issue or bug report by reproducing context, finding likely root cause, and recommending next steps. Use when the user asks to triage an issue, analyze a bug report, investigate a regression, or decide whether an issue is actionable.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/triage-issue
---

# Triage Issue

Investigate an issue before implementing a fix. The goal is to determine whether the issue is valid, actionable, reproducible, and where the likely root cause lives.

## Workflow

1. Read the issue text, linked discussions, screenshots, logs, and reproduction steps.
2. Inspect the relevant code paths.
3. Try to reproduce the issue if the project can be run locally.
4. Determine whether the report is a bug, feature request, support question, duplicate, or invalid report.
5. Identify likely root cause and affected area.
6. Recommend labels, priority, owner, and next action.

## Output

Include:

- Summary.
- Reproduction status.
- Evidence.
- Likely root cause.
- Suggested labels or classification.
- Recommended next step.

If the issue is not actionable, state exactly what information is missing.

## GitHub CLI

If `gh` is authenticated and the user asks you to update GitHub, you may comment, label, or close the issue. Otherwise, draft the comment and recommendations locally.
