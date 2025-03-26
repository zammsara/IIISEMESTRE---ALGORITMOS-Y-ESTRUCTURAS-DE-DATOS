import math

def calcular_area():
    while True:
        print("\n======================================")
        print(" CÁLCULO DE SUPERFICIES (versión 1.0)")
        print("======================================")
        print("1. Cuadrado       lado * lado")
        print("2. Círculo        pi * radio * radio")
        print("3. Rectángulo     base * altura")
        print("4. Trapecio       (base1 + base2) * altura / 2")
        print("5. Triángulo      (base * altura) / 2")
        print("0. Salir")
        
        opcion = int(input("\nSeleccione una opción (0-5): "))
        
        match opcion:

            case 0:
                print("\nSaliendo del programa. ¡Hasta luego!\n")
                break
        
            case 1:
                print("\n======================================")
                lado = float(input("Ingrese el lado del cuadrado: "))
                area = lado * lado
                print(f"\nEl área del cuadrado es: {area}")
        
            case 2:
                print("\n======================================")
                radio = float(input("Ingrese el radio del círculo: "))
                area = math.pi * radio * radio
                print(f"\nEl área del círculo es: {area:.2f}")
        
            case 3:
                print("\n======================================")
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                area = base * altura
                print(f"\nEl área del rectángulo es: {area}")
        
            case 4:
                print("\n======================================")
                base1 = float(input("Ingrese la base menor del trapecio: "))
                base2 = float(input("Ingrese la base mayor del trapecio: "))
                altura = float(input("Ingrese la altura del trapecio: "))
                area = (base1 + base2) * altura / 2
                print(f"\nEl área del trapecio es: {area}")
        
            case 5:
                print("\n======================================")
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area = (base * altura) / 2
                print(f"\nEl área del triángulo es: {area}")
        
            case _:
                print("\nOpción no válida. Por favor, seleccione una opción entre 0 y 5.")


calcular_area()