# Clase-Python
---
## Instalación python
Para sistemas operativos windows, se deberá descargar python del sigueinte link:
```
https://www.python.org/downloads/
```
Para Linux se seguirán los soguientes comandos:
* Actualizar paquetes del sistema operativo
```
sudo apt update
sudo apt upgrade
```
* Instalar Python
```
sudo apt install python3
```
* Verificar version de python
```
python3 --version
```
* Instalar paquetes pip para gestión de instalación de librerías de Python
```
sudo apt install python3-pip
```
* Verificar version de pip
```
pip3 --version
```
## Librerías usadas en este Curso
### Videojuegos
* pygame: Librería utilizada para la creación del juego "Invación Espacial"
### Web Scraping
* bs4: Beautyfull soap se utiliza para parcear un texto en html o demás.
* requests: Para búsqueas de los sitios web por medio de una url.
### Aplicaciones ejecutables
* tkinter: usado para generar una ventana donde se desarrollan elementos internos que pueden ser ejecutadas de forma sencilla (Se deberá generar un loop para que la ejecución sea continua y no se cierre).
```
from tkinter import *

#Iniciar tkinter
application = Tk()

#Evitar que la pnatalla se cierre por sí sola
application.mainloop()
```
### Asistente de voz
* pyttsx3: Usada para que el sistemapueda hablar con nosotros
* SpeechRecognition: usada para que el sistema pueda reconocer nuestra voz y la convierta en texto.
* pywhatkit: Permite que el sistema pueda abrir un sitio web desde python.
* yfinance(yahoo finance): Permite ver los estados de las acciones de las compañias
* pyjokes: Permite obtener chistes en la aplicación desarrollada en python
### Reconocimiento Facial
**Se deberá instalar el compilador C para gestionar el procesamiento del reconocimiento de python https://visualstudio.microsoft.com/es/downloads/**
* cmake: Utilizada para compilar librerías que están desarrolladas en C/C++
* dlib: Librería de machine learning yvisión por computadora
* face-recognition: Usada para la detección de rostros
* numpy: Usada para procesos matemáticos y manejo de arrays
* opencv-python: Es la adaptación de la librería más famosa para visión por computadora.
### Machine learning
**Se realizan los ejercicios en Google Colab para reducir el esfuerzo de las máquinas personales**
* numpy: Usada para procesos matemáticos y manejo de arrays
* pandas: Utilizada para leer, crear o editar archivos CSV, SQL, Excel, Json, etc.
* matplotlib: Librería por excelencia de gráficos para python.

# Django
---
Framework de python destinado en su mayoría para apliaciones web
### Entornos virtuales
Utilizado para generar proyectos con versiones específicas sin que se alamacenen las mismas en el pc ``(**venv** deberá estár instalado)``

* En el lugar donde se desea generar el entorno virtual, utilizaremos el simbolo del sistema o consola con el siguiente comando:
```
cd ruta/donde_está mi proyecto_a_manejar_en_un_entorno_virtual
```
#### Crear el entorno virtual
Una vez nosa encontramos en la ruta donde se alojará el proyecto que requiere el entorno virtual.

* para windows
```
python -m venv nombre_del_entorno
```
* En Linux
```
python3 -m venv nombre_del_entorno
```
#### Activar el entorno Virtual
* Para windows
```
.\venv\Scripts\activate
```
* Para Linux
```
source venv/bin/activate
```
***Si lorealizaste correctamente, la consola se verá así:***
``
(venv) usuario@pc:~/mi_proyecto$
``
#### Desactivar Entorno Virtual
en la misma ruta se lanza el comando:
```
deactivate
```
### Instalar Django
---
Se instala por medio del manejador de paquetes python ***pip*** para aamacenar la última versión de Django, se recomienda hacerlo en el entorno virtual activo
```
pip install django
```