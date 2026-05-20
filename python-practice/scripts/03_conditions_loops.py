# =============================================
# STEP 3: If-Else and Loops
# DevOps Decision Making Scripts
# =============================================

print("=" * 50)
print("PART 1: IF-ELSE CONDITIONS")
print("=" * 50)

# Check CPU usage and take action
cpu_usage = 85

print(f"\nCurrent CPU Usage: {cpu_usage}%")

if cpu_usage >= 90:
    print("CRITICAL: CPU extremely high!")
    print("Action: Immediately scale to 6 replicas")
elif cpu_usage >= 80:
    print("WARNING: CPU usage is high!")
    print("Action: Scale up to 4 replicas")
elif cpu_usage >= 60:
    print("NOTICE: CPU usage moderate")
    print("Action: Monitor closely")
else:
    print("OK: CPU usage is normal")
    print("Action: No action needed")

# Check disk space
print("\n" + "-" * 40)
disk_usage = 75
print(f"Disk Usage: {disk_usage}%")

if disk_usage >= 90:
    print("ALERT: Disk almost full — clean up immediately!")
elif disk_usage >= 75:
    print("WARNING: Disk usage getting high — schedule cleanup")
else:
    print("OK: Disk usage is fine")

# =============================================
print("\n" + "=" * 50)
print("PART 2: FOR LOOPS")
print("=" * 50)

# Loop through servers and check status
servers = [
    {"name": "web-server-1", "status": "running"},
    {"name": "web-server-2", "status": "stopped"},
    {"name": "db-server-1",  "status": "running"},
    {"name": "jenkins-server", "status": "running"},
    {"name": "k8s-master",   "status": "stopped"},
]

print("\nServer Health Check Report:")
print("-" * 40)

running_count = 0
stopped_count = 0

for server in servers:
    if server["status"] == "running":
        print(f"  ✅ {server['name']} — RUNNING")
        running_count += 1
    else:
        print(f"  ❌ {server['name']} — STOPPED")
        stopped_count += 1

print("-" * 40)
print(f"Total Running : {running_count}")
print(f"Total Stopped : {stopped_count}")

# =============================================
print("\n" + "=" * 50)
print("PART 3: WHILE LOOP")
print("=" * 50)

# Simulate retry logic
max_retries = 3
attempt = 1
success = False

print("\nSimulating deployment with retry logic:")

while attempt <= max_retries:
    print(f"\nAttempt {attempt} of {max_retries}...")
    
    # Simulate success on attempt 2
    if attempt == 2:
        print("Deployment successful!")
        success = True
        break
    else:
        print("Deployment failed — retrying...")
    
    attempt += 1

if not success:
    print("All attempts failed — alerting team!")
else:
    print(f"\nDeployment completed on attempt {attempt}")