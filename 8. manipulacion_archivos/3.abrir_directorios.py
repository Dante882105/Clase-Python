import os #Se usa para interactuar con elementos del sistema operativo
from pathlib import Path 

#ruta = os.getcwd() #obtiene la ruta actual en la que se encuentra el script
'''nueva_ruta = os.chdir("C:\\Users\\DANTE\\OneDrive\\Desktop\\alternativa") #modificar u obtener la ruta de algún archivo según se desee (recuerde que en windows, se debe usar el "\\" para llegar a los directorios o se nos mostrará un error)
archivo = open("texto.txt")'''

#Crear un elemento, sea carpeta o archivos txt, word, etc.
'''crear_ruta = os.makedirs("C:\\Users\\DANTE\\OneDrive\\Desktop\\alternativa\\otra") #usada para crear una nueva carpeta en un directorio'''

#Rutas y elementos dentro de las rutas
'''ruta2 = "C:\\Users\\DANTE\\OneDrive\\Desktop\\Proyectos\\Clase-Python\\8. manipulacion_archivos\\prueba.txt"

elemento = os.path.basename(ruta2) #USando la base de la rutapara mostrar el elemento
ruta_elemento = os.path.dirname(ruta2) #Usando la base para mostrar la carpweta que contiene el elemento
ruta_en_dupla = os.path.split(ruta2) #alamacenar y mostrar los dos elementos, tanto la ruta, como el archivo que se encuentra en la ruta2'''

#Eliminar directorios
'''os.rmdir("C:\\Users\\DANTE\\OneDrive\\Desktop\\alternativa\\otra") # Se requieren permisos de administrador para poder borrar la carpeta en este caso'''

#Abrir archivos sin la necesidad de los diferentes elementos de ruta "\\" o "/", etc.

#carpeta = Path('C:/Users/DANTE/OneDrive/Desktop/alternativa') #Permite que cualquier sistema operativo interprete correctamente la ruta
#archivo = carpeta / "texto.txt"
carpeta2 = Path('C:/Users/DANTE/OneDrive/Desktop/alternativa') / 'texto.txt' #funciona de la misma forma que el ejemplo de arriba

mi_archivo = open(carpeta2)

print(mi_archivo.read())

#print(ruta)
#print(archivo)
'''print(elemento)
print(ruta_elemento)
print(ruta_en_dupla)'''