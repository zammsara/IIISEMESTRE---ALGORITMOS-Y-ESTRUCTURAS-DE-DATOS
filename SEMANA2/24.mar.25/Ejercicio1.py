import os
os.system('cls')

while True: 
    print("Calcular monto de importe, selecciona el tipo de vehículo")
    print("""
      1. Bicicleta
      2. Moto / Carro
      3. Camión
      """)

    opcion = int(input("Seleccione una opción: "))

    match opcion:
        case 1: 
            print("\n---------------------------------\n")
            print("El importe a pagar es de: C$100")
        case 2:
            print("\n---------------------------------\n")
            km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
            importe = km * 30

            print(f"\nEl importe a pagar es de: C${importe:.2f}")
        case 3:
            print("\n---------------------------------\n")
            km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
            toneladas = float(input("Ingrese las cantidad de toneladas: "))
            importeKM = km * 30
            importeToneladas = toneladas * 25
            total = importeKM + importeToneladas

            print(f"\nEl importe a pagar es de: C${total:.2f}")
        case _:
            print("\nOpcion inválida")

    print("\n---------------------------------\n")