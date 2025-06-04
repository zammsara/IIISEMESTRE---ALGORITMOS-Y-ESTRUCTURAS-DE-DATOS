# Clase que representa un nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor # valor almacenado en el nodo
        self.derecha = None # referencia al hijo derecho
        self.izquierda = None # referencia al hijo izquierdo
 
# Clase que representa al árbol binario de búsqueda       
class ArbolBin:
    def __init__(self):
        self.raiz = None # inicialmente el árbol está  vacío
    
    # Método paea insertar un valor en el árbol    
    def insertar(self, valor):
        self.raiz = self.insertarecursiva(self.raiz, valor)
     
    # Inserta un valor de forma recursiva en la posición correcta   
    def insertarecursiva(self, node, valor):
        if node is None:
            return Nodo(valor) # se crea un nuevo nodo si se llega a una posición vacía
        
        if valor < node.valor: # si es menor a la raíz
            node.izquierda = self.insertarecursiva(node.izquierda, valor) # se inserta en subárbol izquierda
        else: # si es mayor a la raíz
            node.derecha = self.insertarecursiva(node.derecha, valor) # se inserta en subárbol derecho
            
        return node # retorna el nodo actual
    
    # Método para buscar un valor en el árbol
    def buscar(self, valor):
        return self.buscarecursiva(self.raiz, valor)
   
   # Busca un valor de forma recursiva 
    def buscarecursiva(self, node, valor):
        if node is None: # si se llegó a una hoja sin encontrar el valor
            return False # regresará False
        
        if node.valor == valor: # si el valor del nodo actual coincide con el valor que se busca
            return True # regrasará verdadero
        
        if valor < node.valor: # si el valor es menor a la raíz
            return self.buscarecursiva(node.izquierda, valor) # busca en el subárbol izquierdo
        
        else: # si el valor es mayor a la raíz
            return self.buscarecursiva(node.derecha, valor)  # busca en el subárbol izquierdo
        
    # Método para recorrer el árbol en pre-orden (raíz, izquierda, derecha)
    def recorridopreorden(self, node):
        if node is not None:
            print(node.valor, end=" ")
            self.recorridopreorden(node.izquierda)
            self.recorridopreorden(node.derecha)
     
    # Método para recorrer el árbol en in-orden (izquierda, raíz, derecha)       
    def recorridoinorden(self, node):
        if node is not None:
            self.recorridoinorden(node.izquierda)
            print(node.valor, end=" ")
            self.recorridoinorden(node.derecha)  
   
   # Método para recorrer el árbol en post-orden (izquierda, derecha, raíz)         
    def recorridopostorden(self, node):
        if node is not None:
            self.recorridopostorden(node.izquierda)
            self.recorridopostorden(node.derecha)
            print(node.valor, end=" ")
            
