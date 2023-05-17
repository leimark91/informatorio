

# Ingresa el texto y las letras deacuerdo a los tips dados
print('\n')
texto_original = str(input('Ingrese un texto: '))
texto_procesado = texto_original.lower().strip()
print('\n')
letras = str(input('ingrese tres letras a elección separadas por un espacio: ')).lower()
letras = letras.split(' ')

# 1- Cantidad de veces que aparece cada una de letras que ingresó en el texto.
print('\n')
for letra in letras:
    print(f'veces que aparece {letra}: {texto_procesado.count(letra)}')
print('\n')

# 2- Cuantas palabras hay en total en todo el texto.

 
palabras = texto_procesado.split(' ')
palabras_validas = []
for palabra in palabras:
    if palabra != '':
        palabras_validas.append(palabra)

print(f'El texto contiene: {len(palabras_validas)}, palabras')
print('\n')

# 3- Cual es la primera letra y cuál es la última. (Indexación)

print(f'El texto comienza con la letra: {texto_original.strip()[0]}')
print(f'El texto termina con la letra: {texto_original.strip()[-1]}')
print('\n')

# 4- Texto en orden inverso
texto_inverso = " ".join(texto.split()[::-1])
print(f"El texto en orden inverso es: {texto_inverso}")

# 5- Decir si la palabra "python" aparece en el texto.

if texto_procesado.find('python') != -1:
    print(f'El texto contiene la palabra \'python\'')
else:
    print(f'El texto NO contiene la palabra \'python\'')
print('\n')
















                     



