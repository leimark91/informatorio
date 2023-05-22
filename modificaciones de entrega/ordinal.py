# def  ordinal(num)
#     dic_ordinal={'1':Primero,'2':Segundo,'3':Tercero,'4':Cuarto,'5':Quinto,'6':Sexto,'7':Septimo,'8':Octavo,'9':Noveno,'10':Décimo,'11':Undécimo,'12':duodécimo}
#   	if dic_ordinal.has_key('num'):
# 	print dic_ordinal['num']

# numero=int(input("ingrese un numero entero:"))
# ordi= ordinal(numero)

####################################################################################################################


# def suma(nu1,nu2):
# 	adi = nu1 + nu2
# 	print (adi)
# num1=int(input ('ingrese un numero entero:'))
# num2= int(input ('ingrese un segundo numero entero:'))
# sum= suma(num1,num2)
##############################################################################################################
# # Ejercicio 3

# def invertir_cadena(cadena):
# 	cadena_invertida= cadena [::-1]
# 	print(cadena_invertida)
# palabra = input('ingrese una cadena de caracteres para invertirla:')
# palabra_invertida = invertir_cadena(palabra)
###############################################################################################################
#Ejercicio 4

#-Crea una función llamada es_capicua que tome un número como parámetro y
#devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
#erecha a izquierda) y False en caso contrario.#

# def es_capicua (num):
# 	if  num  == num[::-1]:
# 		print(True)
# 	else:
# 		print (False)
	
# numero=input("ingrese un numero entero:")
# numcap = es_capicua(numero)

#########################################################################################################################################################
# 5-Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.



# def  es_divisible(num1,num2):

# 	if (num1  % num2==0):
# 		print({num1},'es divisible por:', {num2})
	
# 	else:
# 		print( {num1}, 'no es divisible por:',{num2})
	
# nu1=int(input('ingrese un numero entero:'))
# nu2=int(input('ingrese un segundo numero:'))


# divi=es_divisible(nu1,nu2)




##################################################################################################################################################################
def  agregar(lista):
	while True:
	

		inmueble={}
		while True:

			año=int(input('ingrese el año del inmueble:'))
	 
			if año < 2000 :
 	
				print("ha ocurrido un error , introduce bien el año")
			else:
				inmueble['año']=año
			break
	

		while True:
		
			metros=int(input('ingrese los metros que posee el inmueble:'))
	 
			if metros < 60:
			
				print("ha ocurrido un error , introduce bien los metros")

			else: 
				inmueble['Metros']= metros
				break
	
		while True:
		
			habit=int(input('ingrese la cantidad de habitaciones:'))
	 
			if habit < 2:
			
				print("ha ocurrido un error , introduce bien la cantidad de habitaciones")
			else:
				inmueble['habitaciones']=habit
				break
		while True:
		
			gar= input('ingrese posee o no garage,  :')
	 
			if gar =="t"  or gar== "f":
				inmueble['garage']= gar
				break
			else:
				print("ha ocurrido un error , introduce ")
		
		
	
		while True:
		
			zona=input('indique la zona donde se encuentra el inmueble, A,B o C  :')
	 
			if zona== "A" or zona=="B" or zona=="C":
				inmueble['Zona']=zona
				break
		
			else:
				print("ha ocurrido un error , introduce bien la zona A, B,o C")
		while True:
		
			estado=input('ingrese el estado del inmueble Disponible, Vendido o Reservado :')
	 
			if estado == "disponible" or  estado== "vendido" or estado== "reservado":
				inmueble['Estado']=estado
				break
			
		
			else:
				print("ha ocurrido un error , introduce bien el estado del inmueble")




		lista.append(inmueble)
		print(lista)

		cargar= input ("¿desea seguier cargando la lista? s/n, ingrese una opcion:")
		if  cargar=="n":
			break


lista1=[]
agrega=agregar(lista1)





	
	# metros=int(input("ingrese la cantidad de metros que posee el inmueble"))
	# if metros>= 60:
	# 	inmueble['metros']= metros
	# else:
	# 	print("los metros ingresados no son validos, por favor ingrese datos validos")
