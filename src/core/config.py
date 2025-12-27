"""Configuration loader and validator for SugarBuilder."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Any
import sys

# tomllib available in Python 3.11+, use tomli as fallback
if sys.version_info >= (3, 11):
    import tomllib
else:
    try:
        import tomli as tomllib
    except ImportError:
        raise ImportError(
            "Python 3.10 requires 'tomli' package. "
            "Install with: pip install tomli"
        )


@dataclass
class Config:
    """
    Configuration container for a SugarBuilder project.
    
    Loads and validates sugar.toml configuration file.
    """
    
    project_name: str
    project_type: str  # exe, static, shared
    compiler: str  # MSVC, GCC, Clang
    platform: str  # Windows, Linux, macOS
    source_paths: List[str]
    build_path: str
    output_path: str
    link_dependencies: List[str]
    
    @classmethod
    def load(cls, config_path: str | Path) -> "Config":
        """
        Load configuration from sugar.toml file.
        
        Args:
            config_path: Path to sugar.toml file.
            
        Returns:
            Config: Loaded configuration object.
            
        Raises:
            FileNotFoundError: If sugar.toml does not exist.
            ValueError: If required fields are missing or invalid.
        """
        config_path = Path(config_path)
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        with open(config_path, "rb") as f:
            data: Dict[str, Any] = tomllib.load(f)
        
        return cls._from_dict(data)
    
    @classmethod
    def _from_dict(cls, data: Dict[str, Any]) -> "Config":
        """
        Create Config instance from dictionary, with validation.
        
        Args:
            data: Dictionary containing configuration data.
            
        Returns:
            Config: Configuration object.
            
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        required_fields = [
            "project_name",
            "project_type",
            "compiler",
            "platform",
            "source_paths",
            "build_path",
            "output_path",
        ]
        
        missing = [f for f in required_fields if f not in data]
        if missing:
            raise ValueError(f"Missing required configuration fields: {', '.join(missing)}")
        
        # Validate project_type
        if data["project_type"] not in ["exe", "static", "shared"]:
            raise ValueError(
                f"Invalid project_type: {data['project_type']}. "
                "Must be 'exe', 'static', or 'shared'."
            )
        
        # Validate compiler
        if data["compiler"] not in ["MSVC", "GCC", "Clang"]:
            raise ValueError(
                f"Invalid compiler: {data['compiler']}. "
                "Must be 'MSVC', 'GCC', or 'Clang'."
            )
        
        # Validate platform
        if data["platform"] not in ["Windows", "Linux", "macOS"]:
            raise ValueError(
                f"Invalid platform: {data['platform']}. "
                "Must be 'Windows', 'Linux', or 'macOS'."
            )
        
        # Ensure source_paths is a list
        if not isinstance(data["source_paths"], list):
            raise ValueError("source_paths must be a list of paths.")
        
        # link_dependencies is optional
        link_deps = data.get("link_dependencies", [])
        if not isinstance(link_deps, list):
            raise ValueError("link_dependencies must be a list.")
        
        return cls(
            project_name=data["project_name"],
            project_type=data["project_type"],
            compiler=data["compiler"],
            platform=data["platform"],
            source_paths=data["source_paths"],
            build_path=data["build_path"],
            output_path=data["output_path"],
            link_dependencies=link_deps,
        )
    
    def validate(self) -> None:
        """
        Validate the configuration.
        
        Raises:
            ValueError: If configuration is invalid.
        """
        if not self.project_name.strip():
            raise ValueError("project_name cannot be empty.")
        
        if not self.source_paths:
            raise ValueError("source_paths cannot be empty.")
        
        # Check that source paths are not empty strings
        if any(not path.strip() for path in self.source_paths):
            raise ValueError("source_paths cannot contain empty strings.")
