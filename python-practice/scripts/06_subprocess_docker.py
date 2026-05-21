# =============================================
# STEP 6: Subprocess Module
# Docker Container Health Checker
# =============================================

import subprocess
import datetime

print("=" * 50)
print("DOCKER CONTAINER HEALTH CHECKER")
print(f"Check Time: {datetime.datetime.now()}")
print("=" * 50)

# =============================================
# CRITICAL: This function MUST stay at the top!
# =============================================
def run_command(command):
    """Run a shell command and return output"""
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True
    )
    return result.stdout, result.stderr, result.returncode

# =============================================
print("\nPART 1: Check Docker Version")
print("-" * 40)

output, error, code = run_command("docker --version")
if code == 0:
    print(f"✅ Docker found: {output.strip()}")
else:
    print(f"❌ Docker not found: {error.strip()}")

# =============================================
print("\nPART 2: List Running Containers")
print("-" * 40)

# FIXED: Escaped double quotes work perfectly on Windows PowerShell
output, error, code = run_command('docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"')
if code == 0:
    if output.strip():
        print(output)
    else:
        print("No containers currently running")
else:
    print(f"Error: {error}")

# =============================================
print("\nPART 3: Check Specific Containers")
print("-" * 40)

containers_to_check = ["jenkins", "anil-web-container"]

for container in containers_to_check:
    # FIXED: Removed the Linux-only '2>/dev/null' to prevent Windows syntax issues
    output, error, code = run_command(
        f"docker inspect --format {{{{.State.Running}}}} {container}"
    )
    
    status = output.strip().lower()
    
    if status == "true":
        print(f"  ✅ {container} — RUNNING")
    elif code != 0 or "error" in error.lower():
        print(f"  ❌ {container} — NOT FOUND")
    else:
        print(f"  ⚠️  {container} — STOPPED")

# =============================================
print("\nPART 4: Docker System Info")
print("-" * 40)

output, error, code = run_command("docker system df")
if code == 0:
    print(output)

# =============================================
print("\nPART 5: Git Information")
print("-" * 40)

output, error, code = run_command("git log --oneline -5")
if code == 0:
    print("Last 5 Git Commits:")
    print(output)
else:
    print("Not a git repository or no commits yet")