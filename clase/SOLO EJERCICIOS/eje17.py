#Escribe un programa que solicite al usuario dos palabras y luego las imprima en orden inverso. 
# Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir"mundo hola". Importante!!! Utiliza un solo print() �


#EJEMPLO 1 DE OTRA FORMA:

# nombre = input ("escriba un saludo y mundo: ")

# letra=nombre [::-1]

# print(f"la palabra {nombre} al reves es {letra}", )

#EJEMPLO 2 DE OTRA FORMA:

 #nombre= input("escriba un saludo y mundo: ")

 #lista=nombre.split()

 #print(lista)

 #lista.reverse()

 #print(lista)

 #texto= " ".join(lista)

 #print(texto)

nombre= input("escriba un saludo y mundo: ")

lista=nombre.split()

lista.reverse()

texto= " ".join(lista)

print(texto)