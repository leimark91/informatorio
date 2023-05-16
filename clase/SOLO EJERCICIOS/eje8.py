##Escribe un programa que calcule el área de un triángulo a partir de la base y la altura dadas.

radio=float(input("Ingrese el radio del circulo: "))

pi = 3.1416
diametro = 2 * radio
circunferencia = 2 * pi * radio

area= pi * (radio**2)

print("EL diametro del circulo es:", diametro)

print("la circunferencia del circulo es:", circunferencia)

print("La circunferencia del circulo:" , area)