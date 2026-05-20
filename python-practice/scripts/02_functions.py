# =============================================
# STEP 2: Functions
# Reusable DevOps Functions
# =============================================

# Function 1 — Simple greeting function
def greet_engineer(name):
    print(f"Welcome DevOps Engineer: {name}")

# Function 2 — Check if port is valid
def is_valid_port(port):
    if port >= 1 and port <= 65535:
        return True
    else:
        return False

# Function 3 — Generate container name
def generate_container_name(app, environment):
    container_name = f"{app}-{environment}-container"
    return container_name

# Function 4 — Calculate replica recommendation
def recommend_replicas(cpu_usage):
    if cpu_usage >= 80:
        replicas = 4
        message = "HIGH load — scaling up"
    elif cpu_usage >= 50:
        replicas = 2
        message = "MEDIUM load — normal"
    else:
        replicas = 1
        message = "LOW load — scaling down"
    return replicas, message

# Function 5 — Print deployment summary
def print_deployment_summary(app, version, environment, replicas):
    print("=" * 50)
    print("DEPLOYMENT SUMMARY")
    print("=" * 50)
    print(f"Application  : {app}")
    print(f"Version      : {version}")
    print(f"Environment  : {environment}")
    print(f"Replicas     : {replicas}")
    print("=" * 50)

# =============================================
# CALL ALL FUNCTIONS
# =============================================

# Call function 1
greet_engineer("Anil Kumar Reddy")

# Call function 2
port = 8080
result = is_valid_port(port)
print(f"\nPort {port} is valid: {result}")

port2 = 99999
result2 = is_valid_port(port2)
print(f"Port {port2} is valid: {result2}")

# Call function 3
name = generate_container_name("jenkins", "staging")
print(f"\nGenerated Container Name: {name}")

# Call function 4
cpu = 85
replicas, message = recommend_replicas(cpu)
print(f"\nCPU Usage: {cpu}%")
print(f"Recommendation: {message}")
print(f"Suggested Replicas: {replicas}")

# Call function 5
print()
print_deployment_summary("jenkins", "2.0", "staging", replicas)