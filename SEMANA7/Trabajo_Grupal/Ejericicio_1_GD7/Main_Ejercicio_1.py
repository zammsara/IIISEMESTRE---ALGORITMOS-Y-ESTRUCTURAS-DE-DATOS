
import os 
from Modulos_Ejercicio_1 import Pila 

# Crear una instancia de la clase Pila con capacidad 100
pila = Pila(100)

def revisar_ultimo():
    doc = pila.top()
    if doc is None:
        return
    print(f"Documento a revisar (tope): {doc}")
    confirmar = input("¿Revisar y eliminar este documento? (s/n): ")
    if confirmar.lower() == 's':
        revisado = pila.pop()
        print(f"Documento '{revisado}' revisado y removido.")
    else:
        print("Operación cancelada.")
        
def agregar_Documento():
    #Agrega un nuevo documento a la pila.
    documento = input("Ingrese el nombre del documento: ")
    pila.push(documento)
    print(f"Documento '{documento}' agregado a la pila.")
    return
def mostrar_Documentos():
    #Muestra los documentos pendientes en la pila.
    if not pila.is_empty():
        print("Documentos pendientes:")
        for i in range(pila.tope, -1, -1):
            print(f"Documento {i + 1}: {pila.elementos[i]}")
    else:
        print("No hay documentos pendientes.")
        return
def limpiarPila():
    #Limpia la pila de documentos.
    pila.clear()
    print("Pila de documentos limpiada.")
    return
    



# Agregar algunos documentos a la pila
def limpiarPantalla():
    """Limpia la pantalla de la consola."""
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    

def main(): 
    #Menu 
    while True:
        
        print("======       Ejercicio 1       ======")
        print("=== Oficina de Atención Ciudadana ===")
        print("1. Agregar documento")
        print("2. Revisar documentos")
        print("3. Limpiar pila")
        print("4. Mostrar documentos pendientes")
        print("5. Salir")  
        try:
            opc = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.\n")
            continue
        
        match opc:
            case 1:
                agregar_Documento()
                limpiarPantalla()
            case 2:
                revisar_ultimo()
                limpiarPantalla()
            case 3:
                limpiarPila()
                limpiarPantalla() 
                
            case 4:
                mostrar_Documentos()    
                limpiarPantalla()
                
            case 5:
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                continue
   
if __name__ == "__main__":
    main()
    
    
    
    
    
    