# 19-Escribe un programa que solicite al usuario un número decimal y luego
# imprima la parte entera y decimal por separado. 


numero_decimal = float(input("Ingresa un número decimal: "))

parte_entera = int(numero_decimal)
parte_decimal = numero_decimal - parte_entera

print("La parte entera del número es:", parte_entera)
print("La parte decimal del número es:", parte_decimal)