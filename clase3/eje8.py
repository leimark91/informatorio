# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima el número de palabras que contiene.

texto = input("Introduce una cadena de texto: ")
palabras = 0
indice = 0

while indice < len(texto):
    # Si el caracter actual no es un espacio y el siguiente caracter es un espacio o estamos en el final del texto, entonces contamos una palabra
    if texto[indice] != " " and (indice == len(texto) - 1 or texto[indice + 1] == " "):
        palabras += 1
    indice += 1

print("El número de palabras en la cadena de texto es:", palabras)