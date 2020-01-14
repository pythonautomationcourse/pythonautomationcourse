#!/usr/bin/env  python3


from netmiko import Netmiko

# ip_list = [
#   "192.168.100.1", "192.168.100.2", "192.168.100.3",
#   "192.168.100.4", "192.168.100.254",
#    ]

ip_list = "192.168.100.1"


ios_device = {
    "device_type": "cisco_ios",     # Tipo de dispositivo.
    "ip": ip_list,                  # IP Address.
    "username": "python",            # Nombre de Usuario.
    "password": "pythonautomationcourse",    # Password de usuario.
    "secret": "pythonautomationcourse",      # Password enable secret.
    }


# Creacion de la conexion SSH
net_connect = Netmiko(**ios_device) # ** Significa que es pasado todas los
                                    # valores de las llaves del diccionario.

net_connect.enable()                # Entrar en "Modo Privilegiado".

# Variable de texto con valor del comando para L2 o L3.
show_version = "show version | section include Cisco IOS Software"

# Enviar el comando "show_version" y guardar en la variable "output"
# para su posterior tratamiento.
output = net_connect.send_command(show_version)

# Si "el texto" se encuentra en la variable "output" entonces se realiza
# la siguiente actividad.
if "vios_l2-ADVENTERPRISEK9-M" in output:
    
    # Declaracion de la lista vacia de "vlan_list".
    vlan_list = []
    # Crear vlans.
    for vlan in range(2, 41):
        # Evitar agregar las vlan 7, 10, 20, 35 a la lista.
        if vlan != 7 and vlan != 10 and vlan != 20 and vlan != 30:
            # Se agregan las vlan a la lista "vlan_list"
            vlan_list.append(vlan)


    # Enviar comando para la creacion de VLAN's
    for vlan in vlan_list:
        # Variable de texto con el comando para crear vlan".
        vlan_id = "vlan {}".format(vlan)
        # Ingresado al modo "VLAN" enviar el respectivo nombre.
        vlan_name = "name Automation_VLAN_{}".format(vlan)
        
        # Ingresar las variables a una lista para enviar en "send_config_set".
        command_list = [
            vlan_id, vlan_name,
            ]
        
        # Enviar lista de comandos en "Modo Configuracion Global".
        net_connect.send_config_set(command_list)
    
    
    # Salvar la configuracion en el Swtich.
    net_connect.save_config()
    
    # Finalizar la conexion del dispositivo.
    net_connect.disconnect()
        


elif "VIOS-ADVENTERPRISEK9-M" in output:
    # Imprimir que es un Router
    print("Este es un dispositivo L3 no necesita crear VLAN's")
    
    # Finalizar la conexion del dispositivo.
    net_connect.disconnect()