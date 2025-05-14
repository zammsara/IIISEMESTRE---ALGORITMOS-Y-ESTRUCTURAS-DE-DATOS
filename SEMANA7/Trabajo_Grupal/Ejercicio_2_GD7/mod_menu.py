import os
from colorama import Fore, Style, init

def limpiar_consola():
    # Detecta el sistema operativo y ejecuta el comando correspondiente
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # MacOS y Linux
        os.system('clear')
        
def menu():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n=== Menú ===")  # Azul claro y brillante
    print("1. Agregar Pan Recien Horneado")
    print("2. Mostrar Ultimo Pan Agregado")
    print("3. Vender Pan")
    print("4. Mostrar Panes en Stock")
    print("5. Salir")
    print(Fore.LIGHTBLACK_EX + Style.DIM + "====================")  # Gris y tenue

def pan_agregar():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n=== Agregar Pan ===")  # Azul claro y brillante
    print("1. Pan de Chocolate")
    print("2. Pan de Ajo")
    print("3. Pan de Mantequilla")
    print("4. Pan de Pasas")
    print("5. Pan de Frutas")
    print("6. Pan de Almendras")
    print("7. Croissant")
# Inicializar colorama (necesario para Windows)
init(autoreset=True)

def pausa():
    print(Fore.LIGHTBLACK_EX + Style.DIM + "Presione Enter para continuar...")  # Gris y tenue
    input()