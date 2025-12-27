# SugarBuilder

**A simple, powerful manual C++ build tool for Windows, Linux, and macOS.**

SugarBuilder is a lightweight build system that lets you compile C++ projects without complex build file syntax. Define your project once in `sugar.toml` and build anywhere.

## Features

- ✅ **TOML-based configuration** - Simple, human-readable project config
- ✅ **Multi-compiler support** - MSVC, GCC, Clang with automatic detection
- ✅ **Cross-platform** - Windows, Linux, macOS from one config
- ✅ **Multiple output types** - Executables, static libraries, shared libraries
- ✅ **Standalone executable** - No Python required (Windows)
- ✅ **Type-safe** - 100% Python type hints for IDE support
- ✅ **Well-documented** - Complete docstrings on all functions

## Quick Start

### All Platforms (Using Python)

```bash
# Setup
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Build a project
python -m src build

# Validate configuration
python -m src configure
```

### Windows Setup Script

Alternatively, use the interactive setup script:

```powershell
.\setup.ps1
```

## Configuration (sugar.toml)

Create a `sugar.toml` file in your project root:

```toml
# Project metadata
project_name = "MyApp"
project_type = "exe"              # exe, static, shared

# Compiler settings
compiler = "MSVC"                 # MSVC, GCC, or Clang
platform = "Windows"              # Windows, Linux, macOS

# Directories (relative to sugar.toml)
source_paths = ["src"]            # Where .cpp files are located
build_path = "build"              # Object files output
output_path = "bin"               # Executable/library output

# Optional: External libraries
# link_dependencies = ["mylib", "pthread"]
```

## Commands

```bash
# Validate configuration
python -m src configure

# Build the project
python -m src build

# Build with custom config
python -m src build --config custom.toml

# Show help
python -m src --help
```

## Example Project

The repository includes a working `Calculator` example:

```bash
cd example
python -m src build
# Run the generated executable (location depends on OS and compiler)
```

Output:
```
================================
  Calculator Example Program
================================
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
================================
Program completed successfully!
================================
```
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
================================
Program completed successfully!
================================
```

## Project Structure

```
sugar-builder/
├── src/                          # Python package
│   ├── __main__.py              # CLI entry point
│   ├── main.py                  # Legacy entry point
│   ├── core/                    # Core functionality
│   │   ├── config.py            # TOML configuration loader
│   │   ├── project.py           # Project management
│   │   └── compiler.py          # Compiler enumeration
│   ├── toolchains/              # Compiler implementations
│   │   ├── base.py              # Abstract toolchain
│   │   ├── msvc.py              # MSVC/Visual C++
│   │   ├── gcc.py               # GCC/G++
│   │   └── clang.py             # Clang/LLVM
│   ├── platforms/               # Platform abstractions
│   │   └── base.py              # Platform interface
│   └── commands/                # CLI commands
│       ├── base.py              # Base command class
│       ├── configure.py         # Validate config
│       └── build.py             # Build project
├── example/                      # Working example project
│   ├── src/                     # C++ source files
│   ├── sugar.toml               # Configuration
│   └── README.md                # Example instructions
├── docs/                        # Documentation
├── setup.ps1                    # Interactive setup script (Windows)
├── requirements.txt             # Python dependencies
└── LICENSE                      # MIT License
```

## Compiler Auto-Detection

### Windows (MSVC)
- Automatically finds Visual Studio installation
- Locates `cl.exe`, `link.exe`, `lib.exe`
- Includes Windows SDK headers automatically

### Linux/macOS (GCC/Clang)
- Uses system PATH to find compilers
- Supports both `-o` and `-shared` linking

## Requirements

- **Windows**: Visual Studio 2019+ with MSVC (optional, GCC/Clang also supported)
- **Linux**: GCC 9+ or Clang 10+
- **macOS**: Xcode Command Line Tools
- **Python**: Python 3.10+ (required for building from source)

## Building from Source

To build and develop SugarBuilder:

```bash
# Clone and setup
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Then run the project directly:

```bash
python -m src build example/sugar.toml
```

## Development

### Setup

```bash
# Clone and setup
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running Commands

```bash
# Test configuration loading
python -m src configure example/sugar.toml

# Build the example project
python -m src build example/sugar.toml
```

### Code Quality

All code includes:
- ✅ 100% type hints (PEP 484)
- ✅ Complete docstrings
- ✅ Clear error messages

## Supported Configurations

| Compiler | Platform | Output Type | Status |
|----------|----------|-------------|--------|
| MSVC | Windows | exe, static, shared | ✅ |
| GCC | Linux/macOS | exe, static, shared | ✅ |
| Clang | Linux/macOS | exe, static, shared | ✅ |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## Roadmap

- [ ] Incremental compilation
- [ ] Build caching
- [ ] Dependency management
- [ ] Multiple target configurations
- [ ] Plugin system

---

**Created with ❤️ by [Hamim-Ally](https://github.com/Hamim-Ally)**
