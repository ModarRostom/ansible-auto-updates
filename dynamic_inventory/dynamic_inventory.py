#!/usr/bin/env python3
import json
import subprocess
import os
from datetime import datetime

# Log file path
log_file = "../logs/update.log"

# Function to log messages
def log_message(message):
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

# Function to generate dynamic inventory
def get_dynamic_inventory():
    try:
        # Run nmap to scan the local network for active hosts
        result = subprocess.run(["nmap", "-sn", "192.168.1.0/24"], capture_output=True, text=True)
        hosts = []
        for line in result.stdout.splitlines():
            # Check if the line contains an IP address from the scan result
            if "Nmap scan report for" in line:
                ip = line.split(" ")[-1]
                hosts.append(ip)

        # Create the inventory in JSON format
        inventory = {
            "webservers": {
                "hosts": hosts,
                "vars": {
                    "ansible_user": "root"
                }
            }
        }

        # Save the inventory to a JSON file
        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
        log_message("✅ Inventory updated successfully with dynamic IPs.")
    except Exception as e:
        log_message(f"❌ Error updating inventory: {str(e)}")

# Main function to execute the script
if __name__ == "__main__":
    get_dynamic_inventory()
