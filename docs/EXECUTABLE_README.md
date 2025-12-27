# SugarBuilder Executable Distribution

The `sugar-builder.exe` is a standalone Windows executable that doesn't require Python to be installed on the system.

## Location
```
sugar-builder/dist/sugar-builder.exe
```

## Requirements
- Windows 10/11 (x64)
- Visual Studio with MSVC compiler installed (the toolchain auto-detects it)

## Usage

### Basic Build
```powershell
cd your-project-directory
C:\path\to\sugar-builder.exe build
```

### Validate Configuration
```powershell
C:\path\to\sugar-builder.exe configure
```

### Use Custom Config
```powershell
C:\path\to\sugar-builder.exe build --config custom.toml
```

### Show Help
```powershell
C:\path\to\sugar-builder.exe --help
```

## Example

```powershell
cd C:\Users\hamim\Documents\GitHub\sugar-builder\example
..\dist\sugar-builder.exe build
# Output: bin\Calculator.exe
.\bin\Calculator.exe
```

## Configuration (sugar.toml)

Create a `sugar.toml` file in your project root:

```toml
project_name = "MyApp"
project_type = "exe"           # exe, static, shared
compiler = "MSVC"              # MSVC, GCC, Clang
platform = "Windows"           # Windows, Linux, macOS
source_paths = ["src"]         # Where .cpp files are
build_path = "build"           # Object files output
output_path = "bin"            # Executable/library output
```

## How the Auto-Detection Works

The executable automatically:

1. **Finds MSVC compiler** by searching:
   - `C:\Program Files\Microsoft Visual Studio\*\Community\VC\Tools\MSVC\*\bin\Hostx64\x64\cl.exe`
   - `C:\Program Files (x86)\Microsoft Visual Studio\*\Community\VC\Tools\MSVC\*\bin\Hostx64\x64\cl.exe`
   - System PATH

2. **Finds system includes** for:
   - MSVC C++ runtime headers
   - Windows SDK headers (ucrt, um)

3. **Links with default libraries**:
   - kernel32.lib
   - user32.lib
   - msvcrt.lib

## Rebuilding the Executable

To rebuild `sugar-builder.exe` after making code changes:

```powershell
cd C:\path\to\sugar-builder
.\.venv\Scripts\python.exe build_exe.py
```

This requires:
- Python 3.10+
- Virtual environment (`.venv`)
- PyInstaller installed

## Distribution

You can copy just the `.exe` file to another machine without Python installed, and it will work as long as that machine has Visual Studio with MSVC installed.

The executable is self-contained (10.9 MB) and includes all Python runtime dependencies.
