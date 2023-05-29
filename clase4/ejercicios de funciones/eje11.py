# 11-Crea una función llamada contar_vocales que tome una cadena de texto como
# parámetro y devuelva el número de vocales que contiene.

def contar_vocales(cadena):
    contador = 0
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    for letra in cadena.lower():
        if letra in vocales:
            contador += 1
    
    return contador

cadena = "Hola, mundo"
resultado = contar_vocales(cadena)
print(resultado)