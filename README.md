# Agent Skills

A curated repository of reusable AI agent skills.

This repo is intended to be the source of truth for skills that can be pulled into different agent environments as needed. Keep each skill self-contained, concise, and easy for an agent to load only when relevant.

## Repository Layout

```text
agent-skills/
├── skills/                 # Published skills, one directory per skill
├── templates/skill-template/
│   └── SKILL.md            # Starting point for new skills
├── scripts/
│   └── validate_skills.py  # Local and CI validation
└── AGENTS.md               # Instructions for AI agents editing this repo
```

## Skill Layout

Each skill must include a `SKILL.md` file:

```text
skills/example-skill/
├── SKILL.md
├── agents/        # Optional UI metadata
├── scripts/       # Optional deterministic helpers
├── references/    # Optional detailed docs loaded only when needed
└── assets/        # Optional templates or files used as outputs
```

## Add a Skill

1. Copy `templates/skill-template` into `skills/<skill-name>`.
2. Edit `SKILL.md` with concise trigger metadata and operational instructions.
3. Add optional `scripts/`, `references/`, or `assets/` only when they directly support the skill.
4. Run validation:

```bash
python3 scripts/validate_skills.py
```

## Design Rules

- Make `name` and `description` specific enough that an agent knows when to use the skill.
- Keep `SKILL.md` concise. Move long details into `references/`.
- Do not add README files inside individual skill directories.
- Prefer scripts for fragile, repeated, or deterministic workflows.
- Avoid duplicating the same instructions across multiple skills.
