#Ejercicio 2
def clasificador_letras(letras):
    conjunto_letras = []
    for letra in letras:
        conjunto_letras.append(letra)
    sin_repetidas = set(conjunto_letras)
    ordenadas = sorted(sin_repetidas)
    return ordenadas

print(clasificador_letras("entretenido"))