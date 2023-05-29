# 15-Crea una función llamada contar_palabras que tome una cadena de texto
# como parámetro y devuelva el número de palabras que contiene. Se considera
# que las palabras están separadas por espacios.

def contar_palabras(cadena):
    palabras = cadena.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

texto = "Este es un ejemplo de texto"
cantidad_palabras = contar_palabras(texto)
print(cantidad_palabras)
