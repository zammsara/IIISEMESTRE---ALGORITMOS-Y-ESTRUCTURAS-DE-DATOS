# Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
# PANADERIA || Versión 1.0
# 07.mayo.2025

#Descripción del programa: 
"""
En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja. El primero que se vende es el último que se colocó. Simula el proceso de agregar panes a la bandeja (push), vender uno (pop), y visualizar qué tipo de pan está listo para vender (peek). 
"""

from pila import Pila
import mod_menu as menu
from colorama import Fore, Style, init

pila = Pila()

opcion = 0

while opcion != 5:
    menu.limpiar_consola()  # Limpia la consola antes de mostrar el menú
    menu.menu()
    #Valida si el usuario ingresó un número entero.
    try:
        opcion = int(input("Respuesta: "))
        print("\n")
    except ValueError:
        print(Fore.RED+"Opción no válida. Intenta de nuevo.")
        menu.pausa() 
        continue

    match opcion:
        case 1:  # Agregar elemento a la pila 
            precio = 0
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Agregar Pan Recien Horneado:") 
            print(Fore.LIGHTBLACK_EX + Style.DIM + "Ejemplo: Pan de Chocolate, Pan de Ajo, Pan de Mantequilla, Pan de Pasas, Pan de Frutas, Pan de Almendras, Croissant")  # Gris y tenue
            tipo = input("Respuesta: ")
            
            try:
                precio = int(input("Precio del pan(c$): "))
            except ValueError:
                print(Fore.RED+"Respuesta tiene que ser un numero. Intenta de nuevo.")
                menu.pausa() 
                continue
            pila.push(tipo, precio)  # Agrega el tipo de pan a la pila
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Elemento agregado a la pila.")
            menu.pausa()


        case 2:  # Mostrar el último pan agregado
            menu.limpiar_consola()  
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Último pan agregado:")  # Azul claro y brillante
            ultimo_pan = pila.peek()
            if ultimo_pan:
                print(f"Tipo: {ultimo_pan[0]}, Precio: {ultimo_pan[1]} c$")
            else:
                print(Fore.RED + "No hay panes en la bandeja.")
            menu.pausa()
        
        
        case 3:  # Vender pan
            menu.limpiar_consola()  
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Vendiendo pan...")  # Azul claro y brillante
            vendido = pila.pop()
            if vendido:
                print(f"Pan vendido: {vendido}")
            else:
                print(Fore.RED + "No hay panes en la bandeja para vender.")
            menu.pausa()
        
        
        case 4:  # Imprimir pila
            menu.limpiar_consola()  # Limpia la consola antes de mostrar el contenido de la pila
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Contenido del Stack de panes:")  # Azul claro y brillante
            pila.imprimir()
            menu.pausa()


        case 5:  # Salir
            print(Fore.LIGHTRED_EX + Style.BRIGHT + "Saliendo del programa...")  # Rojo brillante
            print(Fore.CYAN+"Gracias por usar el programa. ¡Hasta luego! 👋")


        case _:  # Opción no válida
            print(Fore.RED + "Opción no válida. Intenta de nuevo.")
            menu.pausa()