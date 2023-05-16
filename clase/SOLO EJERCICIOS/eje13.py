#Escribe un programa que solicite al usuario su nombre y su edad, y luego imprima un mensaje que indique cuántos años tendrá el usuario
# en 10 años más. 

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
edad_en_10_anios = edad + 10
print("Hola ", nombre + "! En 10 años más tendrás", edad_en_10_anios, "años.")