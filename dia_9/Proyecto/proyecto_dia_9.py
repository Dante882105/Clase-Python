import os
import re
import datetime
import time
from pathlib import Path
import math
#variable que toma el tiempo de inicio
inicio = time.time()

#Priemro definimos la ruta donde se encontrarán las carpetas
ruta = "C:\\Users\\DANTE\\OneDrive\\Desktop\\Proyectos\\Clase-Python\\dia_9\\Proyecto\\documentacion\\proyecto_extraido\\Mi_Gran_Directorio"

#Establecemos la expresión regular te tienen los consecutivos
patron_r = r'N\D{3}-\d{5}'

#Establecemos la fecha del día de la consulta con "now"
hoy = datetime.datetime.today()

#Números encontrados
nmros_encontrados = []

#Archivos encontrados
arch_encontrados = []

#Realizará el proceso de búsquedas
def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto): #Si el valor existe
        return re.search(patron, texto) #realizará la busqueda del patron y texto
    else: #De lo contrario retornará un valor vacio
        return ""

#Creará una lista con los archivos que obtendrá de la consulta
def crear_lista():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta, a), patron_r) #Se ejecuta la busqueda y se alamacena en dicha variable
            if resultado != "":
                nmros_encontrados.append((resultado.group()))
                arch_encontrados.append((a.title()))

def mostrar_todo():
    indice = 0
    print("-" * 50)
    print(f"fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}\n")#para definir el formáto dd/mm/yyyy
    print(f"ARCHIVO\t\t\t NRO. SERIE\n")
    print(f"_______\t\t\t\t __________\n")
    for a in arch_encontrados:
        print(f'{a}\t{nmros_encontrados[indice]}')
        indice += 1  
    print("\n")
    print(f'numeros encontrados: {len(nmros_encontrados)}')
    #variable que toma el finale del proceso
    fin = time.time()
    duracion = fin - inicio #resta de tiempo de inicio y fin
    print(f'Duración de la búsqueda: {math.ceil(duracion)}')
    print("-" * 50)

crear_lista()
mostrar_todo()