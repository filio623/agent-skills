#!/usr/bin/env python3
"""Validate skill directories in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_KEYS = ("name", "description")
DISALLOWED_SKILL_FILES = {
    "CHANGELOG.md",
    "INSTALLATION_GUIDE.md",
    "QUICK_REFERENCE.md",
    "README.md",
}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str | None]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, "missing YAML frontmatter"

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, "unterminated YAML frontmatter"

    metadata: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            return {}, f"invalid frontmatter line: {line!r}"
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"'")

    return metadata, None


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []

    if not NAME_RE.fullmatch(skill_dir.name):
        errors.append(f"{skill_dir}: directory name must be lowercase kebab-case")

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        errors.append(f"{skill_dir}: missing SKILL.md")
        return errors

    metadata, parse_error = parse_frontmatter(skill_file)
    if parse_error:
        errors.append(f"{skill_file}: {parse_error}")
        return errors

    for key in REQUIRED_KEYS:
        if not metadata.get(key):
            errors.append(f"{skill_file}: missing required frontmatter key {key!r}")

    if metadata.get("name") and metadata["name"] != skill_dir.name:
        errors.append(
            f"{skill_file}: frontmatter name must match directory name "
            f"({metadata['name']!r} != {skill_dir.name!r})"
        )

    if len(metadata.get("description", "")) < 40:
        errors.append(f"{skill_file}: description should be specific and at least 40 characters")

    for filename in DISALLOWED_SKILL_FILES:
        if (skill_dir / filename).exists():
            errors.append(f"{skill_dir / filename}: avoid auxiliary docs inside skill directories")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"Missing skills directory: {SKILLS_DIR}", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    errors: list[str] = []

    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
