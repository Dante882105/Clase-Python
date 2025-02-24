#Se importa pygame
import pygame

#Se importa ramdom para la posición de los enemigos, que sea aleatorio
import random

#Se importa el método Map para calcular las colisiones
import math

#Se importa herramientas de sonido de la librería de pyegames
from pygame import mixer

#Se inicializa pygame
pygame.init()

#Agregamos la música de fondo
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

#Para crear la pantalla se procede a utilizar el método display y set_mode nos permite definir las dimenciones de la pantalla
pantalla = pygame.display.set_mode((800, 600))

#Título e Ícono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('ovni.png')

pygame.display.set_icon(icono)

#imágen de fondo
img_fondo = pygame.image.load("Fondo.jpg")

#Imágen de protagonista
img_protagonista = pygame.image.load("cohete.png")

#Definimos unas posiciones en x e y para el jugador
jugador_x = 368
jugador_y = 500
jugador_posicion_x = 0

#Se genera una función la cual establecerá la posición en el eje x e y del jugador
def jugador(x, y):
    pantalla.blit(img_protagonista, (x,y))

#Cantidad de enemigos
cantidad_enemigos = 8
#Imágen del enemigo
img_enemigo = []
#Definimos una posición inicial en x e y del enemigo
enemigo_x = []
enemigo_y = []
#Definimos la taza de cambio para modificaciones de posición automática en el eje x e y
enemigo_posicion_x = []
enemigo_posicion_y = []

#Texto final de juego
fuente_final = pygame.font.Font('rafika__.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("FIN DEL JUEGO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))

for e in range(cantidad_enemigos):

    img_enemigo.append(pygame.image.load("enemigo.png"))

    #Definimos una posición inicial en x e y del enemigo
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50, 200))

    print(enemigo_y[e])

    #Definimos la taza de cambio para modificaciones de posición automática en el eje x e y
    enemigo_posicion_x.append(0.1)
    enemigo_posicion_y.append(50)

#Se genera una función la cual establecerá la posición en el eje x e y del enemigo
def enemigo(x, y, enemigo):
    pantalla.blit(img_enemigo[enemigo], (x,y))

#Imágen de la bala
img_bala = pygame.image.load("bala.png")

#Definimos una posición inicial en x e y de la bala
bala_x = 0
bala_y = 500
#Definimos la taza de cambio para modificaciones de posición automática en el eje x e y
bala_posicion_x = 0
bala_posicion_y = 0.8

#visibilidad de la bala
bala_visible = False

def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


#Puntaje
puntaje = 0
fuente = pygame.font.Font('rafika__.ttf', 32)
texto_x = 10
texto_y = 10

def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


#Detectar Colisiones
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1,2))
    if distancia < 27:
        return True
    else: 
        return False

#Loop del juego en true para hacerlo infinito
se_ejecuta = True

while se_ejecuta:

    #pantalla.fill((76, 49, 102)) #Se define así para dar color a la pantalla
    #Para agregar una imágen de fondo, se debe establecer con el método blit y se agrega la imagne alamacenada en la variable y se determina la posición en la pantalla (0(x),0(y))
    pantalla.blit(img_fondo, (0,0))


    for event in pygame.event.get(): #Validación de eventos en pygame por medio de un for
        if event.type == pygame.QUIT: #Se detecta el click en el botón de cerrar de la pantalla
            se_ejecuta = False #Se cambia el valor de dicho valor y se cerrará la ventana creada en pygame

        #Se establece la metodología para los eventos click del teclado   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #Cuando sea la flecha izquierda
                jugador_posicion_x = -1 #disminuye la posición
            if event.key == pygame.K_RIGHT: #Cuando sea la flecha derecha
                jugador_posicion_x = 1 #aumenta la posición
            if event.key == pygame.K_SPACE: #Evento de disparo de la bala
                #Agregar sonido de bala o disparo
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    #Asegurar que la bala sea independiente al movimiento 
                    bala_x = jugador_x                
                    disparar_bala(bala_x, bala_y)

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
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_posicion_x[e]
   
        #Mantener dentro de los bordes de la pantalla al enemigo
        if enemigo_x[e] <= 0:
            enemigo_posicion_x[e] = 0.8
            enemigo_y[e] += enemigo_posicion_y[e]
        elif enemigo_x[e] >= 736:
            enemigo_posicion_x[e] = -0.8
            enemigo_y[e] += enemigo_posicion_y[e]

        #Detectar si hubo colisión
        estado_colision = colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if estado_colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    #Movimiento Bala

    #disparar más de una bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    #ver labala al dispararse
    if bala_visible:
        disparar_bala(jugador_x, bala_y)
        bala_y -= bala_posicion_y

    #Mostrar el puntaje en la pantalla
    mostrar_puntaje(texto_x, texto_y )

    #fin del juego
    for e in range(cantidad_enemigos):
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

    pygame.display.update()#Se actualiza para que tome el color, o imágenes
