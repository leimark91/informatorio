#Escribe un programa que solicite al usuario su peso y su altura, y luego calcule e 
# imprima su índice de masa corporal (IMC). La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

n1 = int(input("Ingrese su peso : ", ))

n2 = int(input("Ingrese su Altura : ", ))


IMC = n1 / (n2 ** 2)



print ("Su masa corporal IMC es" , IMC  )