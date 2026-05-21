# =============================================
# STEP 5: File Read and Write
# DevOps Log Writing Script
# =============================================

import datetime
import os

# =============================================
print("=" * 50)
print("PART 1: WRITING FILES")
print("=" * 50)

# Write a deployment log
log_file = "scripts/deployment.log"

def write_log(message, level="INFO"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    print(f"Logged: {log_entry.strip()}")

# Write multiple log entries
write_log("Deployment pipeline started")
write_log("Pulling latest code from GitHub")
write_log("Building Docker image")
write_log("Running unit tests")
write_log("Tests passed successfully")
write_log("Pushing image to registry")
write_log("Deploying to Kubernetes cluster")
write_log("Health check passed", "SUCCESS")
write_log("Deployment complete", "SUCCESS")

# =============================================
print("\n" + "=" * 50)
print("PART 2: READING FILES")
print("=" * 50)

print(f"\nReading deployment log: {log_file}")
print("-" * 50)

with open(log_file, 'r') as f:
    content = f.read()
    print(content)

# =============================================
print("=" * 50)
print("PART 3: READING LINE BY LINE")
print("=" * 50)

print("\nFiltering only SUCCESS entries:")
print("-" * 50)

with open(log_file, 'r') as f:
    for line in f:
        if "SUCCESS" in line:
            print(f"  ✅ {line.strip()}")

# =============================================
print("\n" + "=" * 50)
print("PART 4: WRITING CONFIG FILE")
print("=" * 50)

config_content = """# Application Configuration
APP_NAME=jenkins
APP_PORT=8080
APP_HOST=0.0.0.0
ENVIRONMENT=staging
MAX_REPLICAS=4
MIN_REPLICAS=2
LOG_LEVEL=INFO
"""

config_file = "scripts/app.config"

with open(config_file, 'w') as f:
    f.write(config_content)

print(f"Config file written: {config_file}")

# Read it back
print("\nReading config file:")
print("-" * 40)
with open(config_file, 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            key, value = line.split('=')
            print(f"  {key}: {value}")