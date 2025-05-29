class Pila:
    
    # Constructor de la clase: se ejecuta al crear un objeto de tipo Pila
    def __init__(self):
        self.frases = []  # Inicializa una lista vacía que almacenará los elementos de la pila

    # Método para agregar un elemento al tope de la pila
    def push(self, frase):
        self.frases.append(frase)  # Usa append para insertar el valor al final (tope) de la lista

    # Método para eliminar y retornar el elemento del tope de la pila
    def pop(self):
        if not self.esta_vacia():  # Verifica si la pila NO está vacía
            return self.frases.pop()  # Elimina y retorna el último elemento de la lista
        else:
            return None  # Si la pila está vacía, retorna None
        
    def ultimo(self):
        if not self.esta_vacia():
              cima = self.frases[-1] # se imprime solo el ultimo valor de la pila (el ultimo saco)
              print(" La última frase es:  ", cima)
        else:
            return None
    def esta_vacia(self): # verifica si la lista esta vacia
        return len(self.frases) == 0
        
