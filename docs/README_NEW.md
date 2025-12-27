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

### Windows (Using Standalone Executable)

```powershell
# Clone the repository
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder

# Build a project
.\sugar-builder.bat build

# Or use the executable directly
.\dist\sugar-builder.exe build
```

### Linux/macOS (Using Python)

```bash
# Setup
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Build a project
python -m sugar_builder build
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

```powershell
# Validate configuration
sugar-builder.bat configure

# Build the project
sugar-builder.bat build

# Build with custom config
sugar-builder.bat build --config custom.toml

# Show help
sugar-builder.bat --help
```

## Example Project

The repository includes a working `Calculator` example:

```powershell
cd example
..\sugar-builder.bat build
.\bin\Calculator.exe
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

## Project Structure

```
sugar-builder/
├── dist/
│   └── sugar-builder.exe         # Standalone Windows executable
├── sugar-builder.bat             # Batch wrapper script
├── build_exe.py                  # Script to build the .exe
├── sugar_builder/                # Python package
│   ├── __main__.py              # CLI entry point
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
│       ├── configure.py         # Validate config
│       └── build.py             # Build project
├── example/                      # Working example project
│   ├── src/                     # C++ source files
│   ├── sugar.toml               # Configuration
│   └── README.md                # Example instructions
└── docs/                        # Documentation
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

- **Windows**: Visual Studio 2019+ with MSVC
- **Linux**: GCC 9+ or Clang 10+
- **macOS**: Xcode Command Line Tools
- **Python** (optional, only needed if building from source or on Linux/macOS)

## Building from Source

To build the Windows executable yourself:

```powershell
cd sugar-builder
.\.venv\Scripts\python.exe build_exe.py
```

This creates `dist/sugar-builder.exe` using PyInstaller.

## Development

### Setup

```bash
# Clone and setup
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder
python3 -m venv venv
source venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running Tests

```bash
# Test configuration loading
python -m sugar_builder configure example/sugar.toml

# Build the example
python -m sugar_builder build example/sugar.toml
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
