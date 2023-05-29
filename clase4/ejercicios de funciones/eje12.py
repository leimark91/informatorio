# 12-Crea una función llamada convertir_temperatura que tome una temperatura
# en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = 25
fahrenheit = convertir_temperatura(celsius)
print(fahrenheit)