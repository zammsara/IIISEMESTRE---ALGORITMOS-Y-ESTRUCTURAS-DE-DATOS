def imprimir_piramide(n, nivel=1): #n es cuántas filas tendrá la pirámide
                        #nivel es una ayuda interna para saber cuántos espacios poner, empieza en 1
    if n < 1: #si ya no quedan más filas, no hace nada y termina
        return
    imprimir_piramide(n - 1, nivel + 1)
    print(' ' * (nivel - 1) + '*' * (2 * n - 1))

# Ejemplo de uso:
altura = 5
imprimir_piramide(altura)
