from netmiko import ConnectHandler

def ssh_command(device,show_cmd):
    net_connect = ConnectHandler(**device)
    show_cmd_out = net_connect.send_command(show_cmd)
    net_connect.disconnect()
    print(show_cmd_out)    

def ssh_command2(device,show_cmd):
    net_connect = ConnectHandler(**device)
    show_cmd_out = net_connect.send_command(show_cmd)
    net_connect.disconnect()
    return show_cmd_out

def ssh_command3(device):
    net_connect = ConnectHandler(**device)
    if device["device_type"] == "juniper_junos":
        show_cmd_out = net_connect.send_command("show arp")
    else:
        show_cmd_out = net_connect.send_command("show ip arp")
    net_connect.disconnect()
    return show_cmd_out
