# 7-Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).

palabra = input("Ingresa una palabra: ")
inversa = ""
i = len(palabra) - 1

while i >= 0:
    inversa += palabra[i]
    i -= 1

if palabra == inversa:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")