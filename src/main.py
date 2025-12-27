#!/usr/bin/env python3
"""
SugarBuilder - Manual C++ Build Tool
CLI entry point for executable creation.
"""

if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    # Add parent directory to path so src module can be imported
    sys.path.insert(0, str(Path(__file__).parent.parent))
    
    from src.__main__ import main
    sys.exit(main())
