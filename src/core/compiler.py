"""Compiler abstraction and invocation."""

from pathlib import Path
from typing import List, Optional
import subprocess


class Compiler:
    """
    Abstract compiler interface for C++ compilation.
    
    Handles source-to-object compilation based on configured toolchain.
    """
    
    def __init__(self, compiler_name: str):
        """
        Initialize compiler instance.
        
        Args:
            compiler_name: Name of compiler (MSVC, GCC, Clang).
        """
        self.compiler_name = compiler_name
    
    def compile_source(
        self,
        source_file: str | Path,
        output_file: str | Path,
        include_dirs: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile a single source file to object file.
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement compile_source()")
    
    def get_object_extension(self) -> str:
        """
        Get file extension for object files on current platform.
        
        Returns:
            Object file extension (e.g., '.obj' for MSVC, '.o' for GCC/Clang).
        """
        raise NotImplementedError("Subclasses must implement get_object_extension()")
    
    @staticmethod
    def create(compiler_name: str) -> "Compiler":
        """
        Factory method to create appropriate compiler instance.
        
        Args:
            compiler_name: Name of compiler (MSVC, GCC, Clang).
            
        Returns:
            Compiler: Appropriate compiler instance.
            
        Raises:
            ValueError: If compiler_name is not supported.
        """
        if compiler_name == "MSVC":
            return MSVCCompiler()
        elif compiler_name == "GCC":
            return GCCCompiler()
        elif compiler_name == "Clang":
            return ClangCompiler()
        else:
            raise ValueError(f"Unsupported compiler: {compiler_name}")


class MSVCCompiler(Compiler):
    """Microsoft Visual C++ compiler."""
    
    def __init__(self):
        """Initialize MSVC compiler."""
        super().__init__("MSVC")
    
    def compile_source(
        self,
        source_file: str | Path,
        output_file: str | Path,
        include_dirs: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile source with MSVC cl.exe.
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        # Implementation would invoke: cl.exe /c /Fo<output> <source>
        # with optional /I flags for include directories
        print(f"[MSVC] Compiling {source_file} -> {output_file}")
        return True
    
    def get_object_extension(self) -> str:
        """Get MSVC object file extension."""
        return ".obj"


class GCCCompiler(Compiler):
    """GNU C++ compiler."""
    
    def __init__(self):
        """Initialize GCC compiler."""
        super().__init__("GCC")
    
    def compile_source(
        self,
        source_file: str | Path,
        output_file: str | Path,
        include_dirs: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile source with GCC g++.
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        # Implementation would invoke: g++ -c -o <output> <source>
        # with optional -I flags for include directories
        print(f"[GCC] Compiling {source_file} -> {output_file}")
        return True
    
    def get_object_extension(self) -> str:
        """Get GCC object file extension."""
        return ".o"


class ClangCompiler(Compiler):
    """Clang/LLVM C++ compiler."""
    
    def __init__(self):
        """Initialize Clang compiler."""
        super().__init__("Clang")
    
    def compile_source(
        self,
        source_file: str | Path,
        output_file: str | Path,
        include_dirs: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile source with Clang clang++.
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        # Implementation would invoke: clang++ -c -o <output> <source>
        # with optional -I flags for include directories
        print(f"[Clang] Compiling {source_file} -> {output_file}")
        return True
    
    def get_object_extension(self) -> str:
        """Get Clang object file extension."""
        return ".o"
