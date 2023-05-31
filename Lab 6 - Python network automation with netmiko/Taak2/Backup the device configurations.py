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
connection = ConnectHandler(**device)

config = connection.send_command('show running-config')

backup = f"{device['host']}_config.txt"
with open(backup, 'w') as file:
    file.write(config)

connection.disconnect()
