#Ejercicio 1
def devolver_distintos(*args):
    minimo = min(args)
    maximo = max(args) 
    suma = 0
    
    for value in args:
        suma += value
    if suma > 15:
        return maximo
    elif suma < 10:
        return(minimo)
    elif suma >=10 or suma <=15:
        intermediate = suma - (minimo + maximo)
        return intermediate
print(devolver_distintos(2,5,3))