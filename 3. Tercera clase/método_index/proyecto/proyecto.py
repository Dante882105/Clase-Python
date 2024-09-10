texto_a_analizar = (input("agrega un texto cualquiera, para ser analizado: ")).lower()
letras_seleccionadas = {"primera letra": "", "segunda letra": "", "tercera letra": ""}

letra1 = input("ingrese la primera letra: ")
letras_seleccionadas["primera letra"] = letra1.lower()
letra2 = input("ingresa la segunda letra: ")
letras_seleccionadas["segunda letra"] = letra2.lower()
letra3 = input("ingrese la tercera letra: ")
letras_seleccionadas["tercera letra"] = letra3.lower()

leter1 = texto_a_analizar.count(letras_seleccionadas["primera letra"])
leter2 = texto_a_analizar.count(letras_seleccionadas["segunda letra"])
leter3 = texto_a_analizar.count(letras_seleccionadas["tercera letra"])

cantidad_de_palabras = texto_a_analizar.split()
numero_palabras = len(cantidad_de_palabras)

letra_inicial = texto_a_analizar[0]
letra_final = texto_a_analizar[-1]

invertir_frase = cantidad_de_palabras[::-1]
frase_invertida = " ".join(invertir_frase)

frase = "python"
#validacion = frase in cantidad_de_palabras

if frase in cantidad_de_palabras:
    validacion = "Si se encuentra en el texto"
else:
    validacion = "No existe la palabra en el texto"



print(f"La cantidad de veces que aparece la letra {letras_seleccionadas['primera letra']}, {letras_seleccionadas['segunda letra']} y {letras_seleccionadas['tercera letra']} es la siguiente: {leter1, leter2, leter3}.\n La cantidad de palabras en el texto es la siguiente: {numero_palabras}.\n La letra inicial es {letra_inicial} y la final es {letra_final}.\n La frase invertida es {frase_invertida}.\n La búsqueda de la frase 'Python' da como resultado que {validacion}.")