# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

resultado = es_capicua(12321)
print(resultado)

resultado = es_capicua(12345)
print(resultado)