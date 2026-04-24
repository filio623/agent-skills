---
name: ubiquitous-language
description: Improve naming and domain language across a codebase by identifying inconsistent terminology and proposing a shared vocabulary. Use when the user asks about domain modeling, naming cleanup, confusing concepts, ubiquitous language, or aligning code with product language.
license: MIT
metadata:
  author: Matt Pocock
  source: https://github.com/mattpocock/skills/tree/main/ubiquitous-language
---

# Ubiquitous Language

Build or improve the shared vocabulary between product, domain experts, and code.

## Workflow

1. Inspect the relevant code, docs, tests, UI copy, and issue language.
2. List the domain concepts that appear repeatedly.
3. Identify synonyms, overloaded terms, ambiguous names, and mismatches between product language and code language.
4. Propose a vocabulary table.
5. Recommend targeted renames or documentation updates.
6. Separate safe mechanical renames from conceptual redesigns.

## Vocabulary Table

Use this shape:

```markdown
| Concept | Preferred Term | Avoid | Meaning | Code Locations |
|---------|----------------|-------|---------|----------------|
```

## Guidance

- Prefer terms users and domain experts already use.
- Do not rename stable code casually; weigh migration cost.
- Flag overloaded words that mean different things in different contexts.
- Avoid inventing abstractions before the vocabulary is stable.
