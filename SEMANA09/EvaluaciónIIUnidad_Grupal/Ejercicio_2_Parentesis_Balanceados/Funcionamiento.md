¡Claro! Aquí tienes **todo el contenido en formato `.md` listo para copiar y pegar directamente en tu archivo `README.md`**:

---

````md
# 🧪 Ejercicio 2: Verificación de Paréntesis Balanceados

## 📘 Descripción

Este programa permite verificar si una cadena de texto contiene **paréntesis correctamente balanceados**. Se consideran los tres tipos de paréntesis:

- Paréntesis: `()`
- Corchetes: `[]`
- Llaves: `{}`

El algoritmo utiliza una estructura de **pila (stack)** para rastrear los paréntesis abiertos y asegurar que se cierren en el orden correcto.

> ⚠️ **Importante:** Los paréntesis deben cerrarse en el orden **inverso** al que fueron abiertos (principio LIFO: último en entrar, primero en salir).

---

## ✅ Ejemplos de Cadenas Balanceadas

```plaintext
[()]
{[(){}]}
(()[{}])
````

## ❌ Ejemplos de Cadenas No Balanceadas

```plaintext
[(])
{[}]
((())
[({)]
```

---

## 🔄 Algoritmo de Verificación

### 🧠 Lógica del Algoritmo

1. Recorrer cada carácter de la cadena.
2. Si el carácter es un paréntesis **de apertura** (`(`, `[`, `{`), se apila.
3. Si el carácter es un paréntesis **de cierre** (`)`, `]`, `}`):

   * Verificar que la pila **no esté vacía**.
   * Verificar que **coincida** con el paréntesis correspondiente.
   * Si alguna verificación falla, la cadena está **desbalanceada**.
4. Al finalizar, si la pila está vacía → ✔️ la cadena está balanceada.
   Si hay elementos en la pila → ❌ la cadena no está balanceada.

---

## 📄 Pseudocódigo: Verificación de Paréntesis

```plaintext
Función esBalanceado(cadena):
    Crear una pila vacía

    Para cada caracter en la cadena:
        Si caracter es '(', '[', '{':
            Apilar(caracter)

        Si caracter es ')', ']', '}':
            Si la pila está vacía:
                Retornar FALSO

            tope ← cima de la pila
            Si tope y caracter no coinciden:
                Retornar FALSO

            Desapilar()

    Si la pila está vacía:
        Retornar VERDADERO
    Sino:
        Retornar FALSO
```

---

## 🧰 Algoritmo Extra: Balancear Cadena (Eliminar Paréntesis Incorrectos)

Este segundo algoritmo genera una **versión balanceada de la cadena**, eliminando los paréntesis no emparejados. Es útil para corregir expresiones con errores.

### 📄 Pseudocódigo: Balanceo de Cadena

```plaintext
Función balancearCadena(cadena):
    Crear una pila vacía para índices de apertura
    Crear una lista resultado ← caracteres de cadena

    Para i desde 0 hasta longitud(cadena) - 1:
        caracter ← cadena[i]

        Si caracter es paréntesis de apertura:
            Apilar(i)

        Si caracter es paréntesis de cierre:
            Si pila no está vacía Y empareja con el último:
                Desapilar()
            Sino:
                resultado[i] ← "" // Eliminar cierre no emparejado

    Mientras pila no esté vacía
```

