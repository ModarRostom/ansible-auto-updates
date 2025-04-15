#!/bin/bash
cd ~/ansible-auto-updates

log_file="logs/update.log"
timestamp=$(date "+%Y-%m-%d %H:%M:%S")

log_message() {
    echo "[$timestamp] $1" >> $log_file
}

send_error_notification() {
    webhook_url="YOUR_SLACK_WEBHOOK_URL"  # Set your Slack Webhook URL here
    curl -X POST -H 'Content-type: application/json' --data "{\"text\":\"$1\"}" $webhook_url
}

log_message "Starting automatic network scan and update"

# Update the dynamic inventory
log_message "Starting IP scan..."

if python3 dynamic_inventory/dynamic_inventory.py; then
    log_message "IP scanning completed successfully."
else
    log_message "IP scanning failed."
    send_error_notification "IP scanning failed during automation."
    exit 1
fi

log_message "Running Ansible playbook for updates..."

# Run the Ansible playbook
if ansible-playbook -i dynamic_inventory/inventory.json playbooks/update_playbook.yml; then
    log_message "Update process completed successfully."
else
    log_message "Update process failed."
    send_error_notification "Ansible playbook execution failed during automation."
    python3 dynamic_inventory/dynamic_inventory.py --send-error
    exit 1
fi

log_message "Automatic network update tasks finished."
