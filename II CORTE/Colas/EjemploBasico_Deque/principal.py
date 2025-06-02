from collections import deque
from colorama import Fore, Style, init
import os

init(autoreset=True)

# Método para limpiar pantalla
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')

# Creamos una cola usando deque
cola = deque()

while True:
    print("="*40)
    print(" COLA con deque - Menú interactivo ")
    print("="*40)
    print("1. Agregar elemento al final (append)")
    print("2. Agregar elemento al frente (appendleft)")
    print("3. Eliminar elemento del frente (popleft)")
    print("4. Eliminar elemento del final (pop)")
    print("5. Ver primer elemento (peek)")
    print("6. Ver último elemento")
    print("7. Mostrar todos los elementos")
    print("8. Ver si la cola está vacía")
    print("9. Salir")
    print("="*40)

    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print(Fore.RED + "\nIngrese un número válido.\n")
        continue

    match opc:
        case 1:
            clear()
            dato = input("Ingrese el dato a agregar al final: ")
            cola.append(dato)
            print(Fore.GREEN + f"'{dato}' agregado al final de la cola.")
            
        case 2:
            clear()
            dato = input("Ingrese el dato a agregar al frente: ")
            cola.appendleft(dato)
            print(Fore.GREEN + f"'{dato}' agregado al frente de la cola.")
            
        case 3:
            clear()
            if cola:
                eliminado = cola.popleft()
                print(Fore.YELLOW + f"Elemento eliminado del frente: '{eliminado}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 4:
            clear()
            if cola:
                eliminado = cola.pop()
                print(Fore.YELLOW + f"Elemento eliminado del final: '{eliminado}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 5:
            clear()
            if cola:
                print(Fore.CYAN + f"Primer elemento: '{cola[0]}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 6:
            clear()
            if cola:
                print(Fore.CYAN + f"Último elemento: '{cola[-1]}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 7:
            clear()
            if cola:
                print(Style.BRIGHT + "\nContenido de la cola:")
                for item in cola:
                    print(item)
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 8:
            clear()
            print(Fore.CYAN + ("La cola está vacía." if not cola else "La cola tiene elementos."))
            
        case 9:
            clear()
            print(Fore.CYAN + "Saliendo del programa...")
            break
        
        case _:
            print(Fore.RED + "Opción inválida.")
