from Producto import Producto  # Importamos la clase Producto
from colorama import init, Fore

init(autoreset=True)

class Inventario:
    def __init__(self):
        # Se inicializa un diccionario para almacenar los productos
        self.productos = {} # DICCIONARIO (CLAVE, VALOR)


                            #parametro  #debe de pertenecer a la clase Producto
    def agregarProducto(self, producto: Producto):
        
       #diccionario   #clave             #valor, objeto completo
        self.productos[producto.codigo] = producto


    # Función para buscar un producto en el inventario por su código
    def buscarProducto(self, codigo):
    
        producto = self.productos.get(codigo)  # Obtener el producto si existe
    
        if producto:  # Si el producto se encuentra en el diccionario
            print(Fore.GREEN+f"\nProducto encontrado:")
            print(f"Nombre: {producto.nombre}")
            print(f"Precio: {producto.precio}")
            print(f"Cantidad en stock: {producto.cantidad}")
        else:
            print(Fore.RED+"\nProducto no encontrado en el inventario.")



    def actualizarProducto(self, codigo, nuevoPrecio=None, nuevaCantidad=None):
        
        producto = self.buscarProducto(codigo)
        if producto:
            if nuevoPrecio is not None:
                Producto.actualizarPrecio(nuevoPrecio)  
            if nuevaCantidad is not None:
                Producto.actualizarStock(nuevaCantidad) 
            return True
        return False
    
    def eliminarProducto(self, codigo):
        
        if codigo in self.productos:
            del self.productos[codigo]
            return True # True si se eliminó
        return False # False si no existía
    
    
    def listarProductos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\nLista de productos en el inventario:")
            for producto in self.productos.values():
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: C${producto.precio}, Stock: {producto.cantidad}")

    

