#!/usr/bin/env python3
"""
Skill workflow manager - pack and unpack skills

This is a thin wrapper around pack_skill.py and unpack_skill.py
for backward compatibility with existing workflows.

Usage:
    python skill_workflow.py pack <skill-directory>
    python skill_workflow.py unpack <skill-file> [--output-dir DIR] [--force]
"""

import sys
import subprocess
from pathlib import Path

# Paths
SCRIPT_DIR = Path(__file__).parent
PACK_SCRIPT = SCRIPT_DIR / "pack_skill.py"
UNPACK_SCRIPT = SCRIPT_DIR / "unpack_skill.py"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "pack":
        if len(sys.argv) < 3:
            print("Usage: python skill_workflow.py pack <skill-directory>")
            sys.exit(1)

        skill_dir = sys.argv[2]
        result = subprocess.run([sys.executable, str(PACK_SCRIPT), skill_dir])
        sys.exit(result.returncode)

    elif command == "unpack":
        if len(sys.argv) < 3:
            print("Usage: python skill_workflow.py unpack <skill-file> [--output-dir DIR] [--force]")
            sys.exit(1)

        # Pass all remaining arguments to unpack_skill.py
        args = sys.argv[2:]
        result = subprocess.run([sys.executable, str(UNPACK_SCRIPT)] + args)
        sys.exit(result.returncode)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
