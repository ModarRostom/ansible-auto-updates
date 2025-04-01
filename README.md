# Automatic Server Updates with Ansible

This project automates server updates using Ansible with a **dynamic inventory script**. The IP addresses of the servers are **automatically detected** using **Nmap**. The entire process runs daily at **00:00** via a **systemd service** on Linux without manual intervention.

---

## Project Structure:  
```
ansible-auto-updates/
├── dynamic_inventory/       # Contains the dynamic inventory script (Python)
│   └── dynamic_inventory.py
├── scripts/                 # Contains the Bash script for automation
│   └── auto_update.sh
├── playbooks/               # Contains the Ansible playbook for server updates
│   └── update_playbook.yml
├── services/                # Contains systemd service and timer files
│   └── ansible-auto-update.service
│   └── ansible-auto-update.timer
├── logs/                    # Directory for storing log files
│   └── update.log
└── README.md                # Project description and instructions
```

---

## How It Works:  
1. The **Python script** automatically scans the network to detect server IPs.  
2. The **dynamic inventory** is updated with the latest IPs.  
3. The **Ansible playbook** runs to update packages on the detected servers.  
4. The process is automated via a **systemd service** to run daily at **00:00**.  
5. **Logs** are generated to track the update process and identify any errors.  
6. **Email notifications** are sent if an update fails.  

---

## Manual Execution (For Testing):  
### Run the automation script manually:  
```bash
./scripts/auto_update.sh
```

### Check the latest log:  
```bash
cat logs/update.log
```

### Test the dynamic inventory:  
```bash
ansible -i dynamic_inventory/inventory.json webservers -m ping
```

---

## Automating with systemd on Linux:  
### Setting Up the Service and Timer:
1. Copy the service and timer files to systemd:
   ```bash
   sudo cp services/ansible-auto-update.service /etc/systemd/system/
   sudo cp services/ansible-auto-update.timer /etc/systemd/system/
   ```
2. Reload systemd to recognize the new files:
   ```bash
   sudo systemctl daemon-reload
   ```
3. Enable and start the timer:
   ```bash
   sudo systemctl enable ansible-auto-update.timer
   sudo systemctl start ansible-auto-update.timer
   ```
4. Check the status:
   ```bash
   systemctl status ansible-auto-update.timer
   ```
5. To run the script manually:
   ```bash
   sudo systemctl start ansible-auto-update.service
   ```

---

## Logging:  
All logs are saved in the **logs/update.log** file.  
- Each entry contains a timestamp and the update status.  
- You can review the logs for both successes and failures.  

---

## Features:  
- **Automated Inventory Management:** Uses a dynamic inventory script to keep server IPs up to date.  
- **Scheduled Daily Updates:** Runs automatically every day at **00:00**.  
- **Detailed Logging:** Logs all actions and errors for easy troubleshooting.  
- **Cross-Platform Compatibility:** Uses WSL on Windows and systemd on Linux for automation.  
- **Email Notifications:** Notifies in case of update failures.  

---

## Future Improvements:  
- Add more advanced email reporting.  
- Integrate backup functionality before updates.  
- Implement a web dashboard for monitoring updates.  

---

## License:  
This project is licensed under the MIT License.  

---

## Contact:  
For issues or suggestions, please open an issue on the GitHub repository:  
[GitHub Issues](https://github.com/ModarRostom/ansible-auto-updates/issues)  

