def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print("Gracias por sumar")

try:
    #código a probar
    suma()
except TypeError:
    #código a ejecutar si se presentya un error
    print("Estás intentando concatenar tipos distintos")
except ValueError:
    print("Ese no es un número")
else:
    #Código a ejecutar si no hay un error
    print("Hiciste todo bien!")
finally:
    #Código que se va a ejecutar de todos modos
    print("eso fue todo")