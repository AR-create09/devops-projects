#!/bin/bash
# Practice Session 1 - Linux Practice
# Date: $(date)

echo "=== System Information ==="
echo "User: $(whoami)"
echo "Date: $(date)"
echo "Uptime: $(uptime)"

echo "=== Disk Usage ==="
df -h

echo "=== Memory Usage ==="
free -m

echo "=== Top 5 CPU Processes ==="
ps aux --sort=-%cpu | head -5

echo "=== Practice Complete ==="