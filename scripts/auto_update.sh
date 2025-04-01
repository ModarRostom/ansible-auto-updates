#!/bin/bash
cd ~/ansible-auto-updates

log_file="logs/update.log"
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

log_message() {
    echo "[$timestamp] $1" >> $log_file
}

log_message "Starting automatic network scan and update"

# Update the dynamic inventory
if python3 dynamic_inventory/dynamic_inventory.py; then
    log_message "IP scanning completed."
else
    log_message "IP scanning failed."
    exit 1
fi

# Run the Ansible playbook
if ansible-playbook -i dynamic_inventory/inventory.json playbooks/update_playbook.yml; then
    log_message "Update process completed."
else
    log_message "Update process failed."
    python3 dynamic_inventory/dynamic_inventory.py --send-error
fi
