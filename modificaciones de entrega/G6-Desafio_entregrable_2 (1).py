#Requisitos técnicos:
#Métodos y propiedades de string.
#Indexar estructuras de datos.
#Todos los tipos de datos.
#Se te pide crear un programa que le pida al usuario que ingresar un texto
#cualquiera, por ejemplo, un artículo o una frase.
#Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
#elección.
#Nuestro código va a procesar esa información para realizar los análisis
#necesarios para devolverle al usuario la siguiente información:
#1- Cantidad de veces que aparece cada una de letras que eligió.
#Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
#string
#Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
#encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
#minúscula.
#2- Cuantas palabras hay en total en todo el texto.
#Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
#3- Cual es la primera letra y cuál es la última. (Indexación)
#4- Mostrar el texto en orden inverso.
#5- Decir si la palabra "python" aparece en el texto.
#Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
#string para mostrar al usuario

# Pedir al usuario que ingrese un texto
texto = input("Ingrese un texto: ")

print()

# Pedir al usuario que ingrese 3 letras
letras = input("Ingrese 3 letras separadas por espacios: ").lower().split()

print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print()

# 1- Cantidad de veces que aparece cada una de las letras que eligió
for letra in letras:
    cantidad = texto.lower().count(letra)
    print(f"La letra {letra} aparece {cantidad} veces en el texto")
    print()

# 2- Cantidad de palabras en el texto
palabras = texto.split()
cantidad_palabras = len(palabras)
print(f"El texto tiene {cantidad_palabras} palabras")

print()

# 3- Primera y última letra del texto
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra del texto es {primera_letra} y la última letra es {ultima_letra}")

print()

# 4- Texto en orden inverso
texto_inverso = " ".join(texto.split()[::-1])
print(f"El texto en orden inverso es: {texto_inverso}")

print()

# 5- Verificar si la palabra "python" aparece en el texto
contiene_python = "python" in texto.lower()
mensaje = {True: "El texto contiene la palabra 'python'", False: "El texto no contiene la palabra 'python'"}
print(mensaje[contiene_python])

#Integrantes G6: Lucas Matias Almiron, Mauricio Acevedo, Gustavo Medina, Alfonzo Luis Andres, Omar Alejandro Maciel, Alejandor Gutierrez, Federico Peralta, Matias Martin Satina, Rodolfo Sanchez, Luis Marcos Antonio Leiva