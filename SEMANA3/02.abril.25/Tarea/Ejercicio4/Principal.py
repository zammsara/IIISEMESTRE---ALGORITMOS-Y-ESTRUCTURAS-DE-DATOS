from colorama import init, Fore
from Producto import Producto
from Inventario import Inventario

init(autoreset=True)

def menu():

    print("\n--- Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Listar productos")
    print("6. Salir")

# Crear el inventario y agregar productos iniciales
inventario = Inventario()
inventario.agregarProducto(Producto("001", "Laptop", 1500.00, 10))
inventario.agregarProducto(Producto("002", "Mouse", 20.00, 50))
inventario.agregarProducto(Producto("003", "Teclado", 35.00, 30))

while True:
    menu()
    opcion = int(input("\nSeleccione una opción: "))

    match opcion:
        case 1:  # Agregar producto
            codigo = input("Ingrese código del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            try:
                precio = float(input("Ingrese precio del producto: C$ "))
                cantidad = int(input("Ingrese cantidad en stock: "))
                inventario.agregarProducto(Producto(codigo, nombre, precio, cantidad))
                print(Fore.GREEN+"Producto agregado correctamente.")
            except ValueError:
                print(Fore.RED+"Error: Ingrese valores numéricos para precio y cantidad.")

        case 2:  # Buscar producto
            codigo = input("Ingrese código del producto a buscar: ")
            
            inventario.buscarProducto(codigo)

        case 3:  # Actualizar producto
            codigo = input("Ingrese código del producto a actualizar: ")
            if inventario.buscarProducto(codigo):
                try:
                    nuevoPrecio = input("Ingrese nuevo precio (deje vacío si no quiere cambiarlo): C$")
                    nuevaCantidad = input("Ingrese nueva cantidad en stock (deje vacío si no quiere cambiarla): ")

                    nuevoPrecio = float(nuevoPrecio) if nuevoPrecio else None
                    nuevaCantidad = int(nuevaCantidad) if nuevaCantidad else None

                    if inventario.actualizarProducto(codigo, nuevoPrecio, nuevaCantidad):
                        print(Fore.GREEN+"Producto actualizado correctamente.")
                    else:
                        print(Fore.RED+"Error al actualizar el producto.")
                except ValueError:
                    print(Fore.RED+"Error: Ingrese valores numéricos válidos.")
            else:
                print(Fore.RED+"Producto no encontrado.")

        case 4:  # Eliminar producto
            codigo = input("Ingrese código del producto a eliminar: ")
            if inventario.eliminarProducto(codigo):
                print(Fore.GREEN+"Producto eliminado correctamente.")
            else:
                print(Fore.RED+"Producto no encontrado.")

        case 5:  # Listar productos
            print("\n📦 Inventario actual:")
            inventario.listarProductos()

        case 6:  # Salir
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        case _:  # Opción inválida
            print(Fore.RED+"Opción no válida, intente de nuevo.")
