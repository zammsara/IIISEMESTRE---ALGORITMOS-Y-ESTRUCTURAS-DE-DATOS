# Este es un progrma práctico en donde se ejemplifica el uso de las listas
# Este será un sistema de gestión de una lista de compras, en donde será posible:
    # Agregar un producto a la lista
    # Marcar un producto como comprado
    # Eliminar los productos comprados de la lista
    
# Función para agregar un producto a la lista
def agregar_producto(lista, producto):
    lista.append(producto)  # Usamos append() para agregar el producto al final de la lista
    print(f"✅ Producto '{producto}' agregado a la lista de compras.")

# Función para marcar un producto como comprado
def marcar_comprado(lista, numero):
    if 1 <= numero <= len(lista):  # Verificamos si el número es válido
        lista[numero - 1] += " (Comprado)"  # Marcamos el producto como comprado
        print(f"🎉 Producto '{lista[numero - 1]}' marcado como comprado.")
    else:
        print("❌ Número de producto no válido.")

# Función para eliminar los productos comprados de la lista
def eliminar_comprados(lista):
    lista[:] = [producto for producto in lista if "(Comprado)" not in producto]  # Filtramos los productos no comprados
    print("🧹 Productos comprados eliminados de la lista.")

# Función para mostrar todos los productos en la lista
def mostrar_lista(lista):
    if not lista:  # Si la lista está vacía
        print("📭 La lista de compras está vacía.")
    else:
        print("\n🛒 Lista de compras:")
        for i, producto in enumerate(lista, start=1):
            print(f"{i}. {producto}")

# =====================================================================================================

lista_compras = []  # Inicializamos la lista vacía al principio

while True:
        
    # Mostrar menú de opciones
    print("\n--- MENÚ ---")
    print("1. Agregar producto")
    print("2. Mostrar lista de compras")
    print("3. Marcar producto como comprado")
    print("4. Eliminar productos comprados")
    print("5. Salir")

    opc = int(input("Selecciona una opción: "))

    match opc:
        
        case 1:
            producto = input("Escribe el nombre del producto: ")
            agregar_producto(lista_compras, producto)

        case 2:
            mostrar_lista(lista_compras)

        case 3:
            try:
                numero = int(input("Número del producto a marcar como comprado: "))
                marcar_comprado(lista_compras, numero)
            except ValueError:
                print("⚠️ Ingresa un número válido.")

        case 4:
            eliminar_comprados(lista_compras)

        case 5:
            print("👋 ¡Hasta pronto!")
            break

        case _:
            print("❌ Opción no válida. Intenta de nuevo.")


