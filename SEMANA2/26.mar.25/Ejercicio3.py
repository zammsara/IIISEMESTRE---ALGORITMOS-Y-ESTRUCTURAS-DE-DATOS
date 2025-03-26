# Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
# ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. 
# Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. 
# Diseñe un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y el número 
# de unidades de obsequio por la compra de cierta cantidad de docenas del producto.

import os
os.system('cls')

def calcular_compra(docenas, precio_por_docena):
    
    monto_compra = docenas * precio_por_docena # Calcular el monto de la compra sin descuento
    
    # Determinar el descuento
    if docenas > 3:
        descuento = 0.15  # 15%
    else:
        descuento = 0.10  # 10%
    
    monto_descuento = monto_compra * descuento
    monto_a_pagar = monto_compra - monto_descuento
    
    # Calcular unidades de obsequio
    if docenas > 3:
        unidades_obsequio = (docenas - 3) * 1  # 1 unidad por cada docena extra sobre 3
    else:
        unidades_obsequio = 0
    
    # Mostrar resultados
    print("\n---------------------------------\n")
    print(f"Monto de la compra: ${monto_compra:.2f}")
    print(f"Monto del descuento: ${monto_descuento:.2f}")
    print(f"Monto a pagar: ${monto_a_pagar:.2f}")
    print(f"Unidades de obsequio: {unidades_obsequio}")
    print("\n---------------------------------\n")


# Ejecutar cuantas veces se desea
while True:
    print("\n---------------------------------\n")
    docenas_compradas = int(input("Ingrese la cantidad de docenas compradas: "))
    precio_por_docena = float(input("Ingrese el precio por docena: "))

    calcular_compra(docenas_compradas, precio_por_docena)

    continuar = input("Desea realizar otra compra? (si/no): ").strip().lower() #.strip() elimina los espacios, .lower() convierte la cadena a minusculas
    if continuar != "si":
        print("Saliendo del programa...")
        break