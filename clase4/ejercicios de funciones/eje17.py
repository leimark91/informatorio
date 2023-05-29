# 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
# parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
# letras pero en distinto orden), o False en caso contrario.

def es_anagrama(cadena1, cadena2):
    # Convertir las cadenas a listas de caracteres
    lista1 = list(cadena1.lower())
    lista2 = list(cadena2.lower())
    
    # Ordenar las listas de caracteres
    lista1.sort()
    lista2.sort()
    
    # Verificar si las listas ordenadas son iguales
    if lista1 == lista2:
        return True
    else:
        return False

cadena1 = "roma"
cadena2 = "amor"
if es_anagrama(cadena1, cadena2):
    print("Las cadenas son anagramas")
else:
    print("Las cadenas no son anagramas")