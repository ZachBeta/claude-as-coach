#!/usr/bin/env python3
"""
Test script to create skills in both formats:
- Format A (flat): SKILL.md at ZIP root
- Format B (nested): SKILL.md inside skill-name/ folder

This helps determine which format Claude.ai actually expects.

Usage:
    python test_both_formats.py <skill-directory>

Example:
    python test_both_formats.py skills/daily-summary-base/
"""

import sys
import zipfile
from pathlib import Path


def create_flat_zip(skill_dir: Path, output_file: Path) -> Path:
    """
    Format A (Flat): Files at ZIP root level

    Structure:
        my-skill.zip
        ├── SKILL.md
        └── resources/
    """
    print(f"\n📦 Creating Format A (FLAT)...")
    print(f"   Output: {output_file}")

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_dir.rglob('*'):
            if file_path.is_file():
                # Files go directly at root level
                arcname = file_path.relative_to(skill_dir)
                zf.write(file_path, arcname)
                print(f"   ✓ Added: {arcname}")

    print(f"   ✅ Created: {output_file}")
    return output_file


def create_nested_zip(skill_dir: Path, output_file: Path) -> Path:
    """
    Format B (Nested): Files inside skill-name/ directory

    Structure:
        my-skill.zip
        └── my-skill/
            ├── SKILL.md
            └── resources/
    """
    print(f"\n📦 Creating Format B (NESTED)...")
    print(f"   Output: {output_file}")

    skill_name = skill_dir.name

    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_dir.rglob('*'):
            if file_path.is_file():
                # Files go inside skill-name/ directory
                arcname = Path(skill_name) / file_path.relative_to(skill_dir)
                zf.write(file_path, arcname)
                print(f"   ✓ Added: {arcname}")

    print(f"   ✅ Created: {output_file}")
    return output_file


def compare_zips(flat_zip: Path, nested_zip: Path):
    """Show side-by-side comparison of ZIP contents."""
    print("\n" + "=" * 80)
    print("COMPARISON: ZIP Contents")
    print("=" * 80)

    print("\n📋 Format A (FLAT) - Current Implementation:")
    print("-" * 40)
    with zipfile.ZipFile(flat_zip, 'r') as zf:
        for info in zf.infolist():
            print(f"  {info.filename}")

    print("\n📋 Format B (NESTED) - Documentation Format:")
    print("-" * 40)
    with zipfile.ZipFile(nested_zip, 'r') as zf:
        for info in zf.infolist():
            print(f"  {info.filename}")

    print("\n" + "=" * 80)
    print("Key Difference:")
    print("  Format A: SKILL.md at root")
    print("  Format B: SKILL.md inside {skill-name}/ directory")
    print("=" * 80)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    skill_dir = Path(sys.argv[1]).resolve()

    # Validate skill directory
    if not skill_dir.exists() or not skill_dir.is_dir():
        print(f"❌ Error: Not a valid directory: {skill_dir}")
        sys.exit(1)

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: No SKILL.md found in {skill_dir}")
        sys.exit(1)

    skill_name = skill_dir.name

    # Create test output directory
    test_dir = Path("test")
    test_dir.mkdir(exist_ok=True)

    print("=" * 80)
    print(f"Testing Skill Packaging Formats: {skill_name}")
    print("=" * 80)

    # Create both formats
    flat_zip = test_dir / f"{skill_name}-flat.zip"
    nested_zip = test_dir / f"{skill_name}-nested.zip"

    create_flat_zip(skill_dir, flat_zip)
    create_nested_zip(skill_dir, nested_zip)

    # Show comparison
    compare_zips(flat_zip, nested_zip)

    print("\n✅ Test files created successfully!")
    print(f"\n📝 Next Steps:")
    print(f"   1. Upload {flat_zip} to Claude.ai")
    print(f"   2. Upload {nested_zip} to Claude.ai")
    print(f"   3. Test which format works (or if both work)")
    print(f"   4. Document findings in docs/SKILL-FORMAT-TESTING.md")
    print()


if __name__ == "__main__":
    main()
