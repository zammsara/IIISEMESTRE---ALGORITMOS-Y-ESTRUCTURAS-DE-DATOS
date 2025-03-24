print("Bienvenido a Python!")
print("""Operaciones básicas:
      1. Sumar
      2. Restar
      3. Multiplicar
      4. Dividir""")

opcion = int(input("Introduce la opción: "))

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

match opcion:
    case 1:
        suma = num1 + num2 
        print("El resultado de la suma es: ", suma)
    case 2:
        resta = num1 - num2
        print("El resultado de la resta es: ", resta)
    case 3:
        multipicacion = num1 * num2
        print("El resultado de la multipliocación es: ", multipicacion)
        