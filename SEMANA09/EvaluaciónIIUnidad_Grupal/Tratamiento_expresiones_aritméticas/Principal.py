"""
===========================================
CONVERSIÓN DE EXPRESIONES INFIJAS A POSTFIJAS
===========================================

Este programa convierte expresiones aritméticas en notación INFija (como A + B)
a su equivalente en notación POSTfija.

NOTACIÓN INFIJA:
- Forma tradicional: los operadores están entre los operandos (ej. A + B)
- Necesita paréntesis para indicar el orden

NOTACIÓN POSTFIJA:
- Los operadores van DESPUÉS de los operandos (ej. AB+)
- No requiere paréntesis: el orden de operaciones está implícito
- Muy útil para evaluación por parte de una computadora o calculadora RPN

¿CÓMO FUNCIONA ESTE PROGRAMA?
Usamos la estructura de datos llamada PILA, implementada manualmente con NODOS.
Durante la conversión:
- Los operandos se agregan directamente a la salida.
- Los operadores y paréntesis se manejan en la pila según reglas de prioridad.
- Al final, obtenemos una cadena en postfijo lista para evaluarse fácilmente.

"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato#dato que almacena el nodo (ej. '+', '*', 'A')
        self.previo = None#enlace al nodo anterior (como puntero hacia abajo en la pila)


class PilaExpresion:
    def __init__(self):
        self.tope = None#referencia al nodo en la cima de la pila

    def push(self, dato):
        # Se crea un nuevo nodo con el dato recibido y se conecta con el nodo anterior
        nuevo = Nodo(dato)
        nuevo.previo = self.tope
        self.tope = nuevo  # El nuevo nodo ahora es el tope

    def pop(self):
        # Se elimina y devuelve el elemento que está en el tope de la pila
        if self.tope:
            valor = self.tope.dato
            self.tope = self.tope.previo  # El nuevo tope es el nodo anterior
            return valor
        return None#si la pila estaba vacía, devuelve None

    def peek(self):
        # Devuelve el valor del nodo en el tope sin eliminarlo
        if self.tope:
            return self.tope.dato
        return None

    def esta_vacia(self):
        # Devuelve True si la pila no tiene nodos
        return self.tope is None


# Funciones auxiliares

# Verificamos si un carácter es un operador válido
def es_operador(c):
    return c in "+-*/^"

# Devuelve la prioridad de un operador
def prioridad(op):
    if op == '^':
        return 3  # Potencia (más alta prioridad)
    elif op in '*/':
        return 2  # Multiplicación y división
    elif op in '+-':
        return 1  # Suma y resta
    return 0      # Paréntesis u otros caracteres no considerados operadores


# Conversión de notación infija a notación postfija 
def infija_a_postfija(expresion):
    pila = PilaExpresion()# Pila para operadores y paréntesis
    salida = []# Lista para construir la expresión postfija

    # Recorremos cada carácter de la expresión
    for simbolo in expresion:
        if simbolo.isalnum():
            # Si es operando (letra o número), va directo a la salida
            salida.append(simbolo)

        elif simbolo == '(':
            # Paréntesis de apertura se apila sin condiciones
            pila.push(simbolo)

        elif simbolo == ')':
            # Paréntesis de cierre: desapilar operadores hasta encontrar '('
            while not pila.esta_vacia() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()#elimina el '(' (no se agrega a la salida)

        elif es_operador(simbolo):#si es operador
            # Mientras haya operadores en la pila con mayor o igual prioridad
            while (not pila.esta_vacia() and
                   pila.peek() != '(' and
                   (prioridad(simbolo) < prioridad(pila.peek()) or
                    (prioridad(simbolo) == prioridad(pila.peek()) and simbolo != '^'))):
                salida.append(pila.pop())
            # Apilar el operador actual
            pila.push(simbolo)

    # Al finalizar el recorrido, vaciamos lo que queda en la pila
    while not pila.esta_vacia():
        salida.append(pila.pop())

    return ''.join(salida)#convertimos la lista de caracteres en una cadena final



# ------------------------------------------
# Prueba del programa:

if __name__ == "__main__":
    # Ejemplo 1
    expresion = "(A+B)*C"
    print("Expresión infija: ", expresion)
    resultado = infija_a_postfija(expresion)
    print("Expresión postfija:", resultado)

    # Ejemplo 2 (más compleja)
    expresion2 = "A+(B*C-(D/E^F)*G)*H"
    print("\nExpresión infija: ", expresion2)
    print("Expresión postfija:", infija_a_postfija(expresion2))
