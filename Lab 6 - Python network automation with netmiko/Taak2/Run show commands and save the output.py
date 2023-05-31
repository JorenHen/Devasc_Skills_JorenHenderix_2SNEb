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

commands = ['show ip int bri', 'show ip ospf', 'show startup-config']

for device in devices:
    net_connect = ConnectHandler(**device)

    for command in commands:
        output = net_connect.send_command(command)
        print('Output from {}: {}'.format(device['host'], output))

net_connect.disconnect()

