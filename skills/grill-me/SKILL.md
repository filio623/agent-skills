---
name: grill-me
description: Interview the user rigorously about a plan, architecture, product decision, or design until the decision tree is resolved. Use when the user asks to be grilled, stress-test a plan, pressure-test assumptions, or turn vague intent into concrete choices.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/grill-me
---

# Grill Me

Interview the user relentlessly about every aspect of their plan until there is shared understanding.

## Workflow

1. Identify the plan, design, or decision being stress-tested.
2. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
3. Ask one question at a time.
4. For each question, provide your recommended answer or default.
5. If a question can be answered by exploring the codebase, inspect the codebase instead of asking.
6. Continue until the material choices, risks, constraints, and next actions are explicit.

## Question Style

- Prefer concrete tradeoff questions over broad open-ended prompts.
- Make the implicit decision visible before asking.
- Do not ask questions just to gather context that can be found in local files.
- When the user answers, update the decision tree and ask the next blocking question.

## Output

When the interview is complete, summarize:

- Resolved decisions
- Open risks
- Assumptions
- Recommended next steps
