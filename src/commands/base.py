"""Base command abstraction."""

from abc import ABC, abstractmethod
from typing import Optional


class Command(ABC):
    """
    Abstract base class for SugarBuilder commands.
    
    Defines the interface for all CLI commands.
    """
    
    def __init__(self, name: str):
        """
        Initialize command.
        
        Args:
            name: Name of the command.
        """
        self.name = name
    
    @abstractmethod
    def execute(self, config_path: Optional[str] = None) -> int:
        """
        Execute the command.
        
        Args:
            config_path: Optional path to sugar.toml configuration file.
            
        Returns:
            Exit code (0 for success, non-zero for failure).
        """
        pass
    
    def get_help(self) -> str:
        """
        Get help text for this command.
        
        Returns:
            Help text describing the command.
        """
        return f"Command: {self.name}"
