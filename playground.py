from netmiko import ConnectHandler


ios7200 = {
    "device_type": "cisco_ios",
    "ip": "10.10.10.1",
    "username": "admin",
    "password": "cisco",
    "secret": "cisco",
}

net_connect = ConnectHandler(**ios7200)

net_connect.enable()

output = net_connect.send_command("sh run")
print(output)

f = open("sh_run.txt","wb")
f.write(output.encode())
f.close()

#output = net_connect.send_config_set("")
#print(output)

# = net_connect.send_command("sh run | sec bgp")
#print(output)