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
    
transformar_audio_en_texto()