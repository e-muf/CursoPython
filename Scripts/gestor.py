import pickle

class Personaje:
	def __init__(self, nombre, vida, ataque, defensa, alcance):
		self.nombre = nombre
		self.vida = vida
		self.ataque = ataque
		self.defensa = defensa
		self.alcance = alcance

	def __str__(self):
		return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor():
	personajes = []

	def __init__(self):
		self.cargar()

	def agregar(self, p):
		for pTemp in self.personajes:
			if pTemp.nombre == p.nombre:
				return
		self.personajes.append(p)
		self.guardar()

	def borrar(self, nombre):
		for pTemp in self.personajes:
			if pTemp.nombre == nombre:
				self.personajes.remove(pTemp)
				self.guardar()
				print('\nPersonaje {} borrado'.format(nombre))
				return

	def mostrar(self):
		if len(self.personajes) == 0:
			print('EL gestor esta vacío')
			return
		for p in self.personajes:
			print(p)

	def cargar(self):
		file = open('personajes.pckl', 'ab+')
		file.seek(0)
		try:
			self.personajes = pickle.load(file)
		except:
			pass
		finally:
			file.close()
			print('Se han cargado {} personales'.format(len(self.personajes)))

	def guardar(self):
		file = open('personajes.pckl', 'wb')
		pickle.dump(self.personajes, file)
		file.close()

G = Gestor()
G.agregar(Personaje('Caballero', 4, 2, 4, 2))
G.agregar(Personaje('Guerrero', 2, 4, 2, 4))
G.agregar(Personaje('Arquero', 2, 4, 1, 8))
G.mostrar()
