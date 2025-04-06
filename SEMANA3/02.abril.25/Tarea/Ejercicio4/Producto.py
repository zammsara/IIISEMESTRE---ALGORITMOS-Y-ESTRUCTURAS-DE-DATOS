class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        

    def actualizarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio

    def actualizarStock(self, nuevaCantidad):
        self.cantidad = nuevaCantidad

    def imprimir(self):
        return f"Producto({self.codigo}, {self.nombre}, Precio: {self.precio}, Stock: {self.cantidad})"
