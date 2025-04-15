import json
import subprocess

def scan_network():
    # Beispielhafte Funktion für die IP-Scans (ersetzt mit echter Netzwerkscan-Logik)
    return ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

def create_inventory(ip_list):
    # Erstelle das dynamische Inventory
    inventory = {
        "all": {
            "hosts": ip_list
        }
    }
    return inventory

def save_inventory(inventory):
    with open("dynamic_inventory/inventory.json", "w") as f:
        json.dump(inventory, f, indent=4)

def main():
    ip_list = scan_network()
    inventory = create_inventory(ip_list)
    save_inventory(inventory)

if __name__ == "__main__":
    main()
