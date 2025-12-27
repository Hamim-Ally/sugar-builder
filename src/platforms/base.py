"""Platform abstraction and configuration."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Platform:
    """
    Represents a target platform for C++ compilation.
    
    Encapsulates platform-specific settings like object/library extensions.
    """
    
    name: str  # Windows, Linux, macOS
    
    @property
    def object_extension(self) -> str:
        """Get object file extension for this platform."""
        if self.name == "Windows":
            return ".obj"
        else:  # Linux, macOS
            return ".o"
    
    @property
    def static_lib_extension(self) -> str:
        """Get static library extension for this platform."""
        if self.name == "Windows":
            return ".lib"
        elif self.name == "Linux":
            return ".a"
        elif self.name == "macOS":
            return ".a"
        return ".a"
    
    @property
    def shared_lib_extension(self) -> str:
        """Get shared library extension for this platform."""
        if self.name == "Windows":
            return ".dll"
        elif self.name == "Linux":
            return ".so"
        elif self.name == "macOS":
            return ".dylib"
        return ".so"
    
    @property
    def executable_extension(self) -> str:
        """Get executable extension for this platform."""
        if self.name == "Windows":
            return ".exe"
        return ""
    
    @staticmethod
    def create(platform_name: str) -> "Platform":
        """
        Factory method to create a platform instance.
        
        Args:
            platform_name: Name of platform (Windows, Linux, macOS).
            
        Returns:
            Platform: Platform instance.
            
        Raises:
            ValueError: If platform_name is not supported.
        """
        if platform_name not in ["Windows", "Linux", "macOS"]:
            raise ValueError(f"Unsupported platform: {platform_name}")
        return Platform(name=platform_name)
