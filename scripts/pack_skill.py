#!/usr/bin/env python3
"""
Pack a skill directory into a .skill ZIP file.

Correct format for Claude.ai:
  my-skill.zip
  ├── SKILL.md (at root level)
  └── resources/
      └── file.txt

Usage:
    python pack_skill.py <skill-directory> [output-file]

Examples:
    python pack_skill.py skills/daily-summary-base/
    python pack_skill.py skills/daily-summary-base/ skills/daily-summary-base.zip
"""

import sys
import zipfile
from pathlib import Path


def pack_skill(skill_dir: Path, output_file: Path = None) -> Path | None:
    """
    Pack a skill directory into a ZIP file with nested structure.

    Creates ZIP with skill directory as root:
        my-skill.zip
        └── my-skill/
            ├── SKILL.md
            └── resources/

    Args:
        skill_dir: Path to skill directory containing SKILL.md
        output_file: Optional output path. Defaults to {skill_dir.name}.zip in parent dir

    Returns:
        Path to created ZIP file, or None on error
    """
    skill_dir = Path(skill_dir).resolve()

    # Validate directory exists
    if not skill_dir.exists():
        print(f"❌ Error: Directory not found: {skill_dir}")
        return None

    if not skill_dir.is_dir():
        print(f"❌ Error: Not a directory: {skill_dir}")
        return None

    # Check for SKILL.md (try both cases for forward compatibility)
    skill_md = None
    for name in ["SKILL.md", "Skill.md"]:
        candidate = skill_dir / name
        if candidate.exists():
            skill_md = candidate
            break

    if not skill_md:
        print(f"❌ Error: No SKILL.md or Skill.md found in {skill_dir}")
        return None

    # Determine output file
    if output_file is None:
        output_file = skill_dir.parent / f"{skill_dir.name}.zip"
    else:
        output_file = Path(output_file).resolve()

    # Create parent directory if needed
    output_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"📦 Packing skill: {skill_dir.name}")
    print(f"   Source: {skill_dir}")
    print(f"   Output: {output_file}")

    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Add all files from skill directory
            # Files are nested inside skill-name/ directory per official docs
            skill_name = skill_dir.name
            for file_path in skill_dir.rglob('*'):
                if file_path.is_file():
                    # Calculate relative path and nest inside skill directory
                    arcname = Path(skill_name) / file_path.relative_to(skill_dir)
                    zf.write(file_path, arcname)
                    print(f"  ✓ Added: {arcname}")

        print(f"\n✅ Successfully created: {output_file}")
        return output_file

    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    result = pack_skill(skill_dir, output_file)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
