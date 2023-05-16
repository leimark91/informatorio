tipo_cambio = 0.84

cantidad_dolares= float(input ("Ingrese la cantidad de dolares: "))
 
cambio= tipo_cambio * cantidad_dolares

print( 
f"""El cambio de dolar a euros es:
Dolar ingresados es {cantidad_dolares}
Euros EU$ {cambio}
"""
)