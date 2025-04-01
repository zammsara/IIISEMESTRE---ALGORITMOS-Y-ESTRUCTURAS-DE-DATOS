import Modulos as mo # Importamos las funciones ubicadas en Modulos

import os
os.system('cls')

nombre = input("Ingresa tu nombre: ")

mo.Saludo(nombre)

numero = mo.ingresar_numero() # Solicitar el número impar dentro del rango al usuario antes de mostrar el menú
mo.menu(numero)