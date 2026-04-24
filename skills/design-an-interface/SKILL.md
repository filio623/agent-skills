---
name: design-an-interface
description: Design a clean software interface or API by exploring multiple alternatives, comparing tradeoffs, and recommending a concrete shape. Use when the user asks for interface design, module boundaries, public APIs, adapters, service contracts, or abstraction design.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/design-an-interface
---

# Design An Interface

Help the user design an interface before implementation. The goal is to make the boundary clear, small, and hard to misuse.

## Workflow

1. Identify the behavior the interface must expose.
2. Inspect the local codebase for existing callers, types, conventions, and constraints.
3. State the forces acting on the design: simplicity, flexibility, testability, performance, migration cost, and future extension.
4. Produce at least three materially different interface designs.
5. Show short usage examples for each design.
6. Compare tradeoffs and recommend one option.
7. If implementation is requested, implement only after the interface direction is chosen.

## Design Constraints

- Prefer a small public surface hiding a larger implementation.
- Make the common path easy and the unsafe path explicit.
- Avoid abstractions that merely rename existing implementation details.
- Prefer concrete examples over abstract descriptions.
- Design from the caller's perspective first, then validate implementation feasibility.

## Output

For each candidate interface, include:

- Signature or shape.
- Usage example.
- What complexity it hides.
- What future changes it handles well.
- What it makes harder.

End with a clear recommendation.
