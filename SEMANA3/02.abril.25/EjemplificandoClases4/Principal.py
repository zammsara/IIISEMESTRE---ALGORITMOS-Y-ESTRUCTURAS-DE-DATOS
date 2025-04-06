# Ejemplificando clases en python 

from Modulo import Alumno # Importamos la clase


alumno1 = Alumno(input("Ingresa tu nombre: "), input("Ingresa tu apellido: "), int(input("Ingresa tu edad: ")))

# Llamamos al método
alumno1.saludar()