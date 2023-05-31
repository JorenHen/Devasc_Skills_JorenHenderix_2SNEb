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
def backup_device_config(device):
connection = ConnectHandler(**device)
output = connection.send_command('show running-config')
filename = f"{device['ip']}_config.txt"
with open(filename, 'w') as f:
    f.write(output)
print(f"Configuration backup from {device['ip']} saved to {filename}")
connection.disconnect()
threads = []

for device in devices:
thread = threading.Thread(target=backup_device_config, args=(device,))
thread.start()
threads.append(thread)

for thread in threads:
thread.join()
