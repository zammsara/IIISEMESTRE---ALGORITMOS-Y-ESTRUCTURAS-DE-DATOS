from Factura import Factura
from colorama import init, Fore

init(autoreset=True)

facturas = {} # Se inicializa el diccionario que alamacenará las facturas a crearse

while True:
    print("========================================")
    print("\t\tMenú:")
    print("========================================")
    print("1. Crear nueva factura")
    print("2. Agregar producto a factura")
    print("3. Mostrar reporte de factura")
    print("4. Salir")
    print("========================================")
    
    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print(Fore.RED+"Ingrese un número válido.")
        continue
    
    match opc:
        case 1:
            numero = input("\nIngrese número de factura: ")
            cliente = input("Nombre del cliente: ")
            facturas[numero] = Factura(numero, cliente)
            print(Fore.GREEN+"Factura creada con éxito.")

        case 2:
            numero = input("\nIngrese número de factura: ")
            if numero in facturas:
                nombre = input("Nombre del producto: ")
                try:
                    cantidad = int(input("Cantidad: "))
                    precio = float(input("Precio unitario: "))
                    descuento = float(input("Descuento (%): "))
                except ValueError:
                    print(Fore.RED+"Datos numéricos inválidos.")
                    continue
               #dict    #clave                   #valor
                facturas[numero].agregar_producto(nombre, cantidad, precio, descuento)
                print(Fore.GREEN+"Producto agregado.")
            else:
                print(Fore.RED+"Factura no encontrada.")

        case 3:
            numero = input("\nIngrese número de factura para mostrar reporte: ")
            if numero in facturas:
                if facturas[numero].validar_datos():
                    facturas[numero].generar_reporte()
                else:
                    print(Fore.RED+"La factura no contiene productos válidos.")
            else:
                print(Fore.RED+"Factura no encontrada.")

        case 4:
            print(Fore.CYAN+"Saliendo del sistema de facturación...")
            break

        case _:
            print(Fore.RED+"Opción no válida.")