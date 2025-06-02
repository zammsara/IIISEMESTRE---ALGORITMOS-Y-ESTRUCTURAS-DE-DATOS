from colorama import Fore, Style, init
import os

init(autoreset=True)

# Método para limpiar pantalla
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')

# Creamos una cola usando lista
cola = []

while True:
    print("="*40)
    print(" COLA con listas - Menú interactivo ")
    print("="*40)
    print("1. Agregar un elemento (al final)")
    print("2. Eliminar un elemento (del frente)")
    print("3. Ver primer elemento (peek)")
    print("4. Ver último elemento")
    print("5. Mostrar todos los elementos")
    print("6. Ver si la cola está vacía")
    print("7. Salir")
    print("="*40)

    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print(Fore.RED + "\nIngrese un número válido.\n")
        continue

    match opc:
        case 1:
            clear()
            dato = input("Ingrese el dato a agregar: ")
            cola.append(dato)  # Se agrega al final
            print(Fore.GREEN + f"'{dato}' agregado a la cola.")
            
        case 2:
            clear()
            if cola:
                eliminado = cola.pop(0)  # Se elimina el primer elemento
                print(Fore.YELLOW + f"Elemento eliminado: '{eliminado}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 3:
            clear()
            if cola:
                print(Fore.CYAN + f"Primer elemento: '{cola[0]}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 4:
            clear()
            if cola:
                print(Fore.CYAN + f"Último elemento: '{cola[-1]}'")
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 5:
            clear()
            if cola:
                print(Style.BRIGHT + "\nContenido de la cola:")
                for item in cola:
                    print(item)
            else:
                print(Fore.RED + "La cola está vacía.")
                
        case 6:
            clear()
            print(Fore.CYAN + ("La cola está vacía." if not cola else "La cola tiene elementos."))
            
        case 7:
            clear()
            print(Fore.CYAN + "Saliendo del programa...")
            break
        
        case _:
            print(Fore.RED + "Opción inválida.")
