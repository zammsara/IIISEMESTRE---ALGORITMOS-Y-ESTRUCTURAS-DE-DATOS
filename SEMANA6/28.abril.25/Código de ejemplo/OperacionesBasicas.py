# Ejemplificación de operaciones básicas en pila utilizando lista enlazada

class Nodo:
    def __init__(self, dato):
        self.dato = dato #dato del nodo
        self.siguiente = None #puntero al siguiente nodo

class Pila: 
    def __init__(self):
        self.tope = None # Inicia vacía
    
    # Agregar un elemento
    def push(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope #el nuevo apunta al anterior tope
        self.tope = nuevo_nodo #el nuevo ahora es el tope
        print(f"Elemento '{dato}' insertado.")
        
    # Eliminar y retornar el último elemento insertado
    def pop(self):
        if self.tope is None:
            print("Error: pila vacía. No se puede eliminar.")
            return None
        eliminado = self.tope.dato
        self.tope = self.tope.siguiente #avanza el tope al siguiente nodo
        print(f"\nElemento '{eliminado}' eliminado.")
        return eliminado
    
    # Método que devuelve el elemento tope sin eliminarlo
    def cima(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        return self.tope.dato
    
    # Método para imprimir los datos de la pila
    def imprimir(self):
        if self.tope is None:
            print("La pila está vacía.")
            return None
        else:
            print("\nContenido de la pila (de arriba hacia abajo): ")
            actual = self.tope
            while actual is not None:
                print(actual.dato)
                actual = actual.siguiente
                
# Principal    
if __name__=="__main__":
    mi_pila = Pila()
    mi_pila.push("Uno")
    mi_pila.push("Dos")
    mi_pila.push("Tres")
    
    mi_pila.imprimir()
    
    mi_pila.pop()        
    
    mi_pila.imprimir()