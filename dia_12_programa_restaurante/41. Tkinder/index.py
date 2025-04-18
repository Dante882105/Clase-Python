from tkinter import *

#Iniciar a tkinter
aplicacion = Tk()

#Tamaño de la pantalla
aplicacion.geometry("1020x630+0+0")

#Evitar máximizar
aplicacion.resizable(0,0)

#tituo de la venta
aplicacion.title('Restaurante - sistema de facturación')

#color de fondo de la ventana
aplicacion.config(bg="blue violet")

#Se deberá evitar que la panmtalla se cierre
aplicacion.mainloop()