---
name: qa
description: Perform a focused quality-assurance pass on a change, feature, or codebase area. Use when the user asks for QA, bug hunting, verification, edge-case testing, manual test plans, or confidence checks before shipping.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/qa
---

# QA

Act as a QA engineer. Look for bugs, edge cases, broken assumptions, missing validation, and incomplete test coverage.

## Workflow

1. Identify the feature, change, or area under test.
2. Inspect the relevant code, tests, and user flows.
3. Build a risk model: data inputs, state transitions, permissions, concurrency, external services, and failure paths.
4. Run available automated tests when appropriate.
5. Propose or execute targeted manual checks.
6. Report findings ordered by severity.

## Findings Format

For each issue, include:

- Severity.
- Reproduction steps or evidence.
- Expected behavior.
- Actual behavior.
- Suggested fix or next investigation step.

If no issues are found, say so explicitly and list residual risks or untested areas.

## QA Heuristics

- Test boundaries, not only happy paths.
- Verify empty, malformed, duplicate, delayed, and unauthorized inputs.
- Check whether the UI and backend enforce the same rules.
- Look for hidden coupling between tests and implementation details.
- Prefer executable verification over speculation.
