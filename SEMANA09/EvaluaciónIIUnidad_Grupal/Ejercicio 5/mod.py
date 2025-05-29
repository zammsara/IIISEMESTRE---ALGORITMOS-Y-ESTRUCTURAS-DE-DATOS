import os

class Nodo:
    def __init__(self, valor):
        self.valor = valor    
        self.prev = None        #referencia al nodo anterior
        self.next = None        #referencia al nodo siguiente

class Valores:
    def __init__(self):
        self.cabeza = None      #primer nodo (inicio de la lista)
        self.cola = None        #último nodo (final de la lista)

    def Agregar(self, valor):
        nuevo = Nodo(valor)     

        if self.cola != None:   
            self.cola.next = nuevo     # el último nodo apunta al nuevo
            nuevo.prev = self.cola     # el nuevo apunta al anterior
            self.cola = nuevo          # el nuevo se convierte en el último
        else:                   
            self.cabeza = nuevo       
            self.cola = nuevo          

    def Buscar(self, valor):
        actual = self.cabeza     #empieza desde el inicio de la lista
        posicion = 0

        while actual != None:    
            if actual.valor == valor:   
                return posicion         #devuelve la posición
            actual = actual.next        #avanza al siguiente nodo
            posicion += 1

        return -1    #si no  se encuentra el valor, devuelve -1

    def Mostrar(self):
        actual = self.cabeza 
        if actual == None:     
            print("La lista está vacía.\n")
            return

        print("Contenido de la lista:")
        pos = 0
        while actual != None:     #mientras existan nodos
            print("[" + str(pos) + "] " + str(actual.valor)) 
            actual = actual.next   
            pos += 1
        print("")  

    def limpiarPantalla(self):
        input("Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')