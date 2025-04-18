import cv2
import face_recognition as fr
import os

print("Ruta actual:", os.getcwd())  # imprime dónde está parado el script
print("Archivo esperado:", os.path.abspath('fotos/FotoA.jpg'))  # imprime la ruta completa esperada


#print("face_recognition version:", fr.__version__)

#cargar imágenes
foto_control = fr.load_image_file(r'C:/Users/DANTE/OneDrive/Desktop/Proyectos/Clase-Python/dia_14_asistencia_por_reconocimineto_rostro/66. Cargar_imagenes/fotos/FotoA.jpg')
foto_prueba = fr.load_image_file(r'C:\Users\DANTE\OneDrive\Desktop\Proyectos\Clase-Python\dia_14_asistencia_por_reconocimineto_rostro\66. Cargar_imagenes\fotos\FotoB.jpg')

#Asegurar el procesamiento de imágenes en RGB
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

#mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

#mantener el programa abierto
cv2.waitKey(0)