'''
Se deberá instalar las siguientes librerías
# pyttsx3 Permite que interactuemos verbalmente con el programa python
# SpeechRecognition Permite que el programa reconozca la voz del usuario
# pywhatkit Permite abrir sitios web (youtube, wikipedia, etc)
# yfinance Permite verificar el precio de acciones y demás de la bolsa
# pyjokes Permite que el asistente cuente bromas
'''
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pyjokes
import webbrowser
import datetime
import wikipedia

opt1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
opt2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# Escuchará el microfono y devolverá el audio como texto.
def transformar_audio_en_texto():
    #Alamacvenar el reconocedor en una variable
    r= sr.Recognizer()

    #Configurar el microfono y lo renombramos como origen
    with sr.Microphone() as origen:

        #tiempo de espera en el microfono 0.8 segundos
        r.pause_threshold = 0.8

        #Informar que empezó la grabación para testear enl funcionamiento de la aplicación
        print("Ya puedes hablar")

        #Creamos una variable que guarde lo que escuche el audio en el microfono llamado origen
        audio = r.listen(origen)

        #Manejar posibles errores

        try: 
        #Buscar en google lo que escuche en el microfono
            solicitud = r.recognize_google(audio, language="es-AR")

            #Prueba de funcionamiento
            print("Dijiste: "+ solicitud )

            return solicitud
        
        except sr.UnknownValueError:
            #Prueba de que no comprendi el audio
            print("Upss, no entendí")

            #Devolver error
            return "Sigo esperando"
        
        except sr.Request:
            #Prueba de que no comprendi el audio
            print("Upss, no hay servicio")

            #Devolver error
            return "Sigo esperando"
        
        except:
            #Prueba de que no comprendi el audio
            print("Upss, algo salió mal")

            #Devolver error
            return "Sigo esperando"

#función para que el asistente pueda hablar
def hablar(mensaje):
    #Encender e motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', opt1)

    #Pronunciar mensaje
    engine.say(mensaje)
    #Ejecuta y espera
    engine.runAndWait()

#Función para informar el dia de la semana
def pedir_dia():

    #Crear variable con los datos del día de hoy
    dia = datetime.date.today()
    print(dia)

    #Crear una variable que nos indique el día de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #Creamos un diccionario con los días de la semana
    calendario = {
        0: 'lunes',
        1: 'martes',
        2: 'miércoles',
        3: 'jueves',
        4: 'viernes',
        5: 'sábado',
        6: 'domingo'
    }

    #decir día de la semana
    hablar(f'hoy es {calendario[dia_semana]}')

#Función para pedir la hora al asistente
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    #Decir la hora
    hablar(hora)


#hablar("¡Papito rico. que bello estás!")
#transformar_audio_en_texto()
#pedir_dia()
pedir_hora()


'''
#Ejercicio para mostrar las voces instaladas en el pc
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)

'''