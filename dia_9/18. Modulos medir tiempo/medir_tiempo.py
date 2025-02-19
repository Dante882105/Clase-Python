#para medir el tiempo de x o y función o método de procesamiento, usamos time aunque el problema radica en que procesos muy cortos pueden no ser medidos por dicho módulo
'''import time

def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

#Para evidenciar el tiempo se deberá invocar la función entre dos medidores de tiempo que para el caso son "inicio" y "fin"
inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final-inicio)

inicio = time.time()
prueba_for(1000000)
final = time.time()
print(final-inicio)'''

#Para ejecuciones con tiempos más pequeños, usamos timeit
import timeit


declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero+1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number = 1000000) #Se especifican declaración, setup y número de veces a repetir el código para medir tiempo

print(duracion)

declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2, mi_setup2, number = 1000000) #Se especifican declaración, setup y número de veces a repetir el código para medir tiempo

print(duracion2)