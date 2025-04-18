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

#Saludo_inicial
def saludo_inicial():

    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "buenas tardes"

    #decir mensaje
    hablar(f"{momento} soy Helena, tu asistente personal. Por favor, ¿dime en qué te puedo ayudar?")

#Función central del asistente
def pedir_cosas():

    #activar a saluido inicial
    saludo_inicial()


    #variable de corte
    comenzar = True

    #loop Central
    while comenzar:
        #activar el micrófono y guardar el pedido en un string en minúsculas
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido: #abrir youtube
            hablar('Con guisto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido: #abrir el navegador
            hablar("Claro, estoy en eso")
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido: #día de la semana
            pedir_dia()
            continue
        elif 'qué hora es' in pedido: #hora
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido: #Buscar en wikipedia
            hablar('Entiendo, lo buscaré en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido: #buscar en internet
            hablar('Ya mismo lo busco por tí')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Lo que he encontrado es lo siguiente:')
            continue
        elif 'reproducir' in pedido: #reproducir desde youtube
            hablar('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido: # bromas con pyjokes
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido: #Buscar acciones por medio de yahoo finance
            accion = pedido.split('de')[-1].strip()
            cartera = {'coca-cola':'KO', 'amazon':'AMZN', 'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yfinance.Ticker(accion_buscada)
                precio_actual = accion_buscada.info[r'regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón, pero no la he encontrado')
        elif 'adiós' in pedido: #Finalizar la charla con el asistente
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


#hablar("¡Papito rico. que bello estás!")
#transformar_audio_en_texto()
#pedir_dia()
#pedir_hora()
#saludo_inicial()
pedir_cosas()


'''
#Ejercicio para mostrar las voces instaladas en el pc
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)

'''