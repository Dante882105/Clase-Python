'''from random import choice

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

def registro_error():
    archivo = open("log_errores.txt", "a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()
    data = open("log_errores.txt", "r")
    return data.read()

print(registro_error())'''

class Personaje:
    flechas = 10
    
    def lanzar_flecha(self, flecha):
        self.flechas = self.flechas - flecha
        print(self.flechas)

robin_hood = Personaje()

robin_hood.lanzar_flecha(2)