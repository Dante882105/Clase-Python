#Expresiones regulares para validaciones y demás, se utilizan por medio del módulo re
import re

texto = "Si requieres ayuda, llama al (601) 222 2222 para ayuda en línea"

'''palabra = "ayuda" in texto #Con métodos de los strings

print(palabra)'''

patron = 'ayuda'

busqueda = re.search(patron, texto) #Con expresiones regulares
busqueda2 = re.findall(patron, texto) #Búsqueda de todas las coincidencias exactas

print(busqueda, busqueda.span(), busqueda.start(), busqueda.end())
print(busqueda2, len(busqueda2))

for hallazgo in re.finditer(patron, texto): #iteraciones de búsquedas
    print(hallazgo.span())

#Creación de patrones específicos

texto2 = "Llama al 335-458-5874 justo ahora"

#patron3 = r'\d\d\d-\d\d\d-\d\d\d\d' #re normal
patron3 = r'\d{3}-\d{3}-\d{4}' #re reducido a cantidad de números antes del "-"

resultado = re.search(patron3, texto2)

print(resultado)

#Permitiendo solo si se cumple una condición

clave = input("Clave: ")
patron4 = r'\D{1}\w{7}'

chequear = re.search(patron4, clave)

print(chequear)

#busqueda con o |

mensaje = "NO atendemos los viernes, así que no vengas"

encontrar = re.search(r'lunes|martes', mensaje)

print(encontrar)


def verificar_saludo(frase):
    patron = r'^Hola'
    buscar = re.search(patron, frase)
    print(buscar)
    if buscar != None:
        print("Ok")
    else:
        print("No has saludado")

verificar_saludo("Hola qué tal?")