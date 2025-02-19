#Uso de Counter
from collections import Counter
#si deseamos saber cuantas veces se repite un elemento de una lista o un string

numeros = [8,6,4,7,5,9,8,7]
print(Counter(numeros))
#ejemplo con string

print(Counter("misisispi"))

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

#Se puede asignar a una variable
serie = Counter([1,1,1,1,1,1,2,2,2,2,3,3,3,4])

print(serie.most_common())

#Uso de defaultdict
from collections import defaultdict
#En caso de que no existe una clave de un diccionario, defaultdict mostrará el string "nada"
mi_dic = defaultdict(lambda: 'nada')

mi_dic["uno"] = "verde"
print(mi_dic["cuatro"])

#Uso de namedtupple
from collections import namedtuple
#Utilizado para nominar los elementos de las tuplas

Persona = namedtuple('Persona', ["nombre", "altura", "peso"])

ariel = Persona("Ariel", 1.76, 79)

print(ariel.altura)