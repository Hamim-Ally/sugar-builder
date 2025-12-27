# SugarBuilder Project Map

This document describes the relationships and interactions between different components of SugarBuilder.

## Component Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        User Interface                       │
│                   (Command Line / __main__)                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Command Dispatcher                       │
│              (ConfigureCommand / BuildCommand)              │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              Configuration Management Layer                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Config Loader (config.py)                           │   │
│  │ - Reads sugar.toml                                  │   │
│  │ - Validates configuration                           │   │
│  │ - Returns ConfigData object                         │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                 Project Management Layer                    │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Project Manager (project.py)                        │   │
│  │ - Organizes project structure                       │   │
│  │ - Locates source files                              │   │
│  │ - Manages build artifacts                           │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│            Compiler Detection & Selection Layer             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Compiler Detection (compiler.py)                    │   │
│  │ - Detects available compilers                       │   │
│  │ - Validates compiler selection                      │   │
│  │ - Returns Compiler enum                             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Toolchain Layer                          │
│  ┌──────────────┬──────────────┬──────────────────────┐    │
│  │  MSVC Tool   │   GCC Tool   │   Clang Tool         │    │
│  │  (msvc.py)   │   (gcc.py)   │   (clang.py)         │    │
│  │              │              │                      │    │
│  │ - Command    │ - Command    │ - Command generation │    │
│  │   generation │   generation │ - Linker setup       │    │
│  │ - Flags      │ - Flags      │ - Standard flags     │    │
│  │ - Linking    │ - Linking    │                      │    │
│  └──────────────┴──────────────┴──────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Execution Layer                            │
│  - Runs compiler commands                                   │
│  - Captures output/errors                                   │
│  - Reports results                                          │
└─────────────────────────────────────────────────────────────┘
```

## Dependency Graph

```
__main__.py
    ├── ConfigureCommand
    │   └── config.py (ConfigLoader)
    │       └── compiler.py (CompilerType, detect_compiler)
    │
    └── BuildCommand
        ├── config.py (ConfigLoader)
        ├── project.py (ProjectManager)
        ├── compiler.py (CompilerType, detect_compiler)
        └── toolchains/
            ├── base.py (Toolchain abstract class)
            ├── msvc.py (MSVCToolchain)
            ├── gcc.py (GCCToolchain)
            └── clang.py (ClangToolchain)
```

## Data Flow for Build Command

```
1. Parse Arguments
   Input: Command-line args (--config path)
   Output: Parsed config path

2. Load Configuration
   Input: Config file path
   Module: config.py
   Output: ConfigData object with:
           - project_name
           - project_type (exe/static/shared)
           - compiler
           - platform
           - source_paths
           - build_path
           - output_path

3. Create Project Manager
   Input: ConfigData
   Module: project.py
   Output: ProjectManager with:
           - Source file list
           - Build directory structure
           - Output path

4. Detect/Validate Compiler
   Input: CompilerType enum, ProjectManager
   Module: compiler.py
   Output: Validated compiler executable path

5. Select Toolchain
   Input: Compiler type, ProjectManager
   Module: Appropriate toolchain (msvc.py, gcc.py, clang.py)
   Output: Toolchain instance

6. Generate Commands
   Input: Source files, build settings
   Module: Toolchain.generate_*_command()
   Output: List of compiler commands to execute

7. Execute Build
   Input: Generated commands
   Module: subprocess or platform API
   Output: Compiled executables/libraries

8. Report Results
   Input: Build output/errors
   Output: User-friendly success/failure message
```

## Module Interaction Patterns

### Pattern 1: Configuration Loading
```
User Request
    ↓
ConfigureCommand.execute()
    ↓
ConfigLoader.load() from config.py
    ↓
Parse TOML → Validate → Return ConfigData
```

### Pattern 2: Compiler Detection
```
ConfigData (compiler: "MSVC")
    ↓
detect_compiler() from compiler.py
    ↓
Check system for compiler executable
    ↓
Return compiler path or raise error
```

### Pattern 3: Build Process
```
ConfigData + ProjectManager
    ↓
Select appropriate Toolchain
    ↓
Generate compilation commands
    ↓
Execute each command
    ↓
Output artifacts to build_path and output_path
```

## Key Classes and Their Responsibilities

| Class | Module | Responsibility |
|-------|--------|-----------------|
| `ConfigData` | config.py | Represents loaded configuration |
| `ConfigLoader` | config.py | Loads and validates TOML files |
| `ProjectManager` | project.py | Manages project structure and files |
| `Compiler` | compiler.py | Enum for compiler types |
| `Toolchain` | base.py | Abstract compiler implementation |
| `MSVCToolchain` | msvc.py | MSVC-specific implementation |
| `GCCToolchain` | gcc.py | GCC-specific implementation |
| `ClangToolchain` | clang.py | Clang-specific implementation |
| `ConfigureCommand` | commands/configure.py | CLI validate command |
| `BuildCommand` | commands/build.py | CLI build command |

## Extension Points

To add support for a new compiler:

1. **Create new toolchain** - Extend `Toolchain` in `toolchains/yourcompiler.py`
2. **Add to Compiler enum** - Update `compiler.py`
3. **Update detection** - Add detection logic in `compiler.py`
4. **Update imports** - Register in `toolchains/__init__.py`

Example:
```python
# toolchains/icc.py
from .base import Toolchain

class ICCToolchain(Toolchain):
    def generate_compile_command(self, source_file):
        # ICC-specific compilation
        pass
    
    def generate_link_command(self, object_files):
        # ICC-specific linking
        pass
```

## Platform Support

The project abstracts platform differences:

```
platforms/
    └── base.py
        ├── Detect current platform
        ├── Provide path normalization
        ├── Handle executable extensions (.exe on Windows)
        └── Manage line endings and separators
```

Each toolchain can override platform-specific behavior as needed.
