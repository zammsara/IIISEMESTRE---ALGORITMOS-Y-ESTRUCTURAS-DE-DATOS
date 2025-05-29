# Ejercicio #5: Búsqueda en una lista enlazada. Cree una función que busque un
# valor específico en una lista enlazada. La función debe devolver la posición del valor
# si se encuentra, o un mensaje indicando que el valor no está en la lista.

from mod import Valores

def main():
    valores = Valores()  

    while True:
        print("-"*30, "MENU", "-"*30)
        print("1. Agregar valor.")
        print("2. Buscar valor.")
        print("3. Mostrar lista.")
        print("4. Salir.")

        try:
            op = int(input("Seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.\n")
            continue

        match op:
            case 1:
                valor = input("Ingrese un valor para agregar: ")
                valores.Agregar(valor)  #se pasa valor como argumento para agregarlo a la lista
                print("Valor agregado.\n")
                valores.limpiarPantalla()  

            case 2:
                valor = input("Ingrese el valor a buscar: ")
                posicion = valores.Buscar(valor)

                if posicion != -1:
                    print("Valor '" + valor + "' encontrado en la posición " + str(posicion) + ".\n")
                else:
                    print("Valor '" + valor + "' no está en la lista.\n")
                
                valores.limpiarPantalla()  

            case 3:
                valores.Mostrar()  #se imprime la lista completa
                valores.limpiarPantalla()  

            case 4:
                print("Saliendo...")
                break


if __name__ == "__main__":
    main()
