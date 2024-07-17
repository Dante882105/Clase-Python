# comisiones del 13% y se deberá preguntar a los usuarios por el nombre y el monto total de ventas del mes
nombre = input("Indicanos tu nombre y apellido: ")

ventas_totales = float(input("Indicanos el total en dinero correspondientes a tus ventas de este mes: "))

comision = round(ventas_totales*0.13, 2);

print(f"Ok {nombre}. este mes ganaste ${comision}")