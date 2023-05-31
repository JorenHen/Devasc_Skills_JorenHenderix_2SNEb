from netmiko import ConnectHandler

cisco1 = { 
    "device_type": "cisco_ios",
    "host": "172.16.8.5",
    "username": "admin",
    "password": "Administrator123.",
}

# Show command that we execute.
command = "show ip int brief"

with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()
