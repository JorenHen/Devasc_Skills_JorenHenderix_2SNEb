from netmiko import ConnectHandler

cisco_01 = {
    "device_type": "cisco_ios",
    "host": "172.16.8.5",
    "username": "admin",
    "password": "Administrator123.",
    "secret": "Admin123."
}

connection = ConnectHandler(**cisco_01)
connection.enable()

config_commands = ['interface gi0/1', 'descri WAN', 'exit']
connection.send_config_set(config_commands)

print('Closing Connection')
connection.disconnect()

