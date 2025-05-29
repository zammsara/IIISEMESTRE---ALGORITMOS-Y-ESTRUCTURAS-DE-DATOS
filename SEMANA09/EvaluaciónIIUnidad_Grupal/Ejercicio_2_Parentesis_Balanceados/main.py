# main.py
from metodos import verificar_balanceo, balancear

def main():
    while True:
        print("\n--- Menú ---")
        print("1. Verificar balanceo")
        print("2. Balancear cadena")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cadena = input("Ingrese la cadena a verificar: ")
            if verificar_balanceo(cadena):
                print("✅ La cadena está balanceada.")
            else:
                print("❌ La cadena NO está balanceada.")

        elif opcion == "2":
            cadena = input("Ingrese la cadena a balancear: ")
            balanceada = balancear(cadena)
            print(f"Cadena balanceada: {balanceada}")

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    main()
