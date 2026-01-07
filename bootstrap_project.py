#!/usr/bin/env python3
"""Bootstrap script to generate all project files for local-warp-agent."""

import os
import sys
from pathlib import Path

print("\n🚀 Local Warp Agent - Project Bootstrap\n")
print("This script will generate all project files and directories.\n")

# Create directory structure
dirs = [
    "agents",
    "agents/tools",
    "ui",
    "config",
    "logs"
]

for dir_path in dirs:
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    print(f"✓ Created directory: {dir_path}")

# Generate __init__.py files
init_files = [
    "agents/__init__.py",
    "agents/tools/__init__.py",
    "ui/__init__.py"
]

for init_file in init_files:
    with open(init_file, 'w') as f:
        f.write(f'"""Local Warp Agent - {Path(init_file).parent.name} package."""\n')
    print(f"✓ Created: {init_file}")

# Create .gitkeep for logs
Path("logs/.gitkeep").touch()
print("✓ Created: logs/.gitkeep")

print("\n📦 Bootstrap complete!\n")
print("Next steps:")
print("1. Run: pip install -r requirements.txt")
print("2. Visit: https://github.com/AXI0MH1VE/local-warp-agent")
print("3. Download remaining Python files from the repo")
print("4. Start Ollama: ollama serve")
print("5. Run: python agent_launcher.py\n")
