file = open('personas.txt', 'r', encoding='utf-8')
lines = file.readlines()
file.close()

personas = []
for line in lines:
	campos = line.replace('\n', '').split(';')
	persona = {'id':campos[0], 'nombre':campos[1], 'apellido':campos[2], 'nacimiento':campos[3]}
	personas.append(persona)

for p in personas:
    print("(id={}) {} {} => {} ".format( p['id'], p['nombre'], p['apellido'], p['nacimiento']) )