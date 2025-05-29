#La cancion que se va a estar agregando
class Cancion:
    def __init__(self, nombre, artista):
        self.nombre = nombre
        self.artista = artista

    #Para cuando se quiera imprimir la cancion
    def __str__(self):
        return f"{self.nombre} - {self.artista}"


class Nodo: 
    def __init__(self, dato): #El dato mencionado aca, va a ser de tipo Cancion
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
    #Para cuando se quiera imprimir el nodo (La cancion)
    def __str__(self):
        return str(self.dato)
        
#Uso de una lista doblemente enlazada para movernos entre las canciones
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0

    #Agregamos una cancion a la lista
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        # Si la lista está vacía, el nuevo nodo es tanto la cabeza como la cola
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        # Si la lista no está vacía, enlazamos el nuevo nodo al final y actualizamos la cola
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamanio += 1 
    
    #Eliminamos una cancion de la lista
    def eliminar(self, dato):
        actual = self.cabeza
        while actual is not None:
            # Comparamos el dato del nodo actual con el dato que queremos eliminar
            if (actual.dato.nombre == dato.nombre and actual.dato.artista == dato.artista):
                #Si no es el primero, conecta el nodo anterior con el siguiente.
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    # Si es el primer nodo, actualizamos la cabeza
                    self.cabeza = actual.siguiente
                # Si no es el último nodo, conecta el nodo siguiente con el anterior
                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                    # Si es el último nodo, actualizamos la cola
                else:
                    self.cola = actual.anterior
                self.tamanio -= 1 #Se reduce el tamaño de la lista 
                return True
            else:
                # Si no es el nodo que queremos eliminar, seguimos buscando
                actual = actual.siguiente
        return False
    #Para mostrar todas las canciones de la lista
    def mostrar_todo(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato)
            actual = actual.siguiente
    