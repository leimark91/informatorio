# 13-Crea una función llamada calcular_descuento que tome dos parámetros:
# precio y porcentaje_descuento. La función debe calcular y devolver el precio después de aplicar el descuento.

def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_con_descuento = precio - descuento
    return precio_con_descuento

precio = 100
porcentaje_descuento = 20
precio_con_descuento = calcular_descuento(precio, porcentaje_descuento)
print(precio_con_descuento)
