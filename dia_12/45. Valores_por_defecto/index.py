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

#Lista de productos
lista_comidas = ['Pollo', 'Res', 'Cerdo', 'Merluza', 'Pizza Hawaiana', 'Pizza Pollo Champiñon', 'Pizza carnes']
lista_bebidas = ['agua', 'soda', 'jugo', 'gaseosa', 'jugo natural', 'café', 'malteada', 'mate']
lista_postres = ['helado', 'fruta', 'brownies', 'mousse', 'pastel 1', 'pastel 2', 'pastel 3', 'pastel 4']


#Checkbutton con for
#Generar ítems comida
variables_comida = []
cuadros_comidas = []
texto_comida = []

contador = 0

for comida in lista_comidas:
    #crear checkButtons
    variables_comida.append('')
    variables_comida[contador] = IntVar()

    comida = Checkbutton(panel_comidas, 
                         text=comida.title(),
                         font=('Dosis', 16, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador])
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Cuadros de entrada
    cuadros_comidas.append('')
    texto_comida.append('')
    #Se establece el valor por defecto 0
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas,
                                      font=('Dosis', 14, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_comida[contador])
    cuadros_comidas[contador].grid(row=contador,
                                   column=1)


    contador += 1

#Generar ítems Bebida
variables_bebida = []
cuadros_bebidas = []
texto_bebidas = []

contador = 0

for bebida in lista_bebidas:
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()

    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 16, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador])
    bebida.grid(row=contador,
                column=0,
                sticky=W)

# Cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    #Se establece el valor por defecto 0
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                      font=('Dosis', 14, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                   column=1)

    contador += 1

#Generar ítems postres
variables_postres = []
cuadros_postres = []
texto_postres = []

contador = 0

for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()

    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 16, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador])
    postre.grid(row=contador,
                column=0,
                sticky=W)
    

#cuadros de Entrada
    cuadros_postres.append('')
    texto_postres.append('')
    #Se establece el valor por defecto 0
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 14, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    
    contador += 1

#Se deberá evitar que la panmtalla se cierre
aplicacion.mainloop()