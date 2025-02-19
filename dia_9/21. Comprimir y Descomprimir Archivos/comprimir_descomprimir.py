# SE pueden usar dos módulos integrados a pyton: 1. zipfile y 2. shutil
import zipfile
'''
#Se crea la carpeta y se especifíca que sea de escritura para lamacenar elementos en ella
mi_zip = zipfile.ZipFile("archivo_comprimido.zip", 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()'''

#Descomprimir archivos con zipfile
'''
zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", 'r') #Se deberá hacer con el método lectura "r"

zip_abierto.extractall()

zip_abierto.close()'''

#Comprimir archivos con shutil

import shutil
'''
carpeta_origen = "C:\\Users\\DANTE\\OneDrive\\Desktop\\alternativa" #Se indiica la ruta donde se encunetran los archivos a comprimir

archivo_destino = "comprimido_alternativa" #Se genera un nombre para la carpeta

shutil.make_archive(archivo_destino, 'zip', carpeta_origen) #Se ejecuta el modulo con las tres variables, incluyendo el tipo de carpeta a comprimir que es para este caso 'zip'.'''

#Descomprimir archivos con shutil

shutil.unpack_archive('comprimido_alternativa.zip', 'extraccion_terminada', 'zip')