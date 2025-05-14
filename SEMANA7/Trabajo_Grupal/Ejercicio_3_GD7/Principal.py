# Programa "Registro de donantes - Hospital Estelí"
# Desarrollado por: Sara Zambrana
# Versión 1
# 07.mayo.2025

# Descripción del ejercicio (#03):
# En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se
# almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe
# revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último
# (pop), y mostrar el donante actual en proceso.

from Pila import Nodo, PilaDonantes
from colorama import init, Fore, Style
import os

init(autoreset=True)

def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')
    
# Creamos una pila vacía
pila = PilaDonantes()

while True:
    print('=' * 40)
    print("Registro de donantes - Hospital Estelí")
    print('=' * 40)
    print("1. Registrar nuevo donante")
    print("2. Eliminar último donante")
    print("3. Mostrar donante actual")
    print("4. Salir")
    print('=' * 40)
    
    try:
            opc = int(input("Seleccione una opción: "))
    except ValueError:
            print(Fore.RED+"Ingrese un número válido.\n")
            continue
        
    match opc:
        
        # Registrar nuevos donantes
        case 1:
            clear()
            print("\n========== Registrar Donante ===========")
            nombre = input("Nombre completo: ")
            tipo_sangre = input("Tipo de sangre (A+, A-, B+, B-, AB+, AB-, O+, O-): ")
            datos = f"{nombre} - {tipo_sangre}"
            pila.push(datos)
            input("\nPresione Enter para continuar...\n")

        
        # Eliminar último donante
        case 2:
            clear()
            pila.pop()
            input("\nPresione Enter para continuar...\n")
        
        # Mostrar donante actual
        case 3:
            clear()
            pila.mostrar_actual()
            input("\nPresione Enter para continuar...\n")
            
        # Salir del programa
        case 4:
            print(Fore.CYAN+"\nSaliendo del Registro.")
            print(Fore.CYAN+"Gracias por usar el programa. ¡Hasta luego!")
            break
        
        case _:
            print(Fore.RED+"Opción no válida. Intenta de nuevo.\n") 