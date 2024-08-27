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
print(len(poema))
