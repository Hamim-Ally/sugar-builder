"""Configure command for SugarBuilder."""

from pathlib import Path
from typing import Optional
from .base import Command
from src.core import Config, Project


class ConfigureCommand(Command):
    """
    Configure command validates the sugar.toml configuration.
    
    Loads and validates project configuration without building.
    """
    
    def __init__(self):
        """Initialize configure command."""
        super().__init__("configure")
    
    def execute(self, config_path: Optional[str] = None) -> int:
        """
        Load and validate configuration.
        
        Args:
            config_path: Optional path to sugar.toml (defaults to ./sugar.toml).
            
        Returns:
            0 on success, 1 on failure.
        """
        try:
            # Default to ./sugar.toml if not specified
            if config_path is None:
                config_path = "sugar.toml"
            
            print(f"Configuring from: {config_path}")
            
            # Load configuration
            config = Config.load(config_path)
            
            # Validate configuration
            config.validate()
            
            # Create project to verify paths
            project = Project(config)
            
            print("Configuration validation successful!")
            print(f"  Project: {config.project_name}")
            print(f"  Type: {config.project_type}")
            print(f"  Compiler: {config.compiler}")
            print(f"  Platform: {config.platform}")
            print(f"  Source paths: {', '.join(config.source_paths)}")
            print(f"  Build path: {config.build_path}")
            print(f"  Output path: {config.output_path}")
            if config.link_dependencies:
                print(f"  Dependencies: {', '.join(config.link_dependencies)}")
            
            return 0
        
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return 1
        except ValueError as e:
            print(f"Configuration Error: {e}")
            return 1
        except Exception as e:
            print(f"Unexpected error: {e}")
            return 1
    
    def get_help(self) -> str:
        """Get help text for configure command."""
        return """
configure - Validate sugar.toml configuration

Usage: sugar-builder configure [--config <path>]

Options:
  --config <path>    Path to sugar.toml (defaults to ./sugar.toml)

Description:
  Loads and validates the sugar.toml configuration file without building.
  Checks for required fields and validates project settings.
"""
