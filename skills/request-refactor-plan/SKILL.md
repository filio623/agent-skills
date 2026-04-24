---
name: request-refactor-plan
description: Create a practical refactor plan before changing code. Use when the user wants to improve structure, reduce complexity, migrate patterns, split work into phases, or make a risky code change safer.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/request-refactor-plan
---

# Request Refactor Plan

Plan a refactor before implementation. The plan should reduce risk, preserve behavior, and create reviewable steps.

## Workflow

1. Inspect the codebase area involved.
2. State the current architecture and pain points.
3. Identify behavior that must not change.
4. Find tests or commands that can verify safety.
5. Break the refactor into small commits or phases.
6. Call out migration risks, rollback points, and sequencing constraints.
7. Ask for approval before making large edits unless the user already asked for implementation.

## Plan Shape

Include:

- Goal.
- Non-goals.
- Files or modules likely involved.
- Proposed phases.
- Verification for each phase.
- Risks and mitigations.
- Decision points that need user input.

Prefer a plan that can be stopped safely after any phase.
