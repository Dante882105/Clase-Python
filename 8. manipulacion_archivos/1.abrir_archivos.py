'''import os

print("Directorio actual de trabajo:", os.getcwd())'''

mi_archivo = open("prueba.txt")
##ver o leer archivo
#print(mi_archivo.read())

#leer una linea y las demás de forma consecutiva
'''una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea)'''

#Leer todas las lineas
todas_las_lineas = mi_archivo.readlines()

print(todas_las_lineas)






#Cerrar el archivo (buena práctica)
mi_archivo.close()