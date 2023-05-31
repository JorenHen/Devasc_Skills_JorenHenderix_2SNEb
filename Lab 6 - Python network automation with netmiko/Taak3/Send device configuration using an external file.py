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
def send_config_from_file(device, config_file):
with open(config_file, 'r') as file:
    config_commands = file.read().splitlines()
connection = ConnectHandler(**device)
output = connection.send_config_set(config_commands)
print(f"Configuration applied to {device['ip']}")
connection.disconnect()

threads = []

config_file = 'configuratie.txt'

for device in devices:
thread = threading.Thread(target=send_config_from_file, args=(device, config_file))
thread.start()
threads.append(thread)

for thread in threads:
thread.join()
