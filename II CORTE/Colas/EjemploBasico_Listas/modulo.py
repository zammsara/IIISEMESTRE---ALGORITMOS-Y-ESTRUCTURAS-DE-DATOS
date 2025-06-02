from colorama import Fore

class ColaLista:
    def __init__(self):
        self.cola = []

    # Agregar al final
    def insertar(self, dato):
        self.cola.append(dato)
        print(Fore.GREEN + f"'{dato}' agregado a la cola.")

    # Eliminar del frente
    def eliminar(self):
        if self.cola:
            eliminado = self.cola.pop(0)
            print(Fore.YELLOW + f"Elemento eliminado: '{eliminado}'")
        else:
            print(Fore.RED + "La cola está vacía.")

    # Ver primer elemento
    def peek(self):
        if self.cola:
            print(Fore.CYAN + f"Primer elemento: '{self.cola[0]}'")
        else:
            print(Fore.RED + "La cola está vacía.")

    # Ver último elemento
    def ver_ultimo(self):
        if self.cola:
            print(Fore.CYAN + f"Último elemento: '{self.cola[-1]}'")
        else:
            print(Fore.RED + "La cola está vacía.")

    # Mostrar todos los elementos
    def imprimir(self):
        if self.cola:
            print("\nContenido de la cola:")
            for elemento in self.cola:
                print(elemento)
        else:
            print(Fore.RED + "La cola está vacía.")

    # Verificar si la cola está vacía
    def esta_vacia(self):
        return len(self.cola) == 0
