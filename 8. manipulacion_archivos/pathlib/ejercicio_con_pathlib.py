from pathlib import Path

carpeta = Path('C:/Users/DANTE/OneDrive/Desktop/alternativa/texto.txt')

'''print(carpeta.read_text())
print(carpeta.suffix)
print(carpeta.stem)'''

#Uso de Path a profundidad
#instancias de las extenciones.
base = Path.home()
guia = Path("Barcelona", "Sagrada_familia")
base_guia = Path(base,"Barcelona", "Sagrada_familia" )
#print(base, guia, base_guia)

#utilizando una ruta previa pero redireccionando
guia2 = guia.with_name("La_Pedrera.txt")
#print(guia2)

#Mostrar la carpeta más cercana al fin de una ruta
'''print(base_guia.parent)
print(base_guia.parent.parent)'''

#interactuar con archivos, carpetas y su posición
guia3 = Path(Path.home(), "OneDrive","Desktop","Europa")
'''for txt in Path(guia3).glob("**/*.txt"):
    print(txt)'''

guia4 = Path(Path.home(), "OneDrive","Desktop","Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia4.relative_to(Path.home(), "OneDrive","Desktop","Europa")
en_espania = guia4.relative_to(Path.home(), "OneDrive","Desktop","Europa", "España")

print(en_europa)
print(en_espania)
