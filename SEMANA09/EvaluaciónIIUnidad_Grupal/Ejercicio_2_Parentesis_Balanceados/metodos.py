# metodos.py

"""
Ejercicio 2: Verificación de Paréntesis Balanceados
Descripción:
Verificación de paréntesis balanceados. Escriba un programa que
determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ] balanceados.
Use una pila para realizar el seguimiento de los paréntesis abiertos.


Nota (Parentesis Balanceados): Los parentesis abiertos deben cerrarse en el orden inverso
al que fueron abiertos.

Ejemplo de cadenas balanceadas:
    - "[()]" -> balanceado

Ejemplo de cadenas no balanceadas:  
    - "[(])" -> no balanceado

ALGORITMO DE VERIFICACIÓN DE PARÉNTESIS BALANCEADOS:

El algoritmo funciona utilizando una estructura tipo pila (stack) p
ara realizar un seguimiento de los paréntesis abiertos:

    1. Recorre cada caracter de la cadena.
    2. Si encuentra un paréntesis de apertura ('(', '[', '{'), lo inserta en la pila.
    3. Si encuentra un paréntesis de cierre (')', ']', '}'), verifica:
    - Que la pila no esté vacía.
    - Que el paréntesis de cierre coincida con el último paréntesis de apertura insertado.
    4. Si alguno de estos dos puntos falla, la cadena no está balanceada.
    5. Al finalizar, si la pila está vacía, la cadena está balanceada. De lo contrario, no lo está.
    
ALGORITMO PARA BALANCEAR PARÉNTESIS EN UNA CADENA:

El algoritmo genera una versión balanceada de una cadena:
1. Utiliza una pila para llevar registro de índices de símbolos de apertura.
2. Cuando encuentra símbolos de cierre verifica la pila:
   - Si la pila tiene símbolos abiertos compatibles, los empareja.
   - Si no, omite el símbolo de cierre (no balanceado).
3. Finalmente, elimina los símbolos de apertura que quedaron sin emparejar (no balanceados).
4. Retorna la cadena resultante balanceada.

"""

from pila import Pila


"Definición de los paréntesis"
apertura = '([{' # Paréntesis de apertura
cierre = ')]}' # Paréntesis de cierre
pares = {')': '(', ']': '[', '}': '{'} # Diccionario para pares de paréntesis


def verificar_balanceo(cadena):
    pila = Pila()
    
    for caracter in cadena:
        if caracter in apertura:
            pila.push(caracter)  # Se agrega el paréntesis de apertura a la pila
        elif caracter in cierre: # Se encuentra un paréntesis de cierre
            if pila.is_empty(): 
                return False  # No hay apertura correspondiente
            if pila.pop() != pares[caracter]:
                return False  # No coincide con la apertura correcta

    return pila.is_empty()  # True si pila está vacía (balanceado), False en caso contrario

## Función para balancear la cadena
def balancear(cadena):
    pila = Pila() 
    indices_invalidos = set() # Conjunto para almacenar índices inválidos
    
    if verificar_balanceo(cadena):
        print("La cadena ya está balanceada: .")
        return cadena

    for idx, caracter in enumerate(cadena): # Por cada indice y caracter en la cadena enumerada
        if caracter in apertura: # si el caracter es de apertura
            pila.push((caracter, idx)) # Se agrega el paréntesis de apertura y su índice a la pila
        elif caracter in cierre: # si el caracter es de cierre
            """Si la pila no está vacía y el último elemento de la pila es
            el paréntesis de apertura correspondiente"""""
            if not pila.is_empty() and pila.peek()[0] == pares[caracter]: 
                pila.pop() # Se elimina el paréntesis de apertura de la pila
            else:
                indices_invalidos.add(idx) # Si nada de esto se cumple,
                #se agrega el índice del paréntesis de cierre a los inválidos

    indices_invalidos.update(idx for _, idx in pila.items)

    """Elimina los caracteres en los índices inválidos de la cadena
    y devuelve la cadena balanceada"""
    return ''.join(
        caracter for idx, caracter in enumerate(cadena) if idx not in indices_invalidos
    )