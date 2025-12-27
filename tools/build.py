#!/usr/bin/env python3
"""
Build SugarBuilder as a standalone Windows executable.
This script uses PyInstaller to create a single .exe file.
"""

import subprocess
import sys
from pathlib import Path


def build_exe():
    """Build SugarBuilder executable using PyInstaller."""
    root = Path(__file__).parent
    main_script = root / "../src/main.py"
    
    if not main_script.exists():
        print(f"Error: {main_script} not found")
        return False
    
    print("Building SugarBuilder executable...")
    print(f"Source: {main_script}")
    
    # PyInstaller command
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",  # Create a single executable
        "--name",
        "sugar-builder",  # Executable name
        "--distpath",
        str(root / "../dist"),  # Output directory
        "--workpath",
        str(root / "../build"),  # Build temp directory
        "--specpath",
        str(root / "../build"),  # Spec file directory
        str(main_script),
    ]
    
    result = subprocess.run(cmd, cwd=str(root))
    
    if result.returncode == 0:
        exe_path = root / "dist" / "sugar-builder.exe"
        if exe_path.exists():
            print("\n" + "=" * 60)
            print("✓ Build successful!")
            print(f"Executable: {exe_path}")
            print(f"Size: {exe_path.stat().st_size / (1024*1024):.1f} MB")
            print("\nUsage:")
            print(f"  {exe_path} configure <config.toml>")
            print(f"  {exe_path} build [config.toml]")
            print("=" * 60)
            return True
    
    return False


if __name__ == "__main__":
    success = build_exe()
    sys.exit(0 if success else 1)
