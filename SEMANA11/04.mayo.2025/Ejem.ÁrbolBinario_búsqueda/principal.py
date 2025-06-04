from modulo import ArbolBin

from colorama import init, Style, Fore
init(autoreset=True)

import os
def clear():
    # Limpiar la consola
    os.system('clear') 
    os.system('cls')

tree = ArbolBin() #Instancia de árbol binario 

while True: 
    print('='*25)
    print("\tMenú")
    print('='*25)
    print("1. Insertar valor")
    print("2. Buscar valor")
    print("3. Recorrido inorden")
    print("4. Recorrido preorden")
    print("5. Recorrido postorden")
    print("6. Salir")
    print('='*25)
    
    try:
        opc = int(input("Ingresa una opción: "))
    except ValueError:
        print(Fore.RED+"Ingresa un número válido.\n")
        continue
    
    match opc:
        case 1:
            clear()
            try:
                valor = int(input("Ingrese el valor a insertar: "))
                tree.insertar(valor)
                print(Fore.GREEN + f"Valor {valor} insertado correctamente.")
            except ValueError:
                print(Fore.RED + "El valor debe ser un número entero.")

        case 2:
            clear()
            try:
                valor = int(input("Ingrese el valor a buscar: "))
                encontrado = tree.buscar(valor)
                print(Fore.GREEN + "Valor encontrado." if encontrado else Fore.RED + "Valor no encontrado.")
            except ValueError:
                print(Fore.RED + "El valor debe ser un número entero.")

        case 3:
            clear()
            print(Style.BRIGHT + Fore.CYAN + "Recorrido inorden:", end=" ")
            tree.recorridoinorden(tree.raiz)
            print()
            
        case 4:
            clear()
            print(Style.BRIGHT + Fore.CYAN + "Recorrido preorden:", end=" ")
            tree.recorridopreorden(tree.raiz)
            print()
            
        case 5:
            clear()
            print(Style.BRIGHT + Fore.CYAN + "Recorrido postorden:", end=" ")
            tree.recorridopostorden(tree.raiz)
            print()
            
        case 6:
            clear()
            print(Fore.YELLOW + "Saliendo del programa.")
            break
        
        case _:
            print(Fore.RED + "Opción no válida. Intente nuevamente.")