#Se importa el módulo datetime
'''import datetime

mi_hora = datetime.time(17,35, 50, 1500)
mi_fecha = datetime.date(2025, 2, 13)

print(mi_hora, mi_fecha)'''

#Para unir hora y fecha, se importará así
'''from datetime import datetime

mi_fecha = datetime(2025,5,15,22,10,45,1874)

print(mi_fecha)

#Para reemplazar un valor se hará de la siguiente manera
mi_fecha = mi_fecha.replace(month = 11)

print(mi_fecha)'''

#Calcular tiempo entre fechas y horas

from datetime import date

nacimineto = date(1956, 6, 18)
defuncion = date(2023, 6, 12)

vida = defuncion - nacimineto

print(vida)

from datetime import datetime

desperto = datetime(2025, 2, 13, 5, 30)
durmio = datetime(2025, 2, 13, 23, 50)

vigilia = durmio - desperto

print(vigilia, vigilia.seconds)

#Capturar solo los minutos de la fecha y hora actuales
import datetime

today = datetime.datetime.now()
minutos = today.minute

print(minutos)