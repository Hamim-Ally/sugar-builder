# SugarBuilder Project Skeleton

This document describes the initial project structure and how to scaffold new SugarBuilder projects.

## Minimal Project Structure

```
my-project/
├── src/
│   └── main.cpp
└── sugar.toml
```

This is the absolute minimum required to build with SugarBuilder.

## Basic Project Structure

```
my-project/
├── src/
│   ├── main.cpp
│   ├── util.cpp
│   └── util.h
├── include/
│   └── util.h
├── sugar.toml
└── .gitignore
```

## Recommended Project Structure

```
my-project/
├── src/                          # Source files
│   ├── main.cpp
│   ├── module1.cpp
│   ├── module2.cpp
│   └── internal/
│       ├── helper.cpp
│       └── helper.h
│
├── include/                      # Public headers
│   ├── module1.h
│   └── module2.h
│
├── third_party/                  # External dependencies
│   └── mylib/
│       ├── lib/
│       └── include/
│
├── build/                        # Build artifacts (generated)
│   └── *.o                       # Object files
│
├── bin/                          # Output binaries (generated)
│   └── my-project               # Executable
│
├── docs/                         # Documentation
│   ├── README.md
│   ├── USAGE.md
│   └── API.md
│
├── tests/                        # Unit tests
│   ├── test_module1.cpp
│   └── test_module2.cpp
│
├── sugar.toml                    # SugarBuilder configuration
├── .gitignore                    # Git ignore rules
├── LICENSE                       # Project license
└── README.md                     # Project README
```

## Configuration Skeleton

### Minimal sugar.toml

```toml
project_name = "my-project"
project_type = "exe"

compiler = "GCC"
platform = "Linux"

source_paths = ["src"]
build_path = "build"
output_path = "bin"
```

### Complete sugar.toml

```toml
# Project Information
project_name = "my-project"
project_type = "exe"              # exe, static, shared
project_version = "1.0.0"

# Compiler Settings
compiler = "GCC"                  # MSVC, GCC, or Clang
platform = "Linux"                # Windows, Linux, macOS

# Directory Paths (relative to sugar.toml location)
source_paths = ["src", "src/internal"]
include_paths = ["include", "third_party/mylib/include"]
build_path = "build"
output_path = "bin"

# Compilation Flags (optional)
# cpp_standard = "17"             # 11, 14, 17, 20
# optimization = "O2"             # O0, O1, O2, O3
# debug = true                    # Enable debugging symbols

# Linking (optional)
# link_directories = ["third_party/mylib/lib"]
# link_dependencies = ["mylib", "pthread", "m"]

# Output Options (optional)
# output_name = "my-custom-name"  # Override executable name
```

## Common Project Patterns

### Console Application

```
my-app/
├── src/
│   ├── main.cpp               # Entry point
│   └── app.cpp                # Application logic
├── include/
│   └── app.h
└── sugar.toml
```

Configuration:
```toml
project_name = "my-app"
project_type = "exe"
source_paths = ["src"]
include_paths = ["include"]
```

### Library (Static)

```
my-lib/
├── src/
│   ├── module1.cpp
│   └── module2.cpp
├── include/
│   ├── module1.h
│   └── module2.h
└── sugar.toml
```

Configuration:
```toml
project_name = "my-lib"
project_type = "static"
source_paths = ["src"]
include_paths = ["include"]
```

### Library (Shared)

```
my-shared-lib/
├── src/
│   ├── module1.cpp
│   └── module2.cpp
├── include/
│   ├── module1.h
│   └── module2.h
└── sugar.toml
```

Configuration:
```toml
project_name = "my-shared-lib"
project_type = "shared"
source_paths = ["src"]
include_paths = ["include"]
```

### Multi-Module Application

```
my-app/
├── src/
│   ├── main.cpp               # Entry point
│   ├── ui/                    # UI module
│   │   ├── window.cpp
│   │   └── window.h
│   ├── core/                  # Core module
│   │   ├── engine.cpp
│   │   └── engine.h
│   └── util/                  # Utilities
│       ├── helper.cpp
│       └── helper.h
├── include/                   # Public API
│   ├── app_ui.h
│   └── app_core.h
└── sugar.toml
```

Configuration:
```toml
project_name = "my-app"
project_type = "exe"
source_paths = ["src", "src/ui", "src/core", "src/util"]
include_paths = ["include", "src"]
build_path = "build"
output_path = "bin"
```

### Application with External Dependencies

```
my-app/
├── src/
│   └── main.cpp
├── include/
│   └── app.h
├── third_party/
│   └── zlib/
│       ├── lib/
│       │   └── libz.a
│       └── include/
│           └── zlib.h
└── sugar.toml
```

Configuration:
```toml
project_name = "my-app"
project_type = "exe"
source_paths = ["src"]
include_paths = ["include", "third_party/zlib/include"]
link_directories = ["third_party/zlib/lib"]
link_dependencies = ["z"]
```

## Scaffolding Checklist

When creating a new SugarBuilder project:

- [ ] Create project directory
- [ ] Create `src/` directory for source files
- [ ] Create `include/` directory for headers
- [ ] Create minimal `main.cpp` or starting module
- [ ] Create `sugar.toml` with basic configuration
- [ ] Create `.gitignore`
- [ ] Create `README.md`
- [ ] Test with `python -m src configure`
- [ ] Build with `python -m src build`
- [ ] Verify executable in `output_path`

## .gitignore Template

```
# Build artifacts
build/
bin/
dist/
*.o
*.obj
*.a
*.lib
*.exe
*.so
*.dll
*.dylib

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Python
__pycache__/
*.pyc
*.pyo
venv/
.venv/
```

## Next Steps

1. Choose a project pattern from above
2. Create directory structure
3. Create initial `sugar.toml`
4. Write your C++ code
5. Run `python -m src configure` to validate
6. Run `python -m src build` to compile
7. Test your executable

See [Getting Started Guide](03-GETTING_STARTED.md) for detailed instructions.
