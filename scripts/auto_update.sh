#!/bin/bash
# Navigate to the project directory
cd ~/ansible-auto-updates

log_file="logs/update.log"
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

# Log function
log_message() {
    echo "[$timestamp] $1" >> $log_file
}

log_message "🚀 Starting automatic network scan and update"

# Step 1: Update the dynamic inventory
log_message "🔄 Scanning network for active IPs..."
if python3 dynamic_inventory/dynamic_inventory.py; then
    log_message "✅ IP scanning completed successfully."
else
    log_message "❌ Error during IP scanning."
    exit 1
fi

# Step 2: Run the Ansible playbook
log_message "🔧 Running Ansible playbook for updates..."
if ansible-playbook -i dynamic_inventory/inventory.json playbooks/update_playbook.yml; then
    log_message "✅ Update process completed successfully."
else
    log_message "❌ Update process failed."
fi
