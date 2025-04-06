from Cliente import Cliente, ClienteRegular, ClienteVIP
from Pedido import Pedido
from colorama import init, Fore

init(autoreset=True)

# Se inicializan los diccionarios vacíos
clientes = {}
pedidos = {}

while True:
    print("========================================")
    print("\t\tMenú:")
    print("========================================")
    print("1. Registrar nuevo cliente")
    print("2. Agregar producto a un pedido")
    print("3. Mostrar información de un pedido")
    print("4. Salir")
    print("========================================")
    opc = int(input("Seleccione una opción: "))
    
    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ingrese un número válido.")
        continue

    
    match opc:
        case 1:
            print("\n========================================")
            id_cliente = input("\nIngrese el ID del cliente: ")
            nombre = input("Ingrese el nombre: ")
            contacto = input("Ingrese el contacto: ")
            print("\nTipos de cliente:")
            print("1. Cliente normal (sin descuento)")
            print("2. Cliente Regular (10% de descuento)")
            print("3. Cliente VIP (15% de descuento)")
            tipo = int(input("\nSeleccione el tipo de cliente: "))
            
            match tipo:
                case 1:
                    cliente = Cliente(id_cliente, nombre, contacto)
                case 2: 
                    cliente = ClienteRegular(id_cliente, nombre, contacto)
                case 3:
                    cliente = ClienteVIP(id_cliente, nombre, contacto)
                case _:
                    print(Fore.RED+"Tipo de cliente no válido. Se creará como Cliente normal.")
                    cliente = Cliente(id_cliente, nombre, contacto)
             
           #dict    #clave        #valor
            clientes[id_cliente] = cliente
           #se crea un nuevo objeto "Pedido", pasandole como argumento "cliente", para guardarse en el diccionario "pedidos" utilizando "id_cliente" como clave
            pedidos[id_cliente] = Pedido(cliente) 
            print(Fore.GREEN+"Cliente registrado:")
            print(cliente)
            
        case 2:
            id_cliente = input("\nIngrese el ID del cliente para agregar productos: ")
            if id_cliente in pedidos:
                pedido = pedidos[id_cliente]
                nombreProducto = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                pedido.agregar_producto(nombreProducto, precio)
                print(Fore.GREEN+"Producto agregado.")
            else:
                print(Fore.RED+"Cliente no encontrado.")
        
        case 3:
            id_cliente = input("\nIngrese el ID del cliente para mostrar su pedido: ")
            if id_cliente in pedidos:
                print(pedidos[id_cliente])
            else:
                print(Fore.RED+"Cliente no encontrado...")
        
        case 4:
            print(Fore.CYAN+"Saliendo del programa...")
            
        case _:
            print(Fore.RED+"Opción no válida. Intente de nuevo.")
    