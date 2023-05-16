# 19-Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. Un número perfecto es aquel que es igual a
# la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

num = int(input("Ingrese un número: "))
divisores = []

# Buscamos los divisores propios del número
for i in range(1, num):
    if num % i == 0:
        divisores.append(i)

# Sumamos los divisores propios
suma_divisores = sum(divisores)

# Verificamos si el número es perfecto o no
if suma_divisores == num:
    print(num, "es un número perfecto")
else:
    print(num, "no es un número perfecto")