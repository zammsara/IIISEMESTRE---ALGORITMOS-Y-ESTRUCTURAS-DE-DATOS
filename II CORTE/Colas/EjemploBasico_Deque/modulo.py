from colorama import Fore

# Importamos "deque" desde "collections" para trabajar con colas de doble extremo
from collections import deque

# Definimos la clase ColaDeque
class ColaDeque:
    def __init__(self):
        # Creamos una cola vacía utilizando deque
        self.cola = deque()

    # Método para insertar un elemento al final de la cola (comportamiento normal de una cola)
    def insertar(self, dato):
        self.cola.append(dato)  # Se agrega el dato al final de la cola
        print(Fore.GREEN + f"'{dato}' agregado al final de la cola.")

    # Método para insertar un elemento al frente de la cola (no es típico de una cola normal, pero posible con deque)
    def insertar_frente(self, dato):
        self.cola.appendleft(dato)  # Se agrega el dato al inicio de la cola
        print(Fore.GREEN + f"'{dato}' agregado al frente de la cola.")

    # Método para eliminar el primer elemento (del frente) de la cola
    def eliminar_frente(self):
        if self.cola:
            eliminado = self.cola.popleft()  # Elimina y devuelve el primer elemento de la cola
            print(Fore.YELLOW + f"Elemento eliminado del frente: '{eliminado}'")
        else:
            # Si la cola está vacía, muestra un mensaje de advertencia
            print(Fore.RED + "La cola está vacía.")

    # Método para eliminar el último elemento de la cola
    def eliminar_final(self):
        if self.cola:
            eliminado = self.cola.pop()  # Elimina y devuelve el último elemento de la cola
            print(Fore.YELLOW + f"Elemento eliminado del final: '{eliminado}'")
        else:
            # Si la cola está vacía, muestra un mensaje de advertencia
            print(Fore.RED + "La cola está vacía.")

    # Método para ver el primer elemento sin eliminarlo (peek)
    def peek(self):
        if self.cola:
            print(Fore.CYAN + f"Primer elemento: '{self.cola[0]}'")  # Muestra el primer elemento de la cola
        else:
            print(Fore.RED + "La cola está vacía.")

    # Método para ver el último elemento sin eliminarlo
    def ver_ultimo(self):
        if self.cola:
            print(Fore.CYAN + f"Último elemento: '{self.cola[-1]}'")  # Muestra el último elemento de la cola
        else:
            print(Fore.RED + "La cola está vacía.")

    # Método para imprimir todos los elementos de la cola en orden
    def imprimir(self):
        if self.cola:
            print("\nContenido de la cola:")
            for elemento in self.cola:
                print(elemento)  # Imprime cada elemento de la cola
        else:
            print(Fore.RED + "La cola está vacía.")

    # Método para verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.cola) == 0  # Retorna True si la cola está vacía, False si no lo está

