'''#Poliformismo

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Muuuu!")

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " Beeee!")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

animales = [vaca1, oveja1]

#se pueden iterar al ser diferentes clases pero con un método llamado exactamente igual en ellas
for animal in animales:
    animal.hablar()

#se puede crear una función o un método ue interactue con los métodos de las clases
def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca1)'''
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

arquero = Arquero()
mago = Mago()
samurai = Samurai()
        
personajes = [arquero, mago, samurai]

for personaje in personajes:
    personaje.atacar()