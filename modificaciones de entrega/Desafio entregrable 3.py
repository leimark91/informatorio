#Desafío 3: Adivina el número
#Requisitos técnicos:
#- Operadores lógicos.
#- Operadores de comparación.
#- Control de flujo - Condicionales.
#- Control de Flujo - Repetitivas.
#Vamos a crear un juego completamente funcional.
#Para ello el programa debe:
#* Pedir al usuario que ingrese su nombre.
#* Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
#* Generar aleatoriamente un número entero entre 1 y 100.
#tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
#* Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
#El "número" ingresado por el usuario puede:
#* No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
#tip 2: con el método isdigit() puedes saber si es posible convertir a entero
#* Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
#* Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
#* Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento lo adivinó.
#* Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si debes descontarle un intento.
#* En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que ingrese otro número.
#* Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el número que tenía que adivinar.

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
    
    # Descontamos un intento al usuario

    intentos_restantes -= 1
    
    # Verificamos si el usuario adivinó el número

    if numero_usuario == numero_a_adivinar:
        print(f"¡Felicidades, {nombre}! Adivinaste el número en el intento {8 - intentos_restantes}.")
        break
    elif numero_usuario < numero_a_adivinar:
        print("El número a adivinar es mayor.")
    else:
        print("El número a adivinar es menor.")
    
    # Informamos al usuario cuántos intentos le quedan

    print(f"Te quedan {intentos_restantes} intentos.")
    
# Si se acabaron los intentos y el usuario no adivinó el número, se lo informamos

if intentos_restantes == 0:
    print(f"Lo siento, {nombre}, se te acabaron los intentos. El número que debías adivinar era {numero_a_adivinar}.")
