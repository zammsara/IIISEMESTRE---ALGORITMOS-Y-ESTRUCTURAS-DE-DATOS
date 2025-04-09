#  Se define la clase "Estudiante"
class Estudiante:
    def __init__(self, nombre: str, edad: int, carrera: str):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []  # Lista a almacenar las aclificaciones
    
    # Funciones principales: 
    
    def agregar_calificacion(self, nota: float):
        
        # See valida que la nota  está en el rango de 0 a 100
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
        else:
            print("La calificación debe estar entre 0 y 100.")
        
    def promedio(self):
        
        # Se calcula y devuelve el promedio de notas
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0.0
  
    def mostrar_info(self):
        
        # Se nuestra toda la información del estudiante
        print(f"\n📘 Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}") #con dos decimales, como se indicó
    

    
    
        
    

    
