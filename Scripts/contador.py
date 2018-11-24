import sys

file = open('contador.txt', 'a+')
file.seek(0)
contenido = file.readline()

if len(contenido) == 0:
	contenido = '0'
	file.write(contenido)

file.close()

try:
	contador = int(contenido)

	if len(sys.argv) == 2:
		if sys.argv[1] == 'inc':
			contador += 1
		elif sys.argv[1] == 'dec':
			contador -= 1

	print(contador)

	file = open('contador.txt', 'w')
	file.write(str(contador))
	file.close()
except:
	print('Error: Fichero corrupto')