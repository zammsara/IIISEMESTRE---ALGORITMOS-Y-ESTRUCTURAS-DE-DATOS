class Factura:
    def __init__(self,numero_factura, cliente):
        # Atributos encapsulados con _ para indicar que son internos
        self._numero_factura = numero_factura
        self._cliente = cliente
        self._productos = [] #Aqui se alamacenrán las tuplas con toda la info del producto
        
    def agregar_producto(self, nombre, cantidad, precio_unitario, descuento):
        # Se añade una tupla con los detalles completos del producto
        self._productos.append((nombre, cantidad, precio_unitario, descuento))
        
    def calcular_total(self):
        total = 0
        for _, cantidad, precio, descuento in self._productos:
            subtotal = cantidad * precio
            total += subtotal * (1 - descuento / 100)
        return total
    
    def generar_reporte(self):
        print(f"\n{'*' * 12} FACTURA N° {self._numero_factura} {'*' * 12}")
    
        for nombre, cantidad, precio, descuento in self._productos:
            subtotal = cantidad * precio
            descuento_aplicado = subtotal * (descuento / 100)

            print(f"\nProducto: {nombre}")
            print(f"Cantidad: {cantidad}")
            print(f"Precio unitario: ${precio:.2f}")
            print(f"Subtotal (sin descuento): ${subtotal:.2f}")
            print(f"Descuento aplicado: {descuento}% (-${descuento_aplicado:.2f})")
            print("-" * 40)
    
        print(f"TOTAL A PAGAR: ${self.calcular_total():.2f}")
        print(f"{'*' * 40}")

            
    # Método para validar que la lista de productos no esté vacía y que cada producto nombre válido, cantidad positiva y precio positivos    
    def validar_datos(self):
        if not self._productos: # Esto es equivalente a 'if len(self._productos) == 0'
            return False
        for nombre, cantidad, precio_unitario, _ in self._productos:
            if not nombre or cantidad <= 0 or precio_unitario <= 0: # si los datos son válidos retornara false, ya que las condiciones no se estarían cumpliendo
                return False 
        return True
        # todos los productos son válidos, retorna True; si no, retornará False