texto = input("Ingrese un texto: ")
letras = input("Ingrese tres letras separadas por comas: ").split(",")

# Contar la cantidad de veces que aparece cada letra
apariciones = [texto.lower().count(letra.lower().strip()) for letra in letras]

# Contar la cantidad de palabras en el texto
palabras = len(texto.split())

# Obtener la primera y última letra
primera_letra = texto[0]
ultima_letra = texto[-1]

# Mostrar el texto en orden inverso
texto_inverso = texto[::-1]

# Verificar si la palabra "python" aparece en el texto
contiene_python = "python" in texto.lower()

# Mostrar los resultados
print("Cantidad de veces que aparece cada letra:")
for i in range(len(letras)):
    print(f"{letras[i].strip()}: {apariciones[i]}")

print("Cantidad de palabras en el texto:", palabras)
print("Primera letra:", primera_letra)
print("Última letra:", ultima_letra)
print("Texto en orden inverso:", texto_inverso)
print("La palabra 'python' aparece en el texto:", "Sí" if contiene_python else "No")

