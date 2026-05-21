# =============================================
# STEP 8: Error Handling
# Safe DevOps Automation Script
# =============================================

import os
import subprocess
import datetime

print("=" * 50)
print("SAFE DEVOPS AUTOMATION SCRIPT")
print("With Proper Error Handling")
print("=" * 50)

# =============================================
def safe_run_command(command, description):
    """Safely run a command with error handling"""
    print(f"\nRunning: {description}")
    print(f"Command: {command}")
    print("-" * 40)
    
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"✅ SUCCESS")
            if result.stdout:
                print(result.stdout.strip())
            return True
        else:
            print(f"❌ FAILED")
            if result.stderr:
                print(f"Error: {result.stderr.strip()}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ TIMEOUT: Command took too long")
        return False
    except Exception as e:
        print(f"❌ UNEXPECTED ERROR: {e}")
        return False

# =============================================
def safe_read_file(filepath):
    """Safely read a file with error handling"""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            print(f"✅ File read successfully: {filepath}")
            return content
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        return None
    except PermissionError:
        print(f"❌ Permission denied: {filepath}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error reading file: {e}")
        return None

# =============================================
def safe_write_log(message):
    """Safely write to log file"""
    try:
        timestamp = datetime.datetime.now()
        with open("scripts/automation.log", 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"✅ Log written: {message}")
    except Exception as e:
        print(f"❌ Could not write log: {e}")

# =============================================
print("\nPART 1: Safe Command Execution")
print("=" * 50)

# These commands run safely with error handling
safe_run_command("docker --version", "Check Docker")
safe_run_command("git --version", "Check Git")
safe_run_command("kubectl version --client", "Check kubectl")
safe_run_command("this_command_doesnt_exist", "Test Error Handling")

# =============================================
print("\nPART 2: Safe File Operations")
print("=" * 50)

# Try reading files that exist and don't exist
content1 = safe_read_file("scripts/deployment.log")
content2 = safe_read_file("scripts/app.config")
content3 = safe_read_file("scripts/file_that_doesnt_exist.txt")

# =============================================
print("\nPART 3: Safe Log Writing")
print("=" * 50)

safe_write_log("Automation script started")
safe_write_log("Docker version checked successfully")
safe_write_log("Git version checked successfully")
safe_write_log("Error handling tested successfully")
safe_write_log("Automation script completed")

print("\nAutomation log contents:")
print("-" * 40)
content = safe_read_file("scripts/automation.log")
if content:
    print(content)

print("=" * 50)
print("Error handling practice complete!")
print("All errors caught gracefully ✅")