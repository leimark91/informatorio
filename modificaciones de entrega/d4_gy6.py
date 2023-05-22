#  Requisitos técnicos:
##- Operadores.
##- Estructuras de datos.
##- Estructuras de control de flujo.
##- Funciones

import sqlite3

# Definición de la clase Inmueble
class Inmueble:
    def __init__(self, direccion, tamaño, precio, estado):
        self.direccion = direccion
        self.tamaño = tamaño
        self.precio = precio
        self.estado = estado

    def obtener_precio(self):
        return self.precio

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


# Definición de la clase Inmobiliaria
class Inmobiliaria:
    def __init__(self, db_file):
        self.inmuebles = []
        self.conn = sqlite3.connect(db_file)
        self.crear_tabla()

    def crear_tabla(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS inmuebles
                     (direccion TEXT, tamaño REAL, precio REAL, estado TEXT)''')
        self.conn.commit()

    def agregar_inmueble(self, inmueble):
        self.inmuebles.append(inmueble)
        self.guardar_inmueble_db(inmueble)

    def buscar_inmuebles_disponibles(self):
        return [inmueble for inmueble in self.inmuebles if inmueble.estado == "Disponible"]

    def buscar_inmuebles_por_precio(self, precio_max):
        return [inmueble for inmueble in self.inmuebles if inmueble.precio <= precio_max]

    def guardar_inmueble_db(self, inmueble):
        c = self.conn.cursor()
        c.execute("INSERT INTO inmuebles VALUES (?, ?, ?, ?)",
                  (inmueble.direccion, inmueble.tamaño, inmueble.precio, inmueble.estado))
        self.conn.commit()

    def cargar_inmuebles_db(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM inmuebles")
        rows = c.fetchall()
        for row in rows:
            inmueble = Inmueble(row[0], row[1], row[2], row[3])
            self.inmuebles.append(inmueble)

    def cerrar_conexion(self):
        self.conn.close()


# Ejemplo de uso del sistema
inmobiliaria = Inmobiliaria("inmuebles.db")

# Cargamos los inmuebles desde la base de datos
inmobiliaria.cargar_inmuebles_db()

# Creamos nuevos inmuebles
inmueble1 = Inmueble("Calle A, 123", 100, 200000, "Disponible")
inmueble2 = Inmueble("Calle B, 456", 150, 300000, "Vendido")

# Agregamos los nuevos inmuebles al sistema
inmobiliaria.agregar_inmueble(inmueble1)
inmobiliaria.agregar_inmueble(inmueble2)

# Buscamos los inmuebles disponibles
disponibles = inmobiliaria.buscar_inmuebles_disponibles()
for inmueble in disponibles:
    print(f"Inmueble disponible: {inmueble.direccion} - Precio: {inmueble.precio}")

# Buscamos los inmuebles con un precio máximo
precio_maximo = 250000
resul = inmobiliaria.buscar_inmuebles_por_precio(precio_maximo)
for inmueble in resul:

 print(f"Inmueble dentro del rango de precio:  {inmueble.direccion}")

