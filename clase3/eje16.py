# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima la misma cadena pero con cada palabra al revés.

cadena = input("Ingrese una cadena de texto: ")

# Dividir la cadena en una lista de palabras
palabras = cadena.split()

# Invertir cada palabra y crear una lista de palabras invertidas
palabras_invertidas = []
for palabra in palabras:
    palabras_invertidas.append(palabra[::-1])

# Unir las palabras invertidas en una cadena de texto
cadena_invertida = " ".join(palabras_invertidas)

# Imprimir la cadena de texto invertida
print(cadena_invertida)