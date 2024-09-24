from random import randint

intentos = 1

numero_a_adivinar = randint(0,101)

nombre_usuario = input("¿Dime cuál es tu nombre?: ")

print((f"Bueno {nombre_usuario}, he pensado en un número de 0 a 100, y tienes solo ocho intentos para adivinar cuál crees que es el número”. "))
numero_usuario = int(input("Dime un número y te diré si es o no el número que tengo en mente: "))

while intentos < 8:
    if numero_usuario < 1 or numero_usuario > 100:
        numero_usuario = int(input("Elegiste un número no permitido, vuelve a intentarlo: "))
        intentos+=1
    elif numero_usuario < numero_a_adivinar:
        numero_usuario = int(input("El número que escogiste es menor al número que pense: "))
        intentos+=1
    elif numero_usuario > numero_a_adivinar:
        numero_usuario = int(input("El número que escogiste es mayor al número que pense: "))
        intentos+=1
    elif numero_usuario == numero_a_adivinar:
        print(f"¡Muy Bien!, {numero_a_adivinar} era el número que pense, haz adivinado en {intentos} intentos")
        break   
if numero_usuario != numero_a_adivinar:
    print(f"Perdiste, perdiste das lástima mi amor, el número a adivinar era el {numero_a_adivinar}")