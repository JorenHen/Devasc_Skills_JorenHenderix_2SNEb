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
def connect_to_device(device):
connection = ConnectHandler(**device)
# Perform actions on the device, such as running commands or sending configurations
connection.disconnect()

threads = []

for device in devices:
thread = threading.Thread(target=connect_to_device, args=(device,))
thread.start()
threads.append(thread)

for thread in threads:
thread.join()
