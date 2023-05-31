from netmiko import ConnectHandler

devices = [
 {
     "device_type": "cisco_ios",
     "host": "172.16.8.4",
     "username": "admin",
     "password": "Administrator123."

},
{
    'device_type': 'cisco_ios',
    'host': '172.16.8.5',
    'username': 'admin',
    "password": "Administrator123."
    
}
]

interfaces = ['GigabitEthernet0/0', 'GigabitEthernet0/1']

config_commands = [
'interface ' + intf for intf in interfaces,
'ip address 172.168.8.5 255.255.255.0',
'no shut'
]

for device in devices:
# Connect to the device
connection = ConnectHandler(**device)

# Send the configuration commands for the subset of interfaces
output = connection.send_config_set(config_commands)

# Print the output to the console
print(output)

# Disconnect from the device
connection.disconnect()
