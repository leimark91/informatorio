# Inportar la biblioteca random para generar un numero random con random.randint

import random

# Pedimos al usuario que ingrese su nombre

nombre = input("¡Bienvenido! ¿Cómo te llamas? ")

# Generamos un número aleatorio entre 1 y 100

numero_a_adivinar = random.randint(1, 100)

# Inicializamos el número de intentos en 8

intentos_restantes = 8

# Comenzamos el juego

print(f"{nombre}, estoy pensando en un número entre 1 y 100. Tienes 8 intentos para adivinarlo.")

print("-~-" * 30)

# Mientras queden intentos, seguimos jugando

while intentos_restantes > 0:

    # Pedimos al usuario que ingrese un número

    numero_str = input("Ingresa un número: ")
    
    # Verificamos que el usuario haya ingresado un número entero

    if not numero_str.isdigit():
        print("Eso no es un número entero. Intenta de nuevo.")
        continue
    
    # Convertimos el número ingresado a entero

    numero_usuario = int(numero_str)
    
    # Verificamos si el usuario adivinó el número

    if numero_usuario == numero_a_adivinar:
        print("~" * 90)
        print(f"¡Felicidades, {nombre}! Adivinaste el número en el intento {9 - intentos_restantes}.")
        print("~" * 90)
        break
    elif numero_usuario < numero_a_adivinar:
        print("El número a adivinar es mayor.")
        print("+" * 90)
    else:
        print("El número a adivinar es menor.")
        print("-" * 90)

    # Descontamos un intento al usuario

    intentos_restantes -= 1
    
    # Informamos al usuario cuántos intentos le quedan
    
    print(f"Te quedan {intentos_restantes} intentos.")
    
    print("*" * 90)
# Si se acabaron los intentos y el usuario no adivinó el número, se lo informamos

if intentos_restantes == 0:
    print(f"Lo siento, {nombre}, se te acabaron los intentos. El número que debías adivinar era {numero_a_adivinar}.")

#Integrantes G6: 
# Lucas Matias Almiron 
# Mauricio Acevedo 
# Gustavo Medina 
# Alfonzo Luis Andres 
# Omar Alejandro Maciel 
# Alejandor Gutierrez 
# Federico Peralta 
# Matias Martin Satina 
# Rodolfo Sanchez 
# Luis Marcos Antonio Leiva