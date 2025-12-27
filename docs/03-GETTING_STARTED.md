# Step by Step Guide

## Installation

### Prerequisites

- Python 3.10 or higher
- Git
- A C++ compiler (MSVC, GCC, or Clang)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Hamim-Ally/sugar-builder.git
cd sugar-builder
```

### Step 2: Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

You're all set!

## Creating Your First Project

### Step 1: Create a Project Directory

```bash
mkdir my-cpp-project
cd my-cpp-project
mkdir src
```

### Step 2: Create a Simple C++ File

Create `src/main.cpp`:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

### Step 3: Create sugar.toml

```toml
project_name = "hello-world"
project_type = "exe"

compiler = "MSVC"                    # Change based on your system
platform = "Windows"                 # Change based on your system

source_paths = ["src"]
build_path = "build"
output_path = "bin"
```

### Step 4: Validate Configuration

From the SugarBuilder root directory:

```bash
python -m src configure /path/to/my-cpp-project/sugar.toml
```

You should see:
```
✓ Configuration loaded successfully
✓ All source files found
✓ Ready to build
```

### Step 5: Build Your Project

```bash
python -m src build /path/to/my-cpp-project/sugar.toml
```

### Step 6: Run Your Executable

```bash
# Windows
.\bin\hello-world.exe

# Linux/macOS
./bin/hello-world
```

## Using the Example Project

The repository includes a working Calculator example:

```bash
# Navigate to example
cd example

# Build from SugarBuilder directory
python -m src build sugar.toml

# Run the executable
# Windows
.\bin\calculator.exe

# Linux/macOS
./bin/calculator
```

## Common Configuration Options

### Project Types

- `exe` - Executable program (default)
- `static` - Static library (.lib/.a)
- `shared` - Shared library (.dll/.so/.dylib)

### Compiler Selection

- `MSVC` - Microsoft Visual C++ (Windows only)
- `GCC` - GNU Compiler Collection (Linux, macOS, Windows)
- `Clang` - LLVM Clang (Linux, macOS, Windows)

### Platform Selection

- `Windows` - Windows x64
- `Linux` - Linux x64
- `macOS` - macOS x64

## Troubleshooting

### Error: "Compiler not found"

**Windows (MSVC)**
- Ensure Visual Studio is installed with C++ build tools
- Restart your terminal after installing

**Linux**
- Install build tools: `sudo apt-get install build-essential`
- Check GCC: `gcc --version`

**macOS**
- Install Xcode: `xcode-select --install`
- Or install via Homebrew: `brew install gcc`

### Error: "Configuration file not found"

Make sure you're running the command from the SugarBuilder directory, and the path to sugar.toml is correct.

### Build fails with linking errors

Check that:
1. All `.cpp` files are in the directories specified in `source_paths`
2. Include paths are correct
3. Any external libraries are properly linked in `link_dependencies`

## Next Steps

- Read the [Quick Reference](02-QUICK_REFERENCE.md) for more command options
- Explore the [Project Structure](04-PROJECT_STRUCTURE.md) to understand how it works
- Check [Project Templates](06-PROJECT_TEMPLATES.md) for different project patterns
