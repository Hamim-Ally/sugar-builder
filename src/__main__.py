"""SugarBuilder - Manual C++ Build Tool."""

from src.commands import ConfigureCommand, BuildCommand
from typing import Optional
import sys


def main(argv: Optional[list[str]] = None) -> int:
    """
    Main entry point for SugarBuilder CLI.
    
    Usage:
        sugar-builder configure [--config <path>]
        sugar-builder build [--config <path>]
        sugar-builder --help
    
    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).
        
    Returns:
        Exit code (0 for success, non-zero for failure).
    """
    if argv is None:
        argv = sys.argv[1:]
    
    if not argv or argv[0] in ["--help", "-h", "help"]:
        print_help()
        return 0
    
    command_name = argv[0]
    args = argv[1:]
    
    # Parse config path if provided
    config_path = None
    if "--config" in args:
        config_idx = args.index("--config")
        if config_idx + 1 < len(args):
            config_path = args[config_idx + 1]
    
    # Execute command
    try:
        if command_name == "configure":
            cmd = ConfigureCommand()
            return cmd.execute(config_path)
        elif command_name == "build":
            cmd = BuildCommand()
            return cmd.execute(config_path)
        else:
            print(f"Error: Unknown command '{command_name}'")
            print_help()
            return 1
    except KeyboardInterrupt:
        print("\nBuild cancelled by user")
        return 130
    except Exception as e:
        print(f"Fatal error: {e}")
        return 1


def print_help() -> None:
    """Print help text for SugarBuilder."""
    help_text = """
SugarBuilder - Manual C++ Build Tool

Usage:
  sugar-builder <command> [options]

Commands:
  configure [--config <path>]    Validate sugar.toml configuration
  build [--config <path>]        Compile and link the C++ project
  help                           Show this help message

Options:
  --config <path>                Path to sugar.toml (defaults to ./sugar.toml)

Examples:
  sugar-builder configure
  sugar-builder build
  sugar-builder build --config custom.toml

For detailed command help:
  sugar-builder configure --help
  sugar-builder build --help
"""
    print(help_text)


if __name__ == "__main__":
    sys.exit(main())
