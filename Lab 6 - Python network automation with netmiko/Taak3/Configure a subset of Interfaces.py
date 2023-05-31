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
def configure_interfaces(device, interfaces):
connection = ConnectHandler(**device)
interface_commands = []
for interface in interfaces:
    interface_commands.append(f"interface {interface}")
    interface_commands.append("description Test")  # Example configuration command
    # Add more configuration commands for each interface as needed
output = connection.send_config_set(interface_commands)
print(f"Configuration applied on {device['ip']}")
connection.disconnect()
threads = []

interfaces_to_configure = ['GigabitEthernet1', 'GigabitEthernet2']

for device in devices:
thread = threading.Thread(target=configure_interfaces, args=(device, interfaces_to_configure))
thread.start()
threads.append(thread)

for thread in threads:
thread.join()
