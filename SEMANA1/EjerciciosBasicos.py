from datetime import date #date es una clase dentro del módulo datetime, que representa solo una fecha (sin la hora)

while True:

    print("Ejercicios básicos")
    print("""
            1. Calcular el promedio de 3 números
            2. Calcular el IVA de un producto
            3. Aumentar salario en un 25%
            4. Intercambio de valores
            5. Calcular potencia
            6. Determinar la edad de una persona
            7. Calcular el total a pagar
            8. Salir
            """)
    opcion = int(input("Selecciona una opción: "))

    match opcion:
        case 1:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            num3 = float(input("Ingresa el tercer número: "))

            promedio = (num1 + num2 + num3) /3
            print(f"El promedio es: {promedio}")
        case 2:
            precio = float(input("Ingresa el precio del producto: "))
        
            iva = precio * 0.15

            print(f"El IVA es: C${iva:.2f}")
        case 3:
            salarioActual = float(input("Ingresa tu salario actual: "))

            salarioAumentado = salarioActual *1.25

            print(f"El salario con el aumento del 25% es: ${salarioAumentado:.2f}")
        case 4:
            val1 = float(input("Ingrese el primer valor para el intercambio: "))
            val2 = float(input("Ingrese el segundo valor para el intercambio: "))

            print(f"Valor 1: {val2:.2f}")
            print(f"Valor 2: {val1:.2f}")
        case 5:
            base = int(input("Ingresa la base: "))
            exponente = int(input("Ingresa el exponente: "))

            potencia = base ** exponente

            print(f"El resultado de {base} elevado a {exponente} es: {potencia}")

        case 6:
            añoActual = date.today().year

            añoNacimiento = int(input("Ingresa tu año de nacimiento: "))

            edad = añoActual - añoNacimiento

            print(f"Edad: {edad}")

        case 7:
            subtotal = float(input("Ingresa el subtotal: "))
            impuesto = subtotal *0.10 # Calcular el impuesto (10%)
            subtotalImpuesto = subtotal + impuesto # Calcular el subtotal con el impuesto
            descuento = subtotalImpuesto * 0.05 # Calcular el descuento que se aplicará (5%)
            total = subtotalImpuesto - descuento # Calcular el total a pagar

            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Impuesto: ${impuesto:.2f}")
            print(f"Subtotal con impuesto: ${subtotalImpuesto:.2f}")
            print(f"Descuento: ${descuento:.2f}")
            print(f"TOTAL: ${total:.2f}")
        case 8:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no válida")
        
    print("\n---------------------------------\n")