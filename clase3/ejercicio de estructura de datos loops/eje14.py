# 14-Escribe un programa que pida al usuario un número y luego imprima un triángulo de números como el siguiente:
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5


num = int(input("Ingresa un número: "))

for i in range(1, num+1):
    for j in range(i):
        print(i, end=" ")
    print()