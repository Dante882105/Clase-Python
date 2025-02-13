import random

vidas = 6
letras_acertadas = []
letras_no_acertadas = []

palabras = ["hipopotamo", "correspondiente", "parangaricutirimicuaro", "esternocleidomastoideo", 
"sorpresivamente"]

def seleccionar_palabra(palabras):
    palabra = random.choice(palabras)
    return palabra

def ocultar_letras(word):
    palabra = []
    for w in word:
        palabra.append("_")
    return palabra

def mostrar_letras(letra_seleccionada):
    i = -1
    for p in palabra_seleccionada:
        i += 1
        if p == letra_seleccionada:
            palabra_oculta[i] = p

def validar_estado_letras():
    encontrada = palabra_oculta.count("_")
    if encontrada > 0:
        return False
    else:
        return True

palabra_seleccionada = seleccionar_palabra(palabras)

palabra_oculta = ocultar_letras(palabra_seleccionada)

letras_encontradas = validar_estado_letras()

#Método para la búsqueda de letras vs la palabra oculta
while vidas > 0 and letras_encontradas == False:
    print(f"Vidas: {vidas}")
    print(palabra_oculta)
    letra = input("Ingrese una letra: ").lower()

    while len(letra)>1 or len(letra)<1:
        letra = input("Ingrese solamente una letra: ").lower()

    for letras in palabra_seleccionada:
        if letra == letras:
            letras_acertadas.append(letra)
            mostrar_letras(letra)
            print("Excelente, la letra se encuentra en la palabra a encontrar")
            letras_encontradas = validar_estado_letras()
            break
    else:
        letras_no_acertadas.append(letra)
        print(letras_no_acertadas)
        vidas-=1
        print (f"¡Upsss. Perdiste una vida por menso!")
else:
    if letras_encontradas == True:
        print(f"Encontraste la palabra oculta {palabra_oculta} y te quedaban {vidas} vidas")
    elif vidas == 0:
        print(f"Ya no te quedan vidas amigo y la palabra era {palabra_seleccionada}")