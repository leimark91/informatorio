# 19-Crea una función llamada es_bisiesto que tome un año como parámetro y
# devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
# es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
# divisible por 400.

def es_bisiesto(ano):
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return "Bisiesto"
    else:
        return "No es Bisiesto"

ano = 2024
resultado = es_bisiesto(ano)
print(ano, "es", resultado)