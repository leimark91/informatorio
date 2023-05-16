# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato dd/mm/aaaa y luego imprima su edad en años.
# utiliza la funcion split()

nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")
dia, mes, anio = nacimiento.split("/")

edad = 2023 - int(anio)
print(f"Tenes {edad} años")

 # manera 1 de imprimir
