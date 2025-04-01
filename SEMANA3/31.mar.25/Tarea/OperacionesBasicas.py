from operaciones import suma, resta, multiplicacion, division # Importamos los módulos
from operaciones.suma import suma # Importo solo la función especifíca
from colorama import init, Fore
init(autoreset=True) # Restablece los colores automáticamente, para que no todo el texto se convierta en el color que estemos utilizando

import os
os.system('cls')


while True: 
    print("\n======================================================")
    print("\t\tOperaciones Básicas")
    print("======================================================")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")
    print("======================================================")
    opc = int(input("Seleccione una opción: "))
    
    match opc:
        case 1:
            print("======================================================")
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
            
            print("\nEl resultado de la suma es: ", suma(num1,num2))
        case 2: 
            print("======================================================")
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
             
            print("\nEl resultado de la resta es: ", resta.resta(num1, num2))
        case 3: 
            print("======================================================")
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
             
            print("\nEl resulado de la multiplicación es: ", multiplicacion.multiplicacion(num1, num2))
        case 4: 
            print("======================================================")
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
             
            print("\nEl resultado de la división es: ", division.division(num1, num2))
        case 5: 
            print(Fore.RED+"Saliendo del programa...")
            break
        case _:
            print(Fore.RED+"Opción inválida. Ingresa una opción válida")
            



