from modulos5 import Pila
pila = Pila()

while True:
        
   
        print("===================\n--- Menú de Opciones===================") # Menu de opciones 
        print("1. Apilar un saco")
        print("2. Descargar un saco (pop)")
        print("3. Ver el saco que está encima (peek)")
        print("4. Salir")
        print("===================\n--- Menú de Opciones===================")

        op = 0
        op = int(input(" Ingrese una de las 4 opciones del menú: "))
        if op == 1:
                elementos = input(" Ingresa el nombre de los productos que tendra cada saco: ")
                pila.push(elementos) # se ingresa el nmbre de los sacos y se agrega a la pila
                print(f"Saco '{elementos}' apilado.")
        elif op == 2:
                saco = pila.pop()  # Se elimina el ultimo valor agregado de la pila (el ultimo saco)
                if saco:
                    print(f"Saco descargado: {saco}") # Si el saco existe se elimina el ultimo valor
                else:
                    print("No hay sacos que descargar.") # si no hay nada en la pila, manda un mensaje
        elif op == 3:
              cima = pila.ultimo()
              if cima:
                print(f"El saco en la cima es: {cima}") # Si la pila existe se muestra el ultimo elemento de la pila (ultimo saco)
              else:
                 print("La pila está vacía.")
        elif op == 4: # opcion para 
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
                
                
  