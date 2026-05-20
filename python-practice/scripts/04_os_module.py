# =============================================
# STEP 4: OS Module
# System Monitoring Script
# =============================================

import os
import datetime

print("=" * 50)
print("DEVOPS SYSTEM MONITORING SCRIPT")
print(f"Run Time: {datetime.datetime.now()}")
print("=" * 50)

# Get current user
user = os.environ.get("USERNAME", "unknown")
print(f"\nRunning as user: {user}")

# Get current directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Check if a file exists
files_to_check = [
    "scripts/01_variables.py",
    "scripts/02_functions.py",
    "scripts/03_conditions_loops.py",
    "scripts/missing_file.py"
]

print("\nFile Existence Check:")
print("-" * 40)
for file_path in files_to_check:
    if os.path.exists(file_path):
        print(f"  ✅ Found    : {file_path}")
    else:
        print(f"  ❌ Missing  : {file_path}")

# List files in current directory
print("\nFiles in current directory:")
print("-" * 40)
for item in os.listdir("."):
    if os.path.isdir(item):
        print(f"  📁 {item}/")
    else:
        print(f"  📄 {item}")

# Run system commands
print("\n" + "=" * 50)
print("SYSTEM COMMANDS")
print("=" * 50)

print("\nDocker Status:")
print("-" * 40)
os.system("docker ps")

print("\nGit Status:")
print("-" * 40)
os.system("git status")

# Create a log entry
print("\n" + "=" * 50)
print("WRITING LOG ENTRY")
print("=" * 50)

log_message = f"System check completed at {datetime.datetime.now()} by {user}"
print(f"Log: {log_message}")