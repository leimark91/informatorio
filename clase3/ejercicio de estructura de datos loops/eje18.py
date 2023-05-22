# 18-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
#     1
#    2 3
#   4 5 6
#  7 8 9 10


n = int(input("Ingrese un número: "))
contador = 1
for i in range(n):
    for j in range(i+1):
        print(contador, end=' ')
        contador += 1
    print() # para imprimir la nueva línea al final de cada fila