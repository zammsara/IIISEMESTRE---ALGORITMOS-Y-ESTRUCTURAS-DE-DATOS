"""Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua recibe documentos para
revisión. Por cada solicitud, se apilan los documentos entregados en el orden en que llegan. El
personal debe revisar el último documento entregado primero. Se debe simular el proceso de
revisión, utilizando una pila, y permitir agregar nuevos documentos, eliminar el último revisado y
mostrar los pendientes."""

class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad # Inicializa la pila con una capacidad fija 
        self.tope = -1 # Índice del último elemento agregado

    
    def push(self, elemento):  # Agrega un elemento a la cima de la pila si hay espacio
        if self.tope < self.capacidad - 1:
            self.tope += 1
            self.elementos[self.tope] = elemento
        else:
            print("Error: Pila llena. No se puede insertar.")

    def is_empty(self): # Verifica si la pila está vacía
        return self.tope == -1
    def pop(self):
        if self.is_empty():
            print("Error: Pila vacía. No se puede eliminar.")
            return None
        eliminado = self.elementos[self.tope]
        self.elementos[self.tope] = None
        self.tope -= 1
        return eliminado
    def top(self):
        """Retorna el elemento del tope sin eliminarlo."""
        if self.is_empty():
            print("La pila está vacía.")
            return None
        return self.elementos[self.tope]
    
    