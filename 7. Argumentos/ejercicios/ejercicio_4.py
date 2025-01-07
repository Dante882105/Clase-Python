def contar_primos(val):
    suma_primos = 0
    if val < 1:
        return False
    else:
        for valor in range(2, val+1):
            for i in range(2, valor):
                if int(valor % i) == 0:
                    break
            else:
                suma_primos += valor
                print(valor)
    return(suma_primos)
print(contar_primos(12))