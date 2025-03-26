# Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número

import os
os.system('cls')

def es_palindromo(numero):
  
    if len(numero) != 3:
        print("El número debe tener exactamente tres cifras.")
        return
    
    # Invertimos la cadena y comparamos
    if numero == numero[::-1]:
        print(f"\nEl número {numero} es igual al revés.")
    else:
        print(f"\nEl número {numero} NO es igual al revés.")

while True: 

    print("\n-------------------------------------\n")
    numero = input("Ingrese un número de tres cifras: ")
    es_palindromo(numero)
    print("\n-------------------------------------\n")

    continuar = input("Desea continuar? (si/no)").strip().lower()
    if continuar != "si":
        print("Saliendo del sistema...")
        break