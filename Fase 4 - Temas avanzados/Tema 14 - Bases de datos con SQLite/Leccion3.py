import sqlite3

conexion = sqlite3.connect('usuarios_autoincremental.db')
cursor = conexion.cursor()

#cursor.execute('SELECT * FROM usuario WHERE edad=22')

#usuarios = cursor.fetchall()
#print(usuarios)

#cursor.execute('UPDATE usuario SET nombre="Emanuel Flores", edad=23 WHERE dni="11111111A"')

cursor.execute('DELETE FROM usuario WHERE dni="11111111A"')

conexion.commit()
conexion.close()