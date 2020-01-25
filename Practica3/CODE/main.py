#!/usr/bin/env  python3.6


import subprocess
from os import name
from os import system
from netmiko import Netmiko


def clear_screen():
    """
    Funcion para limpia la pantalla. 
    """
    if name == "nt":
        _ = system("cls")

    else:
        _ = system("clear")


def ping_alive(ip):
    """
    Funcion para realizar pruebas de conectividad PING.
    """
    respuesta = subprocess.call(
        "ping -c 4 {}".format(ip),
        shell=True,
        stdout=open("/dev/null", "w"),
        )

    if respuesta == 0:
        with open("{}_file.txt".format(ip), mode="w") as file:
            file.write("El dispositivo {} esta vivo".format(ip))
            file.close()

    else:
        with open("{}_file.txt".format(ip), mode="w") as file:
            file.write("El dispositivo {} no esta vivo".format(ip))
            file.close()


def read_files(name_file):
    """
    Funcion para leer el contenido de los archivos.
    """
    with open(name_file, mode="r") as file:
        list = file.read()
        file.close()
    return list


def main():
    """
    Funcion principal
    """
    
    # Llamada a la funcion "clear_screen"
    clear_screen()

    # variable de texto con el valor "ips.txt"
    name_file_ip_list = "ips.txt"
    # variable de texto con el valor "commands.txt"
    name_file_commands_list = "commands.txt"

    # Llamada a la funcion "read_files" y guardarla en la variable "ips_list".
    ips_list = read_files(name_file_ip_list)
    # Dividir las lineas de la variable ips_list en una lista. 
    ips_list = ips_list.splitlines()

    # Llamada a la funcion "read_files" y guardarla en la variable
    # "command_list".
    command_list = read_files(name_file_commands_list)
    # Dividir las lineas de la variable ips_list en una lista.
    command_list = command_list.splitlines()

    # Realizar ciclo for con la lista "ip_list". para determinar que "ips"
    # estan activas.
    for ip in ips_list:
        # Llamada a la funcion "ping_alive" con el argumento "ip".
        ping_alive(ip)

    # Realizar ciclo for con la lista "ip_list". para realizar las conexions
    # y configuraciones con la libreria Netmiko.
    for ip in ips_list:
        dispositivo = {
            "username": "python",
            "ip": ip,
            "password": "pythonautomationcourse",
            "device_type": "cisco_ios",
            "secret": "pythonautomationcourse",
            }

        # Creacion de la conexion SSH.
        net_connect = Netmiko(**dispositivo)    # ** Significa que es pasado
                                                # todos los valores del
                                                # Diccionario.

        net_connect.enable()                    # Entrar en modo Privilegiado.

        # Enviar lista "command_list" en modo "Configuracion Global".
        net_connect.send_config_set(command_list)
        
        # Salvar la configuracion en los dispositivos.
        net_connect.save_config()
        
        # Finalizar la conexión del dispositivo.
        net_connect.disconnect()


if __name__ == '__main__':
    main()