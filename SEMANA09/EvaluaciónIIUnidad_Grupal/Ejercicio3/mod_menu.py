import os
from colorama import Fore, Style, init

# PARA LIMPIAR LA CONSOLA
def limpiar_consola():
    # Detecta el sistema operativo y ejecuta el comando correspondiente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS y Linux
        os.system('clear')

# MENU PRINCIPAL
def menu():
    limpiar_consola()
    print(Fore.CYAN + Style.BRIGHT + "Bienvenido a la aplicación de música" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + "1. Agregar canción")
    print(Fore.YELLOW + Style.BRIGHT + "2. Eliminar canción")
    print(Fore.YELLOW + Style.BRIGHT + "3. Mostrar lista de canciones")
    print(Fore.YELLOW + Style.BRIGHT + "4. Abrir Reproductor")
    print(Fore.YELLOW + Style.BRIGHT + "5. Salir" + Style.RESET_ALL)
    
# MENU REPRODUCTOR DE MÚSICA
def menu_reproductor(cancion):
    actual = cancion
    resp_rep = 0
    while resp_rep != 3:
        limpiar_consola()
        print(Fore.MAGENTA + Style.BRIGHT + "="*40)
        print(Fore.CYAN + Style.BRIGHT + "      🎵  REPRODUCTOR DE MÚSICA  🎵")
        print(Fore.MAGENTA + Style.BRIGHT + "="*40 + Style.RESET_ALL)
        #Parte importante: Mostramos la canción actual
        print(Fore.YELLOW + Style.BRIGHT + f"\n▶  Reproduciendo: {actual}\n" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + "Opciones:")
        print(Fore.GREEN + "  1.← Rep.Ant\t\t2. Rep. Sig. →")
        print(Fore.GREEN + "  3. ↩ Volver a Menu")
        print(Fore.MAGENTA + Style.BRIGHT + "="*40 + Style.RESET_ALL)

        #Validamos la opción ingresada
        try:
            resp_rep = int(input(Fore.YELLOW + Style.BRIGHT + "Selecciona una opción: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Opción no válida. Intenta de nuevo." + Style.RESET_ALL)
            pausar()
            continue
        
        match resp_rep:
            
            #Retroceder a la canción anterior
            case 1:
                #Si hay una canción anterior, la asignamos a "actual"
                if actual.anterior:
                    actual = actual.anterior
                else:
                    print("No hay canción anterior.")
                    pausar()
            
            #Avanzar a la canción siguiente
            case 2:
                #Si hay una canción siguiente, la asignamos a "actual"
                if actual.siguiente:
                    actual = actual.siguiente
                else:
                    print("No hay canción siguiente.")
                    pausar()
            
            #Volver al menú principal 
            case 3:
                print(Fore.YELLOW + Style.BRIGHT + "Volviendo al menú principal..." + Style.RESET_ALL)
                pausar()
                break # Solo rompemos el bucle del reproductor para volver 
            
            #Si se ingresa una opción no válida
            case _:
                print(Fore.RED + Style.BRIGHT + "Opción no válida. Intenta de nuevo." + Style.RESET_ALL)
                pausar()
                
#Para pausar la consola...          
def pausar():
    input(Fore.GREEN + Style.BRIGHT + "Presiona Enter para continuar..." + Style.RESET_ALL)
    
