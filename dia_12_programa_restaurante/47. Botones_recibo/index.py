from tkinter import *

#Iniciar a tkinter
aplicacion = Tk()

#Tamaño de la pantalla
aplicacion.geometry("1350x630+0+0")

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
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=100)
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
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT, bg='burlywood')
panel_derecha.pack(side=RIGHT)

#calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

#Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

#Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

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
#etiquetas de costos y los campos de entrada

#variable
var_costo_comida = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_impuesto = StringVar()
var_subtotal = StringVar()
var_total = StringVar()

#Comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Costos Comidas',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

#Bebidas
etiqueta_costo_bebidas = Label(panel_costos,
                              text='Costos Bebidas',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_bebidas.grid(row=1, column=0)

texto_costo_bebidas = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row=1, column=1, padx=41)

#Postres
etiqueta_costo_postres = Label(panel_costos,
                              text='Costos Postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

#Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

#Impuesto
etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

#Total
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

#Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
contador_columna = 0

for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)
    boton.grid(row=0,
               column=contador_columna)
    contador_columna += 1

#área de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

#Se deberá evitar que la panmtalla se cierre
aplicacion.mainloop()