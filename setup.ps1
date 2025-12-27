# SugarBuilder Interactive Setup (PowerShell)
# Fully VS Code-safe arrow-key menu with multi-step support

$VENV_NAME = "venv"
$VENV_PATH = Join-Path -Path $PSScriptRoot -ChildPath $VENV_NAME

$options = @(
    "Create Virtual Environment",
    "Activate Virtual Environment",
    "Upgrade pip",
    "Install Dependencies",
    "Install SugarBuilder (editable)",
    "Run All Steps",
    "Build",
    "Clean",
    "Exit"
)

$selected = 0

# Safe cursor hide (won't crash in VS Code)
$oldCursor = $null
if ($Host.UI.RawUI -and $Host.UI.RawUI.PSObject.Properties.Match("CursorVisible")) {
    $oldCursor = $Host.UI.RawUI.CursorVisible
    $Host.UI.RawUI.CursorVisible = $false
}

function Show-Menu {
    Clear-Host
    Write-Host "========================================"
    Write-Host "         Sugar Builder Setup"
    Write-Host "========================================"
    Write-Host ""
    for ($i = 0; $i -lt $options.Length; $i++) {
        if ($i -eq $selected) {
            Write-Host "> $($options[$i])" -ForegroundColor Cyan
        } else {
            Write-Host "  $($options[$i])"
        }
    }
    Write-Host ""
    Write-Host "Use ↑↓ to navigate and Enter to select an action."
    Write-Host "You can run multiple actions; the menu will reappear after each action."
}

function Execute-Action($action) {
    switch ($action) {
        0 { Create-Venv }
        1 { Activate-Venv }
        2 { Upgrade-Pip }
        3 { Install-Requirements }
        4 { Install-Package }
        5 { Run-All-Steps }
        6 { Build }
        7 { Clean-Project }
        8 { Exit-Setup }
    }
}

function Create-Venv {
    if (-Not (Test-Path "$VENV_PATH\Scripts\Activate.ps1")) {
        Write-Host "Creating virtual environment at '$VENV_NAME'..."
        python -m venv $VENV_NAME
        Write-Host "[OK] Virtual environment created!"
    } else {
        Write-Host "[OK] Virtual environment already exists!"
    }
    Pause
}

function Activate-Venv {
    if (Test-Path "$VENV_PATH\Scripts\Activate.ps1") {
        Write-Host "Activating virtual environment..."
        & "$VENV_PATH\Scripts\Activate.ps1"
        Write-Host "[OK] Virtual environment is active!"
    } else {
        Write-Host "[ERROR] Virtual environment does not exist. Create it first!"
    }
    Pause
}

function Upgrade-Pip {
    Write-Host "Upgrading pip..."
    python -m pip install --upgrade pip
    Write-Host "[OK] pip upgraded!"
    Pause
}

function Install-Requirements {
    if (Test-Path "requirements.txt") {
        Write-Host "Installing dependencies from requirements.txt..."
        python -m pip install -r requirements.txt
        Write-Host "[OK] Dependencies installed!"
    } else {
        Write-Host "[WARNING] requirements.txt not found. Skipping."
    }
    Pause
}

function Install-Package {
    if (Test-Path "tools\setup.py") {
        Write-Host "Installing SugarBuilder in editable mode..."
        python -m pip install -e .
        Write-Host "[OK] SugarBuilder installed!"
    } else {
        Write-Host "[WARNING] setup.py not found. Skipping."
    }
    Pause
}

function Build {

    $root = $PSScriptRoot
    $python = Join-Path $root "venv\Scripts\python.exe"
    $buildScript = Join-Path $root "tools\build.py"

    if (!(Test-Path $python)) {
        Write-Host "[ERROR] venv Python not found at: $python"
        Pause
        return
    }

    if (!(Test-Path $buildScript)) {
        Write-Host "[ERROR] build.py not found at: $buildScript"
        Pause
        return
    }

    Write-Host ""
    Write-Host "Running build.py using venv Python..."
    Write-Host "$python $buildScript"
    Write-Host ""

    & $python $buildScript

    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n[OK] Build completed successfully!"
    } else {
        Write-Host "`n[ERROR] Build failed (exit code $LASTEXITCODE)."
    }

    Pause
}

function Clean-Project {
    $autoFolders = @(
        "build",
        "dist",
        "__pycache__",
        "$VENV_NAME",
        "*.egg-info",
        "bin",
        "obj"
    )

    foreach ($folder in $autoFolders) {
        $paths = Get-ChildItem -Path $PSScriptRoot -Filter $folder -Recurse -Directory -ErrorAction SilentlyContinue
        foreach ($path in $paths) {
            try {
                Remove-Item $path.FullName -Recurse -Force -ErrorAction Stop
                Write-Host "[OK] Removed $($path.FullName)"
            } catch {
                Write-Host "[ERROR] Could not remove $($path.FullName): $_" -ForegroundColor Red
            }
        }
    }

    Write-Host "[DONE] Project cleaned."
    Pause
}

function Run-All-Steps {
    Create-Venv
    Activate-Venv
    Upgrade-Pip
    Install-Requirements
    Install-Package
}

function Exit-Setup {
    Write-Host "Exiting setup. Bye!"
    if ($oldCursor -ne $null) { $Host.UI.RawUI.CursorVisible = $oldCursor }
    exit
}

# Main loop
while ($true) {
    Show-Menu
    $key = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    switch ($key.VirtualKeyCode) {
        38 { $selected = ($selected - 1 + $options.Length) % $options.Length } # Up
        40 { $selected = ($selected + 1) % $options.Length } # Down
        13 { Execute-Action $selected } # Enter
    }
}
