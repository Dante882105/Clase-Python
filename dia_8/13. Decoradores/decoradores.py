#inicializan con el caracter @ y son funciones que modifican el comportamiento de otras funciones

def decorar_saludo(function): #decorador
    def otra_funcion(palabra):
        print("Hola")
        function(palabra)
        print("Adios")

    return otra_funcion


#@decorar_saludo #Se agrega el decorador precio a la función que se desea decorar
def mayuscula(texto):
    print(texto.upper())


#@decorar_saludo #Se agrega el decorador precio a la función que se desea decorar
def minuscula(texto):
    print(texto.lower())

#Si no se desea activar o no el decorador
mayuscula_decorada = decorar_saludo(mayuscula)

minuscula_decorada = decorar_saludo(minuscula)


minuscula_decorada("PyThOn")

mayuscula_decorada("python")

