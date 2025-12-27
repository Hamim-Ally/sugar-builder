"""Build command for SugarBuilder."""

from pathlib import Path
from typing import Optional
from .base import Command
from src.core import Config, Project
from src.toolchains import Toolchain


class BuildCommand(Command):
    """
    Build command compiles and links a C++ project.
    
    Compiles source files to object files and links them into final target.
    """
    
    def __init__(self):
        """Initialize build command."""
        super().__init__("build")
    
    def execute(self, config_path: Optional[str] = None) -> int:
        """
        Build the C++ project.
        
        Steps:
        1. Load and validate configuration
        2. Create build and output directories
        3. Compile all source files to object files
        4. Link object files into target (exe/static/shared)
        
        Args:
            config_path: Optional path to sugar.toml (defaults to ./sugar.toml).
            
        Returns:
            0 on success, 1 on failure.
        """
        try:
            # Default to ./sugar.toml if not specified
            if config_path is None:
                config_path = "sugar.toml"
            
            print(f"Building from: {config_path}")
            
            # Load configuration
            config = Config.load(config_path)
            config.validate()
            
            # Create project
            project = Project(config)
            
            # Create directories if they don't exist
            build_dir = project.get_build_directory()
            output_dir = project.get_output_directory()
            build_dir.mkdir(parents=True, exist_ok=True)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            print(f"Build directory: {build_dir}")
            print(f"Output directory: {output_dir}")
            
            # Get toolchain
            toolchain = Toolchain.create(config.compiler)
            
            # Get source files
            source_files = project.get_source_files()
            if not source_files:
                print("Warning: No source files found!")
                return 1
            
            print(f"Found {len(source_files)} source files")
            
            # Compile sources to objects
            object_files = []
            obj_ext = toolchain.get_object_extension()
            
            for source_file in source_files:
                obj_name = source_file.stem + obj_ext
                obj_file = build_dir / obj_name
                
                print(f"Compiling: {source_file.name} -> {obj_name}")
                
                # TODO: Pass include dirs from config
                success = toolchain.compile_object(source_file, obj_file)
                
                if not success:
                    print(f"Error compiling {source_file}")
                    return 1
                
                object_files.append(obj_file)
            
            # Link objects into target
            target_name = project.get_target_filename()
            target_path = output_dir / target_name
            
            print(f"\nLinking: {target_name}")
            
            if config.project_type == "exe":
                success = toolchain.link_executable(
                    object_files,
                    target_path,
                    libraries=config.link_dependencies,
                )
            elif config.project_type == "static":
                success = toolchain.link_static_library(object_files, target_path)
            elif config.project_type == "shared":
                success = toolchain.link_shared_library(
                    object_files,
                    target_path,
                    libraries=config.link_dependencies,
                )
            else:
                raise ValueError(f"Unknown project type: {config.project_type}")
            
            if not success:
                print("Error during linking")
                return 1
            
            print(f"\nBuild successful!")
            print(f"Target: {target_path}")
            
            return 0
        
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1
        except ValueError as e:
            print(f"Configuration Error: {e}")
            return 1
        except Exception as e:
            print(f"Build Error: {e}")
            return 1
    
    def get_help(self) -> str:
        """Get help text for build command."""
        return """
build - Compile and link the C++ project

Usage: sugar-builder build [--config <path>]

Options:
  --config <path>    Path to sugar.toml (defaults to ./sugar.toml)

Description:
  Builds the C++ project by:
  1. Validating sugar.toml configuration
  2. Creating build and output directories
  3. Compiling all source files to object files
  4. Linking object files into final executable/library

The project type (exe/static/shared) determines linking behavior.
Dependencies are linked as specified in the configuration.
"""
