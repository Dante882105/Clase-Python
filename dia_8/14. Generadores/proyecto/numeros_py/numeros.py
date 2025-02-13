#Se inicia con la definiciòn de los mètodos para adquirir los nùmeros segùn se desea

def turno_perfumeria():
    p = 0
    while True:
        p += 1
        yield f"P - {p}"

def turno_farmacia():
    f = 0
    while True:
        f += 1
        yield f"F - {f}"

def turno_cosmeticos():
    c = 0
    while True:
        c += 1
        yield f"C - {c}"

p = turno_perfumeria()
f = turno_farmacia()
c = turno_cosmeticos()

# Genero el Decorador para los mensajes de los turnos
def mensaje_decorado(seccion):
    def mensaje_cordial():
        print("\n" + 28 * "*")
        print("\nSu turno es:")
        if seccion == "p":
            print(next(p))
        elif seccion == "f":
            print(next(f))
        elif seccion == "c":
            print(next(c))
        print("En breve será atendido.\n")
        print("\n" + 28 * "*")
    return mensaje_cordial()