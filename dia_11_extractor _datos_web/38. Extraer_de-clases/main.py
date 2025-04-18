#Se importan librerias de scraping (requests) y de arreglo de datos extraidos de la búsqueda (bs4)
import bs4
import requests

#Se extraer el texto del sitio definido por una ur
titulo_sitio = requests.get('https://escueladirecta-blog.blogspot.com/')

#Se arregla el texto con bs4 y su método BeautifullSoup
texto_arreglado = bs4.BeautifulSoup(titulo_sitio.text, 'html')


columna_lateral = texto_arreglado.select('.sidebar-container div')

print(columna_lateral[0])