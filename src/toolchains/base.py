"""Base toolchain abstraction."""

from typing import List, Optional
from pathlib import Path


class Toolchain:
    """
    Abstract toolchain for C++ compilation and linking.
    
    Defines interface for compiling sources and linking object files.
    """
    
    def __init__(self, name: str):
        """
        Initialize toolchain.
        
        Args:
            name: Toolchain name (MSVC, GCC, Clang).
        """
        self.name = name
    
    def compile_object(
        self,
        source_file: Path,
        output_file: Path,
        include_dirs: Optional[List[Path]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile a source file to an object file.
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            flags: Optional list of compiler flags.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement compile_object()")
    
    def link_executable(
        self,
        object_files: List[Path],
        output_file: Path,
        lib_dirs: Optional[List[Path]] = None,
        libraries: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Link object files into an executable.
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output executable.
            lib_dirs: Optional list of library directories.
            libraries: Optional list of libraries to link.
            flags: Optional list of linker flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement link_executable()")
    
    def link_static_library(
        self,
        object_files: List[Path],
        output_file: Path,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Link object files into a static library.
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output library.
            flags: Optional list of archiver flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement link_static_library()")
    
    def link_shared_library(
        self,
        object_files: List[Path],
        output_file: Path,
        lib_dirs: Optional[List[Path]] = None,
        libraries: Optional[List[str]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Link object files into a shared library.
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output library.
            lib_dirs: Optional list of library directories.
            libraries: Optional list of libraries to link.
            flags: Optional list of linker flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement link_shared_library()")
    
    def get_object_extension(self) -> str:
        """
        Get file extension for object files.
        
        Returns:
            Object file extension (e.g., '.obj', '.o').
        """
        raise NotImplementedError("Subclasses must implement get_object_extension()")
    
    @staticmethod
    def create(toolchain_name: str) -> "Toolchain":
        """
        Factory method to create appropriate toolchain.
        
        Args:
            toolchain_name: Name of toolchain (MSVC, GCC, Clang).
            
        Returns:
            Toolchain: Appropriate toolchain instance.
            
        Raises:
            ValueError: If toolchain_name is not supported.
        """
        if toolchain_name == "MSVC":
            from .msvc import MSVCToolchain
            return MSVCToolchain()
        elif toolchain_name == "GCC":
            from .gcc import GCCToolchain
            return GCCToolchain()
        elif toolchain_name == "Clang":
            from .clang import ClangToolchain
            return ClangToolchain()
        else:
            raise ValueError(f"Unsupported toolchain: {toolchain_name}")
