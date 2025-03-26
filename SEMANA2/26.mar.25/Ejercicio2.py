# Escribir un programa que permita emitir la FACTURA correspondiente, 
# a una compra de un artículo determinado, del que se adquieren una o varias unidades. 
# El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), 
# es mayor de 1000, se aplicará un descuento del 12%.

import os
os.system('cls')

while True: 
    print("Bienvenido al sistema de facturación")
    print("""
            1) Voy a facturrar un solo artículo
            2) Voy a facturar más de un artículo
            3) Salir""")

    opcion = int(input("\nSeleccione una opción: "))

    match opcion:
        case 1:
            precioArt = float(input("Ingrese el precio del producto: "))
            IVA = precioArt * 0.15
            subtotalIVA = precioArt + IVA

            if subtotalIVA >= 1000:
                descuento = subtotalIVA * 0.12
                total = subtotalIVA - descuento
                print(f"""
                        Subtotal: C${subtotal:.2f}
                        IVA(15%): C${IVA:.2f}
                        Descuento(12%): C${descuento:.2f}
                        Total: C${total:.2f}""")
            else:
                print(f"""
                        Subtotal: C${precioArt:.2f}
                        IVA(15%): C${IVA:.2f}
                        Total: C${subtotalIVA:.2f}""")
        case 2:
            cantArt = float(input("Ingrese la cantidad de artículos a facturar: "))
            precioArt = float(input("Ingrese el precio del producto: "))
            subtotal = cantArt * precioArt
            IVA = subtotal * 0.15
            aplicIVA = subtotal + IVA

            if aplicIVA >= 1000:
                descuento = aplicIVA * 0.12
                total = aplicIVA - descuento
                print(f"""
                        Subtotal: C${subtotal:.2f}
                        IVA(15%): C${IVA:.2f}
                        Descuento(12%): C${descuento}
                        Total: C${total:.2f}""")
            else: 
                print(f"""
                        Subtotal: C${subtotal:.2f}
                        IVA(15%): C${IVA:.2f}
                        Total: C${aplicIVA:.2f}""")
        
        case 3:
            print("Saliendo del sistema...")
            break
        
        case _:
            print("Opción no válida")
        
    print("\n---------------------------------\n")
