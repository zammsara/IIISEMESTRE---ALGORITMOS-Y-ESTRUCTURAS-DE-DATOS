# Programa "Cola prioritaria" desarrollado por: Sara Zambrana
# 20.mayo.2025
# Versión 1.0

# Descripción del programa/ejercicio:
# Implementación de una cola de prioridad. Diseñe una cola de
# prioridad donde los elementos se desencolan según su prioridad. Cada elemento
# tendrá un nombre y una prioridad (un número entero, donde un número menor indica
# mayor prioridad).

# Importamos el módulo
from Modulo import Elemento, Cola
cola = Cola() # Inicializamos la cola

# Importamos la librería colorama para hacer el programa más agradable visualmente
from colorama import init, Fore, Style
init(autoreset=True)

# Librería que utilizaremos en el método "clear" para limpiar pantalla
import os

# Método para limpiar pantalla
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')

while True:
    print('=' * 35)
    print("\tCola Prioritaria")
    print('=' * 35)
    print("1. Colocar elemento en la cola")
    print("2. Descolocar elemento de la cola")
    print("3. Mostrar elementos de la cola")
    print("4. Salir")
    print('=' * 35)
    
    try:
        opc = int(input("Ingresa una opción: "))
    except ValueError:
        print(Fore.RED+"Ingresa un número válido.\n")
        continue
    
    match opc:
        case 1:
            clear()
            nombre_elemento = input("Ingresa el nombre del elemento: ")
            while True:
                prioridad= input("Ingresa la prioridad (1-5): ")

                #se verifica que se ingrese un número
                if not prioridad.isdigit():
                    print(Fore.RED+"Error: La prioridad debe ser un número entero.")
                    continue

                prioridad = int(prioridad)

                #se verifica que esté en el rango permitido
                if prioridad < 1 or prioridad > 5:
                    print(Fore.RED+"Error: La prioridad debe estar entre 1 y 5.")
                    continue

                break#si la entrada es válida, salimos del ciclo

            #creamos el objeto y lo agregamos a la cola
            nuevo_elemento = Elemento(nombre_elemento, prioridad)
            cola.Colocar_Elemento(nuevo_elemento)
            print(Fore.GREEN+f"Elemento: {nuevo_elemento} agregado correctamente.")
        
        case 2:
            clear()
            cola.Descolocar_Elemento()
        
        case 3:
            clear()
            cola.Mostrar_Cola()
        
        case 4:
            clear()
            print(Fore.CYAN+Style.BRIGHT+"Saliendo...")
            break
        
        case _:
            print(Fore.RED+"Opción inválida. Intenta de nuevo\n") 
    

