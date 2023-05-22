# 9-Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

# Pedimos al usuario un número
n = int(input("Introduce un número: "))

# Inicializamos las variables de la serie
a, b = 0, 1

# Creamos una lista para almacenar la serie
fibonacci = []

# Generamos la serie de Fibonacci hasta el número ingresado por el usuario
while a <= n:
    fibonacci.append(a)
    a, b = b, a + b

# Mostramos la serie resultante
print(f"La serie de Fibonacci hasta {n} es: {fibonacci}")