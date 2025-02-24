#Se importa pygame
import pygame

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

#Definimos unas posiciones en x e y
posicion_x = 368
posicion_y = 536
jugador_posicion_x = 0

#Se genera una función la cual establecerá la posición en el eje x e y
def jugador(x, y):
    pantalla.blit(img_protagonista, (x,y))

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

    #Se modifica la posición
    posicion_x += jugador_posicion_x

    #Mantener dentro de los bordes de la pantalla
    if posicion_x <= 0:
        posicion_x = 0
    elif posicion_x >= 736:
        posicion_x = 736
    jugador(posicion_x, posicion_y)


    pygame.display.update()#Se actualiza para que tome el color, o imágenes
