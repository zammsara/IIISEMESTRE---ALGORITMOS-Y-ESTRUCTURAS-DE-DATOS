# main.py
'''
Ejercicio 4 de "Pilas"
Desarrollado por: Aguilera Franco, Estrada Alicia, Duarte Andrea, Sanchez David, Zambrana Sara
Versión 1.0
07.mayo.2025

Una docente de informática en una secundaria revisa tareas impresas que sus estudiantes colocan
sobre su escritorio. Siempre revisa primero la última tarea entregada. Implementa un sistema que
permita agregar tareas (push), revisar una (pop), y mostrar cuál es la siguiente en revisar (peek),
todo usando una pila.
'''

from pila import Pila
import os

def limpiar_pantalla():
    # Espera que el usuario presione Enter y luego limpia la pantalla
    input("Presione Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("-" * 30)
    print("            MENU")
    print("-" * 30)
    print("1. Agregar tarea.")
    print("2. Revisar tarea.")
    print("3. Mostrar siguiente tarea.")
    print("4. Salir")

def main():
    entrada = Pila()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_menu()

        try:
            op = int(input("Opción: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            limpiar_pantalla()
            continue

        if op == 1:
            tarea = input("Ingrese la tarea: ")
            entrada.push(tarea)
            print("Tarea agregada.")

        elif op == 2:
            resultado = entrada.pop()
            print(resultado)

        elif op == 3:
            resultado = entrada.peek()
            print(resultado)

        elif op == 4:
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida.")
        
        limpiar_pantalla()

if __name__ == "__main__":
    main()
