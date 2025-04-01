# Ejemplificando funciones en Python

import os
os.system('cls')

# Definición de la función sumar 
def sumar(a, b): 
    return a + b

# Definicion de la función saludo
def saludo():
    print("\nBienvenido al programa!\n")

saludo() # Llamada de la función saludo
print("Ejemplificando funciones")

num1 = int(input("\nIngrese un número: "))
num2 = int(input("Ingrese un número: "))

resp = sumar(num1, num2)
print("La suma de ambos número es: ", resp) # Llamada de la función sumar