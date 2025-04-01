# Función que permita obtener el producto de 2

import os
os.system('cls')

def producto(a, b):
    return a * b

# Multiplicar 2
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))

resp = producto(num1, num2)
print(num1, " * ", num2, " = ", resp)

# Obtener la tabla de multiplicar de un número
num = int(input("\nIngresar un número: \n"))

for i in range(1,13):
    r = producto(num, i)
    print(num, " * ", i, " = ", r)