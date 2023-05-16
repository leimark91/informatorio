#15-Escribe un programa que pida al usuario una cadena de texto y determine
# cuántas veces aparece cada letra en la cadena.

texto = input("Introduce una cadena de texto: ")
frecuencia = {}

for letra in texto:
    if letra != " ":
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1

print("Frecuencia de letras en la cadena:")
for letra, count in frecuencia.items():
    print(f"{letra}: {count}")
