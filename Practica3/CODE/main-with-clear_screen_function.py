#!/usr/bin/env 	python3

from os import name
from os import system


def clear_screen():
   if name == "nt":
       _ = system("cls")

   else:
       _ = system("clear")



def main():
    # Mandar a llamar a la funcion clear_screen
    clear_screen()


if __name__ == '__main__':
    main()
