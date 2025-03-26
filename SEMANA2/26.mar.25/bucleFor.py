# Con el bucle for, imprimir solo los numeros pares del 2 al 100, y luego sumar cada número
suma = 0

for i in range(2,101,2):
    print (i, end= "")
    suma += i
    print(suma)