#!/usr/bin/env 	python3

from os import name
from os import system
# Importar los modulos necesarios para la funcion ping

def clear_screen():
   if name == "nt":
       _ = system("cls")

   else:
       _ = system("clear")



def ping(ip):
    # Aqui va el codigo de la funcion ping



def main():
    # Mandar a llamar a la funcion clear_screen
    clear_screen()


    # Mandar a llamar a la funcion clear_screen
    ping(ip)



if __name__ == '__main__':
    main()
