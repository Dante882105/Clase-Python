#Se importan las librerías, en mi caso molesto el proceso de importación y debí hacerlo de esa forma

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from numeros_py import numeros

#Se genera la función generar_turno, la cual realiza el loop de pregunta sobre el área a reservar turno 

def generar_turno():

    print("Hola, Bienveniod@ A la famracia 'Mata Sanos', sigue las indicaciones del programa.\n")
#Bucle infinito para ralizar la petición de turnos a numeros.mensaje_decorado


    while True:
        try:
            categoria = input("Por favor ingrese la sigla de la sección a la que desea ingresar:\nFarmacia(F), Perfumería (P), Cosméticos (C) o salir del programa (S). ").strip().lower()
#Se indica el error en caso de no contar con cadenas de texto las cuales correspondan a "f", "p", "c", "s"
            if categoria not in ["f", "p", "c", "s"]:
                raise ValueError("Entrada inválida")  # Lanza un error si no es válida
#Se muestra un mensaje en caso de un error generado
        except ValueError:
            print("\n¡Recuerde que solo deberá ingresar las siglas anteriormente mencionadas!\n")
            continue
#Se procede a solictar el turno al módulo creado con el decorador
        else:
            if categoria == "s":
                print("\nFue un placer atenderte,\nFelíz resto de día.\n")
                break
            else:
                numeros.mensaje_decorado(categoria)
#Se llama la función
generar_turno()