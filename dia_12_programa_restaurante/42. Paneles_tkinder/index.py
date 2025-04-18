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

#Paneles
#Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_superior.pack(side=TOP)

#etiqueta con el título
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturación", fg="azure4",
                        font=('Dosis', 30), bg='burlywood', width=27)

etiqueta_titulo.grid(row=0, column=0)


#Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=SUNKEN)
panel_izquierdo.pack(side=LEFT)

#Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#Panel de comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas", font=("Dosis",19, 'bold'),
                           bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)
#Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis",19, 'bold'),
                           bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)
#Panel de postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis",19, 'bold'),
                           bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

#Panel Derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_derecha.pack()

#Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_derecha.pack()

#Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_derecha.pack()






#Se deberá evitar que la panmtalla se cierre
aplicacion.mainloop()