import sqlite3

def crear_bd():
	conexion = sqlite3.connect('restaurante.db')
	cursor = conexion.cursor()
	try:
		cursor.execute('''
			CREATE TABLE categoria (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL
			)
			''')

		cursor.execute('''
			CREATE TABLE plato (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				nombre VARCHAR(100) UNIQUE NOT NULL,
				categoria_id INTEGER NOT NULL,
				FOREIGN KEY (categoria_id) REFERENCES categoria(id)
			)
			''')

		print('[+] Se ha creado la base correctamente.')
	except:
		print('[-] Error al crear la base.')
	finally:
		conexion.commit()
		conexion.close()

def agregar_categoria():
	nombre = input('Ingresa el nombre de la categoría: ')

	conexion = sqlite3.connect('restaurante.db')
	cursor = conexion.cursor()

	try:
		cursor.execute('INSERT INTO categoria VALUES (null, "{}")'.format(nombre))
		print('[+] Se ha agregado la categoría correctamente')
	except:
		print('[-] No se ha agregado la categoría')
	finally:
		conexion.commit()
		conexion.close()

def agregar_plato():
	conexion = sqlite3.connect('restaurante.db')
	cursor = conexion.cursor()

	try:
		cursor.execute('SELECT nombre FROM categoria')
		categorias = cursor.fetchall()
		

crear_bd()

while True:
	opcion = int(input('Seleccione una opción:\n1. Crear categoría\n2. Salir\n>> '))

	if opcion == 1:
		agregar_categoria()
			
	if opcion == 2:
		print('Hasta luego')
		break

