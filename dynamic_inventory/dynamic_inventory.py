#!/usr/bin/env python3

import argparse
import json
import logging
import os
import sys

# Set up logging to a file
logging.basicConfig(
    filename='inventory.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define path to hosts.json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOSTS_FILE = os.path.join(BASE_DIR, 'hosts.json')

def load_inventory():
    """Load hosts.json and return it as a Python dictionary"""
    try:
        with open(HOSTS_FILE, 'r') as f:
            data = json.load(f)
        # Build _meta with hostvars (if any)
        hostvars = {}
        for group, group_data in data.items():
            for host in group_data.get("hosts", []):
                # Example: set ansible_user from group vars
                vars_for_host = group_data.get("vars", {})
                if host not in hostvars:
                    hostvars[host] = vars_for_host
        data["_meta"] = {"hostvars": hostvars}
        return data
    except Exception as e:
        logging.error(f"Error loading inventory: {e}")
        return {}

def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action='store_true', help='List all hosts')
    parser.add_argument('--host', help='Get variables for a single host')
    args = parser.parse_args()

    inventory = load_inventory()

    if args.list:
        print(json.dumps(inventory, indent=2))
    elif args.host:
        # Optional: return specific hostvars
        hostvars = inventory.get("_meta", {}).get("hostvars", {})
        print(json.dumps(hostvars.get(args.host, {}), indent=2))
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
