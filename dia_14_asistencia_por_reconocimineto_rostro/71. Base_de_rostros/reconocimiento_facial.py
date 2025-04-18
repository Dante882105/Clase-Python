import cv2
import face_recognition as fr
#Encontrar carpeta
import os

#Crear base de datos
ruta = r'dia_14_asistencia_por_reconocimineto_rostro\71. Base_de_rostros\Empleados'
mis_imagenes = []
nombre_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombre_empleados.append(os.path.splitext(nombre)[0])

print(nombre_empleados)

#codificar imágenes
def codificar(imagenes):
    #crear lista nueva
    lista_codificada = []

    #Transformar las imágenes a rgb
    for image in imagenes:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #codificar
        codificado = fr.face_encodings(image[0])

        #Agregar a la lista
        lista_codificada.append(codificado)

    #Devolver lista codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

print(len(lista_empleados_codificada))