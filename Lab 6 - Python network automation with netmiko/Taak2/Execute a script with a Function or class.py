from netmiko import ConnectHandler

def connect_to_device(device):
connection = ConnectHandler(**device)


def send_command(connection, command):
output = connection.send_command(command)

# Return the output
return output

def disconnect_from_device(connection):

connection.disconnect()

devices = [
{
    "device_type": "cisco_ios",
    "host": "172.16.8.4",
    "username": "admin",
    "password": "Administrator123."
},
{
    "device_type": "cisco_ios",
    "host": "172.16.8.5",
    "username": "admin",
    "password": "Administrator123."
}

for device in devices:
connection = connect_to_device(device)
output = output + send_command(connection, 'show ip int bri')
print(output)
disconnect_from_device(connection)
