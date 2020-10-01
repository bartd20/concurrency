from datetime import datetime
from netmiko import ConnectHandler
from my_devices import devices

def get_output(device,show_cmd):
    net_connect = ConnectHandler(**device)
    show_cmd_out = net_connect.send_command(show_cmd)
    net_connect.disconnect()
    return show_cmd_out    

start_t = datetime.now()

for elem in devices:
    print("Connecting to: "+elem["host"])
    print(get_output(elem,"show version"))
    print("-----------------------------")

stop_t = datetime.now()

print("Run time: "+str(stop_t - start_t))

