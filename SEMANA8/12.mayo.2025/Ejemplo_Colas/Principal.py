import Modulo
cola = Modulo.Cola()

from colorama import Fore, Style, init
init(autoreset=True)

while True:
    print('='*30)
    print("Operaciones básicas sobre la cola")
    print('='*30)
    print("1. Agregar un nuevo elemento")
    print("2. Eliminar un elemento")
    print("3. Imprimir elementos")
    print("4. Salir")
    print('='*30)
    
    try:
            opc = int(input("Seleccione una opción: "))
    except ValueError:
            print(Fore.RED+"Ingrese un número válido.\n")
            continue
    
    match opc:
        case 1:
            dato = input("Ingresa el dato que deseas agregar: ")
            cola.Insertar(dato)
            
            
        case 2:
            cola.Eliminar()
            
        case 3:
            cola.Imprimir()
            
        case 4:
            print(Fore.CYAN+"Saliendo del programa...")
            break
        case _:
            print(Fore.RED+"Opción inválida")