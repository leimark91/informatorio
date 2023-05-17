#

def es_divisible(num1, num2):
 if num1 % num2 == 0:
     return "Es divisible."
 else:
    return "No es divisible."

numero_divisibles = es_divisible(4, 2)
print (numero_divisibles)