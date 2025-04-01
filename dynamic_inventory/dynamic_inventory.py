#!/usr/bin/env python3
import json
import subprocess

def get_dynamic_inventory():
    result = subprocess.run(["nmap", "-sn", "192.168.1.0/24"], capture_output=True, text=True)
    hosts = []
    for line in result.stdout.splitlines():
        if "Nmap scan report for" in line:
            ip = line.split(" ")[-1]
            hosts.append(ip)

    # JSON-Inventar erzeugen
    inventory = {
        "webservers": {
            "hosts": hosts,
            "vars": {
                "ansible_user": "root"
            }
        }
    }
    print(json.dumps(inventory))

if __name__ == "__main__":
    get_dynamic_inventory()
