from netmiko import ConnectHandler

devices = [
{
    'device_type': 'cisco_ios',
    'host': '172.16.8.4',
    'username': 'admin',
    "password": "Administrator123."
 },
 {
    'device_type': 'cisco_ios',
    'host': '172.16.8.5',
    'username': 'admin',
    "password": "Administrator123."
 }

for device in devices:
connection = ConnectHandler(**device)

interface_name = 'GigabitEthernet0/0'
if interface_name.startswith('GigabitEthernet'):
command = 'show interfaces ' + interface_name
else:
command = 'show interface ' + interface_name

output = output + connection.send_command(command)

print(output)

connection.disconnect()
