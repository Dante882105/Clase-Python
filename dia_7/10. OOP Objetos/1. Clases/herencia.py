#Herencia
'''
Se puede dar a una clase hija algunos atributos de la clase padre
    1. Se pueden heredar métodos
    2. se declara la herencia colocando entre parentesis de la clase hijo el nombre de la clase padre "class Hijo(Padre):"
    3. se pueden crear nuevos métodos
    4. Se pueden modificar métodos del elemento padre
'''
'''class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Éste animal ha nacido")
    
    def hablar(self):
        print("este animal emite un sonido")

class Gato(Animal):
    pass

print(Gato.__base__) #Ver de dónde o de qué clase hereda
print(Gato.__subclasses__()) #Indica quién transmite su herencia

garfield = Gato(2, "orange")

garfield.nacer()
print(garfield.color, garfield.edad)'''

#Herencia extendida
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Éste animal ha nacido")
    
    def hablar(self):
        print("este animal emite un sonido")
        
class Pajaro(Animal):

    '''def __init__(self, edad, color, altura_vuelo): #nuevo atributo altura_vuelo
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo'''
    
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color) #Utilizado para no reescribir las propiedades que ya están en la clase Animal
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio pio pio")
    
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros") #Nueco método no heredado

piolin = Pajaro(3, "amarillo", 50)

# ***********************************************************************************************************************************************
# Herencia multiple

class Padre:
    def hablar(self):
        print("Hola nieto jejejeje desde el más allá jejeje")

class Madre:
    def reir(self):
        print("Buen chiste anciano jajajaja")

    def hablar(self):
        print("Hola que hace?")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()
mi_nieto.reir()