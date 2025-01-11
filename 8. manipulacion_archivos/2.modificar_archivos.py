#para abrir un archivo en modo solo lectura se hará así:
archivo_lectura = open('prueba.txt','r')
#para abrir un archivo en modo escritura (modificar el archivo), tener cuidado; ya que el contenido del archivo será reemplazado por el nuevo texto
archivo_escritura = open("prueba.txt", "w")
#Para abrit un archivo pero que se posicione el elemento al final, lo hacemos así
archivo_escritura_desde_final = open("prueba.txt", "a")

#ejercicios con lectura
"""archivo_lectura.write("Soy el nuevo texto")"""#Genera un error
archivo_lectura.close()

#archivo de escritura
#archivo_escritura.write("Hola Mundo jejejeje \n") #escribir con salto de linea
archivo_escritura.write('''Hola Mundo jejejeje
Espero que esto si funcione
en tres saltos de linea''') #escribir con multiples saltos de linea
#archivo_escritura.writelines(["Hola Mundo ","Cambaré de linea aqui ", "disfruten su tinto jejeje"])

#archivo_escritura.writelines
archivo_escritura.close()

#Archivo de escritura desde la última posición
archivo_escritura_desde_final.write("\nHola, desde el archivo sin cambiar datos del mismo jejeje")
archivo_escritura_desde_final.close()