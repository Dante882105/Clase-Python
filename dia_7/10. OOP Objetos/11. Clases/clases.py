#Crear clases y objetos
'''class Pajaro:
    pass
    
mi_pajaro = Pajaro()
otro_pajaro = Pajaro()'''

#Atributos
#Atributos de instancia
'''class Pajaro:
    alas = True #Ahora el campo alas es obligatorio

    def __init__(self, color, especie): #constructor y cada una de sus instancias o propiedades
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('black', "Loro")

print(f"mi pajaro es {mi_pajaro.especie} y su color es  {mi_pajaro.color}")
print(Pajaro.alas)

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)

print(f"{casa_blanca.color}, {casa_blanca.cantidad_pisos}")

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")
print(cubo_rojo.caras)'''

#Métodos para una clase

'''class Pajaro:
    def __init__(self, color, especie): #constructor y cada una de sus instancias o propiedades
        self.color = color
        self.especie = especie

    #Un método se genera con el nombre que deseemos y entre paréntesis "self" para que tome al propio objeto y le integre el método    
    def piar(self):
        print("pio pio pio, y mi color es {}".format(self.color))
    
    def volar(self, metros):
        print(f"Vuela {metros} mts")

piolin = Pajaro('amarillo', "canario")'''

#piolin.piar()
#piolin.volar(4)

#Decoradores
class Pajaro:

    alas = True

    def __init__(self, color, especie): #constructor y cada una de sus instancias o propiedades
        self.color = color
        self.especie = especie

    '''Los métodos de instancia son aquellos que: 
        1. Permiten acceder a otros métodos
        2. Modifican el estado de las clases
        3. Accede y modifica atributos del objeto  
        '''
    def piar(self):
        print("pio pio pio, y mi color es {}".format(self.color))
    
    def volar(self, metros):
        print(f"Vuela {metros} mts")
        self.piar()
    
    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pájaro es {self.color}")

    '''Métodos de clase son:
        1. delcarados con el decorador @classmethod
        2. en el interior de la función, se indica que es una clase al definirla como "cls"
        3. No puede acceder a métodos de intancia
        4. Puede modificar los atributos de la clase
    '''
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
    
    '''Métodos Estáticos son:
        1. No pueden modificar el estado de una instancia
        2. No puede modificar los atributos de una clase 
    '''
    @staticmethod
    def mirar():
        print("El pájaro mira!")

'''Pajaro.poner_huevos(3)
print(Pajaro.alas)
#Pajaro.piar()

Pajaro.mirar()'''

'''piolin = Pajaro('amarillo', "canario")
piolin.poner_huevos(20)
piolin.pintar_negro()
piolin.volar(50)
piolin.alas = False
print(piolin.alas)'''
