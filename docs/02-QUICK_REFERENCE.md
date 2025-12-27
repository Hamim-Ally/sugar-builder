# SugarBuilder Quick Reference

## Installation

```bash
# Clone the repository
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder

# Setup Python environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Common Commands

```bash
# Validate configuration
python -m src configure [--config <path>]

# Build project
python -m src build [--config <path>]

# Show help
python -m src --help
```

## Basic Configuration (sugar.toml)

```toml
project_name = "MyApp"
project_type = "exe"              # exe, static, shared

compiler = "MSVC"                 # MSVC, GCC, or Clang
platform = "Windows"              # Windows, Linux, macOS

source_paths = ["src"]            # C++ source directories
build_path = "build"              # Object files output
output_path = "bin"               # Executable/library output

# Optional: External libraries
# link_dependencies = ["mylib", "pthread"]
```

## Compiler Support Matrix

| Compiler | Windows | Linux | macOS |
|----------|---------|-------|-------|
| MSVC     | ✅      | ❌    | ❌    |
| GCC      | ⚠️*     | ✅    | ✅    |
| Clang    | ⚠️*     | ✅    | ✅    |

*Possible but not recommended

## File Structure

```
your-project/
├── src/               # Your C++ source files
│   ├── main.cpp
│   └── *.cpp
├── sugar.toml         # Project configuration
└── build/             # Generated object files
```

## Troubleshooting

### Compiler not found
- **Windows (MSVC)**: Install Visual Studio with C++ workload
- **Linux**: Install GCC (`sudo apt-get install build-essential`)
- **macOS**: Install Xcode Command Line Tools (`xcode-select --install`)

### Configuration errors
Run `python -m src configure` to validate your sugar.toml file.

### Build failures
Check that all source files are in the paths specified in sugar.toml.

## More Information

- See [Getting Started Guide](03-GETTING_STARTED.md) for detailed instructions
- Check [Project Structure](04-PROJECT_STRUCTURE.md) to understand organization
- View [Component Map](05-COMPONENT_MAP.md) to learn how everything works
- Visit the main [README](../README.md) for project overview
