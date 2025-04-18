import cv2
import face_recognition as fr
#Encontrar carpeta
import os

import numpy as np

#Crear base de datos
ruta = 'Empleados'
mis_imagenes = []
nombre_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(os.path.join(ruta,nombre))
    if imagen_actual is not None:
        mis_imagenes.append(imagen_actual)
        nombre_empleados.append(os.path.splitext(nombre)[0])
    else:
        print(f'Error al leer imagen: {nombre}')


print(nombre_empleados)

#codificar imágenes
def codificar(imagenes):
    #crear lista nueva
    lista_codificada = []

    #Transformar las imágenes a rgb
    for idx, image in enumerate(imagenes):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #codificar
        codificado = fr.face_encodings(image)

        if len(codificado)>0:
            #Agregar a la lista
            lista_codificada.append(codificado[0])
        else: 
            print(f'No se detectó rostro en la imágen de empleados: {nombre_empleados[idx]}')

    #Devolver lista codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

#Tomar una imágen con cámara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#leer la imágen de la cámara
exito, imagen = captura.read()

if not exito:
    print("NO se ha podido tomar la captura")
else:
    #Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    #Codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    #Buscar coindicidencias con rostros guardados en la base de datos
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        print(distancias)
        indice_coincidencia = np.argmin(distancias)
        
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")
        else:
            print("Bienvenido al trabajo")