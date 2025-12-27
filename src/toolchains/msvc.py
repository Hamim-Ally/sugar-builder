"""Microsoft Visual C++ toolchain."""

from pathlib import Path
from typing import List, Optional
import subprocess
from .base import Toolchain


class MSVCToolchain(Toolchain):
    """Microsoft Visual C++ toolchain (cl.exe, link.exe, lib.exe)."""
    
    def __init__(self):
        """Initialize MSVC toolchain."""
        super().__init__("MSVC")
        self._cl_exe = self._find_cl_exe()
        self._link_exe = self._find_link_exe()
        self._lib_exe = self._find_lib_exe()
        self._include_dirs = self._find_include_dirs()
    
    @staticmethod
    def _find_include_dirs() -> List[Path]:
        """Find MSVC and Windows SDK include directories."""
        includes = []
        
        # Find MSVC includes
        vs_paths = [
            Path("C:/Program Files/Microsoft Visual Studio/18/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC"),
            Path("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC"),
        ]
        
        for vs_path in vs_paths:
            if vs_path.exists():
                versions = sorted(vs_path.glob("*"), reverse=True)
                for version_dir in versions:
                    include_path = version_dir / "include"
                    if include_path.exists():
                        includes.append(include_path)
                        break
        
        # Find Windows SDK includes
        sdk_paths = [
            Path("C:/Program Files (x86)/Windows Kits/10/Include"),
            Path("C:/Program Files/Windows Kits/10/Include"),
        ]
        
        for sdk_path in sdk_paths:
            if sdk_path.exists():
                # Find latest SDK version
                versions = sorted(sdk_path.glob("*"), reverse=True)
                for version_dir in versions:
                    ucrt_path = version_dir / "ucrt"
                    um_path = version_dir / "um"
                    if ucrt_path.exists():
                        includes.append(ucrt_path)
                    if um_path.exists():
                        includes.append(um_path)
                    break
        
        return includes
    
    @staticmethod
    def _find_cl_exe() -> str:
        """Find cl.exe path, checking PATH first then Visual Studio installations."""
        # Try PATH first
        try:
            result = subprocess.run(["where", "cl.exe"], capture_output=True, text=True, check=False)
            if result.returncode == 0:
                return "cl.exe"
        except Exception:
            pass
        
        # Search Visual Studio installations
        vs_paths = [
            Path("C:/Program Files/Microsoft Visual Studio/18/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC"),
            Path("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC"),
        ]
        
        for vs_path in vs_paths:
            if vs_path.exists():
                # Find the latest MSVC version
                versions = sorted(vs_path.glob("*"), reverse=True)
                for version_dir in versions:
                    cl_path = version_dir / "bin" / "Hostx64" / "x64" / "cl.exe"
                    if cl_path.exists():
                        return str(cl_path)
        
        return "cl.exe"  # Fallback to PATH
    
    @staticmethod
    def _find_link_exe() -> str:
        """Find link.exe path."""
        try:
            result = subprocess.run(["where", "link.exe"], capture_output=True, text=True, check=False)
            if result.returncode == 0:
                return "link.exe"
        except Exception:
            pass
        
        vs_paths = [
            Path("C:/Program Files/Microsoft Visual Studio/18/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC"),
            Path("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC"),
        ]
        
        for vs_path in vs_paths:
            if vs_path.exists():
                versions = sorted(vs_path.glob("*"), reverse=True)
                for version_dir in versions:
                    link_path = version_dir / "bin" / "Hostx64" / "x64" / "link.exe"
                    if link_path.exists():
                        return str(link_path)
        
        return "link.exe"
    
    @staticmethod
    def _find_lib_exe() -> str:
        """Find lib.exe path."""
        try:
            result = subprocess.run(["where", "lib.exe"], capture_output=True, text=True, check=False)
            if result.returncode == 0:
                return "lib.exe"
        except Exception:
            pass
        
        vs_paths = [
            Path("C:/Program Files/Microsoft Visual Studio/18/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC"),
            Path("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC"),
        ]
        
        for vs_path in vs_paths:
            if vs_path.exists():
                versions = sorted(vs_path.glob("*"), reverse=True)
                for version_dir in versions:
                    lib_path = version_dir / "bin" / "Hostx64" / "x64" / "lib.exe"
                    if lib_path.exists():
                        return str(lib_path)
        
        return "lib.exe"
    
    def compile_object(
        self,
        source_file: Path,
        output_file: Path,
        include_dirs: Optional[List[Path]] = None,
        flags: Optional[List[str]] = None,
    ) -> bool:
        """
        Compile source with cl.exe.
        
        Invokes: cl.exe /c /Fo<output> [/I<include>] [flags] <source>
        
        Args:
            source_file: Path to source file.
            output_file: Path to output object file.
            include_dirs: Optional list of include directories.
            flags: Optional list of compiler flags.
            
        Returns:
            True if compilation succeeded, False otherwise.
        """
        # Build cl.exe command
        cmd = [self._cl_exe, "/c", f"/Fo{output_file}", str(source_file)]
        
        # Add system include directories (MSVC and Windows SDK)
        for inc_dir in self._include_dirs:
            cmd.append(f"/I{inc_dir}")
        
        # Add user-provided include directories
        if include_dirs:
            for inc_dir in include_dirs:
                cmd.append(f"/I{inc_dir}")
        
        # Add compiler flags
        if flags:
            cmd.extend(flags)
        
        print(f"[MSVC] Compiling {source_file} -> {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: cl.exe not found. Ensure MSVC is installed and in PATH")
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
        Link object files into executable with link.exe.
        
        Invokes: link.exe [/LIBPATH:<lib_dir>] [libraries] /OUT:<output> [flags] <objects>
        
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
        
        # Find MSVC library directories
        msvc_lib_dirs = []
        vs_paths = [
            Path("C:/Program Files/Microsoft Visual Studio/18/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/VC/Tools/MSVC"),
            Path("C:/Program Files (x86)/Microsoft Visual Studio/2019/BuildTools/VC/Tools/MSVC"),
            Path("C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Tools/MSVC"),
        ]
        
        for vs_path in vs_paths:
            if vs_path.exists():
                versions = sorted(vs_path.glob("*"), reverse=True)
                for version_dir in versions:
                    lib_path = version_dir / "lib" / "x64"
                    if lib_path.exists():
                        msvc_lib_dirs.append(lib_path)
                        break
        
        # Find Windows SDK library directories
        sdk_lib_dirs = []
        sdk_paths = [
            Path("C:/Program Files (x86)/Windows Kits/10/Lib"),
            Path("C:/Program Files/Windows Kits/10/Lib"),
        ]
        
        for sdk_path in sdk_paths:
            if sdk_path.exists():
                versions = sorted(sdk_path.glob("*"), reverse=True)
                for version_dir in versions:
                    ucrt_lib = version_dir / "ucrt" / "x64"
                    um_lib = version_dir / "um" / "x64"
                    if ucrt_lib.exists():
                        sdk_lib_dirs.append(ucrt_lib)
                    if um_lib.exists():
                        sdk_lib_dirs.append(um_lib)
                    break
        
        # Build link.exe command
        cmd = [self._link_exe, f"/OUT:{output_file}"]
        
        # Add object files
        cmd.extend([str(obj) for obj in object_files])
        
        # Add MSVC library directories
        for lib_dir in msvc_lib_dirs:
            cmd.append(f"/LIBPATH:{lib_dir}")
        
        # Add Windows SDK library directories
        for lib_dir in sdk_lib_dirs:
            cmd.append(f"/LIBPATH:{lib_dir}")
        
        # Add user-provided library directories
        if lib_dirs:
            for lib_dir in lib_dirs:
                cmd.append(f"/LIBPATH:{lib_dir}")
        
        # Add default MSVC libraries
        cmd.extend(["kernel32.lib", "user32.lib", "msvcrt.lib"])
        
        # Add user-provided libraries
        if libraries:
            cmd.extend([f"{lib}.lib" for lib in libraries])
        
        # Add linker flags
        if flags:
            cmd.extend(flags)
        
        print(f"[MSVC] Linking executable: {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: link.exe not found. Ensure MSVC is installed and in PATH")
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
        Link object files into static library with lib.exe.
        
        Invokes: lib.exe /OUT:<output> [flags] <objects>
        
        Args:
            object_files: List of object file paths.
            output_file: Path to output library.
            flags: Optional list of archiver flags.
            
        Returns:
            True if linking succeeded, False otherwise.
        """
        import subprocess
        
        # Build lib.exe command
        cmd = [self._lib_exe, f"/OUT:{output_file}"]
        
        # Add object files
        cmd.extend([str(obj) for obj in object_files])
        
        # Add archiver flags
        if flags:
            cmd.extend(flags)
        
        print(f"[MSVC] Creating static library: {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: lib.exe not found. Ensure MSVC is installed and in PATH")
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
        Link object files into shared library with link.exe.
        
        Invokes: link.exe /DLL [/LIBPATH:<lib_dir>] [libraries] /OUT:<output> [flags] <objects>
        
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
        
        # Build link.exe command for DLL
        cmd = [self._link_exe, "/DLL", f"/OUT:{output_file}"]
        
        # Add object files
        cmd.extend([str(obj) for obj in object_files])
        
        # Add library directories
        if lib_dirs:
            for lib_dir in lib_dirs:
                cmd.append(f"/LIBPATH:{lib_dir}")
        
        # Add libraries
        if libraries:
            cmd.extend([f"{lib}.lib" for lib in libraries])
        
        # Add linker flags
        if flags:
            cmd.extend(flags)
        
        print(f"[MSVC] Linking shared library: {output_file}")
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                print(f"  Error: {result.stderr}")
                return False
            return True
        except FileNotFoundError:
            print(f"  Error: link.exe not found. Ensure MSVC is installed and in PATH")
            return False
        except Exception as e:
            print(f"  Error: {e}")
            return False
    
    def get_object_extension(self) -> str:
        """Get MSVC object file extension."""
        return ".obj"
