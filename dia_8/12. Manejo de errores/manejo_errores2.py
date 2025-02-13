def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"ingresaste el número {numero}")
            break
    print("Gracias")

pedir_numero()