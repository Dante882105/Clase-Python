#Se importa pygame
import pygame

#Se importa ramdom para la posición de los enemigos, que sea aleatorio
import random

#Se inicializa pygame
pygame.init()

#Para crear la pantalla se procede a utilizar el método display y set_mode nos permite definir las dimenciones de la pantalla
pantalla = pygame.display.set_mode((800, 600))

#Título e Ícono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('ovni.png')

pygame.display.set_icon(icono)

#Imágen de protagonista
img_protagonista = pygame.image.load("cohete.png")

#Definimos unas posiciones en x e y para el jugador
jugador_x = 368
jugador_y = 500
jugador_posicion_x = 0

#Se genera una función la cual establecerá la posición en el eje x e y del jugador
def jugador(x, y):
    pantalla.blit(img_protagonista, (x,y))

#Imágen del enemigo
img_enemigo = pygame.image.load("enemigo.png")

#Definimos una posición inicial en x e y del enemigo
enemigo_x = random.randint(0,736)
enemigo_y = random.randint(50, 200)
#Definimos la taza de cambio para modificaciones de posición automática en el eje x e y
enemigo_posicion_x = 0.30
enemigo_posicion_y = 50

#Se genera una función la cual establecerá la posición en el eje x e y del enemigo
def enemigo(x, y):
    pantalla.blit(img_enemigo, (x,y))

#Loop del juego en true para hacerlo infinito
se_ejecuta = True

while se_ejecuta:

    pantalla.fill((76, 49, 102)) #Se define así para dar color a la pantalla



    for event in pygame.event.get(): #Validación de eventos en pygame por medio de un for
        if event.type == pygame.QUIT: #Se detecta el click en el botón de cerrar de la pantalla
            se_ejecuta = False #Se cambia el valor de dicho valor y se cerrará la ventana creada en pygame

        #Se establece la metodología para los eventos click del teclado   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #Cuando sea la flecha izquierda
                jugador_posicion_x = -0.3 #disminuye la posición
            if event.key == pygame.K_RIGHT: #Cuando sea la flecha derecha
                jugador_posicion_x = 0.3 #aumenta la posición

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador_posicion_x = 0

    #Se modifica la posición jugador
    jugador_x += jugador_posicion_x

    #Mantener dentro de los bordes de la pantalla al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736
    jugador(jugador_x, jugador_y)

    
    #Se modifica la posición enemigo
    enemigo_x += enemigo_posicion_x
   

    #Mantener dentro de los bordes de la pantalla al enemigo
    if enemigo_x <= 0:
        enemigo_posicion_x = 0.3
        enemigo_y += enemigo_posicion_y
    elif enemigo_x >= 736:
        enemigo_posicion_x = -0.3
        enemigo_y += enemigo_posicion_y
    enemigo(enemigo_x, enemigo_y)


    pygame.display.update()#Se actualiza para que tome el color, o imágenes
