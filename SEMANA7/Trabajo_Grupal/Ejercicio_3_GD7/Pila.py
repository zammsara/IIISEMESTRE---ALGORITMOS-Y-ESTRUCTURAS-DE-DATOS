from colorama import Fore, Style

# Clase Nodo representa a cada donante en la pila
class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.previo = None

# Esta clase gestiona el registro de donantes usando una estructura tipo pila
class PilaDonantes:
    def __init__(self):
        self.tope = None #nodo en la cima de la pila (último donante registrado)

    def push(self, datos):
        nuevo_donante = Nodo(datos)
        nuevo_donante.previo = self.tope
        self.tope = nuevo_donante#se crea un nuevo nodo con los datos del donante
        print(Fore.GREEN + f"\nDonante registrado: {datos}")

    def pop(self):
        if self.tope:
            print(Fore.RED + f"\nEliminando último registro: {self.tope.datos}")
            self.tope = self.tope.previo
        else:
            print(Fore.YELLOW + "\nNo hay registros para eliminar.")

    def mostrar_actual(self):
        if self.tope:
            print(Fore.CYAN + f"\nDonante actual en proceso: {self.tope.datos}")
        else:
            print(Fore.YELLOW + "\nNo hay donantes en proceso.")

    def mostrar_historial(self):
        actual = self.tope
        if not actual:
            print(Fore.YELLOW + "\nNo hay historial.")
            return
        print(Style.BRIGHT + "\n--- Historial de Donantes ---")
        while actual:
            print(actual.datos)
            actual = actual.previo
        print("-----------------------------")
