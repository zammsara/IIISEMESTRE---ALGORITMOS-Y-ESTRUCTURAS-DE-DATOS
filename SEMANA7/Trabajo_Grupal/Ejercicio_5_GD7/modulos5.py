#En un mercado de Chinandega, los sacos con productos se cargan en camiones uno encima de otro. 
#Al llegar a destino, el primer saco que se descarga es el último que se cargó. Simula este proceso 
#con una pila que permita apilar sacos (push), descargar uno (pop) y visualizar el que está encima 
#(peek).

class Pila:
    
    # Constructor de la clase: se ejecuta al crear un objeto de tipo Pila
    def __init__(self):
        self.sacos = []  # Inicializa una lista vacía que almacenará los elementos de la pila

    # Método para agregar un elemento al tope de la pila
    def push(self, productos):
        self.sacos.append(productos)  # Usa append para insertar el valor al final (tope) de la lista

    # Método para eliminar y retornar el elemento del tope de la pila
    def pop(self):
        if not self.esta_vacia():  # Verifica si la pila NO está vacía
            return self.sacos.pop()  # Elimina y retorna el último elemento de la lista
        else:
            return None  # Si la pila está vacía, retorna None
        
    def ultimo(self):
        if not self.esta_vacia():
              cima = self.sacos[-1] # se imprime solo el ultimo valor de la pila (el ultimo saco)
              print(" El ultimo saco apilado es de: ", cima)
        else:
            return None
    def esta_vacia(self): # verifica si la lista esta vacia
        return len(self.sacos) == 0
        
