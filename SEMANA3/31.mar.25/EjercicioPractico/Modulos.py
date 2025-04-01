from colorama import init, Fore, Style # Importamos la librería colorama, para hacerlo más agradable visualmente
init(autoreset=True) # Restablece los colores automáticamente, para que no todo el texto se convierta en el color que estemos utilizando


# Función para saludar al usuario
def Saludo(n):
    return print(Fore.GREEN+f"\nBienvenid@ al programa", Fore.GREEN+n, Fore.GREEN+"!")

# Función para solicitar al usuario un número impar entre 1 y 19
def ingresar_numero():
    while True:
        try:
            print("\n======================================================")
            n = int(input("Ingrese un número entero impar entre 1 y 19: "))
            if n % 2 == 1 and 1 <= n <= 19:
                return n
            else:
                print(Fore.RED+"El número debe ser impar y estar entre 1 y 19.")
        except ValueError:
            print(Fore.RED+"Entrada inválida. Intente nuevamente.")

# Función para calcular la suma de la serie de números impares hasta n
def calcular_serie(n):
    return sum(range(1, n + 1, 2))  # suma de la serie de números desde 1 hasta n, añadiendo 2 números en cada iteración

# Función para calcular el producto de los números impares hasta n
def calcular_producto(n):
    producto = 1
    for i in range(1, n + 1, 2): # serie de números desde 1 hasta n, añadiendo 2 números en cada iteración
        producto *= i
    return producto

# Función que muestra el menú de opciones y gestiona la ejecución del programa
def menu(n):
    while True:
        print("\n======================================================")
        print("\t\tMenú de opciones")
        print("======================================================")
        print("1. Calcular la serie numérica 1 + 3 + 5 + ... + n")
        print("2. Calcular el producto 1 * 3 * 5 * ... * n")
        print("3. Salir del programa")
        print("======================================================")
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                print(Fore.MAGENTA+f"\nEl resultado de la serie es: {calcular_serie(n)}")
            case "2":
                print(Fore.MAGENTA+f"\nEl resultado del producto es: {calcular_producto(n)}")
            case "3":
                print(Fore.RED+"\nSaliendo del programa...")
                break
            case _:
                print(Fore.RED+"\nOpción no válida, intente de nuevo.")



