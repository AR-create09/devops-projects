from flask import Flask, render_template

app = Flask(__name__)

# Sample mock monitoring data for your DevOps practice
SYSTEM_DATA = {
    "status": "Healthy",
    "environment": "Development",
    "uptime": "2 hours",
    "active_containers": ["project1-docker-web"]
}

# 1. THE HOME PAGE (http://localhost:5000)
@app.route('/')
def home():
    return "<h1>DevOps Practice Web Server Running Successfully!</h1><p>Try visiting: /health, /info, or /tools</p>"

# 2. THE STATUS PAGE (http://localhost:5000/status)
@app.route('/status')
def status():
    return SYSTEM_DATA

# 3. THE HEALTH CHECKER (http://localhost:5000/health)
@app.route('/health')
def health():
    # Production monitoring tools like Prometheus use this to check if your app is alive
    return {"status": "UP", "database": "Connected", "disk_space": "OK"}

# 4. THE INFO PAGE (http://localhost:5000/info)
@app.route('/info')
def info():
    return {
        "project_name": "DevOps Automation Platform",
        "version": "1.0.0",
        "engineer": "Anil Reddy",
        "framework": "Flask 3.1.3"
    }

# 5. THE TOOLS PAGE (http://localhost:5000/tools)
@app.route('/tools')
def tools():
    return {
        "monitored_tools": ["Docker", "Git", "Jenkins", "Kubernetes", "Terraform"]
    }

# Change the very bottom block to look exactly like this:
if __name__ == '__main__':
    print("🚀 Starting your upgraded Flask web server on http://127.0.0.1:8080")
    app.run(debug=True, port=8080)  # Fixed: Shifted to 8080 to dodge Nginx!