#Escribe un programa que solicite al usuario su información personal, incluyendo 
# su nombre completo, edad, estatura, peso, dirección y número de teléfono.
# A continuación, el programa deberá imprimir un mensaje con los datos
# ingresados por el usuario en el siguiente formato:
# La información ingresada es la siguiente:
# Nombre completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [dirección]
# Número de teléfono: [número de teléfono]

print("Escriba su formacion personal con sus datos SIGUENTES")


nombre = input ("escriba su nombre completo : " )
edad = input ("escriba su edad : " )
ciudad= input ("escriba su ciudad : ")
estatura= input("escriba su estatura : ")
peso= input("escriba su peso : ")
direccion=input("escriba su direccion : ")
tel=input("escriba su numero de telefono : ")

letra= nombre , edad , ciudad, estatura, peso, direccion, tel,

print(f" La informacion que introjuto usted es:    {nombre}, {edad}, {ciudad}, {estatura}cm, {peso}kg, {direccion}, {tel}" )

