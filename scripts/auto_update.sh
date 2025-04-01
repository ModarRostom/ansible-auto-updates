#!/bin/bash
cd ~/ansible-auto-updates
echo "🚀 Starte automatisches Update"
ansible-playbook -i dynamic_inventory/dynamic_inventory.py playbooks/update_playbook.yml
