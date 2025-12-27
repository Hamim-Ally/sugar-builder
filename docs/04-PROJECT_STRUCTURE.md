# SugarBuilder Project Structure

## Directory Layout

```
sugar-builder/
├── src/                          # Main Python package
│   ├── __init__.py              # Package initialization
│   ├── __main__.py              # CLI entry point
│   ├── main.py                  # Legacy entry point
│   │
│   ├── core/                    # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py            # TOML configuration loader
│   │   ├── project.py           # Project management
│   │   └── compiler.py          # Compiler enumeration
│   │
│   ├── toolchains/              # Compiler toolchain implementations
│   │   ├── __init__.py
│   │   ├── base.py              # Abstract base toolchain
│   │   ├── msvc.py              # Microsoft Visual C++ toolchain
│   │   ├── gcc.py               # GCC toolchain
│   │   └── clang.py             # Clang toolchain
│   │
│   ├── platforms/               # Platform abstractions
│   │   ├── __init__.py
│   │   └── base.py              # Base platform interface
│   │
│   └── commands/                # CLI command implementations
│       ├── __init__.py
│       ├── base.py              # Base command class
│       ├── configure.py         # Configuration validation command
│       └── build.py             # Build command
│
├── example/                      # Working example project
│   ├── src/                     # Example C++ source files
│   │   ├── main.cpp
│   │   ├── calculator.cpp
│   │   └── calculator.h
│   ├── sugar.toml               # Example configuration
│   └── README.md                # Example instructions
│
├── docs/                        # Documentation
│   ├── 01-README.md             # Documentation index
│   ├── 02-QUICK_REFERENCE.md    # Quick reference guide
│   ├── 03-GETTING_STARTED.md    # Detailed setup guide
│   ├── 04-PROJECT_STRUCTURE.md  # This file
│   ├── 05-COMPONENT_MAP.md      # Component relationships
│   ├── 06-PROJECT_TEMPLATES.md  # Project scaffolding
│   └── 07-RELEASE_NOTES.md      # Version history
│
├── build/                       # Build artifacts (generated)
│   └── sugar-builder/           # PyInstaller artifacts
│
├── tools/                       # Build and setup tools
│   ├── build.py                 # Build script
│   └── setup.py                 # Setup script
│
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── README.md                    # Main project README
├── requirements.txt             # Python dependencies
└── setup.ps1                    # Interactive setup script
```

## Core Components

### src/core/ - Configuration and Project Management

- **config.py** - Loads and validates `sugar.toml` configuration files
- **project.py** - Represents and manages project information
- **compiler.py** - Defines compiler types and detection logic

### src/toolchains/ - Compiler Implementations

Each toolchain:
1. Extends the base `Toolchain` class
2. Implements compiler-specific command generation
3. Handles platform-specific compilation flags

**Supported Toolchains:**
- **MSVC** - Microsoft Visual C++ for Windows
- **GCC** - GNU Compiler Collection for Linux/macOS/Windows
- **Clang** - LLVM Clang for Linux/macOS/Windows

### src/platforms/ - Platform Abstractions

- **base.py** - Defines platform interface and detection logic
- Handles OS-specific path conventions and file handling

### src/commands/ - CLI Commands

- **base.py** - Abstract command class
- **configure.py** - Configuration validation (`python -m src configure`)
- **build.py** - Project building (`python -m src build`)

## Data Flow

```
User Input
    ↓
CLI Parser (__main__.py)
    ↓
Command Dispatcher (base.py)
    ↓
Configure/Build Command
    ↓
Config Loader (config.py)
    ↓
Project Manager (project.py)
    ↓
Toolchain Selection (compiler.py)
    ↓
Compiler Implementation (msvc.py, gcc.py, clang.py)
    ↓
Execution & Output
```

## How Building Works

1. **Configuration Loading** - Reads `sugar.toml` using `config.py`
2. **Project Validation** - Checks source files and directories exist
3. **Compiler Detection** - Identifies available compilers using `compiler.py`
4. **Toolchain Selection** - Chooses appropriate compiler toolchain
5. **Command Generation** - Creates compiler-specific commands
6. **Compilation** - Executes compilation and linking
7. **Output** - Generates executable/library in output directory

## Dependencies

```
requirements.txt:
  └── tomli (Python 3.10 compatibility)
      └── TOML parsing for sugar.toml
```

Python 3.10+ includes `tomllib` natively, but for Python 3.10 compatibility we use `tomli`.

## File Naming Conventions

- **Module files** - lowercase with underscores: `config.py`, `compiler.py`
- **Classes** - PascalCase: `ConfigLoader`, `ProjectManager`
- **Functions/Methods** - snake_case: `load_config()`, `get_compiler()`
- **Constants** - UPPER_SNAKE_CASE: `MAX_WORKERS`, `BUILD_SUCCESS`

## Key Design Principles

1. **Modularity** - Each component has a single responsibility
2. **Extensibility** - Easy to add new compilers/platforms
3. **Type Safety** - 100% type hints for IDE support
4. **Cross-platform** - Abstractions for Windows/Linux/macOS
5. **User-friendly** - Clear error messages and logging
