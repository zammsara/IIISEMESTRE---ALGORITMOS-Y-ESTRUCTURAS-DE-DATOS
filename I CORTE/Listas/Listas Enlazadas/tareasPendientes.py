# Este es un pequeño programa que simula una lista de tareas usando las listas enlazadas, en el que se podrá:
    # Agregar nuevas tareas
    # Mostrar todas las tareas
    # Marcar las tareas como completadas
    # Eliminar tareas completadas
    
# Definimos la clase "Nodo": cada tarea es un nodo, con un nombre y estado(completado o no)
class Nodo: 
    
    def __init__(self, tarea):
        self.tarea = tarea
        self.completada = False # Estado de la tarea(False = pendiente, True = completada)
        self.siguiente = None

# Definimos la clase que administrará la lista de tareas
class listaDeTareas:
    def __init__(self):
        self.cabeza = None # Al incio la lista esta vacía
    
    # Método para agregar una nueva tarea al final de la lista
    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if not self.cabeza: #si la lista esta vacía
            self.cabeza = nuevo_nodo
        else: #si ya hay tareas, recorremos hasta el final
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo #enlazamos el último nodo con el nuevo
        print(f"✅ Tarea '{tarea}' agregada con éxito.")
        
    # Método para mostrar todas las tareas
    def mostrar_tareas(self):
        actual = self.cabeza
        if not actual: #si no hay tareas
            print("📭 La lista de tareas está vacía.")
            return
        
        print("\n📋 Lista de tareas:")
        i = 1
        while actual:
            estado = "✅" if actual.completada else "❌"  # se muestra el estado visual
            print(f"{i}. {actual.tarea} {estado}")
            actual = actual.siguiente
            i += 1
    
    # Método para marcar una tarea como completada
    def completar_tarea(self, numero):
        actual = self.cabeza
        i = 1
        while actual:
            if i == numero:  # Si llegamos al número indicado
                if actual.completada:
                    print("⚠️ Esa tarea ya estaba completada.")
                else:
                    actual.completada = True
                    print(f"🎉 Tarea '{actual.tarea}' marcada como completada.")
                return
            actual = actual.siguiente
            i += 1
        print("❌ Número de tarea no válido.")   
    
    # Método para eliminar todas las tareas completadas
    def eliminar_completadas(self):
        eliminadas = False #esta variable se utiliza para saber si se han eliminado tareas o no

        # Caso especial: si las primeras tareas están completadas
        while self.cabeza and self.cabeza.completada:
            self.cabeza = self.cabeza.siguiente #se elimina el nodo actual y apuntamos al nodo siguiente
            eliminadas = True

        actual = self.cabeza
        while actual and actual.siguiente:
            if actual.siguiente.completada:
                actual.siguiente = actual.siguiente.siguiente  # cambiamos el enlace del nodo anterior para que apunte al nodo que sigue al nodo completado, eliminando efectivamente ese nodo de la lista
                eliminadas = True
            else:
                actual = actual.siguiente

        if eliminadas:
            print("🧹 Tareas completadas eliminadas.")
        else:
            print("📌 No hay tareas completadas para eliminar.")
            
            
#=========================================================================================================================================================================================================================

lista = listaDeTareas() #inicializamos la lista

while True:
        # Mostrar menú de opciones
        print("\n--- MENÚ ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tareas completadas")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            tarea = input("Escribe la nueva tarea: ")
            lista.agregar_tarea(tarea)

        elif opcion == 2:
            lista.mostrar_tareas()

        elif opcion == 3:
            try:
                numero = int(input("Número de la tarea a completar: "))
                lista.completar_tarea(numero)
            except ValueError:
                print("⚠️ Ingresa un número válido.")

        elif opcion == 4:
            lista.eliminar_completadas()

        elif opcion == 5:
            print("👋 ¡Hasta pronto!")
            break

        else:
            print("❌ Opción no válida. Intenta de nuevo.")