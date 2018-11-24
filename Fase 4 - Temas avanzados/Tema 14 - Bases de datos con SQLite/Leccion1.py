import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

# cursor.execute("CREATE TABLE usuario(nombre VARCHAR(100), edad INTEGER, email VARCH AR(100))")
#cursor.execute("INSERT INTO usuario VALUES('Emanuel', 22, 'emanuel@ejemplo.com')")

# cursor.execute('SELECT * FROM usuario')
# usuario = cursor.fetchone()
# print(usuario)

#usuarios = [
#	('Mario', 51, 'mario@ejemplo.com'),
#	('Ojos', 22, 'ojos@ejemplo.com'),
#	('Baljeet', 33, 'baljeet@ejemplo.com'),
#]

#cursor.executemany('INSERT INTO usuario VALUES (?, ?, ?)', usuarios)

cursor.execute('SELECT * FROM usuario')

usuarios = cursor.fetchall()

for usuario in usuarios:
	print('Nombre: ' + usuario[0], "- Email: " + usuario[2])

conexion.commit()
conexion.close()