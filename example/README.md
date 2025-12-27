# SugarBuilder Example Project

A complete, working example of how to use SugarBuilder to compile C++ code.

## Project Structure

```
example/
├── sugar.toml              # SugarBuilder configuration
├── src/                    # C++ source files
│   ├── main.cpp
│   ├── calculator.cpp
│   └── calculator.h
├── build/                  # Build artifacts (generated)
└── bin/                    # Final executable (generated)
```

## What This Example Does

This is a simple calculator program that:
- Adds two numbers
- Subtracts two numbers
- Multiplies two numbers
- Divides two numbers

## How to Run

### Step 1: Validate Configuration
```bash
cd example
python ../main.py configure
```

Expected output:
```
Configuring from: sugar.toml
Configuration validation successful!
  Project: Calculator
  Type: exe
  Compiler: GCC
  Platform: Linux
  Source paths: src
  Build path: build
  Output path: bin
```

### Step 2: Build the Project
```bash
python ../main.py build
```

Expected output:
```
Building from: sugar.toml
Build directory: build
Output directory: bin
Found 2 source files
Compiling: main.cpp -> main.o
[GCC] Compiling src/main.cpp -> build/main.o
Compiling: calculator.cpp -> calculator.o
[GCC] Compiling src/calculator.cpp -> build/calculator.o

Linking: Calculator
[GCC] Linking executable: bin/Calculator
  Objects: build/main.o build/calculator.o
Build successful!
Target: bin/Calculator
```

### Step 3: Run the Program
```bash
./bin/Calculator
```

Or on Windows:
```bash
bin\Calculator.exe
```

## Configuration

The `sugar.toml` file specifies:
- **project_name**: "Calculator"
- **project_type**: "exe" (executable)
- **compiler**: "GCC" (can be MSVC or Clang)
- **platform**: "Linux" (can be Windows or macOS)
- **source_paths**: ["src"] - Where to find .cpp files
- **build_path**: "build" - Where to put .o object files
- **output_path**: "bin" - Where to put the final executable

## Files Included

### calculator.h
Header file defining the Calculator class interface.

### calculator.cpp
Implementation of the Calculator class with math operations.

### main.cpp
Entry point - creates a Calculator and demonstrates its use.

## Expected Output When Running

```
Calculator Example
==================
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

## Modifying the Example

To change what the calculator does:

1. Edit `src/calculator.cpp` to change the math operations
2. Edit `src/main.cpp` to change what values are calculated
3. Rebuild with `python ../main.py build`

## Key Points

✅ SugarBuilder finds all .cpp files automatically
✅ Configuration is explicit - no magic
✅ Build output goes to configured directories
✅ Works on Windows, Linux, and macOS (with proper compiler)

## Next Steps

1. Try modifying the calculator operations
2. Add more functions to the Calculator class
3. Add more source files and watch SugarBuilder compile them all
4. Change the compiler in sugar.toml and rebuild

See ../README.md for more documentation.
