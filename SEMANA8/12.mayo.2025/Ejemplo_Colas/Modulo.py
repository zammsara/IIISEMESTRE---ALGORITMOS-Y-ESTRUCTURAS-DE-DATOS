from colorama import Fore, Style, init
init(autoreset=True)

# Definimos la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definimos la clase cola y sus métodos: Insertar, 
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        
    # Método para insertar elementos a la cola
    def Insertar(self, dato):
        nuevo = Nodo(dato) #creamos un nuevo Nodo
        if self.final is None: #en caso que la cola este vacía (significa que se está insertando el primer nodo)
            self.frente = self.final = nuevo #tanto como frente y final, tendrán el valor de nuevo(el nuevo nodo)
        else:#en caso que la lista no este vacía, agregamos un nuevo elemento a la cola al final de esta
            self.final.siguiente = nuevo#se redirecciona final, para que este almacene el valor del nuevo nodo
            self.final = nuevo
            print(Fore.YELLOW+f"\nElemento '{nuevo}' insertado a la cola")
            
    def Eliminar(self):
        if self.frente is None:
            print(Fore.RED+"\nLa cola está vacía!!")
            return None

        datoEliminado = self.frente.dato
        self.frente = self.frente.siguiente
        
        if self.frente is None:#si la cola queda vacía
            self.final = None
            print(Fore.YELLOW+f"\nDato '{datoEliminado}' eliminado")
            return datoEliminado
        
    # Método para imprimir todos los datos de la cola
    def Imprimir(self):
        if self.frente is None:#si la pila está vacía
            print(Fore.RED+"\nLa cola está vacía!!")
        else:
            print(Style.BRIGHT+"\nContenido de la cola desde el frente hasta el final:")
            actual = self.frente
            while actual is not None:
                print(actual.dato)
                actual = actual.siguiente