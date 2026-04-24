# Agent Instructions

This repository stores reusable AI agent skills. Treat GitHub as the source of truth; the local checkout is only a working copy.

## Conventions

- Published skills live in `skills/<skill-name>/`.
- Every skill must have `SKILL.md` with YAML frontmatter containing `name` and `description`.
- Skill directory names should be lowercase kebab-case.
- Do not create `README.md`, `CHANGELOG.md`, or setup docs inside individual skill directories.
- Keep skill bodies concise and operational. Put long reference material in `references/`.
- Use `scripts/` for deterministic helpers and `assets/` for output resources.

## Validation

Run this before committing:

```bash
python3 scripts/validate_skills.py
```

## Editing Rules

- Preserve existing user-authored skills unless explicitly asked to modify them.
- Prefer adding a new skill from `templates/skill-template/`.
- Keep changes small and reviewable.
