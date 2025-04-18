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

#Localizar caras control
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

#Encuadrar cara con rectangulos
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]), #Posiciones del eje y
              (lugar_cara_A[1], lugar_cara_A[2]), #POsiciones del eje y
              (0,255,0), #COlor rgb en este caso verde
              2
              )

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (255,0,0),
              2
              )

#mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

#mantener el programa abierto
cv2.waitKey(0)