#Operadores de comparación
"""mi_variabler = "Hola Mundo"
mi_bool = 5+5 == 18-8
mi_bool = "blanco" == "negro"
mi_bool = 5<=5
print(mi_bool)"""
#############################################################################################################################################
#Operadores Lógicos
"""a = 10
b = 5
c = 15
# operador and (y)
#mi_bool = a<b and b<c
#mi_bool = (2*5 == 10 ) and (5*2 == 10)
#mi_bool = (2*5 != 15) and ("perro" == "PerrO".lower())

# Operador Or (O)
texto = "Esta frase es breve"
#mi_bool = 1==10 or 3==30
#mi_bool = ("frase" in texto) or ("python" in texto)

# Operador not

#mi_bool = not "a"=="a"
mi_bool = not ("a" != "a" ) 

print(mi_bool)"""
#############################################################################################################################################
# Control de Flujo (if elif else)

"""if 10>9:
    print("es correcto")"""

"""if(5 == 2):
    print("Es incorrecto")
else:
    print("Es correcto")"""
    

"""mascota = "perro"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perrito")
elif mascota == "pez":
    print("Tu mascota es un escadito")
else:
    print("No sé que animal tienes")"""

"""edad = 16
calificacion = 9

if edad<18:
    print("eres menor de edad")
    if calificacion >=7:
        print("Feliciataciones Aprobado")
    else:
        print("NO aprobado")
else:
    print("eres un adulto")"""

"""num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))


if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
elif num1 == num2:
    print(f"{num1} y {num2} son iguales")"""

"""habla_ingles = True
sabe_python = True

if sabe_python == False:
    if(habla_ingles == False):
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
    elif(habla_ingles == True):
        print("Para postularte, necesitas saber programar en Python")
elif(sabe_python == True):
    if(habla_ingles == False):
        print("Para postularte, necesitas tener conocimientos de inglés")
    elif(habla_ingles == True):
        print("Cumples con los requisitos para postularte")"""

#############################################################################################################################################
# lOOPS
 ## For
 
lista = ["a", "b", "c", "d"]
for letra in lista:
    numero_de_letras = lista.index(letra) + 1
    
    #print(f"Letra: {numero_de_letras}: {letra}")
    
lista2 = ["laura", "luisa", "Marisol", "Monica", "Gladys"]

"""for nombre in lista2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("Nombre que no comienza con L")"""

lista3 = [1,2,3,4,5,6]

mi_valor = 0

for numero in lista3:
    mi_valor = mi_valor+numero

#print(mi_valor)
#iteración en listas
for a,b in [[1,2], [3,4], [5,6]]:
    result = a+b
    #print(a)
    #print(b)

#iteracion en diccionarios
"""dic = {'clave1': 'a', "clave2": "b", "clave3": "c"}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items(): 
    print(a,b)"""
#############################################################################################################################################
#Loop WHile
# monedas = 5

# while monedas>0:
#     print(f"Tengo {monedas} monedas")
#     #monedas = monedas -1
#     monedas -=1
# else: print("No tenbgo más monedas")

respuesta = "s"

"""while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n): ")
else: 
    print("Gracias")"""
    
    
###########################################################################################################################################
#Uso de breack pass y contnue en los loops

#Pass hace que el código no ejuecute el loop y pase a la siguiente funcionalidad
# while respuesta == "s":
#     pass

#Breack hace que el codigo se detenga despues de una iteración
#nombre = input("dime tu nombre: ")

# for letra in nombre:
#     print(letra)
#     if letra == "e":
#         break

#Continue 
# for letra in nombre:
#     print(letra)
#     if letra == "e":
#         continue
    
#numero = 50

# while numero > 0:
#     numero -= 1
#     if numero % 5 == 0:
#         print(numero)
#     else:
#         continue

###########################################################################################################################################
#Rango No recibe integers
"""for numero in range(1, 5):
    print(numero)
    
for numero in range(1, 30, 2):
    print(numero)
    
#lista = list(range(1,101))
#print(lista)"""

############################################################################################################################################
#Enumerador
"""lista = ["A", "B", "C"]

# for item in enumerate(lista):
#     print(item)


for item in enumerate(range(20,35)):
    print(item)
    
mis_tuples = list(enumerate(lista))

print(mis_tuples)"""
############################################################################################################################################
#Zip

nombres = ["Ana", "Hugo", "Valeria"]
edades = [65,29,42]
ciudades = ["Lima", "Bogotá", "México"]

combinados = list(zip(nombres, edades, ciudades))

print(combinados)