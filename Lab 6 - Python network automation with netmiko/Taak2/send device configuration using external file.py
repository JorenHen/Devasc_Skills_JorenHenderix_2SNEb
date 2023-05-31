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

config_file = '172.16.8.0.txt'

for device in devices:
# Connect to the device
verbinding = ConnectHandler(**device)

# Send the configuration commands from the file
output = connection.send_config_from_file(config_file)

# Print the output to the console
print(output)

# Disconnect from the device
verbinding.disconnect()
