#!/usr/bin/env  python3

from netmiko import Netmiko
from getpass import getpass

username = input("Dame usuario: ")          # Pide el nombre del usuario
password = getpass("Dame el password: ")    # Pide el password
secret = getpass("Dame el enable: ")        # Pide el enable

# Definir las ips de los dispositivos a configurar
ip_list = [
    "192.168.100.1", "192.168.100.2",
    "192.168.100.3", "192.168.100.254"
    ]

# Entrar en los dispositivos a traves de SSH con la libreria Netmiko
for ip in ip_list:
    dispositivo = {
        "username": username,
        "ip": ip,
        "password": password,
        "device_type": "cisco_ios",
        "secret": secret,
        }

    net_connect = Netmiko(**dispositivo)
    net_connect.enable()

    output = net_connect.send_command("show cdp")

    if "% CDP is not enabled" in output:
        print("CDP no esta habilitado en {}".format(ip))

        # command = ["no cdp run"]
        # net_connect.send_config_set("no cdp run")
    else:
        print("CDP esta habilitado en {}.".format(ip))
        command = ["no cdp run"]
        net_connect.send_config_set("no cdp run")

    net_connect.save()
