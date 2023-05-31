from netmiko import ConnectHandler

# Define the devices to connect to
devices = [
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.8.4',
        'username': 'admin',
        'password': 'Administrator123.',
        'secret': 'Admin123.'
    },
    {
        'device_type': 'cisco_ios',
        'ip': '172.16.8.5',
        'username': 'admin',
        'password': 'Administrator123.',
        'secret': 'Admin123.'
    }
]

# Define the commands to send to the devices
commands = [
    'interface GigabitEthernet0/1',
    'description Uplink',
    'no shutdown'
]

# Loop through each device and send the commands
for device in devices:
    # Connect to the device
    print('Connecting to device', device['ip'])
    net_connect = ConnectHandler(**device)

    # Enter enable mode
    net_connect.enable()

    # Send the commands
    print('Sending commands to device', device['ip'])
    output = net_connect.send_config_set(commands)
    print(output)

    # Disconnect from the device
    print('Disconnecting from device', device['ip'])
    net_connect.disconnect()

