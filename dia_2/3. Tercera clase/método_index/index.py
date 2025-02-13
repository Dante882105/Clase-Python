#Clase 1
mi_texto = "Esta es una prueba"
#resultado = mi_texto[-5];
#resultado = mi_texto.index("prueba")
#resultado = mi_texto.index("a", 5, 18)
#resultado = mi_texto.rindex("a")



#print(mi_texto.index("o"))
#print(mi_texto[3])

#print(resultado)

######################################################################################################################
#Clase 2

mi_texto2 = "ABCDEFGHIJKLAMÑOPQRSTUVWXYXZ"

#fragmento = mi_texto2[2:] #desde la posición dos hasta el final
#fragmento = mi_texto2[:5] #desde el inicio hasta el caracter anterior a la posicion 5
#fragmento = mi_texto2[2:10:2] #desde el caracter 2 hasta el 10 pero tomando caracteres cada dos caracteres
fragmento = mi_texto2[::-1] #Toma toda la frase y la invierte desde el final hasta el comienzo

print(fragmento)

###########################################################################################################################

#CLase 3

texto = "Este es el texto de Daniel"

#resultado = texto.upper() #COnvertir el texto a Mayúsculas
#resultado = texto[2].upper() #Solo para implementarlo en un índice del texto, para el caso el 2
#resultado = texto.lower() # para la conversión del texto a minúsculas
#resultado = texto.split() #Utilizado para separar el texto en un array o lista
#resultado = texto.split("t") #Separa y no incluye el string que indicamos en un array o lista
'''a= "Aprender"
b= "Python"
c= "es"
d= "genial"
resultado = " ".join([a, b, c, d]) #Utilizado para unir listas o arrays en una variable dejando como separador el espacio '''
#resultado = texto.find("D") #Similar a index pero retorna un -1 cuando no encuentra el string
resultado = texto.replace("Daniel", "Desarrollador")

print(resultado)

#######################################################################################################################################
#clase 4 Propiedades Strings

#inmutabilidad
'''nombre = "Marizol"

nombre[4] = "s"

print(nombre)'''

#Concatenación
'''n1 = "Mari"
n2 = "sol"
print(n1+n2)'''

#Multiplicación
'''n1 = "Mari "
print(n1 * 5)'''

#Salto de linea dentro de la variable
'''poema = """Mil pequeños peces blancos
como si hirvieran
el color del agua
"""
print( "agua" in poema ) #imprime con la condición de que el string "agua" exista'''

#Largo de un string
poema = """Mil pequeños peces blancos
como si hirvieran
el color del agua
"""
#print(len(poema))

#######################################################################################################################################
#clase 5 Listas o Arrays

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f" ]
#Eliminar un elemento
eliminado = mi_lista.pop(1)
#Agregar un elemento
mi_lista2.append("g")
resultado = len(mi_lista)
#print(mi_lista + mi_lista2)
print(mi_lista, eliminado)

#############################################################################################################################################

#Clase 6 Diccionarios u Objetos

diccionario = {"c1":"Valor 1", "c2": "Valor 2"}
resultado = diccionario["c1"]

cliente = {"nombre": "Ángel", "Apellido": "Bernal", "peso": "7900 gr", "talla": 3}
consulta = cliente["Apellido"]

dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}

dic2 = {"c1":["a","b","c"], "c2":["d", "e", "f"]}

dic3 = {1: "a", 2 : "b"}
# agregar un valor
dic3[3] = 'c'
# reemplazar un valor
dic3[2] = "B"

#print(dic["c2"])
#print(dic["c2"][1])
#print(dic["c3"]["s2"])
#print(dic2["c2"][1].upper())
#print(dic3)

#############################################################################################################################################
#Clase 7 Tuples

#mi_tuple = ("Hola", "Mundo", "Developer", "Python")
#mi_tuple2 = "Hola", "Mundo", "Developer", "Python"

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
#Método usado para contar cantidad de veces que aparece un valor
print(mi_tupla.count(2))
#print(type(mi_tuple2))

#############################################################################################################################################
#Clase 8 Sets, se pueden declarar como "set([])" o sin palabra clave y con corchetes "{}", tampoco recibe elementos duplicados y si se hace, Python los descartará

mi_set = set([1,2,3,4,5,6])
#print(type(mi_set), mi_set) 

mi_set2 = {1,2,3,4,5,7,8}
#print(type(mi_set2), mi_set2)

mi_set.add(10)

mi_set2.discard(1)

union = mi_set.union(mi_set2)
print(union)

#############################################################################################################################################
#Clase 9: Booleans

var1 = True
var2 = False

#print(type(var1),var1)

'''number = 5 > 2+3
number2 = bool(5<6)

print(type(number), number)

print(number2)'''

lista = [1,2,3,4]
#control = 5 in lista
control = 5 not in lista

print(type(control), control)
#############################################################################################################################################
