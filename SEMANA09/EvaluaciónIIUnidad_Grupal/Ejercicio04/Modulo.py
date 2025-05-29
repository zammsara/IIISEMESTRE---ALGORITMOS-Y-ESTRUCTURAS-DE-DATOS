# Creamos la clase "Nodo"
class Nodo:
    def __init__(self, dato):
        self.dato = dato #contiene el objeto "Elemento"
        self.siguiente = None #señala al siguiente nodo en la cola
        
# Creamos la clase "Elmento" con sus respectivos atributos
class Elemento:
    def __init__(self, elemento, prioridad: int):
        self.elemento = elemento # Nombre del elemento
        self.prioridad = prioridad # Número entero: menor número = mayor prioridad
        
    # Método para imprimir en pantalla la info del elemento
    def __str__(self):
        return f"{self.elemento} | Prioridad: {self.prioridad}"

# Creamos la clase "Cola" y sus métodos
class Cola:
    def __init__(self):
        self.frente = None #señala al primer nodo en la cola
        self.final = None #señala al último nodo en la cola
    
    # Método para colocar/agregar un nuevo elemento a la cola
    def Colocar_Elemento(self, elemento):
        nuevo = Nodo(elemento)
        if self.final is None: #si la cola está vacía
            self.frente = self.final = nuevo #inicializamos el frente y el final de la cola(frente y final tendrán el mismo valor ya que solo existe un elemento)
        else: #si la cola NO está vacía
            self.final.siguiente = nuevo #enlazamos el nuevo nodo al final de la cola
            self.final = nuevo #actualizamos el final de la cola
    
    # Método para descolocar/eliminar un elemento según su prioridad
    def Descolocar_Elemento(self):
        if self.final is None: #si la cola está vacía
            print("No hay elementos, cola vacía.")
            return None
        
        #inicializamos punteros para recorrer la cola
        actual = self.frente
        anterior = None
        
        #guardamos el nodo con mayor prioridad(asumimos)
        nodo_mayor_prioridad = actual
        nodo_anterior_mayor_prioridad = None
        
        #reorremos la cola en búsqueda de la menor prioridad(mayor prioridad según la lógica)
        while actual is not None:
            if actual.dato.prioridad < nodo_mayor_prioridad.dato.prioridad:
                nodo_mayor_prioridad = actual #nuevo nodo de mayor prioridad (nuevo nodo a eliminar)
                nodo_anterior_mayor_prioridad = anterior #nodo anterior al que se eliminará
            #movemos los punteros al siguiente nodo
            anterior = actual
            actual = actual.siguiente
            
        # Eliminamos el nodo encontrado:
        
        # Si el nodo a eliminar está al inicio
        if nodo_anterior_mayor_prioridad is None:
            self.frente = nodo_mayor_prioridad.siguiente #se mueve el frente
            if self.frente is None:
                self.final = None #si ya no hay más elementos
        else:
            # Si el nodo está en el medio o al final
            nodo_anterior_mayor_prioridad.siguiente = nodo_mayor_prioridad.siguiente
            if nodo_mayor_prioridad == self.final:
                self.final = nodo_anterior_mayor_prioridad #actualizamos el final, si era el último nodo
                
        # Mostramos el elemento eliminado
        print(f"Elemento '{nodo_mayor_prioridad.dato.elemento}' con prioridad {nodo_mayor_prioridad.dato.prioridad} eliminado.")
        return nodo_mayor_prioridad.dato 
                
    
    # Método para mostrar los elementos actuales en la cola
    def Mostrar_Cola(self):
        if self.frente is None:
            print("La cola está vacía.")
            return
        actual = self.frente
        print("Cola actual:")
        while actual:
            print(f"- {actual.dato}")
            actual = actual.siguiente
        print("")