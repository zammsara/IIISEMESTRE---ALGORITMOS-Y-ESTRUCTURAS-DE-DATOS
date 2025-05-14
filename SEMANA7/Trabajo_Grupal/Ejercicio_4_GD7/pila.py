class Pila:
    def __init__(self):
        #lista para almacenar las tareas
        self.tareas = []

    def push(self, tarea):
        #agrega una nueva tarea a la pila
        self.tareas.append(tarea)

    def esta_vacia(self):
        #verifica si la pila está vacía
        return len(self.tareas) == 0

    def pop(self):
        #elimina y devuelve la última tarea agregada
        if not self.esta_vacia():
            return self.tareas.pop()
        else:
            return "No hay tareas para revisar."

    def peek(self):
        #devuelve la última tarea sin eliminarla
        if not self.esta_vacia():
            return self.tareas[-1]
        else:
            return "No hay tareas pendientes."

    def __str__(self):
        #representación en texto de la pila
        return str(self.tareas)
