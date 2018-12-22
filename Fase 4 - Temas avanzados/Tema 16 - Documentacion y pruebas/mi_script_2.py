def palindromo(palabra):
	'''
	La función palíndromo(palabra) recibe una palabra.
	Si la palabraa es un palíndromo devuelve True, si no False.

	Un palíndromo es ua palabra o frase que se lee igual
	tanto de izquierda a derecha como de derecha a izquierda

	>>> palindromo('radar')
	True

	>>> palindromo('somos')
	True

	>>> palindromo('hola')
	False

	>>> palindromo('Ana')
	True

	>>> palindromo('Atar a la rata')
	True
	'''

	if palabra.lower().replace(' ', '') == palabra[::-1].lower().replace(' ', ''):
		return True
	else:
		return False

if __name__ == '__main__':
	import doctest
	doctest.testmod()