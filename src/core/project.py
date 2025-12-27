"""Project representation and management."""

from pathlib import Path
from typing import List
from .config import Config


class Project:
    """
    Represents a SugarBuilder C++ project.
    
    Manages project configuration, source files, and build artifacts.
    """
    
    def __init__(self, config: Config, root_dir: str | Path = "."):
        """
        Initialize project with configuration.
        
        Args:
            config: Project configuration from sugar.toml.
            root_dir: Root directory of the project.
        """
        self.config = config
        self.root_dir = Path(root_dir)
    
    def get_source_files(self) -> List[Path]:
        """
        Collect all C++ source files from configured source paths.
        
        Returns:
            List of Path objects pointing to C++ source files (.cpp, .cc, .cxx, .c).
        """
        source_files = []
        source_extensions = {".cpp", ".cc", ".cxx", ".c"}
        
        for src_path in self.config.source_paths:
            src_dir = self.root_dir / src_path
            if not src_dir.exists():
                continue
            
            for ext in source_extensions:
                source_files.extend(src_dir.glob(f"*{ext}"))
        
        return source_files
    
    def get_build_directory(self) -> Path:
        """
        Get the build directory path.
        
        Returns:
            Path to the build directory.
        """
        return self.root_dir / self.config.build_path
    
    def get_output_directory(self) -> Path:
        """
        Get the output directory path.
        
        Returns:
            Path to the output directory.
        """
        return self.root_dir / self.config.output_path
    
    def get_target_filename(self) -> str:
        """
        Get the target executable/library filename based on project type and platform.
        
        Returns:
            Filename of the build target.
        """
        target_name = self.config.project_name
        
        if self.config.platform == "Windows":
            if self.config.project_type == "exe":
                return f"{target_name}.exe"
            elif self.config.project_type == "static":
                return f"{target_name}.lib"
            elif self.config.project_type == "shared":
                return f"{target_name}.dll"
        
        elif self.config.platform == "Linux":
            if self.config.project_type == "exe":
                return target_name
            elif self.config.project_type == "static":
                return f"lib{target_name}.a"
            elif self.config.project_type == "shared":
                return f"lib{target_name}.so"
        
        elif self.config.platform == "macOS":
            if self.config.project_type == "exe":
                return target_name
            elif self.config.project_type == "static":
                return f"lib{target_name}.a"
            elif self.config.project_type == "shared":
                return f"lib{target_name}.dylib"
        
        return target_name
