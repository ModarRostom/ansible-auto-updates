#!/bin/bash

# Set log file path
LOGFILE="/var/log/ansible-auto-update.log"

# Log start time
echo "===== UPDATE STARTED: $(date) =====" >> "$LOGFILE"

# Update system
if apt update && apt upgrade -y >> "$LOGFILE" 2>&1; then
    echo "System updated successfully at $(date)" >> "$LOGFILE"

    # Optional email notification on success
    echo "System update successful on $(hostname)" | mail -s "Update OK on $(hostname)" admin@example.com
else
    echo "Update failed at $(date)" >> "$LOGFILE"

    # Optional email notification on failure
    echo "System update FAILED on $(hostname)" | mail -s "Update FAILED on $(hostname)" admin@example.com
fi

# Reboot if required
if [ -f /var/run/reboot-required ]; then
    echo "Reboot required. Rebooting system..." >> "$LOGFILE"
    reboot
else
    echo "No reboot required." >> "$LOGFILE"
fi

# Log end time
echo "===== UPDATE FINISHED: $(date) =====" >> "$LOGFILE"
