#Funciones
def saludar_persona(nombre):
    """
    Se recomienda dejar este mensaje con la descripción de lo que hace la función, para este ejemplo estoy usando una función que muestra en la consola un saludo
    """
    print(f"Hola {nombre}, cómo te va?")

saludar_persona("Angelito")
#########################################################################################################################################
#Utilizando return
def sumar(numero1, numero2):
    return int(numero1)+int(numero2)

resultado = sumar(8,10)
#print(resultado)

#########################################################################################################################################
#Funciones Dinámicas

def cheqear_3_cifras(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
        
    return lista_3_cifras

resultado = cheqear_3_cifras([550, 99, 600])
#print(resultado)

#########################################################################################################################################
# Interacción de Funciones
from random import shuffle

# Lista inicial de palitos

palitos = ['-', '--', '---', '----']

# Función para mezclar palitos

def mezclar(lista):
    shuffle(lista)
    return lista


# Función para pedir al usuario para elegir un palito
def probar_suerte():
    intento = ''
    while intento not in ["1", "2", "3", "4"]:
        intento = input("ELige un número entre 1 a 4: ")
    return int(intento)

# Función para comprobar el intento
def checar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("A lavar los platos")
    else: 
        print("Esta vez te salvaste")
    
    print(f"Te tocó el {lista[intento-1]}")

#ejecutar la función
palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
checar_intento(palitos_mezclados, seleccion)