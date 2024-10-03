#Para poder enviar una cantidad no especidicada de argumentos a una función sin definirlos en la misma se usa args y kwargs
#1. *args (se puede hacer con cualquier palabra siempre y cuando lleve previamente el asterisco, *gatos, *perros, etc.)

"""def suma(a,b):
    return a + b
"""
def suma(*args):
    """total = 0
    for arg in args:
        total += arg
    return total""" 
    return sum(args)

#print(suma(5, 6, 7, 8, 25))
##########################################################################################################################

#2. **kwargs (Usado en diccionarios)

def otra_suma(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

otra_suma(x=1, y=2, z=3)