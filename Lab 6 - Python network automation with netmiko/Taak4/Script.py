import requests
import json

def get_device_interfaces(device_ip, username, password):
    """
    Function to retrieve the interfaces of an IOS-XE network device.
    """
    url = f"https://{device_ip}/restconf/data/ietf-interfaces:interfaces"
    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }
    auth = (username, password)

    try:
        response = requests.get(url, headers=headers, auth=auth)
        if response.status_code == 200:
            interfaces = response.json()
            return interfaces
        else:
            print(f"Error: {response.status_code} - Failed to retrieve interfaces.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def configure_interface(device_ip, username, password, interface, config_commands):
    """
    Function to configure an interface on an IOS-XE network device.
    """
    url = f"https://{device_ip}/restconf/data/ietf-interfaces:interfaces/interface={interface}"
    headers = {
        "Content-Type": "application/yang-data+json",
        "Accept": "application/yang-data+json",
    }
    auth = (username, password)
    payload = {
        "ietf-interfaces:interface": {
            "name": interface,
            "description": config_commands[0],
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": config_commands[1].split()[2],
                        "netmask": config_commands[1].split()[3],
                    }
                ],
            },
            "enabled": True,
        }
    }

    try:
        response = requests.put(url, headers=headers, auth=auth, data=json.dumps(payload))
        if response.status_code == 204:
            print("Interface configuration successful.")
        else:
            print(f"Error: {response.status_code} - Failed to configure interface.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

device_ip = "192.168.253.128"
username = "admin"
password = "Admin!"

# Retrieve interfaces of the device
interfaces = get_device_interfaces(device_ip, username, password)
print("Interfaces:")
print(json.dumps(interfaces, indent=4))
print()

# Configure an interface
interface = "GigabitEthernet1"
config_commands = [
    "Connected to Switch1",
    "ip address 192.168.2.1 255.255.255.0",
]
configure_interface(device_ip, username, password, interface, config_commands)

