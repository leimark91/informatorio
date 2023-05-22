#Desafío 3: Adivina el número
#Requisitos técnicos:
#- Operadores lógicos.
#- Operadores de comparación.
#- Control de flujo - Condicionales.
#- Control de Flujo - Repetitivas.
#Vamos a crear un juego completamente funcional.
#Para ello el programa debe:
# Pedir al usuario que ingrese su nombre.
# Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
# Generar aleatoriamente un número entero entre 1 y 100.
#tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
# Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
#El "número" ingresado por el usuario puede:
# No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
#tip 2: con el método isdigit() puedes saber si es posible convertir a entero
# Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
# Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
# Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento
#lo adivinó.
# Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
#debes descontarle un intento.
# En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que
#ingrese otro número.
# Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el
#número que tenía que adivinar.

#Saludo inicial
print("HOLA... JUGUEMOS UN JUEGO...\nYO PIENSO UN NUMERO Y TU TRATAS DE ADIVINARLO")

#Pedimos al usuario que ingrese su nombre.
nombre=input("Antes De Continuar, Por Favor Dime Tu Nombre: ").title()
print("#"*90)
#Explicamos las reglas del juego.
print(f"""Hola {nombre}.
Estoy Pensando En Un Numero Entre 1 y 100.
Podras Adivinarlo? Tienes 8 Intentos.""")
print("~" * 90)
print("¡COMENCEMOS!")
#Comienza el juego. importamos la biblioteca random y generamos aleatoriamente un numero usando la funcion randint
import random
numero_a_adivinar= random.randint(1, 100)

#inicializamos nuestra variable de intentos restantes en 8

intentos_restantes= 8

for i in range(1, intentos_restantes + 1):
  
#Le pedimos que ingrese un numero
    numero_str= input("Ingresa un numero: ")
    if not numero_str.isdigit():
        print("Lo Que Ingresaste No Es Un Numero. Intenta Otra Vez")
        continue

#Corroboramos que el numero ingresado sea un numero entero
    numero_usuario=int(numero_str)

#comprobamos si el numero ingresado es igual al numero que debia adivinar
  

    if numero_usuario == numero_a_adivinar:
        print("-~"*45)
        print(f"¡¡¡FELICIDADES!!!\n Adivinaste El Numero En {9- intentos_restantes} Intentos.")
        break
    elif numero_usuario < numero_a_adivinar:
        print("El Numero Que Debes Adivinar Es Mayor.")
        print("+"*90)
    else:
        print("El Numero Que Debes Adivinar Es Menor.")
        print("-"*90)

#Descontamos un intento
    intentos_restantes -=1

#infotmamos cuantos intentos le quedan
    print(f"Te Quedan {intentos_restantes} Intentos")
    print("-~"*45)
#si se quedo sin intentos se lo informamos

if intentos_restantes == 0:
    print(f"Parece Que Te Quedaste Sin Intentos.\nEl Numero Que Debias Adivinar Era [{numero_a_adivinar}].")    
    print("#"*90)  

