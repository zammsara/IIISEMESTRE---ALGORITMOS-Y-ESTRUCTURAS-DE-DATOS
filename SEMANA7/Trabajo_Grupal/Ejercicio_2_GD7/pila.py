class Nodo:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio
        self.siguiente = None

class Pila: 
    def __init__(self):
        self.tope = None # Inicia vacía
    
    # Agregar un elemento
    def push(self, tipo, precio):
        nuevo_nodo = Nodo(tipo, precio) 
        nuevo_nodo.siguiente = self.tope #el nuevo apunta al anterior tope
        self.tope = nuevo_nodo #el nuevo ahora es el tope
        
    # Eliminar y retornar el último elemento insertado
    def pop(self):
        if self.tope is None:
            print("Pila vacía. No se puede eliminar.")
            return None
        eliminado = self.tope.tipo
        eliminado_precio = self.tope.precio
        self.tope = self.tope.siguiente #avanza el tope al siguiente nodo
        return eliminado
    
    # Retornar el último elemento sin eliminarlo
    def peek(self):
        if self.tope is None:
            print("Pila vacía. No se puede mostrar el elemento.")
            return None
        return self.tope.tipo, self.tope.precio
    
    ## Imprimir todos los elementos de la pila
    def imprimir(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        else:
            actual = self.tope  # Empieza desde el nodo superior
            while actual is not None:  # Recorre todos los nodos
                print(f"- Tipo: {actual.tipo}, Precio(c$): {actual.precio}")  # Imprime el tipo y precio del pan
                actual = actual.siguiente  # Avanza al siguiente nodo