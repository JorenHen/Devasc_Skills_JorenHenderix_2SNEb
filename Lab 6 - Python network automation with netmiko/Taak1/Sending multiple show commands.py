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

# Show the second command that we execute.
command2 = "show ip arp"

with ConnectHandler(**cisco1) as net_connect:
    output2 = net_connect.send_command(command2)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print(output2)
print()

