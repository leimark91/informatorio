#Desafío 1: Trabajas en una empresa X donde sus vendedores cobran comisiones del 6% de
# sus ventas totales y el departamento comercial te solicita que ayudes a los
# vendedores a calcular sus comisiones creando un programa que les pregunte su nombre y cuánto han vendido en éste mes.
# Tu programa le va a responder con una frase que incluya su nombre y el monto que le corresponde por las comisiones

#CONSULTORIA A MI EMPRESA.


# print("ingrese su nombre")

# nombre=float(input())

print ("ingrese el porciento que gana : ")

porcentaje=float (input())

print ("ingrese cuanto vendio este mes: ")

numero=float(input())

resultado =  porcentaje* numero/ 100 


print(f"El su % es igual a : ", { resultado })