#  1.1

from OperBasicListasE import ListaEnlazada
from colorama import init, Fore

init(autoreset=True)

# Inicializamos la lsita
lista = ListaEnlazada()

while True: 
# Menú de opciones
    print('=' * 45)
    print("Menú de opciones")
    print('=' * 45)
    print("1) Insertar un valor al incio de la lista")
    print("2) Insertar un valor al final de la lista")
    print("3) Contar los nodos de la lista")
    print("4) Determinar si la lista esta vacía")
    print("5) Eliminar un valor de la lista")
    print("6) Eliminar el primer valor")
    print("7) Buscar un valor de la lista")
    print("8) Imprimir los valores de la lista")
    print("9) Imprimir el último valor de la lista")
    print("10) Salir")
    print('=' * 45)
    
    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print(Fore.RED+"Ingrese un número válido.\n")
        continue

    match opc:
        # Insertar un valor al incio de la lista
        case 1:
            try:
                valor = int(input("\nIngrese un valor: "))
                lista.insertar_al_principio(valor)
                print(Fore.GREEN+f"El valor {valor} ha sido agregado al incio de la lista correctamente...\n")
            except ValueError:
                print(Fore.RED+"Error: El número debe ser entero. Intenta nuevamente.\n")
        
        # Insertar un valor al final de la lista  
        case 2:
            try:
                valor = int(input("\nIngrese un valor: "))
                lista.insertar(valor)
                print(Fore.GREEN+f"El valor {valor} ha sido agregado al final de la lista correctamente\n")
            except ValueError:
                print(Fore.RED+"Error: El número debe ser entero. Intenta nuevamente.\n")
        
        # Contar los nodos de la lista
        case 3: 
            cantidad = lista.longitudLista()
            print(Fore.BLUE+f"\nLa lista contiene {cantidad} nodo(s).\n")
            
        # Determinar si la lista esta vacía
        case 4:
            if lista.esta_vacia():
                print(Fore.YELLOW+"\nLa lista está vacía.\n")
            else:
                print(Fore.BLUE+"\nLa lista contiene elementos.\n")
        
        # Eliminar el un valor de la lista
        case 5: 
            try:
                valor = int(input("\nIngrese el valor a eliminar: "))
                if lista.eliminar(valor):
                    print(Fore.GREEN+"Valor eliminado correctamente.\n")
                else:
                    print(Fore.RED+"El valor no se encontró en la lista.\n")
            except ValueError:
                print(Fore.RED+"Error: El número debe ser entero. Intenta nuevamente.\n")
                
        # Eliminar el primer valor de la lista
        case 6: 
            try:
                eliminado = lista.eliminar_primero()
                if eliminado is not None:
                    print(Fore.GREEN+f"\nEl primer valor ({eliminado}) ha sido eliminado correctamente.\n")
                else:
                    print(Fore.RED+"\nLa lista ya está vacía. No se puede eliminar ningún valor.\n")
            except ValueError:
                print(Fore.RED+"Error: El número debe ser entero. Intenta nuevamente.\n")
            
        # Buscar un valor de la lista    
        case 7:
            try: 
                valor = int(input("\nIngrese el valor a buscar: "))
                if lista.buscar(valor):
                    print(Fore.GREEN+f"El valor {valor} se encuentra en la lista.\n")
                else:
                    print(Fore.RED+f"El valor {valor} NO se encuentra en la lista.\n")
            except ValueError:
                print(Fore.RED+"Error: El número debe ser entero. Intenta nuevamente.\n")
        
        # Imprimir los valores de la lista        
        case 8:
            lista.imprimir()
        
        # Imprimir el último valor de la lista
        case 9: 
            lista.imprimir_ultimo()
        
        # Salir del programa
        case 10:
            print(Fore.CYAN+"\nSaliendo del programa...")
            break
        
        case _:
            print(Fore.RED+"\nOpción no válida.\n")