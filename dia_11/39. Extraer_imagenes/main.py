#Se importan librerias de scraping (requests) y de arreglo de datos extraidos de la búsqueda (bs4)
import bs4
import requests

#Se extraer el texto del sitio definido por una ur
titulo_sitio = requests.get('https://www.escueladirecta.com/l/products')

#Se arregla el texto con bs4 y su método BeautifullSoup
sopa = bs4.BeautifulSoup(titulo_sitio.text, 'html')

#buscamos la imagen de ser posible por una clase o un id
imagenes = sopa.select('.object-cover')

#Se guarda la imagen y se captura el src de la misma para descargarla más adelante
imagen_curso = requests.get(imagenes[0]['src'])

#Se crea un archivo con la terminación 'wb'(write binary) para tomar el archivo, se le especifica un nombre y el tipo de archivo que debe ser igual al del sitio web
f = open('mi_imagen.jpg', 'wb')

#Se genera el archivo con el texto binario
f.write(imagen_curso.content)

#Se cierra el archivo como buena práctica
f.close()