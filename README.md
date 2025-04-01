# Automatic Server Updates with Ansible

This project automates server updates using Ansible with a dynamic inventory script.  
The IP addresses of the servers are automatically detected using nmap.  
The update process is triggered daily using the Windows Task Scheduler.

## Project Structure:
- **dynamic_inventory/**: Contains the Python script to discover IP addresses.
- **scripts/**: Contains the Bash script to execute the update.
- **playbooks/**: Contains the Ansible playbook to perform the update.
- **README.md**: Project description and instructions.

## Usage:
1. Run the update manually:
