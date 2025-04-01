import Modulos # Importamos el archivo donde se encuentran nuestras funciones
               # Recuerda que también podemos importanlor con un alias con "impor Modulos as mo"
# Con "from Modulos import nombre-de-la-función-especifíca", podemos importar una función especifíca 

import os
os.system('cls')

while True:
    print(Modulos.texto)
    print("""
      1. Sumar
      2. Restar
      3. Dividir
      4. Multiplicar
      5. Salir""")

    opc = int(input("\nSeleccione una opción: "))

    match opc:
        case 1:
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
        
            resp = Modulos.sumar(num1, num2)
        
            print("La suma es: ", resp)
    
        case 2: 
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
        
            resp = Modulos.restar(num1, num2)
        
            print("La resta es: ", resp)
        
        case 3:
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
        
            resp = Modulos.dividir(num1, num2)
        
            print("La división es: ", resp)
        
        case 4: 
            num1 = int(input("Ingrese un número: "))
            num2 = int(input("Ingrese un número: "))
        
            resp = Modulos.multiplicar(num1, num2)
        
            print("La multiplicación es: ", resp)
        
        case 5: 
            print("Saliendo del programa...")
            break
        
        case _:
            print("Opción inválida")
