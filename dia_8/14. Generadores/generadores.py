#Tipo especial de función que genera un valor o un resultado lo según se lo estemos solicitando
'''
#función normal
def function():
    return 4

#función generadora
def mi_generador():
    yield 4 #yield significa generar y se utiliza en lugar del return en Python

print(function())

print(mi_generador()) # No muestra un valor, paa que sea visto se hará de la siguiente forma.
#Se declara una varable que contenga el generador
g = mi_generador()

print(next(g)) # se utiliza la palabra reservada next y en sus parentesis la variable que contiene el generador
'''

#Un ejemplo más difícil será el siguiente:
'''
def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x*10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x*10

print(mi_funcion())

g = mi_generador()

print(next(g))#Se genera según se solicite y por lo tanto no ocupa memoria
print(next(g))
'''

#El último ejemplo será el siguiente:

def mi_generador():
    x = 1
    yield x

    x+=1
    yield x

    x+=1
    yield x

g = mi_generador()

print(next(g))
print(next(g))
print("Hola mundo")
print(next(g))#La función continua sin reiniciarse en la ejecución, es decir; no se interrumpe