---
name: improve-codebase-architecture
description: Explore a codebase to find architectural improvement opportunities, focusing on deeper modules, simpler boundaries, better testability, and more AI-navigable code. Use when the user wants architecture review, refactoring opportunities, module consolidation, or testability improvements.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/improve-codebase-architecture
---

# Improve Codebase Architecture

Explore a codebase like an AI would, surface architectural friction, discover opportunities for improving testability, and propose module-deepening refactors as RFCs or GitHub issues.

A deep module, following John Ousterhout's framing in "A Philosophy of Software Design", has a small interface hiding a large implementation. Deep modules are more testable, more AI-navigable, and let tests target boundaries instead of internals.

## Process

### 1. Explore the codebase

Use available code exploration tools to navigate naturally. Do not follow rigid heuristics; explore organically and note where understanding the codebase creates friction.

Look for:

- Places where understanding one concept requires bouncing between many small files.
- Modules where the interface is nearly as complex as the implementation.
- Pure functions extracted mainly for testability while real bugs hide in orchestration.
- Tightly-coupled modules that create integration risk at their seams.
- Code that is untested or hard to test through public boundaries.

The friction you encounter is the signal.

### 2. Present candidates

Present a numbered list of deepening opportunities. For each candidate, show:

- **Cluster**: Which modules or concepts are involved.
- **Why they are coupled**: Shared types, call patterns, or co-owned concepts.
- **Dependency category**: Use the categories in [REFERENCE.md](REFERENCE.md).
- **Test impact**: What existing tests could be replaced by boundary tests.

Do not propose interfaces yet. Ask the user which candidate they want to explore.

### 3. Frame the problem space

For the selected candidate, write a user-facing explanation of:

- The constraints any new interface must satisfy.
- The dependencies it needs to rely on.
- A rough illustrative code sketch to ground the constraints.

This sketch is not a proposal. It exists to make the constraints concrete.

### 4. Design multiple interfaces

If the host agent supports parallel sub-agents and the user has authorized their use, spawn three or more agents to design radically different interfaces. Otherwise, produce the alternative designs yourself while keeping the same diversity constraints.

Use different design constraints:

- Minimize the interface; aim for one to three entry points.
- Maximize flexibility and future extension.
- Optimize for the most common caller so the default case is trivial.
- Use ports and adapters when the dependency crosses an owned network boundary.

Each design should include:

- Interface signature.
- Usage example.
- Complexity hidden internally.
- Dependency strategy from [REFERENCE.md](REFERENCE.md).
- Tradeoffs.

### 5. Recommend a direction

Present the designs sequentially, compare them in prose, and give a strong recommendation. If a hybrid is best, propose it clearly.

### 6. Capture the RFC

Create a refactor RFC using the template in [REFERENCE.md](REFERENCE.md). If GitHub CLI is configured and the user wants an issue filed, use `gh issue create`; otherwise write the RFC as markdown for review.
