# 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
# números como parámetro y devuelva la mayor diferencia entre el numero mas
# alto y el numero mas bajo en la lista.

def calcular_mayor_diferencia(lista):
    # Verificar si la lista está vacía
    if len(lista) == 0:
        return None
    
    maximo = max(lista)
    minimo = min(lista)
    
    diferencia = maximo - minimo
    
    return diferencia

numeros = [2, 9, 4, 7, 5, 1]
mayor_diferencia = calcular_mayor_diferencia(numeros)
print("La mayor diferencia es:", mayor_diferencia)