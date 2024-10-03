from random import choice

lista_numeros = [2,3,4,1,4,5]

def lanzar_moneda():
    resultados = ["Cara", "Cruz"]
    resultado = choice(resultados)
    return resultado

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        lista = []
        return lista
    else:
        print("La lista fue salvada")
        return lista
    
intento = lanzar_moneda()
prueba = probar_suerte(intento, lista_numeros)
print(prueba)