'''import os

print(os.getcwd())

archivo = open('curso.txt', 'w')

archivo.write('texto de prueba')

archivo.close()

print(os.listdir())'''

#mover archivos
'''import shutil

shutil.move('curso.txt', "C:\\Users\\Dante\\OneDrive\\Desktop")'''

#eliminar archivos con send2trash, librería instalada con "pip´install send2trash"
'''import send2trash

send2trash.send2trash('curso.txt')
'''
#método walk
import os

ruta = "C:\\Users\\Dante\\OneDrive\\Desktop\\Proyectos\\Clase-Python\\dia_9"

for carpeta, _subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son:")
    for sub in _subcarpeta:
        print(f"\t{sub}")
    print(f"Los archivos son:")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")