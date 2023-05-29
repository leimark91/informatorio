# 8-Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso contrario.

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    
    # Verificar si la cadena es igual a su reverso
    if cadena == cadena[::-1]:
        return "es palindromo"
    else:
        return "no es palindromo"

resultado = es_palindromo("Anita lava la tina")
print(resultado)
