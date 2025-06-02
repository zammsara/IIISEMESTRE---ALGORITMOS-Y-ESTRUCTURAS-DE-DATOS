# Importamos el módulo
import modulo
cola = modulo.Cola()

# Importamos la librería colorama para hacer el programa más agradable visualmente
from colorama import Fore, Style, init
init(autoreset=True)

# Librería que utilizaremos en el método "clear" para limpiar pantalla
import os

# Método para limpiar pantalla
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')

while True:
    print('='*35)
    print("Operaciones básicas sobre la cola")
    print('='*35)
    print("1. Agregar un nuevo elemento")
    print("2. Eliminar un elemento")
    print("3. Imprimir elementos")
    print("4. Salir")
    print('='*35)
    
    try:
            opc = int(input("Seleccione una opción: "))
    except ValueError:
            print(Fore.RED+"Ingrese un número válido.\n")
            continue
    
    match opc:
        case 1:
            clear()
            dato = input("Ingresa el dato que deseas agregar: ")
            cola.Insertar(dato)
            
            
        case 2:
            clear()
            cola.Eliminar()
            
        case 3:
            clear()
            cola.Imprimir()
            
        case 4:
            clear()
            print(Fore.CYAN+"Saliendo del programa...")
            break
        
        case _:
            print(Fore.RED+"Opción inválida")