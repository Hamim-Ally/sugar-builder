"""Clang/LLVM toolchain."""

from pathlib import Path
from typing import List, Optional
from .base import Toolchain


class ClangToolchain(Toolchain):
    """Clang/LLVM toolchain (clang++, lld, llvm-ar)."""
    
    def __init__(self):
        """Initialize Clang toolchain."""
        super().__init__("Clang")
    
    def compile_object(
        self,
        source_file: Path,
        output_file: Path,
        include_dirs: Optional[List[Path]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile source with clang++.
        
        Invokes: clang++ -c -o <output> [-I<include>] [flags] <source>
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            flags: Optional list of compiler flags.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        import subprocess
        
        # Build clang++ command
        cmd = ["clang++", "-c", "-o", str(output_file), str(source_file)]
        
        # Add include directories
        if include_dirs:
            for inc_dir in include_dirs:
                cmd.append(f"-I{inc_dir}")
        
        # Add compiler flags
        if flags:
            cmd.extend(flags)
        
        print(f"[Clang] Compiling {source_file} -> {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: clang++ not found. Ensure Clang is installed and in PATH")
            return False
        except Exception as e:
            print(f"  Error: {e}")
            return False
    
    def link_executable(
        self,
        object_files: List[Path],
        output_file: Path,
        lib_dirs: Optional[List[Path]] = None,
        libraries: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Link object files into executable with clang++/lld.
        
        Invokes: clang++ [-L<lib_dir>] [-l<lib>] -o <output> [flags] <objects>
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output executable.
            lib_dirs: Optional list of library directories.
            libraries: Optional list of libraries to link.
            flags: Optional list of linker flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        import subprocess
        
        # Build clang++ link command
        cmd = ["clang++", "-o", str(output_file)] + [str(obj) for obj in object_files]
        
        # Add library directories
        if lib_dirs:
            for lib_dir in lib_dirs:
                cmd.append(f"-L{lib_dir}")
        
        # Add libraries
        if libraries:
            for lib in libraries:
                cmd.append(f"-l{lib}")
        
        # Add linker flags
        if flags:
            cmd.extend(flags)
        
        print(f"[Clang] Linking executable: {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: clang++ not found. Ensure Clang is installed and in PATH")
            return False
        except Exception as e:
            print(f"  Error: {e}")
            return False
    
    def link_static_library(
        self,
        object_files: List[Path],
        output_file: Path,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Link object files into static library with llvm-ar.
        
        Invokes: llvm-ar rcs <output> [flags] <objects>
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output library.
            flags: Optional list of archiver flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        import subprocess
        
        # Build llvm-ar command
        cmd = ["llvm-ar", "rcs", str(output_file)] + [str(obj) for obj in object_files]
        
        # Add archiver flags if provided
        if flags:
            cmd.extend(flags)
        
        print(f"[Clang] Creating static library: {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: llvm-ar not found. Ensure LLVM/Clang is installed and in PATH")
            return False
        except Exception as e:
            print(f"  Error: {e}")
            return False
    
    def link_shared_library(
        self,
        object_files: List[Path],
        output_file: Path,
        lib_dirs: Optional[List[Path]] = None,
        libraries: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Link object files into shared library with clang++/lld.
        
        Invokes: clang++ -shared [-L<lib_dir>] [-l<lib>] -o <output> [flags] <objects>
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output library.
            lib_dirs: Optional list of library directories.
            libraries: Optional list of libraries to link.
            flags: Optional list of linker flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        import subprocess
        
        # Build clang++ link command for shared library
        cmd = ["clang++", "-shared", "-o", str(output_file)] + [str(obj) for obj in object_files]
        
        # Add library directories
        if lib_dirs:
            for lib_dir in lib_dirs:
                cmd.append(f"-L{lib_dir}")
        
        # Add libraries
        if libraries:
            for lib in libraries:
                cmd.append(f"-l{lib}")
        
        # Add linker flags
        if flags:
            cmd.extend(flags)
        
        print(f"[Clang] Linking shared library: {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: clang++ not found. Ensure Clang is installed and in PATH")
            return False
        except Exception as e:
            print(f"  Error: {e}")
            return False
    
    def get_object_extension(self) -> str:
        """Get Clang object file extension."""
        return ".o"
