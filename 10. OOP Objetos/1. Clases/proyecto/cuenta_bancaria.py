class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, persona, numero_cuenta, balance):
        super().__init__(persona.nombre, persona.apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Hola {self.nombre} {self.apellido}\nTu número de cuenta es {self.numero_cuenta}\nEL saldo en tu cuenta bancaria es de ${self.balance}"
    
    def depositar(self, agregar_dinero):
        self.agregar_dinero = int(agregar_dinero)
        self.balance = self.balance + self.agregar_dinero
    
    def retirar(self, retirar):
        self.retirar = int(retirar)
        self.balance = self.balance - self.retirar

nombre_usuario = input("Hola, ¿Cuál es tu nombre?: ")
apellido_usuario = input("Ahora indicanos tu apellido: ")
numero_cuenta_usuario = 123456789
balance_usuario = 30000

opcion = ""

while opcion != "4":

    usuario = Persona(nombre_usuario, apellido_usuario)
    cliente = Cliente(usuario, numero_cuenta_usuario, balance_usuario)

    opcion = input("seleccione\n(1) ver datos de mi cuenta \n(2)Depositar dinero a mi cuenta \n(3)Retirar dinero de mi cuenta \n(4)Salir de mi zona transaccional: ")

    if opcion == "1":
        print(cliente)
    
    elif opcion == "2":
        valor_add = input("Indique el monto a agregar: ")
        cliente.depositar(valor_add)
        print(f"Su cuenta se encuentra con el siguiente saldo: ${cliente.balance}")
    
    elif opcion == "3":
        valor_quitar = input("¿Cuánto desea retirar de su cuenta?: ")
        cliente.retirar(valor_quitar)
        print(f"Su cuenta se encuentra con el siguiente saldo: ${cliente.balance}")
    
    elif opcion == "4":
        print(f"Gracias por usar nuestros servicios, {cliente.nombre} {cliente.apellido}")

    else:
        print("Opción no válida, intente de nuevo.")
   