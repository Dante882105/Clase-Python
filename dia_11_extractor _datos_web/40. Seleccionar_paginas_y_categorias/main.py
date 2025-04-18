#Se importan librerias de scraping (requests) y de arreglo de datos extraidos de la búsqueda (bs4)
import bs4
import requests

#Se genera el string con la url y unas comillas agregadas en el lugar del número de las páginas por medio del método format de los strings
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

#iteramos las páginas
for pagina in range(1,51):

    #Crear sopa en cada página buscada
    url_pagina = url_base.format(pagina)

    resultado = requests.get(url_pagina)

    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #Seleccionamos por medio de una variable

    libros_seleccionados = sopa.select('.product_pod')

    #iterar en los libros seleccionados
    for libro in libros_seleccionados:
        #Chequear cantidad de estrellas, deben ser entre 4 y 5 estrellas

        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            #guardar título en variable
            titulo_libro = libro.select('a')[1]['title']
            #Se sube el título del libro a la lista vacia denominada titulos rango alto
            titulos_rating_alto.append(titulo_libro)

#Ver libros de cuatro y conco libros en consola
for t in titulos_rating_alto:
    print(t)    