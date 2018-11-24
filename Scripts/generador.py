import random
import math

def leer_numero(ini, fin, mensaje):
	numero = int(input(mensaje))
	while numero < ini or numero > fin:
		numero = int(input(mensaje))
	return numero

def generador():
	numeros = leer_numero(1, 20, '¿Cuantos números quieres generar? [1-20]: ')
	modo = leer_numero(1, 3, '¿Como quieres redondaer los números? [1]Al alza [2]A la baja [3]Normal: ') 

	aleatorios = []
	for i in range(numeros):
		numero = random.uniform(0,101)
		if modo == 1: 
			print('{} -> {}'.format(numero, math.ceil(numero)))
			numero = math.ceil(numero)
		elif modo == 2:
			print('{} -> {}'.format(numero, math.floor(numero)))
			numero = math.floor(numero)
		else:
			print('{} -> {}'.format(numero, round(numero)))
			numero = round(numero)
			
		aleatorios.append(numero)

	return aleatorios

generador()
