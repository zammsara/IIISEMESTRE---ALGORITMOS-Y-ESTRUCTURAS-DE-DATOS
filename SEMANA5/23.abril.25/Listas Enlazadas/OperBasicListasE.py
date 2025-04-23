# Programa de "Ejemplificando la creación de una lista enlazada simple"
# Desarrollado por: Sara Zambrana y Alicia Estrada :)
# Versión 1.1
# 23.abril.2025
from colorama import init, Fore
init(autoreset=True)


# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    #Insertar un nuevo valor al principio de la lista
    def insertar_al_principio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
    
    # Método que cuenta el número de nodos en la lista
    def longitudLista(self):
        contador = 0  # Inicializa el contador en 0
        actual = self.cabeza  # Empieza desde la cabeza de la lista
        while actual:  # Recorre la lista mientras haya nodos
            contador += 1  # Incrementa el contador por cada nodo
            actual = actual.siguiente  # Avanza al siguiente nodo
        return contador  # Retorna el número total de nodos
        
    # Método para determinar si la lista está vacía
    def esta_vacia(self):
        return self.cabeza is None  # Retorna True si la cabeza es None, False en caso contrario
    
    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.esta_vacia():  # Verifica si la lista está vacía usando el método esta_vacia
            self.cabeza = nuevo  # Si está vacía, el nuevo nodo se convierte en la cabeza
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar cierto elemento de la lista
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado
    # Eliminar el primer nodo de la lista (la cabeza)
    def eliminar_primero(self):
        if not self.esta_vacia():
            eliminado = self.cabeza.valor
            self.cabeza = self.cabeza.siguiente
            return eliminado
        return None

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    #Metodo para imprimir la lista
    def imprimir(self):
        if self.esta_vacia():  # Usar el método para verificar si la lista está vacía
            print(Fore.YELLOW+"\nLa lista está vacía.\n")
            return
        actual = self.cabeza
        print("\nLista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
        
    # Método para imprimir el ultimo valor de la lista   
    def imprimir_ultimo(self):
        if self.esta_vacia():  # Usar el método para verificar si la lista está vacía
            print(Fore.YELLOW+"\nLa lista está vacía.\n")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print(Fore.BLUE+f"\nEl último valor de la lista es: {actual.valor}")