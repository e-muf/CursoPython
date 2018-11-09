class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película', self.titulo)
    
    # Destructor de clase
    def __del__(self):
        print('Se está borrando la pelicula', self.titulo)
        
p = Pelicula('El Padrino', 175, 1972)