---
name: to-prd
description: Convert an idea, user request, or rough feature discussion into a product requirements document. Use when the user asks for a PRD, spec, product brief, requirements, scope definition, or implementation-ready feature plan.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/to-prd
---

# To PRD

Turn rough product intent into a clear product requirements document.

## Workflow

1. Identify the user problem, target users, and business context.
2. Ask only blocking questions; infer reasonable defaults when the answer is not critical.
3. Define goals, non-goals, user stories, functional requirements, and edge cases.
4. Include technical constraints only when they materially affect product scope.
5. Produce a PRD that can be handed to engineering or converted into issues.

## PRD Template

```markdown
# Product Requirements Document

## Summary

## Problem

## Goals

## Non-Goals

## Users

## User Stories

## Requirements

## Edge Cases

## Success Metrics

## Open Questions

## Rollout / QA Notes
```

## Quality Bar

- Requirements should be testable.
- Non-goals should prevent scope creep.
- Open questions should be real blockers, not generic placeholders.
- Avoid implementation detail unless needed to clarify feasibility or constraints.
