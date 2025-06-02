from colorama import init, Fore, Style
init(autoreset=True)


# Clase Nodo: representa cada elemento de la cola
class Nodo:
    def __init__(self, dato):
        self.dato = dato # almacena el dato del nodo
        self.siguiente = None # puntero al siguiente nodo

# Clase Cola: implementa una cola con operaciones básica
class Cola:
    def __init__(self):
        self.frente = None # referencia al primer nodo (frente de la cola)
        self.final = None # referencia al último nodo (final de la cola)
        
    # Método para insertar un elemento al final de la cola
    def Insertar(self, dato):
        nuevo = Nodo(dato) # creamos un nuevo nodo con el dato proporcionado
        if self.final is None: # si la cola está vacía:
            self.frente = self.final = nuevo # el nuevo nodo será tanto el frente como el final
        else: # si la cola no esta vacía: se agrega al final de la cola
            self.final.siguiente = nuevo # se enlaza el nuevo nodo al final de la cola
            self.final = nuevo # se actualiza el puntero final para que apunte al nuevo nodo
        
        print(Fore.YELLOW + f"\nElemento '{dato}' insertado a la cola\n")
        
    # Método para eliminar un elemento del frente de la cola
    def Eliminar(self):
        if self.frente is None:
            print(Fore.RED + "\nLa cola está vacía!!\n")
            return None
        
        datoEliminado = self.frente.dato # se guarda el dato que se va a eliminar (para imprimirlo)
        self.frente = self.frente.siguiente # se avanza al siguiente nodo
        
        if self.frente is None: # si después de eliminar, la cola queda vacía
            self.final = None # se actualiza el final también
            
        print(Fore.YELLOW + f"\nDato '{datoEliminado}' eliminado\n")
        return datoEliminado
    
    # Método para imprimir todos los elementos de la cola
    def Imprimir(self):
        if self.frente is None:
            print(Fore.RED + "\nLa cola está vacía!!\n")
        else:
            print(Style.BRIGHT + "\nContenido de la cola (de frente a final):")
            actual = self.frente
            while actual is not None:
                print(actual.dato)
                actual = actual.siguiente