# Funciones auxiliares: 

def mostrar_menu():
    print('=' * 40)
    print("📋 Menú de opciones:")
    print('=' * 40)
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")
    print('=' * 40)
        
def validar_edad(valor):
        
    # Se verifica que la edad sea un entero positivo
    try:
        edad = int(valor)
        if edad > 0:
            return edad
        else:
            print("La edad debe ser un número positivo.")
    except ValueError:
        print("Ingrese un número válido.")
        return None
        
def buscar_estudiante(nombre, lista_estudiantes):
        
    #Busca un estudiante por nombre en la lista
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None