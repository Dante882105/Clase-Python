nombre = "Ángel"
print(nombre)

nombre = "Marisol"
print(nombre)

edad = 30
print(edad)

edad2 = 15
print(edad+edad2)

adquirirNombre = input("dime tu nombre")

print("tu nombre es "+adquirirNombre)

#integers and floats

mi_numero = 1 + 3 + 5.8
print(type(mi_numero), mi_numero)

nueva_edad = input("Dime tu edad")

print("tue edad es: "+ nueva_edad)
nueva_edad = int(nueva_edad)

proxima_edad = 1 + nueva_edad

proxima_edad = str(proxima_edad)

print("Cumnpliras: " + proxima_edad, type(proxima_edad) )

#Función Format

x = 10

y = 5

color_auto = "verde"

matricula = 123456

    #Forma 1    
print("mi auto es {} y de matricula {} y sumo los valores de 'x' y 'y' será {}".format(color_auto, matricula, y+x))
    # Forma 2
print(f"Mi auto es {color_auto} y de matricula {matricula} y sumo los valores de 'x' y 'y' será {y+x}")