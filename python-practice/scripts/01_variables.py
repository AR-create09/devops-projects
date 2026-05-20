# =============================================
# STEP 1: Variables and Data Types
# DevOps Configuration Example
# =============================================

# String variables
app_name = "jenkins"
server_host = "0.0.0.0"
environment = "staging"

# Integer variables
port = 8080
max_replicas = 4
min_replicas = 2

# Float variables
app_version = 1.5
cpu_threshold = 80.5

# Boolean variables
is_running = True
is_healthy = False

# List — collection of items
devops_tools = ["Docker", "Kubernetes", "Jenkins", "Terraform", "AWS"]

# Dictionary — key value pairs
app_config = {
    "app_name": "jenkins",
    "port": 8080,
    "host": "0.0.0.0",
    "environment": "staging",
    "replicas": 2
}

# =============================================
# PRINT EVERYTHING
# =============================================

print("=" * 50)
print("APPLICATION CONFIGURATION")
print("=" * 50)

print(f"App Name     : {app_name}")
print(f"Host         : {server_host}")
print(f"Port         : {port}")
print(f"Environment  : {environment}")
print(f"Version      : {app_version}")
print(f"Is Running   : {is_running}")
print(f"Max Replicas : {max_replicas}")

print("\nDevOps Tools I Know:")
for tool in devops_tools:
    print(f"  -> {tool}")

print("\nFull App Config:")
for key, value in app_config.items():
    print(f"  {key}: {value}")

print("=" * 50)