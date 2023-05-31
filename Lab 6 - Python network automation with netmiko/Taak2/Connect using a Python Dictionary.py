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
for device in devices:
    verbinding = ConnectHandler(**device)
    output = output + connection.send_command('show ip int bri')
print(output)
verbinding.disconnect()
