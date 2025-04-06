# Esta clase tiene un método, y dos propiedades

class Alumno: # definición de la clase
    
    # Constructor
    def __init__(self, nombre, apellido,edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
    
    def saludar(self): #Método(sin atributos)
        print(f"Hola, bienvenid@ {self.nombre} {self.apellido}!")