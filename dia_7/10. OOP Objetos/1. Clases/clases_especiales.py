'''mi_lista=[1,1,1,1,1,1,1,1,1,1]
print(len(mi_lista))

class Objeto:
    pass

mi_objeto = Objeto()
print(len(mi_objeto))'''

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
#Se pueden acceder a estos métodos especiales y especificar que se desea obtener de dichos métodos
#clase especial de string
    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"
#clase especial de longitud    
    def __len__(self):
        return self.canciones
#clase especial de eliminación    
    def __del__(self):
        print("Se ha eliminado el cd")

mi_cd = CD("floid", "the Wall", 24)

#print(str(mi_cd))
print(mi_cd, len(mi_cd))

#eliminar una instancia, en este caso "mi_cd"
del mi_cd