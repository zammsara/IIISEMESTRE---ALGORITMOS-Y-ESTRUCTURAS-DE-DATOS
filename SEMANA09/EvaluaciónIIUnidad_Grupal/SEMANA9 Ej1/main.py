#Ejercicio #1: Inversión de palabras en una frase. Desarrolle un programa que 
#utilice una pila para invertir el orden de las palabras en una frase dada. Por ejemplo, 
#la frase "Hola mundo desde UAM" debería invertirse a "UAM desde mundo Hola".





from modulos import Pila

pila = Pila()              # Pila para frases originales
pila_palabras = Pila()     # Pila para frases invertidas 

while True:
    print("===================\n--- Menú de Opciones===================")
    print("1. Ingresar frase y revertirla")
    print("2. Eliminar última frase ingresada")
    print("3. Ver la última frase ingresada")
    print("4. Salir")
    print("===================\n--- Menú de Opciones===================")

    try:
        op = int(input("Ingrese una de las 4 opciones del menú: "))  
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if op == 1:
        frasesIngresadas = input("Ingresa la frase que desee: ")
        pila.push(frasesIngresadas)  # Guarda frase original en la pila 1

        palabra = "" #Variable para construir cada palabra
        pila_temp = Pila()  # Pila temporal donde las palabras individuales se almacenaran para invertirlas

        #Recorremos la frase palabra por palabra   
        for caracter in frasesIngresadas:
            if caracter != " ": # si la frase no es igual a un espacio, se sigue construyendo la palabra
                palabra = palabra + caracter
            else:
                pila_temp.push(palabra)  # Si encontramos un espacio, apilamos la palabra construida
                palabra = "" # Reiniciamos la siguiente palabra

        if palabra: # Verificamos si quedó una palabra al final
            pila_temp.push(palabra)  # Última palabra

        # Vaciar la pila temporal para construir la frase invertida
        frase_invertida = ""
        while not pila_temp.esta_vacia(): 
            frase_invertida += pila_temp.pop() + " " # Extraemos cada palabra y la agregamos

        frase_invertida = frase_invertida.strip() # el .strip solo quita los espacios enblanco 
        pila_palabras.push(frase_invertida)  # Guarda la frase invertida

        print(f"Frase '{frasesIngresadas}', orden invertido: {frase_invertida}")

    elif op == 2:
        frase = pila.pop()              # Quita frase original (ultima de la pila)
        frase_invertida = pila_palabras.pop()  # Quita frase invertida (ultima de la pila)

        if frase: # si la frase existe
            print(f"Frase eliminada: {frase}") # se elimina las dos frase (normal e invertida)
            print(f"Frase invertida eliminada: {frase_invertida}")
        else:
            print("No hay frases que eliminar.")

    elif op == 3:
        cima = pila.ultimo()             # Muestra frase original
        cima_invertida = pila_palabras.ultimo()  # Muestra frase invertida

        if not cima or not cima_invertida: # si no hay cima o cima invertida (las frases)
            print("La pila está vacía.") # se manda mensaje

    elif op == 4:
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
