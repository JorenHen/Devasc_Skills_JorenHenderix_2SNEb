from netmiko import ConnectHandler
import threading
devices = [
{
    'device_type': 'cisco_xe',
    'ip': '192.168.253.128',
    'username': 'admin',
    'password': 'Admin!.',
}

]
def send_config_commands(device, commands):
connection = ConnectHandler(**device)
output = connection.send_config_set(commands)
print(f"Output from {device['ip']}:\n{output}")
connection.disconnect()
threads = []
config_commands = [
'interface GigabitEthernet1',
'ip address 192.168.253.100 255.255.255.0',
'no shutdown',
# Add more configuration commands as needed
]
for device in devices:
thread = threading.Thread(target=send_config_commands, args=(device, config_commands))
thread.start()
threads.append(thread)
for thread in threads:
thread.join()
