import sqlite3

#conexion = sqlite3.connect('usuarios.db')
#cursor = conexion.cursor()


#cursor.execute('''
#	CREATE TABLE usuario (
#		dni VARCHAR(9) PRIMARY KEY,
#		nombre VARCHAR(50),
#		edad INTEGER,
#		email VARCHAR(50)
#	)
#	''')

#usuarios = [
#	('11111111A', 'Emanuel', 22, 'emanuel@ejemplo.com'),
#	('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
#	('33333333C', 'Ojos', 22, 'ojos@ejemplo.com'),
#	('44444444D', 'Baljeet', 33, 'baljeet@ejemplo.com'),
#]

# cursor.executemany('INSERT INTO usuario VALUES (?, ?, ?, ?)', usuarios)

#cursor.execute('''
#	CREATE TABLE producto (
#		id INTEGER PRIMARY KEY AUTOINCREMENT,
#		nombre VARCHAR(50) NOT NULL,
#		marca VARCHAR(50) NOT NULL,
#		precio FLOAT NOT NULL
#	)
#''')

#productos = [
#	('Teclado', 'Logitech', 18.95),
#	('Pantalla 19"', 'LG', 89.95)
#]

#cursor.executemany('INSERT INTO producto VALUES(null, ?, ?, ?)', productos)

#cursor.execute('SELECT * FROM producto')

#productos = cursor.fetchall()
#for producto in productos:
#	print(producto)

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

cursor.execute('''
	CREATE TABLE usuario (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		dni VARCHAR(9) UNIQUE,
		nombre VARCHAR(50),
		edad INTEGER,
		email VARCHAR(50)
	)
	''')

usuarios = [
	('11111111A', 'Emanuel', 22, 'emanuel@ejemplo.com'),
	('22222222B', 'Mario', 51, 'mario@ejemplo.com'),
	('33333333C', 'Ojos', 22, 'ojos@ejemplo.com'),
	('44444444D', 'Baljeet', 33, 'baljeet@ejemplo.com'),
]

cursor.executemany('INSERT INTO usuario VALUES (null, ?, ?, ?, ?)', usuarios)

conexion.commit()
conexion.close()