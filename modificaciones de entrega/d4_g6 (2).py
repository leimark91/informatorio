# Lista de inmuebles

lista_inmuebles = [
    {'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},
    {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},
    {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},
    {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},
    {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}
]

# Función para mostrar el menú y obtener la opción del usuario

def mostrar_menu():
    print('--- Menú ---')

    print("\n")
    print('1. Agregar inmueble')
    print("\n")
    print('2. Editar inmueble')
    print("\n")
    print('3. Eliminar inmueble')
    print("\n")
    print('4. Cambiar estado de inmueble')
    print("\n")
    print('5. Buscar inmuebles según presupuesto')
    print("\n")
    print('6. Mostrar lista de inmuebles')
    print("\n")
    print('7. Salir')
    opcion = input('Ingrese el número de la opción deseada: ')
    return opcion

# Funcion para calcular el precio de un inmueble

def calcular_precio(inmueble):
    precio_base = inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500
    antiguedad = 2023 - inmueble['año']
    zona_factor = {'A': 1, 'B': 1.5, 'C': 2}
    precio = precio_base * (1 - antiguedad / 100) * zona_factor[inmueble['zona']]
    return precio

# Funcion para agregar inmueble, y vadilacion si  cumple con los requisitos

def agregar_inmueble(lista_inmuebles, inmueble):
    if inmueble['zona'] in ('A', 'B', 'C') and inmueble['estado'] in ('Disponible', 'Reservado', 'Vendido'):
        if inmueble['año'] >= 2000 and inmueble['metros'] >= 60 and inmueble['habitaciones'] >= 2:
            lista_inmuebles.append(inmueble)
            print('Inmueble agregado correctamente.')
        else:
            print('El inmueble no cumple con las reglas de validación.')
    else:
        print('El inmueble no cumple con las reglas de validación.')

# Funcion para editar inmueble

def editar_inmueble(lista_inmuebles, indice, nuevos_datos):
    if indice >= 0 and indice < len(lista_inmuebles):
        inmueble = lista_inmuebles[indice]
        for clave, valor in nuevos_datos.items():
            if clave in inmueble:
                inmueble[clave] = valor
        print('Inmueble editado correctamente.')
    else:
        print('Índice de inmueble inválido.')

# Funcion para eleminiar un inmueble

def eliminar_inmueble(lista_inmuebles, indice):
    if indice >= 0 and indice < len(lista_inmuebles):
        del lista_inmuebles[indice]
        print('Inmueble eliminado correctamente.')
    else:
        print('Índice de inmueble inválido.')

# Funcion para cambiar estado del inmueble

def cambiar_estado(inmueble, nuevo_estado):
    if nuevo_estado in ('Disponible', 'Reservado', 'Vendido'):
        inmueble['estado'] = nuevo_estado
        print('Estado del inmueble cambiado correctamente.')
    else:
        print('Estado inválido.')

# Funcion para buscar inmuebles segun presupuesto

def buscar_inmuebles(lista_inmuebles, presupuesto):
    inmuebles_encontrados = []
    for inmueble in lista_inmuebles:
        if inmueble['estado'] in ('Disponible', 'Reservado'):
            precio = calcular_precio(inmueble)
            if precio <= presupuesto:
                inmueble_con_precio = inmueble.copy()
                inmueble_con_precio['precio'] = precio
                inmuebles_encontrados.append(inmueble_con_precio)

    if not inmuebles_encontrados:
        print('No se encontraron inmuebles con el presupuesto dado.')
    return inmuebles_encontrados


# Funcion para mostrar inmuebles

def imprimir_inmuebles(lista_inmuebles):
    for i, inmueble in enumerate(lista_inmuebles):
        print(f'Inmueble {i}:')
        for clave, valor in inmueble.items():
            print(f'{clave}: {valor}')
        print()

# Mostrar menu atravez de su funcion

opcion = mostrar_menu()

while opcion != '7':
    if opcion == '1':
        print("/" * 90, "\n")

        nuevo_inmueble = {
            'año': int(input('Año: ')),
            'metros': int(input('Metros: ')),
            'habitaciones': int(input('Habitaciones: ')),
            'garaje': input('Garaje (S/N): ').upper() == 'S',
            'zona': input('Zona (A/B/C): ').upper(),
            'estado': input('Estado (Disponible/Reservado/Vendido): ')
        }
        agregar_inmueble(lista_inmuebles, nuevo_inmueble)

        print("/" * 90, "\n")

    elif opcion == '2':
        print("/" * 90, "\n")

        indice = int(input('Índice del inmueble a editar: '))
        nuevos_datos = {
            'año': int(input('Nuevo año: ')),
            'metros': int(input('Nuevos metros: ')),
            'habitaciones': int(input('Nuevas habitaciones: ')),
            'garaje': input('Nuevo garaje (S/N): ').upper() == 'S',
            'zona': input('Nueva zona (A/B/C): ').upper(),
            'estado': input('Nuevo estado (Disponible/Reservado/Vendido): ')
        }
        editar_inmueble(lista_inmuebles, indice, nuevos_datos)

        print("/" * 90, "\n")

    elif opcion == '3':
        print("/" * 90, "\n")

        indice = int(input('Índice del inmueble a eliminar: '))
        eliminar_inmueble(lista_inmuebles, indice)

        print("/" * 90, "\n")

    elif opcion == '4':
        print("/" * 90, "\n")

        indice = int(input('Índice del inmueble a cambiar de estado: '))
        nuevo_estado = input('Nuevo estado (Disponible/Reservado/Vendido): ')
        cambiar_estado(lista_inmuebles[indice], nuevo_estado)

        print("/" * 90, "\n")

    elif opcion == '5':
        print("/" * 90, "\n")

        presupuesto = float(input('Presupuesto máximo: '))
        inmuebles_encontrados = buscar_inmuebles(lista_inmuebles, presupuesto)
        imprimir_inmuebles(inmuebles_encontrados)

        print("/" * 90, "\n")

    elif opcion == '6':
        

        imprimir_inmuebles(lista_inmuebles)

        print("/" * 90, "\n")
    

    else:
        print('Opción inválida. Por favor, ingrese un número del 1 al 7.')


    opcion = mostrar_menu()

print('¡Hasta luego!')

#Integrantes G6:
# Lucas Matias Almiron
# Mauricio Acevedo
# Gustavo Medina
# Alfonzo Luis Andres
# Omar Alejandro Maciel
# Federico Peralta
# Matias Martin Satina
# Rodolfo Sanchez
# Luis Marcos Antonio Leiva