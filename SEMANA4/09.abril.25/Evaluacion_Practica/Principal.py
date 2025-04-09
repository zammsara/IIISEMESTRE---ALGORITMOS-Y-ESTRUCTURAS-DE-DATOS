# Programa "Gestión de Estudiantes" desarrollado por: Sara Alejandra Zambrana Taylor / CIF: 24010958
    # Versión 1
    # 09.abril.2025

# Se importa la clases y las funciones auxiliares
from estudiante import Estudiante
from auxiliares import mostrar_menu, validar_edad, buscar_estudiante

from colorama import init, Fore
init(autoreset=True)

# Se inicializa la lista almacenará los estudiantes
estudiantes = []

while True: 
    mostrar_menu()
    try:
        opc = int(input("Seleccione una opción: "))
    except ValueError:
        print(Fore.RED+"Ingrese un número válido.")
        continue
    
    match opc:
        case 1:
            
            # Registrar nuevo estudiante
            nombre = input("\nIngrese el nombre: ")
            edad_valida = None
            while edad_valida is None:
                edad_valida = validar_edad(input("Ingrese la edad: "))
            carrera = input("Ingrese la carrera: ")

            nuevo = Estudiante(nombre, edad_valida, carrera)
            estudiantes.append(nuevo) #se agrega al estudiante al final de la lista
            print(Fore.GREEN+f"Estudiante {nuevo.nombre} registrado con éxito.")
        
        case 2: 
            
            # Agregar calificación
            nombre = input("\nIngrese el nombre del estudiante: ")
            estudiante = buscar_estudiante(nombre, estudiantes) #se busca al estudiante en la lista
            if estudiante:
                try:
                    nota = float(input("Ingrese la calificación (0-100): "))
                    estudiante.agregar_calificacion(nota)
                except ValueError:
                    print(Fore.RED+"Ingrese un número válido.")
            else:
                print(Fore.RED+"Estudiante no encontrado.")
        
        case 3:
            
            # Mostrar la info de un estudiante
            nombre = input("\nIngrese el nombre del estudiante: ")
            estudiante = buscar_estudiante(nombre, estudiantes) #se busca al estudiante enla lista
            if estudiante:
                estudiante.mostrar_info()
            else:
                print(Fore.RED+"Estudiante no encontrado.")
                
        case 4:
            
            # Mostrar todos los estudiantes
            if estudiantes:
                print("\n📚 Lista de estudiantes:")
                for est in estudiantes:
                    est.mostrar_info()
            else:
                print(Fore.RED+"No hay estudiantes registrados.")
        
        case 5:
            print(Fore.CYAN+"Hasta pronto!")
            break
        
        case _:
            print(Fore.RED+"Opción no válida. Intenta de nuevo")

            

