import Cliente

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = [] # lista de productos
                            # cada producto es una tupal (nombre, precio)
    
    def agregar_producto(self, nombre, precio):
        self.productos.append((nombre, precio))
        # se agregan los productos al final de la lista de productos
        
    def calcular_total(self):
        total = sum(precio for _, precio in self.productos)
        total *= (1 - self.cliente.get_descuento() / 100)
        return total
    
    def __str__(self):
        productosCadena = "\n".join(f"{nombre}: ${precio}" for nombre, precio in self.productos)
        return(f"Cliente: {self.cliente}\nProductos:\n{productosCadena}\n"
               f"Total con descuento: ${self.calcular_total():.2f}")