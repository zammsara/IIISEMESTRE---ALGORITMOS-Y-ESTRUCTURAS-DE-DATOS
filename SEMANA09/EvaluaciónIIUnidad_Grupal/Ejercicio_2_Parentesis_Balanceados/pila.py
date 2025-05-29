# pila.py
class Pila:
    """Clase para representar una estructura tipo pila (stack)."""

    def __init__(self):
        """Inicializa una pila vacía."""
        self.items = []

    def push(self, item):
        """Agrega un elemento al tope de la pila."""
        self.items.append(item)

    def pop(self):
        """
        Remueve y retorna el elemento del tope de la pila.
        Retorna None si la pila está vacía.
        """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """
        Retorna el elemento en el tope de la pila sin removerlo.
        Retorna None si la pila está vacía.
        """
        if not self.is_empty():
            return self.items[-1] # Como retorna el ultimo elemento de la lista, no es necesario usar el método pop()
        return None

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def size(self):
        """Retorna el tamaño actual de la pila."""
        return len(self.items)
