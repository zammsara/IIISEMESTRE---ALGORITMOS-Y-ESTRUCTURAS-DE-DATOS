# Programa "Simulación de una lista de reproducción de música" desarrollado por: Alicia Estrada
# 20.mayo.2025
# Versión 1.0

# Descripción del programa/ejercicio:
"""Implemente una lista de reproducción de música utilizando una lista enlazada. El programa debe 
permitir agregar canciones, eliminar canciones, reproducir la siguiente canción, 
reproducir la canción anterior y mostrar la lista de reproducción actual. """

from mod_lista import ListaDoble
from mod_lista import Cancion
from colorama import init

import mod_menu as menu

respuesta = 0
lista = ListaDoble()

init(autoreset=True)  # Inicializa colorama para que los colores se reinicien automáticamente


while respuesta != 5:
    #menu principal
    menu.menu()
    
    #Validamos que la respuesta sea un número
    try:
        respuesta = int(input("Selecciona una opción: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        menu.pausar()
        continue
    
    match respuesta:
        # Agregar canción
        case 1:
            nombre = input("Nombre de la canción: ").upper()
            artista = input("Artista de la canción: ").upper()
            cancion = Cancion(nombre, artista) #Creamos la cancion
            lista.agregar(cancion)
            print(f"Se ha agregado la canción: {cancion}")
            menu.pausar()
            
        # Eliminar canción
        case 2:
            # Validamos que la lista no esté vacía
            if lista.tamanio == 0:
                print("No hay canciones en la lista.")
                menu.pausar()
                continue
            
            # Pedimos el nombre y artista de la canción a eliminar
            nombre = input("Nombre de la canción a eliminar: ").upper()
            artista = input("Artista de la canción a eliminar: ").upper()
            cancion = Cancion(nombre, artista)
            
            #Si la canción está en la lista (coincidiendo nombre y artista), la eliminamos
            if lista.eliminar(cancion):
                print(f"Se ha eliminado la canción: {cancion}")
                menu.pausar()
            #Si la canción no está en la lista, mostramos un mensaje
            else:
                print("La canción no se encuentra en la lista.")
                menu.pausar()
        
        # Mostrar lista de canciones
        case 3:
            print("Lista de canciones:")
            lista.mostrar_todo()
            menu.pausar()
        
        # Abrir reproductor
        case 4:
            # Validamos que la lista no esté vacía
            if lista.tamanio == 0:
                print("No hay canciones en la lista.")
                menu.pausar()
                continue
            
            # Si la lista no está vacía, comenzamos desde la cabeza
            cancion = lista.cabeza
            menu.menu_reproductor(cancion)
        
        case 5:
            # Salir de la aplicación
            print("Saliendo de la aplicación...")
            menu.pausar()
            break
        
        # Si se ingresa una opción no válida
        case _:
            print("Opción no válida. Intenta de nuevo.")
            menu.pausar()
