# 12-Escribe un programa que pida al usuario una lista de números separados por comas y calcule su promedio.

# Pedir al usuario que ingrese una lista de números separados por comas
numeros_str = input("Ingrese una lista de números separados por comas: ")

# Convertir la cadena de texto ingresada en una lista de números
numeros = [int(num) for num in numeros_str.split(',')]

# Calcular el promedio de la lista de números
promedio = sum(numeros) / len(numeros)

# Imprimir el promedio calculado
print(f"El promedio de los números es: {promedio}")