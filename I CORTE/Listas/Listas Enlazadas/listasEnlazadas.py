# Este es un ejemplo básico para explicar como funcionan las listas enlazadas

# Se define la clase "Nodo" (cada elemento individual de la lista enlazada)
class Nodo:
    def __init__(self, dato): # cada nodo guarda: 
        self.dato = dato  # El valor que guarda el nodo (número, texto etc.)
        self.siguiente = None # Referencis al siguiente nodo (inicialmente None, porque aún no se ha conectado con nadie)
        
# Clase que administra los nodos, toda la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None # Este atributo apunta al primer nodo de la lista, que al principio la lista esta vacía porque no hay nodos aún
        
    # Método para agregar un nuevo nodo al final de la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None: #si la lista está vacía, 
           self.cabeza = nuevo_nodo #ese nodo se convierte en la cabeza(el primer elemento)
        else: #si hay nodos:
            actual = self.cabeza
            while actual.siguiente: #recorre la lista hasta llegar al último nodo
                actual = actual.siguiente #donde siguiente es None
            actual.siguiente = nuevo_nodo # luego conecta el último nodo con el nuevo
    
    # Método para imprimir todos los elementos de la lista
    def imprimir(self):
        actual = self.cabeza #incia desde aquí
        while actual: #mientras haya un nodo(actual no sea None):
            print(actual.dato, end=" -> ") #imprime su valor(dato)
            actual = actual.siguiente #y avanza al siguiente nodo
        print("None")  #cuando termina el recorrido, imprime None para indicar el final

mi_lista = ListaEnlazada()
mi_lista.agregar(10)
mi_lista.agregar(20)
mi_lista.agregar(30)

print("Contenido de la lista enlazada:")
mi_lista.imprimir()   



            
            