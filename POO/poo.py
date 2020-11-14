
class Cuenta:

    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0.0

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if self.cantidad - cantidad < 0:
            self.cantidad = 0
        else:
            self.cantidad -= cantidad


class Ejecutable(Cuenta):

    def get(self):
        self.toString(self.cantidad)

    def set(self, op, data):
        if op == 'ingresar':
            self.ingresar(data)
        elif op == 'retirar':
            self.retirar(data)

    def toString(self, data):
        print (str(data))



if __name__ == '__main__':
    cuenta = Ejecutable('Alberto')
    cuenta.set('ingresar', 10)
    cuenta.set('ingresar', 100)
    cuenta.set('retirar', 10.01)
    cuenta.get()