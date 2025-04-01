#!/usr/bin/env python3
import json
import subprocess
import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText

# Email configuration
SENDER_EMAIL = "your-email@example.com"
RECEIVER_EMAIL = "alert@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "your-email@example.com"
SMTP_PASS = "your-password"

# Log file path
log_file = "../logs/update.log"

# Function to log messages
def log_message(message):
    with open(log_file, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

# Function to send email notifications
def send_email(subject, message):
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        log_message(f"Email sent: {subject}")
    except Exception as e:
        log_message(f"Error sending email: {str(e)}")

# Function to generate dynamic inventory
def get_dynamic_inventory():
    try:
        result = subprocess.run(["nmap", "-sn", "192.168.1.0/24"], capture_output=True, text=True)
        hosts = []
        for line in result.stdout.splitlines():
            if "Nmap scan report for" in line:
                ip = line.split(" ")[-1]
                hosts.append(ip)

        inventory = {
            "webservers": {
                "hosts": hosts,
                "vars": {
                    "ansible_user": "root"
                }
            }
        }

        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
        log_message("Inventory updated successfully.")
    except Exception as e:
        log_message(f"Error updating inventory: {str(e)}")
        send_email("Inventory Update Failed", str(e))

if __name__ == "__main__":
    get_dynamic_inventory()

