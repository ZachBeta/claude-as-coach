#!/usr/bin/env python3
"""
Unpack a .skill ZIP file to a directory for editing.

.skill files have contents at ZIP root level:
  my-skill.zip
  ├── SKILL.md
  └── resources/

We extract to a named directory for local editing:
  skills/my-skill/
  ├── SKILL.md
  └── resources/

Usage:
    python unpack_skill.py <skill-file> [output-directory]

Examples:
    python unpack_skill.py daily-summary-base.zip
    python unpack_skill.py daily-summary-base.zip skills/daily-summary-base/
"""

import sys
import zipfile
import shutil
from pathlib import Path


def unpack_skill(skill_file: Path, output_dir: Path = None, force: bool = False) -> Path | None:
    """
    Unpack a skill ZIP file to a directory.

    Args:
        skill_file: Path to skill ZIP file
        output_dir: Destination directory. Defaults to {skill_name}/ next to ZIP file
        force: Overwrite existing directory

    Returns:
        Path to unpacked directory, or None on error
    """
    skill_file = Path(skill_file).resolve()

    # Validate file exists
    if not skill_file.exists():
        print(f"❌ Error: File not found: {skill_file}")
        return None

    if skill_file.suffix not in ['.zip', '.skill']:
        print(f"❌ Error: File must be a .zip file: {skill_file}")
        return None

    # Verify it's a ZIP
    if not zipfile.is_zipfile(skill_file):
        print(f"❌ Error: {skill_file.name} is not a valid ZIP archive")
        return None

    # Extract skill name from filename
    skill_name = skill_file.stem

    # Determine output directory
    if output_dir is None:
        output_dir = skill_file.parent / skill_name
    else:
        output_dir = Path(output_dir).resolve()

    # Check if target already exists
    if output_dir.exists() and not force:
        print(f"⚠️  Directory already exists: {output_dir}")
        print(f"   Use --force to overwrite, or specify different output directory")
        return output_dir

    print(f"📦 Unpacking: {skill_file.name}")
    print(f"   Destination: {output_dir}")

    # Remove existing directory if force is enabled
    if output_dir.exists() and force:
        print(f"   Removing existing directory...")
        shutil.rmtree(output_dir)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Extract all files
        with zipfile.ZipFile(skill_file, 'r') as zf:
            members = zf.namelist()
            if not members:
                print("❌ Error: Empty ZIP file")
                return None

            # Verify SKILL.md exists (handle both flat and nested formats)
            has_skill_md = any(
                m == 'SKILL.md' or m == 'Skill.md' or  # Flat format
                m.endswith('/SKILL.md') or m.endswith('/Skill.md')  # Nested format
                for m in members
            )
            if not has_skill_md:
                print(f"❌ Error: No SKILL.md found in {skill_file.name}")
                print(f"   Contents: {', '.join(members[:5])}")
                return None

            # Extract all files to output directory
            zf.extractall(output_dir)

            for member in members:
                print(f"  ✓ Extracted: {member}")

        print(f"\n✅ Unpacked to: {output_dir}")

        # Find SKILL.md (handle both flat and nested formats)
        skill_md_path = output_dir / "SKILL.md"
        if not skill_md_path.exists():
            skill_md_path = output_dir / "Skill.md"
        if not skill_md_path.exists():
            # Try nested format: output_dir/skill-name/SKILL.md
            nested_dir = output_dir / skill_name
            if nested_dir.exists():
                skill_md_path = nested_dir / "SKILL.md"
                if not skill_md_path.exists():
                    skill_md_path = nested_dir / "Skill.md"

        print(f"\n📝 Edit: {skill_md_path}")
        print(f"\n💡 Next steps:")
        print(f"   1. Edit the skill: {skill_md_path}")

        # For repack, use the directory containing SKILL.md
        pack_dir = skill_md_path.parent
        print(f"   2. Repack: python scripts/pack_skill.py {pack_dir}")

        return output_dir

    except Exception as e:
        print(f"❌ Error extracting .skill file: {e}")
        return None


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    skill_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    force = '--force' in sys.argv or '-f' in sys.argv

    result = unpack_skill(skill_file, output_dir, force)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
