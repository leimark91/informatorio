# 5-Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.

def es_divisible(num1, num2):
    if num1 % num2 == 0:
        return "Es divisible"
    else:
        return "No es divisible"

resultado = es_divisible(10, 2)
print(resultado)